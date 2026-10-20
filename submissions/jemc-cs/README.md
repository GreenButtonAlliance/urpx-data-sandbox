<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Jackson EMC Cooperative Solar Rider

One version of Jackson Electric Membership Corporation's Cooperative Solar Rider rate plan modifier (identifier `CS`), as URPX JSON-LD, with the tariff sheets it was read from.

| Version | Effective | Sheets | Dataset |
|---|---|---|---|
| 2022-06-01 | from 2022-06-01 | CS | [`rate-plan-modifier_jemc_cs_2022-06-01.jsonld`](versions/2022-06-01/rate-plan-modifier_jemc_cs_2022-06-01.jsonld) |

The dataset declares URPX v0.5.1. It names the 4 rate plans it applies to by reference only, so on its own it does not pass gate 1: each referenced rate plan lacks the name, identifier and initial effective date the shapes require. Those rate plans are submitted separately in this repository. See [urpx-org/urpx-data-sandbox#10](https://github.com/urpx-org/urpx-data-sandbox/issues/10).

## Source

- **Utility:** Jackson Electric Membership Corporation, an electric membership cooperative whose board sets its rates.
- **Jurisdiction:** Georgia, United States.
- **Built from a real, published dataset:** yes. Copied unchanged from [`us/ga/jemc/electricity/cs/`](https://github.com/GreenButtonAlliance/urpx-rate-plans/tree/3b64d39/us/ga/jemc/electricity/cs) in [GreenButtonAlliance/urpx-rate-plans](https://github.com/GreenButtonAlliance/urpx-rate-plans) at commit `3b64d39`.
- **Source documents:** the tariff sheets in each `versions/<date>/` directory, as published by Jackson EMC, retrieved on 2026-10-18.

Each version's `tariff.toml` in the source repository records the source URLs, sha256 checksums, and the parts of the tariff the dataset does not yet model.

## Attribution and license

The datasets are copyright 2026 Clark Communications Corporation and licensed under CDLA-Permissive-2.0, as recorded in each file's `.license` sidecar. GreenButtonAlliance contributes them to this repository. The tariff sheets are public records of the issuing utility.

## Disclaimer

Nothing in this repository is reviewed for data content, completeness, or accuracy. A submission is checked for conformance to the URPX version it states it targets, and for nothing else. See the [repository README](../../README.md).
