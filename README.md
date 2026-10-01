<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# urpx-data-sandbox

This repository holds community-contributed rate plan datasets and experiments for URPX, the Utility Rate Plan Exchange ontology. It is the place for a dataset that is unvalidated, in progress, or needs vocabulary that does not exist yet, and for agent-assisted or contributor experiments that do not belong in the standard.

## What this repository is not

Nothing here is normative and nothing here is a released artifact. This is not the standard: the ontology, the SHACL shapes, and the curated test cases live in [`urpx-org/urpx`](https://github.com/urpx-org/urpx). 

A change to the standard's vocabulary or shapes is a pull request against `urpx-org/urpx`, not a submission here.

## Disclaimer

**Nothing in this repository is reviewed for data content, completeness, or accuracy.** A submission is checked for conformance to the URPX version it states it targets, and for nothing else.

Submissions are validated automatically. There is no additional human review before a submission is merged. Peer review may be added later if the community grows.

## Directory structure

Submissions are organized by jurisdiction and commodity:

```
submissions/
  <country>/            two-letter country code, lowercase (for example us)
    <state>/             ISO 3166-2 subdivision code, lowercase (for example us-ca)
      <utility>/          kebab-case utility slug
        <commodity>/       electric, gas, or another commodity type
```

Utility-specific identifiers such as service classes are not directory levels; they are metadata on the utility in the submitted dataset. See [`submissions/README.md`](submissions/README.md) and the template at [`submissions/_template/`](submissions/_template/) for the shape, and [`submissions/_template/country/state/utility/commodity/README.md`](submissions/_template/country/state/utility/commodity/README.md) for what a submission at that depth carries.

## How to submit

Open a pull request that adds your dataset under the directory shape above, using the [pull request template](.github/PULL_REQUEST_TEMPLATE.md). A submission vendors its source document (includes a copy) rather than only linking to it, and declares the URPX version it targets.

Gate 1 runs automatically on every pull request: SHACL validation against the shapes of the URPX version the submission declares, plus summary queries that record the submission in the [catalog index](catalog/README.md). A submission that fails gate 1 does not merge.

## Graduating to the standard

Every dataset starts here. There is no route that skips this repository, including for a dataset that already validates against a released URPX version. A submission can be nominated to be copied into the curated test cases in `urpx-org/urpx`, but only after it passes full review, separate from and later than gate 1.

## License

Prose, source, and meta files are licensed under the Apache License, Version 2.0. Submitted datasets and the catalog index are data, licensed under the Community Data License Agreement - Permissive 2.0 (CDLA-Permissive-2.0). See [NOTICE](NOTICE), [LICENSE](LICENSE), and `LICENSES/` for the CDLA-Permissive-2.0 text.

Security issues: see [SECURITY.md](SECURITY.md).
