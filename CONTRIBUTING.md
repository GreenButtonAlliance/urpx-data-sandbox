<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Contributing to urpx-data-sandbox

Thank you for your interest in contributing a dataset to the URPX data sandbox. This repository holds community-contributed rate plan datasets and experiments for URPX, the Utility Rate Plan Exchange ontology. It is not the standard; the ontology, the SHACL shapes, and the curated test cases live in [`urpx-org/urpx`](https://github.com/urpx-org/urpx).

Anyone with a GitHub account can open a pull request here, including automated agents. The expectations below, the Developer Certificate of Origin, and automated gate-1 validation apply to every submission.

## General expectations

All issues, pull requests, and other repository submissions must be written and reviewed by the person submitting them.

Do not submit content that is fully AI-generated, overly verbose, speculative, or padded with background material that is not necessary to evaluate the request. Submissions that appear to be fully AI-generated or unnecessarily long may be closed without review. They may be re-submitted in a concise and actionable form.

AI-generated or AI-assisted drafting does not excuse the submitter from understanding the proposal, checking it for accuracy, and reducing it to the information needed by the working group.

## Licensing of contributions

By contributing to this repository you agree that your contribution is licensed under the terms that apply to the corresponding file category:

- **Submitted datasets** (the URPX JSON-LD instance documents): the Community Data License Agreement - Permissive 2.0 (CDLA-Permissive-2.0).
- **Prose, source, and meta files**, including a submission's own README: the Apache License, Version 2.0. See [LICENSE](LICENSE).
- **Vendored source documents** (a published tariff or rate filing copied in beside the dataset): a public record of a regulatory process, not your work, marked `LicenseRef-PublicRecord`. See [`LICENSES/LicenseRef-PublicRecord.txt`](LICENSES/LicenseRef-PublicRecord.txt).

See [NOTICE](NOTICE) and [REUSE.toml](REUSE.toml) for how each file is annotated.

## Developer Certificate of Origin (DCO)

All contributions must include a `Signed-off-by` line in every commit. Adding this line certifies that you wrote the contribution, or otherwise have the right to submit it under the applicable license, per the [Developer Certificate of Origin, version 1.1](https://developercertificate.org/).

Append a DCO line by running:

```
git commit --signoff
```

The line looks like this:

```
Signed-off-by: Your Name <you@example.com>
```

Pull requests missing `Signed-off-by` on every commit will be asked to rebase and re-sign.

## How to submit

Open a pull request that adds your dataset in its own directory under `submissions/`, using the [pull request template](.github/PULL_REQUEST_TEMPLATE.md). A submission vendors its source document (includes a copy) rather than only linking to it, and declares the URPX version it targets.

Gate 1 runs automatically on every pull request: SHACL validation against the shapes of the URPX version the submission declares, plus summary queries that record the submission in the [catalog index](catalog/README.md). A submission that fails gate 1 does not merge. On a passing check, any member of the `urpx-committers` GitHub team merges the submission; there is no additional human review before it is merged.

See [`submissions/README.md`](submissions/README.md) and the template at [`submissions/_template/`](submissions/_template/) for what a submission carries, and [AGENTS.md](AGENTS.md) for notes on agent-assisted submissions.

## Changes to the standard

A change to the standard's vocabulary or shapes is a pull request against [`urpx-org/urpx`](https://github.com/urpx-org/urpx), not a submission here. The sandbox is for data, not for edits to the standard.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Security issues

Do **not** open public issues for security concerns. See [SECURITY.md](SECURITY.md).

## Questions

- Working Group mailing list: `urpx-wg@lists.lfenergy.org`
- Chair: `chair@urpx.org`
