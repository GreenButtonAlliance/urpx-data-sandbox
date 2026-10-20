<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Georgia Power Schedule LT Local Tax Adjustment

One version of Georgia Power Company's Schedule LT Local Tax Adjustment rate plan modifier (identifier `LT`), as URPX JSON-LD, with the tariff sheets it was read from.

| Version | Effective | Sheets | Dataset |
|---|---|---|---|
| 1975-06-17 | from 1975-06-17 | LT-1 | [`rate-plan-modifier_gpc_lt_1975-06-17.jsonld`](versions/1975-06-17/rate-plan-modifier_gpc_lt_1975-06-17.jsonld) |

The dataset declares URPX v0.5.1. It names the 41 rate plans it applies to by reference only, so on its own it does not pass gate 1: each referenced rate plan lacks the name, identifier and initial effective date the shapes require. All of them except Schedule ET are submitted separately in this repository. See [urpx-org/urpx-data-sandbox#10](https://github.com/urpx-org/urpx-data-sandbox/issues/10).

## Source

- **Utility:** Georgia Power Company, regulated by the Georgia Public Service Commission.
- **Jurisdiction:** Georgia, United States.
- **Built from a real, published dataset:** yes. Copied unchanged from [`us/ga/gpc/electricity/lt/`](https://github.com/GreenButtonAlliance/urpx-rate-plans/tree/3b64d39/us/ga/gpc/electricity/lt) in [GreenButtonAlliance/urpx-rate-plans](https://github.com/GreenButtonAlliance/urpx-rate-plans) at commit `3b64d39`.
- **Source documents:** the tariff sheets in each `versions/<date>/` directory, as published by Georgia Power, retrieved on 2026-10-16.

Each version's `tariff.toml` in the source repository records the source URLs, sha256 checksums, PSC dockets, and the parts of the tariff the dataset does not yet model.

## Attribution and license

The datasets are copyright 2026 Clark Communications Corporation and licensed under CDLA-Permissive-2.0, as recorded in each file's `.license` sidecar. GreenButtonAlliance contributes them to this repository. The tariff sheets are public records of the issuing utility.

## Disclaimer

Nothing in this repository is reviewed for data content, completeness, or accuracy. A submission is checked for conformance to the URPX version it states it targets, and for nothing else. See the [repository README](../../README.md).
