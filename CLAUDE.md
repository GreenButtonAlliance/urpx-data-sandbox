# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**This file is fork-only.** It belongs to the `GreenButtonAlliance/urpx-data-sandbox` fork, as does `tools/`. Neither goes to `urpx-org/urpx-data-sandbox`. Open pull requests in the fork with `--repo GreenButtonAlliance/urpx-data-sandbox`, since `gh` defaults to upstream. To propose anything upstream, branch from `upstream/main` and cherry-pick the commits; never open a pull request from the fork's `main`.

Read [AGENTS.md](AGENTS.md) first. Its rules (no internal process framing, careful attributions, plain voice, no hard-wrapped prose, keep the disclaimer, scope restraint, no route that skips this repository) apply to everything written here, including commit messages, PR bodies, and READMEs.

## What this repository is

A sandbox for community-contributed URPX rate plan datasets. It provides a submission process (gate 1: SHACL validation) and a generated catalog index, and nothing more. It does not host, resolve, or serve the data. The ontology, SHACL shapes, and curated test cases live in `urpx-org/urpx`; a change that needs new vocabulary or shapes belongs there, not here.

## Commands

All scripts run from the repository root and import their siblings from `scripts/`. Install dependencies with `pip install -r scripts/requirements.txt`.

```
python3 scripts/validate_submission.py submissions/              # gate 1 (needs network)
python3 scripts/update_catalog_index.py check submissions/ catalog/
python3 scripts/update_catalog_index.py build submissions/ catalog/
python3 scripts/corpus.py submissions/ --verify                  # walker agrees with git
python3 -m pytest scripts/                                       # tests
python3 -m pytest scripts/test_urpx_version.py::test_names_a_version
```

CI (`.github/workflows/validate-submission.yml`) runs validate, `check`, and `--verify` on pull requests touching `submissions/**`. After a merge to `main`, a bot runs `build` and commits the regenerated index.

## Architecture

- **Submissions** (`submissions/<slug>/`): one dataset per directory. The slug carries no meaning; utility, commodity, rate plans, service class, version, and effective dates are read from the JSON-LD metadata. `_template/` is a placeholder with no data and is skipped by the validator.
- **Version pinning** (`scripts/urpx_version.py`): the single place that turns a `urpx:targetURPXVersion` value (the ontology version IRI, or a bare `0.5.1` / `v0.5.1`) into a semantic version. Both the validator and the catalog use it.
- **Gate 1** (`scripts/validate_submission.py`): for each `*.jsonld`, reads the declared version, downloads that tagged release's `urpx-ontology-vX.Y.Z.ttl` and `urpx-shacl-vX.Y.Z.ttl` assets from the `urpx-org/urpx` GitHub release (cached under the system temp dir in `urpx-release-shapes/`), and runs pyshacl with RDFS inference. It validates against the declared version, never the current one. It restores rdflib's literal converters after each run because owlrl's inference replaces them process-wide.
- **Corpus walker** (`scripts/corpus.py`): no third-party deps. The one place that classifies a file under a submission as `instance` (`*.jsonld`), `source` (any vendored tariff/rate document), or repository meta (README, `.license` sidecar). The catalog generator imports this decision, so change classification only here.
- **Catalog** (`scripts/update_catalog_index.py` → `catalog/`): builds two projections of the same summaries, `submissions-index.csv` and `submissions-index.jsonld` (a DCAT catalog validated against `submissions-index.schema.json`). Catalog-only terms use the provisional, non-normative `sdx:` prefix rooted at this repository, not a `urpx.org` namespace. `date_added` is preserved from the existing CSV across rebuilds. Both index files are machine-owned: never hand-edit them. `check` fails on a hand-edited row or disagreeing projections, but does not require a new submission to be indexed on its own PR.

## Fork tools

`tools/build_utility.py` copies a utility's rate plan and modifier documents from a `GreenButtonAlliance/urpx-rate-plans` checkout into `submissions/<utility>-<schedule>/`. It copies the JSON-LD unchanged, writes a `.license` sidecar crediting Clark Communications Corporation, copies the tariff PDFs, and generates the README from the document and its `tariff.toml`. It has profiles for Georgia Power (`gpc`) and Jackson EMC (`jemc`); add a profile to `UTILITIES` for a new utility. It needs only rdflib.

```
python3 tools/build_utility.py jemc ../urpx-rate-plans/us/ga/jemc/electricity submissions <commit> a atou
```

Review each generated README before committing, then run gate 1 on the new directories. A modifier fails gate 1 on its own because its referenced base plans lack required properties (urpx-org/urpx-data-sandbox#10). Fork PRs #5 and #6, which hold the modifiers, stay open until that issue is settled. Merging them would fail gate 1 for every later pull request, since CI validates all of `submissions/`.

## Licensing

Licensing is declared through REUSE (`REUSE.toml`). Prose, scripts, and meta files carry an inline Apache-2.0 SPDX header; add one to any new file that can hold a comment. Under `submissions/`, `*.jsonld` datasets are CDLA-Permissive-2.0, and every other vendored file is `LicenseRef-PublicRecord`. The catalog CSV and JSON-LD are CDLA-Permissive-2.0. The schema is Apache-2.0 via its `.license` sidecar.
