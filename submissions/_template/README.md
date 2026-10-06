<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Submission template

This directory shows the shape a submission takes; it carries no real data. Copy it to a directory of your own under `submissions/` — `submissions/<your-submission-name>/` — and fill it in, following [`submissions/README.md`](../README.md).

## What a submission carries

- **The dataset itself**, as URPX JSON-LD, declaring the URPX version it targets and the metadata the catalog reads: the utility (a `UtilityOperator`), the commodity (`urpx:commodity`), the rate plans (`ratePlanUniqueIdentifier` and `name`), the service class (`urpx:serviceClassName`), and the effective dates on the rate plan versions.
- **The source document**, vendored (included as a file here, not only linked), with its capture date.
- **Whether the dataset was built from a real, published dataset**, or is a synthetic or illustrative example.

State these in a README alongside the dataset, and in the pull request using the [submission template](../../.github/PULL_REQUEST_TEMPLATE.md).

The directory's name and place carry no meaning. The catalog reads what the submission is from the metadata above, not from the path, so there is no country, state, utility, or commodity to encode in the directory.

## Disclaimer

Nothing in this repository is reviewed for data content, completeness, or accuracy. A submission is checked for conformance to the URPX version it states it targets, and for nothing else. See the [repository README](../../README.md).
