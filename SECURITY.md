<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Security Policy

## Reporting a security issue

If you believe you have found a security issue in this repository, please do
**not** open a public GitHub issue. Instead, report it privately so
maintainers can triage and coordinate disclosure responsibly.

Report to: `security@urpx.org`

When reporting, please include:

- A description of the issue.
- The commit hash, tag, or file path at which you observed it.
- Steps to reproduce, including any sample data or queries.
- The potential impact as you understand it.
- Any suggested mitigation, if you have one.

## Response timeline

We aim to:

- **Acknowledge** your report within **2 business days**.
- **Assess and triage** within **5 business days**.
- **Provide a status update** at least every **14 calendar days** until
  the issue is resolved or a decision is made not to act on it.

Actual timelines may vary depending on the severity and complexity of
the issue.

## Scope

This repository holds community-contributed rate plan datasets, validated
automatically for conformance to the URPX version they declare and for
nothing else. Relevant security concerns may include:

- **Malformed or malicious submissions** that could exploit downstream
  RDF parsers or SHACL validators, or the validation workflow itself.
- **Supply-chain issues** in the tooling this repository's workflows use
  to validate submissions.

Report concerns in any of these categories through the private channel
above.

## Out of scope

- Disputes over the accuracy or completeness of a submitted dataset.
  Nothing here is reviewed for data content; see [README.md](README.md).
- Issues in third-party software this repository merely references
  (report those to their upstream maintainers).

## Credits

We credit reporters of validated security issues in release notes
unless the reporter requests otherwise.
