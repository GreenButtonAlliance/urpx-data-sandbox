<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# AGENTS.md

Instructions for automated agents and coding assistants working in this repository.

This repository holds community-contributed rate plan datasets and experiments for URPX, the Utility Rate Plan Exchange ontology. It is not the standard; see [`urpx-org/urpx`](https://github.com/urpx-org/urpx) for the ontology, SHACL shapes, and curated test cases.

## Looser than the standard repository

This repository does not carry the standard repository's length and verbosity limits on issues and pull requests, and does not require working group discussion before adding a new submission directory under `submissions/`. It exists so that drafting a submission or trying an agent-assisted vocabulary mapping does not need the standard's ceremony.

## What still holds

- **No internal process framing.** Do not reference private repositories, internal project names, working sessions, codenames, or a commercial platform built on this standard.
- **Careful attributions.** Do not attribute a dataset to a utility, jurisdiction, or contributor without a clear basis in the submission's own source-document reference.
- **Plain, factual voice.** Describe the dataset and the change, not the process that produced it.
- **Prose formatting.** Write for a person reading and reviewing the text. Do not hard-wrap a paragraph mid-sentence to hit a column width. Keep paragraphs and sentences short.
- **The disclaimer travels with the data.** Do not remove or soften the disclaimer in [README.md](README.md) when adding a submission's own README.
- **Scope restraint.** This repository provides the submission process and the cataloguing system, and nothing more. It does not host, resolve, serve, or answer queries over the submitted data; a service that does is a data publisher implementation's role. A change that would make the sandbox host or serve the data, or publish the catalog's data as resolvable linked data, belongs in a working-group discussion, not a pull request here. Keep changes within this scope and as small as the job allows, mindful of maintainer capacity. See the [repository README's Scope section](README.md).

## Submissions

A submission declares the URPX version it targets and is validated automatically against that version's shapes, not against whatever is current. See [`submissions/README.md`](submissions/README.md) and the [pull request template](.github/PULL_REQUEST_TEMPLATE.md).

A dataset that implies a change to the ontology or SHACL constraints belongs in a working group discussion and a pull request against `urpx-org/urpx`, not in a submission here.

**No route skips this repository.** Every dataset starts here, including one that already validates against a released URPX version and needs no ontology change. Do not describe or imply a path that merges a dataset directly into `urpx-org/urpx` `test-cases/`. The only path from here to the curated test cases is a nomination after full review, separate from and later than gate 1.

## Code of conduct and security

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [SECURITY.md](SECURITY.md).
