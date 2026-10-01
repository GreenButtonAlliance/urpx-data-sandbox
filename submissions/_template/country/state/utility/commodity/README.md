<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Submission template

This directory shows the shape a real submission takes; it carries no real data. Copy this depth (`<country>/<state>/<utility>/<commodity>/`) and rename each segment for your submission, following [`submissions/README.md`](../../../../README.md).

## What a submission carries

- **The dataset itself**, as URPX JSON-LD, declaring the URPX version it targets.
- **The source document**, vendored (included as a file here, not only linked), with its capture date.
- **Whether the dataset was built from a real, published dataset**, or is a synthetic or illustrative example.
- **The jurisdiction**: the utility and the state, so the submission is searchable by both.
- **Effective dates**: when the rate plan itself took effect.
- **Service-period dates**: the period the data covers, which is not always the same as the effective dates.

State these in a README alongside the dataset, and in the pull request using the [submission template](../../../../../.github/PULL_REQUEST_TEMPLATE.md).

## Disclaimer

Nothing in this repository is reviewed for data content, completeness, or accuracy. A submission is checked for conformance to the URPX version it states it targets, and for nothing else. See the [repository README](../../../../../README.md).
