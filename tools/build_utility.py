#!/usr/bin/env python3
# SPDX-FileCopyrightText: The URPX Authors
# SPDX-License-Identifier: Apache-2.0

"""Copy a utility's rate plans and modifiers from urpx-rate-plans into sandbox submissions.

Usage: build_utility.py <utility> <rate-plans-electricity-dir> <sandbox-submissions-dir> <commit> <schedule>...

Example, from the repository root:

    python3 tools/build_utility.py jemc ../urpx-rate-plans/us/ga/jemc/electricity submissions 3b64d39 a atou

For each schedule this writes submissions/<utility>-<schedule>/. Each version
directory gets the JSON-LD document copied unchanged, a .license sidecar and
the tariff PDFs. The README is generated from the document and each version's
tariff.toml. PDFs are matched to tariff.toml sources by sha256 to list the
sheets, retrieval dates and Internet Archive retrievals. A source with no
matching PDF is listed as drawn on but not included. Only rdflib is needed
beyond the standard library.

Review each README before committing. Two earlier submissions needed a hand
edit: an Internet Archive note that applies to only one version (gpc-pbd), and
a modifier that references a rate plan not submitted here (gpc-lt, gpc-opt).
The gpc-r README was written by hand and differs from this script's output.
"""

import hashlib
import pathlib
import shutil
import sys
import tomllib

from rdflib import Graph, Namespace

