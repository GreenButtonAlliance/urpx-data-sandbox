<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Catalog index

The catalog is a machine-generated summary of every submission that has passed gate 1, so the sandbox is browsable without opening each file. It is published in two projections of one source of truth, the `submissions/` tree:

- [`submissions-index.jsonld`](submissions-index.jsonld) — a [DCAT](https://www.w3.org/TR/vocab-dcat-3/) catalog. One `dcat:Dataset` per submission, each with its facets (utility, commodity, rate plans, service class, version, effective-date range), a `dcat:Distribution` per file, and the summary counts, as a graph you can load into any RDF tool. This is the machine-readable declaration of the corpus, for scripts and language models. It is a file in this repository, not a hosted service.
- [`submissions-index.csv`](submissions-index.csv) — the same submissions as a flat table, for a quick human read.

Both are data, not prose. Their shape is fixed by [`submissions-index.schema.json`](submissions-index.schema.json), a JSON Schema the generator validates its JSON-LD output against.

## Facets come from metadata

A submission's directory under `submissions/` is storage only. Every facet in the catalog — the utility, the commodity, the rate plans, the service class, the version, the effective dates — is read from the metadata in the submitted documents, not from the directory name. A facet a submission does not declare is left empty rather than guessed from the path. The browsing hierarchy (utility, commodity, rate plan, version) emerges from the facets the submissions carry.

## How it is generated

The gate-1 workflow (`.github/workflows/validate-submission.yml`) regenerates both files on every push to the default branch, by running the summary queries in [`scripts/update_catalog_index.py`](../scripts/update_catalog_index.py) over every submission under `submissions/`:

```
python3 scripts/update_catalog_index.py build submissions/ catalog/
```

They are machine-owned output: do not hand-edit them, and do not add hand-authored content to this directory. A hand edit is overwritten on the next run, and a pull request that hand-edits an indexed row, or that lets the two projections disagree, fails the consistency check:

```
python3 scripts/update_catalog_index.py check submissions/ catalog/
```

A brand-new submission is not required to appear in the index on its own pull request. The index is regenerated after merge, so it never shares a commit path with a hand-edited file.

## Walking the corpus

[`scripts/corpus.py`](../scripts/corpus.py) lists the files that make up the submissions, with no RDF tooling needed:

```
python3 scripts/corpus.py submissions/                # instance documents, one per line
python3 scripts/corpus.py submissions/ --kind source  # the vendored source documents
python3 scripts/corpus.py submissions/ --all          # every file as kind<TAB>path
python3 scripts/corpus.py submissions/ --verify        # agree with git's tracked files
```

A file under a submission is an `instance` (a URPX document a consumer loads, `*.jsonld`), a `source` (a vendored tariff or rate document the dataset is built from), or repository meta (a README or a REUSE `.license` sidecar, which is not part of the corpus). `corpus.py` is the one place that decides which file is which, and the catalog generator imports that decision, so the index and the walker never disagree.

## CSV columns

| Column | Meaning |
|---|---|
| `storage_path` | The submission's directory, relative to the repository root. Storage only; it carries no facet. |
| `utility` | Utility operator named in the submitted metadata (its `UtilityOperator`) |
| `jurisdiction` | Jurisdiction identifier, when the metadata declares one (`urpx:identifierJurisdiction`) |
| `commodity` | Commodities priced, from `urpx:commodity` |
| `rate_plans` | The rate plans in the submission, each as `identifier (name)` |
| `service_class` | Service class names, from `urpx:serviceClassName` |
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

## JSON-LD terms

The JSON-LD catalog uses [DCAT](https://www.w3.org/TR/vocab-dcat-3/) and [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) where they fit: `dcat:Catalog`, `dcat:Dataset`, `dcat:Distribution`, `dcat:downloadURL`, `dcat:mediaType`, and `dct:conformsTo` for the declared ontology version IRI.

The facets read from the metadata (the utility, commodity, rate plans, service class, and version), the summary counts, and the storage path have no term in those vocabularies. They use a provisional, sandbox-local prefix, `sdx:`, rooted at this repository (`https://github.com/urpx-org/urpx-data-sandbox/ns#`), not at a `urpx.org` namespace. Nothing here is normative: these terms are a convenience of the index, and the working group decides whether any of them graduate to an agreed namespace. Each file carries `sdx:fileKind`, `instance` or `source`, so a consumer can tell a loadable document from a vendored source.

The `urpx_version` column records the semantic version (`0.5.1`) that the declared version IRI names; [`scripts/urpx_version.py`](../scripts/urpx_version.py) is the single place that resolves one to the other, shared with the gate-1 validator.

## License

The two index files are data, licensed under the Community Data License Agreement - Permissive 2.0 (CDLA-Permissive-2.0), like the submissions they summarize. The JSON Schema is tooling, licensed Apache-2.0. See [REUSE.toml](../REUSE.toml).
