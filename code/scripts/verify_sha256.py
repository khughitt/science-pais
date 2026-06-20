#!/usr/bin/env python3
"""Verify a file against its LOCKED SHA-256 and emit a sentinel (t035).

Closes the gap where a payload provisioned OUTSIDE Snakemake (a pre-existing
raw GEO file or GMT) would never be hash-checked, because the download rule only
verifies when it actually runs. This rule ALWAYS recomputes the hash of the file
on disk and compares it to the locked config hash, regardless of how the file
got there. Consumers depend on the `<name>.sha256.pass` sentinel, so parsing
never proceeds on unverified bytes.

  empty expected hash  -> HALT (no unverified passthrough; matches fetch_url.py).
  mismatch             -> HALT, sentinel withheld -> DAG stops.
  match                -> write the sentinel (the only output).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from acquire_common import sha256_path


def main() -> int:
    ap = argparse.ArgumentParser(description="verify a file's SHA-256 against the locked hash")
    ap.add_argument("--file", required=True, type=Path)
    ap.add_argument("--sha256", required=True, help="locked expected hash (empty => HALT)")
    ap.add_argument("--sentinel", required=True, type=Path)
    args = ap.parse_args()

    if not args.sha256:
        sys.exit(f"[verify_sha256] HALT: empty expected hash for {args.file.name} "
                 f"(fill the locked hash in config before consuming).")
    if not args.file.exists():
        sys.exit(f"[verify_sha256] HALT: missing {args.file}")

    got = sha256_path(args.file)
    if got != args.sha256:
        sys.exit(f"[verify_sha256] HALT: sha256 mismatch for {args.file.name}\n"
                 f"        expected {args.sha256}\n        got      {got}\n"
                 f"        (provenance drift — re-verify upstream, then amend the locked hash.)")

    args.sentinel.parent.mkdir(parents=True, exist_ok=True)
    args.sentinel.write_text(f"OK {args.file.name} sha256={got}\n", encoding="utf-8")
    print(f"[verify_sha256] OK {args.file} sha256={got}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
