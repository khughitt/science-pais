#!/usr/bin/env python3
"""Reproducible download + SHA-256 verify (t035 WP1).

Replaces the one-off `curl` with a rule-callable fetch that VERIFIES every
payload against a locked hash before it is allowed to exist at its final path.
Fail-early discipline (pre-registration:0002 G1; plan:0003 review finding 6):

  * empty `--sha256`     -> HALT (no unverified passthrough; this is the
                            geneset-GMT "TBD-at-ingest" guard, reused here).
  * hash mismatch        -> HALT, partial file removed (never leave a payload
                            that masquerades as verified).
  * recovery is a deliberate, logged act (re-verify provenance upstream, then
                            amend the locked hash) — never an auto-accept.

Streams to a temporary sibling and atomically renames only after the hash
matches, so a halted/interrupted fetch never satisfies a Snakemake output.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import requests

from acquire_common import sha256_path

CHUNK = 1 << 20  # 1 MiB


def fetch(url: str, out: Path, expected_sha256: str) -> None:
    if not expected_sha256:
        sys.exit(
            f"[fetch] HALT: empty expected sha256 for {out.name} "
            f"(url={url}). Fill the locked hash in config.yaml before fetching."
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.name + ".partial")
    print(f"[fetch] GET {url}", file=sys.stderr)
    with requests.get(url, stream=True, timeout=120) as resp:
        resp.raise_for_status()
        with tmp.open("wb") as fh:
            for chunk in resp.iter_content(CHUNK):
                if chunk:
                    fh.write(chunk)

    got = sha256_path(tmp)
    if got != expected_sha256:
        tmp.unlink(missing_ok=True)
        sys.exit(
            f"[fetch] HALT: sha256 mismatch for {out.name}\n"
            f"        expected {expected_sha256}\n"
            f"        got      {got}\n"
            f"        (upstream re-deposit? re-verify provenance, then amend the "
            f"locked hash — never auto-accept.)"
        )
    tmp.replace(out)
    print(f"[fetch] OK {out} sha256={got} bytes={out.stat().st_size}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description="download a payload and verify its SHA-256")
    ap.add_argument("--url", required=True)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--sha256", required=True, help="locked expected hash (empty => HALT)")
    args = ap.parse_args()
    fetch(args.url, args.out, args.sha256)
    return 0


if __name__ == "__main__":
    sys.exit(main())
