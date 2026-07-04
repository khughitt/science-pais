# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Acquire the two harmonised GWAS-SSF sumstats for the Wave-1 MR pilot.

plan:0007 Task 1. Resolve and download the `*.h.tsv.gz` harmonised
fullPvalueSet files from the exposure/outcome harmonised directories in
config.yaml, into data/raw/gwas/. Record per-file SHA-256, the resolved
filename, the assembly build, and row counts into the manifest; then the
plan's Task 1 upgrades each dataset entity's verification_method + assembly
label. Do NOT leave a PENDING-RETRIEVAL digest in the manifest.

STUB — not yet implemented (WP0 skeleton).
"""
from __future__ import annotations

import argparse
import sys


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--exposure-out", required=True)
    p.add_argument("--outcome-out", required=True)
    p.add_argument("--manifest", required=True)
    p.parse_args()
    sys.stderr.write("acquire_sumstats.py: STUB not implemented (plan:0007 Task 1)\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
