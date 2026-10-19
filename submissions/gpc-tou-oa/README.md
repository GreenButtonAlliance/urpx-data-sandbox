<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Georgia Power Schedule TOU-OA Time of Use - Overnight Advantage

One version of Georgia Power Company's Schedule TOU-OA Time of Use - Overnight Advantage rate plan (identifier `TOU-OA`), as URPX JSON-LD, with the tariff sheets it was read from.

| Version | Effective | Sheets | Dataset |
|---|---|---|---|
| 2026-06-01 | from 2026-06-01 | TOU-OA-15, TOU-FCR-TP-5, ECCR-15, DSM-R-16, MFF-11 | [`rate-plan_gpc_tou-oa_2026-06-01.jsonld`](versions/2026-06-01/rate-plan_gpc_tou-oa_2026-06-01.jsonld) |

The dataset declares URPX v0.5.1 and validates on its own.

## Source

- **Utility:** Georgia Power Company, regulated by the Georgia Public Service Commission.
- **Jurisdiction:** Georgia, United States.
- **Built from a real, published dataset:** yes. Copied unchanged from [`us/ga/gpc/electricity/tou-oa/`](https://github.com/GreenButtonAlliance/urpx-rate-plans/tree/3b64d39/us/ga/gpc/electricity/tou-oa) in [GreenButtonAlliance/urpx-rate-plans](https://github.com/GreenButtonAlliance/urpx-rate-plans) at commit `3b64d39`.
- **Source documents:** the tariff sheets in each `versions/<date>/` directory, as published by Georgia Power, retrieved on 2026-10-16.

Each version's `tariff.toml` in the source repository records the source URLs, sha256 checksums, PSC dockets, and the parts of the tariff the dataset does not yet model.

## Attribution and license

The datasets are copyright 2026 Clark Communications Corporation and licensed under CDLA-Permissive-2.0, as recorded in each file's `.license` sidecar. GreenButtonAlliance contributes them to this repository. The tariff sheets are public records of the issuing utility.

## Disclaimer

Nothing in this repository is reviewed for data content, completeness, or accuracy. A submission is checked for conformance to the URPX version it states it targets, and for nothing else. See the [repository README](../../README.md).
