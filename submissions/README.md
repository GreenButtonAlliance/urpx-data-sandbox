<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Submissions

**Nothing in this directory is reviewed for data content, completeness, or accuracy.** See the disclaimer in the [repository README](../README.md).

## Directory shape

A submission lives at:

```
submissions/<country>/<state>/<utility>/<commodity>/
```

- `<country>`: the two-letter country code, lowercase (for example `us`).
- `<state>`: the ISO 3166-2 subdivision code, lowercase (for example `us-ca` for California). Use the correct subdivision code for the country; do not abbreviate informally.
- `<utility>`: a kebab-case slug for the utility (for example `pge` or `con-edison`).
- `<commodity>`: the commodity type (for example `electric` or `gas`). A utility with more than one commodity gets a directory per commodity, not a combined one.

Utility-specific identifiers such as service classes are not directory levels; record them as metadata in the submitted dataset instead.

See [`_template/`](_template/) for the shape with a README at each level, and [`_template/country/state/utility/commodity/README.md`](_template/country/state/utility/commodity/README.md) for what a submission at that depth carries.

## How to submit

1. Fork the repository and create the directory for your submission, following the shape above.
2. Add your dataset, and vendor its source document (include a copy, not only a link) alongside it.
3. Open a pull request using the [pull request template](../.github/PULL_REQUEST_TEMPLATE.md), which asks for the utility, the jurisdiction, the source-document reference, the declared URPX version, whether the dataset was built from a real dataset, and the effective and service-period dates.
4. Gate 1 runs automatically: SHACL validation against the shapes of the URPX version you declared, plus summary queries that record the submission in the [catalog index](../catalog/README.md).

Every dataset goes through this process, including one that already validates against a released URPX version and needs no ontology change. There is no route that skips the sandbox. A submission can later be nominated to be copied into the curated test cases in `urpx-org/urpx`, but only after it passes full review, separate from and later than gate 1.
