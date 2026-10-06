<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Submissions

**Nothing in this directory is reviewed for data content, completeness, or accuracy.** See the disclaimer in the [repository README](../README.md).

## Directory shape

A submission lives in its own directory under `submissions/`:

```
submissions/<submission-name>/
```

- `<submission-name>`: a short kebab-case slug you choose, for example `pge-e-tou-c` or `con-edison-steam-sc1`. The name helps a human find the files; it carries no meaning for the catalog.

The directory does not encode a country, state, utility, commodity, or service class. The catalog reads all of those from the metadata in the submitted documents: the utility from its `UtilityOperator`, the commodity from `urpx:commodity`, the rate plans from their `ratePlanUniqueIdentifier` and `name`, the service class from `urpx:serviceClassName`, the version from `urpx:targetURPXVersion`, and the effective dates from the rate plan versions. Record those facts in the dataset, not in the path. Keep one submission per directory; a schedule you want listed on its own goes in its own directory.

See [`_template/`](_template/) for what a submission carries.

## How to submit

1. Fork the repository and create a directory for your submission under `submissions/`.
2. Add your dataset, and vendor its source document (include a copy, not only a link) alongside it.
3. Open a pull request using the [pull request template](../.github/PULL_REQUEST_TEMPLATE.md), which asks for the utility, the jurisdiction, the source-document reference, the declared URPX version, whether the dataset was built from a real dataset, and the effective and service-period dates.
4. Gate 1 runs automatically: SHACL validation against the shapes of the URPX version you declared, plus summary queries that record the submission in the [catalog index](../catalog/README.md).

Every dataset goes through this process, including one that already validates against a released URPX version and needs no ontology change. There is no route that skips the sandbox. A submission can later be nominated to be copied into the curated test cases in `urpx-org/urpx`, but only after it passes full review, separate from and later than gate 1.
