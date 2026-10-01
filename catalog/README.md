<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Catalog index

[`submissions-index.csv`](submissions-index.csv) is a machine-generated summary of every submission that has passed gate 1, so the sandbox is browsable without opening a file. It mirrors the shape of `test-cases-index.csv` in the standard repository.

## How it is generated

The gate-1 workflow (`.github/workflows/validate-submission.yml`) regenerates this file on every push to the default branch, by running the summary queries in `scripts/update_catalog_index.py` over every submission under `submissions/`. It is machine-owned output: do not hand-edit it, and do not add hand-authored content to this directory. A hand edit is overwritten on the next run.

## Columns

| Column | Meaning |
|---|---|
| `submission_path` | Directory of the submission, relative to the repository root |
| `utility` | Utility named in the submission |
| `jurisdiction` | State or subdivision the submission covers |
| `urpx_version` | The URPX version the submission declares and validates against |
| `rate_plan_count` | Count of `RatePlan` instances |
| `rate_plan_version_count` | Count of `RatePlanVersion` instances |
| `pricing_model_count` | Count of `PricingModel` instances |
| `price_definition_count` | Count of `PriceDefinition` instances |
| `price_count` | Count of `Price` instances |
| `effective_date_start` | Earliest effective date found in the submission |
| `effective_date_end` | Latest effective date found in the submission |
| `has_external_price_reference` | Whether the submission references an externally-priced value it does not itself supply |
| `date_added` | Date the submission first passed gate 1 |

## License

This file is data, licensed under the Community Data License Agreement - Permissive 2.0 (CDLA-Permissive-2.0), like the submissions it summarizes. See [REUSE.toml](../REUSE.toml).