URPX = Namespace("https://urpx.org/ns/ontology/")
REPO = "https://github.com/GreenButtonAlliance/urpx-rate-plans"
UTILITIES = {
    "gpc": {
        "state": "ga",
        "short": "Georgia Power",
        "legal": "Georgia Power Company",
        "utility": "Georgia Power Company, regulated by the Georgia Public Service Commission",
        "records": "the source URLs, sha256 checksums, PSC dockets, and the parts of the tariff the dataset does not yet model",
    },
    "jemc": {
        "state": "ga",
        "short": "Jackson EMC",
        "legal": "Jackson Electric Membership Corporation",
        "utility": "Jackson Electric Membership Corporation, an electric membership cooperative whose board sets its rates",
        "records": "the source URLs, sha256 checksums, and the parts of the tariff the dataset does not yet model",
    },
}
SIDECAR = (
    "SPDX-FileCopyrightText: 2026 Clark Communications Corporation\n"
    "SPDX-License-Identifier: CDLA-Permissive-2.0\n"
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def and_join(items):
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def sources(manifest):
    src = manifest.get("source", {})
    subs = [v for v in src.values() if isinstance(v, dict)]
    return subs or [src]


def plan_facts(jsonld):
    g = Graph()
    g.parse(jsonld, format="json-ld")
    key = URPX.ratePlanUniqueIdentifier
    if (None, key, None) not in g:
        key = URPX.modifierUniqueIdentifier
    plan = next(g.subjects(key, None))
    version = next(g.subjects(URPX.effectiveDateTime, None))
    return {
        "modifier": key == URPX.modifierUniqueIdentifier,
        "applies_to": len(set(g.objects(None, URPX.applicableToRatePlan))),
        "name": str(g.value(plan, URPX.name)),
        "id": str(g.value(plan, key)),
        "start": str(g.value(version, URPX.effectiveDateTime))[:10],
        "end": (str(g.value(version, URPX.expirationDateTime) or "")[:10]) or None,
    }


def build(slug, src_root, dest_root, commit, schedule):
    u = UTILITIES[slug]
    src = src_root / schedule / "versions"
    dest = dest_root / f"{slug}-{schedule}" / "versions"
    rows, retrieved, archived, missing = [], set(), set(), []
    name = None
    for version_dir in sorted(p for p in src.iterdir() if p.is_dir()):
        out = dest / version_dir.name
        out.mkdir(parents=True, exist_ok=True)
        jsonld = next(version_dir.glob("rate-plan*.jsonld"))
        shutil.copy2(jsonld, out / jsonld.name)
        (out / f"{jsonld.name}.license").write_text(SIDECAR)
        pdfs = sorted(version_dir.glob("*.pdf"))
        for pdf in pdfs:
            shutil.copy2(pdf, out / pdf.name)
        by_hash = {sha256(p): p for p in pdfs}
        sheets = []
        for s in sources(tomllib.loads((version_dir / "tariff.toml").read_text())):
            fid = s.get("filing_id", "?")
            if s.get("sha256") in by_hash:
                sheets.append(fid)
                retrieved.add(s["retrieved_on"])
                if "web.archive.org" in s.get("url", ""):
                    archived.add(fid)
            else:
                missing.append(fid)
        facts = plan_facts(jsonld)
        name = name or facts
        span = f"{facts['start']} to {facts['end']}" if facts["end"] else f"from {facts['start']}"
        rel = f"versions/{version_dir.name}/{jsonld.name}"
        rows.append(f"| {version_dir.name} | {span} | {', '.join(sheets)} | [`{jsonld.name}`]({rel}) |")

    n = len(rows)
    count = "One version" if n == 1 else f"{['', '', 'Two', 'Three', 'Four'][n]} versions"
    dates = sorted(retrieved)
    retrieval = and_join(dates)
    lines = [
        "<!-- SPDX-FileCopyrightText: The URPX Authors -->",
        "<!-- SPDX-License-Identifier: Apache-2.0 -->",
        "",
        f"# {u['short']} {name['name']}",
        "",
        f"{count} of {u['legal']}'s {name['name']} {'rate plan modifier' if name['modifier'] else 'rate plan'} (identifier `{name['id']}`), as URPX JSON-LD, with the tariff sheets {'it was' if n == 1 else 'they were'} read from.",
        "",
        "| Version | Effective | Sheets | Dataset |",
        "|---|---|---|---|",
        *rows,
        "",
        f"{'The dataset declares' if n == 1 else 'Each dataset declares'} URPX v0.5.1 and validates on its own."
        if not name["modifier"]
        else f"The dataset declares URPX v0.5.1. It names the {name['applies_to']} rate plans it applies to by reference only, so on its own it does not pass gate 1: each referenced rate plan lacks the name, identifier and initial effective date the shapes require. Those rate plans are submitted separately in this repository. See [urpx-org/urpx-data-sandbox#10](https://github.com/urpx-org/urpx-data-sandbox/issues/10).",
        "",
        "## Source",
        "",
        f"- **Utility:** {u['utility']}.",
        "- **Jurisdiction:** Georgia, United States.",
        f"- **Built from a real, published dataset:** yes. Copied unchanged from [`us/{u['state']}/{slug}/electricity/{schedule}/`]({REPO}/tree/{commit}/us/{u['state']}/{slug}/electricity/{schedule}) in [GreenButtonAlliance/urpx-rate-plans]({REPO}) at commit `{commit}`.",
        f"- **Source documents:** the tariff sheets in each `versions/<date>/` directory, as published by {u['short']}, retrieved on {retrieval}.",
    ]
    if archived:
        lines.append(f"  The {and_join(sorted(archived))} {'sheet was' if len(archived) == 1 else 'sheets were'} retrieved through the Internet Archive.")
    if missing:
        lines.append(f"  The {and_join(missing)} {'sheet is' if len(missing) == 1 else 'sheets are'} drawn on but not included.")
    lines += [
        "",
        f"Each version's `tariff.toml` in the source repository records {u['records']}.",
        "",
        "## Attribution and license",
        "",
        "The datasets are copyright 2026 Clark Communications Corporation and licensed under CDLA-Permissive-2.0, as recorded in each file's `.license` sidecar. GreenButtonAlliance contributes them to this repository. The tariff sheets are public records of the issuing utility.",
        "",
        "## Disclaimer",
        "",
        "Nothing in this repository is reviewed for data content, completeness, or accuracy. A submission is checked for conformance to the URPX version it states it targets, and for nothing else. See the [repository README](../../README.md).",
        "",
    ]
    (dest.parent / "README.md").write_text("\n".join(lines))


if __name__ == "__main__":
    slug = sys.argv[1]
    src_root, dest_root, commit = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
    for schedule in sys.argv[5:]:
        build(slug, src_root, dest_root, commit, schedule)
        print(f"{slug}-{schedule}")
