#!/usr/bin/env python3
# SPDX-FileCopyrightText: The URPX Authors
# SPDX-License-Identifier: Apache-2.0

"""Walk the submissions corpus: the files that make up the datasets here.

Two kinds of file live under a submission's directory:

* ``instance`` — a URPX document a consumer loads (``*.jsonld``).
* ``source`` — a vendored tariff or rate document the dataset is built from
  (the PDFs, CSVs, and other files copied in beside the dataset).

Repository meta (a README, a REUSE ``.license`` sidecar) is not part of the
corpus. This module is the one place that decides which file is which, so the
catalog generator and any consumer agree.

It has no third-party dependency, so a script or a language model can list the
corpus without installing the catalog's RDF tooling.

Usage::

    corpus.py <submissions-dir>                 instance paths, one per line
    corpus.py <submissions-dir> --kind source   source paths only
    corpus.py <submissions-dir> --all           kind<TAB>path for every file
    corpus.py <submissions-dir> --verify        agree with git's tracked files

Paths print in C-locale byte order so the output is stable across machines.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import subprocess
import sys

# A file is an instance, a source, or neither. Keep this the single decision.
INSTANCE_SUFFIXES = {".jsonld"}
META_NAMES = {"README.md", ".gitkeep", ".gitignore", ".DS_Store"}
META_SUFFIXES = {".license"}

MEDIA_TYPES = {
    ".jsonld": "application/ld+json",
    ".json": "application/json",
    ".pdf": "application/pdf",
    ".csv": "text/csv",
    ".tsv": "text/tab-separated-values",
    ".ttl": "text/turtle",
    ".txt": "text/plain",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".svg": "image/svg+xml",
}


def classify_file(path: pathlib.Path) -> str | None:
    """Return "instance", "source", or None (repository meta, not corpus)."""
    if path.name in META_NAMES or path.suffix in META_SUFFIXES:
        return None
    if path.suffix in INSTANCE_SUFFIXES:
        return "instance"
    return "source"


def media_type(path: pathlib.Path) -> str:
    return MEDIA_TYPES.get(path.suffix, "application/octet-stream")


def find_submission_dirs(root: pathlib.Path) -> list[pathlib.Path]:
    """Each immediate child directory of submissions/ is one submission.

    A submission is a directory of files; its name and place carry no meaning.
    A directory counts as a submission when it holds at least one instance
    document (an .jsonld) somewhere in its subtree. The _template directory and
    dot-directories are skipped.
    """
    dirs = []
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name == "_template" or child.name.startswith("."):
            continue
        if any(child.rglob("*.jsonld")):
            dirs.append(child)
    return dirs


def corpus_files(submission_dir: pathlib.Path) -> list[tuple[str, pathlib.Path]]:
    """Return (kind, path) for every corpus file under a submission, sorted."""
    found = []
    for path in submission_dir.rglob("*"):
        if not path.is_file():
            continue
        kind = classify_file(path)
        if kind is not None:
            found.append((kind, path))
    return sorted(found, key=lambda item: (item[0], str(item[1])))


def repo_relative(path: pathlib.Path, base: pathlib.Path) -> str:
    """Repo-relative, forward-slash path for a file, e.g. submissions/us/...."""
    return os.path.relpath(path.resolve(), base).replace(os.sep, "/")


def walk(root: pathlib.Path) -> list[tuple[str, str]]:
    """Return every (kind, repo-relative-path) in the corpus, sorted by path."""
    base = root.resolve().parent
    pairs = []
    for submission_dir in find_submission_dirs(root):
        for kind, path in corpus_files(submission_dir):
            pairs.append((kind, repo_relative(path, base)))
    return sorted(pairs, key=lambda item: item[1])


def verify(root: pathlib.Path) -> list[str]:
    """Return the ways the walked corpus disagrees with git's tracked files."""
    base = root.resolve().parent
    submission_dirs = find_submission_dirs(root)
    walked = {(kind, path) for kind, path in walk(root)}

    try:
        listed = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", str(root)],
            capture_output=True,
            text=True,
            check=True,
            cwd=base,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError) as error:
        return [f"could not run git ls-files: {error}"]

    tracked = set()
    for line in listed:
        path = (base / line).resolve()
        if not any(_is_within(path, submission_dir) for submission_dir in submission_dirs):
            continue
        kind = classify_file(path)
        if kind is not None:
            tracked.add((kind, repo_relative(path, base)))

    problems = []
    for kind, path in sorted(tracked - walked):
        problems.append(f"git tracks {path} ({kind}) but the walker does not list it")
    for kind, path in sorted(walked - tracked):
        problems.append(f"the walker lists {path} ({kind}) but git does not track it")
    return problems


def _is_within(path: pathlib.Path, directory: pathlib.Path) -> bool:
    try:
        path.resolve().relative_to(directory.resolve())
        return True
    except ValueError:
        return False


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="corpus.py")
    parser.add_argument("submissions_dir")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--kind", choices=("instance", "source"),
                       help="list only files of this kind")
    group.add_argument("--all", action="store_true",
                       help="list every file as kind<TAB>path")
    group.add_argument("--verify", action="store_true",
                       help="check the walked corpus against git's tracked files")
    args = parser.parse_args(argv)

    root = pathlib.Path(args.submissions_dir)

    if args.verify:
        problems = verify(root)
        if problems:
            print("Corpus walker disagrees with git:", file=sys.stderr)
            for problem in problems:
                print(f"- {problem}", file=sys.stderr)
            return 1
        print("Corpus walker agrees with git's tracked files.")
        return 0

    for kind, path in walk(root):
        if args.all:
            print(f"{kind}\t{path}")
        elif args.kind is None and kind == "instance":
            print(path)
        elif args.kind == kind:
            print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
