# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Stage the 1000G-EUR LD reference panel for local plink clumping.

plan:0007 Task 2 (first half) / dataset:1000g-eur-ld-panel. Download + extract
the EUR plink bfile from config.ld_panel.source_url into
data/raw/ld/1000g-eur-phase3/, record per-file SHA-256 + release/version +
build into the manifest, and record the **build-reconciliation** decision vs the
GRCh38 sumstats (GRCh38-lifted panel, or rsID matching via hm_rsid). Hard-stop
if neither reconciliation holds.

STUB — not yet implemented (WP0 skeleton).
"""
from __future__ import annotations

import argparse
import sys


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--bfile-prefix", required=True)
    p.add_argument("--manifest", required=True)
    p.parse_args()
    sys.stderr.write("stage_ld.py: STUB not implemented (plan:0007 Task 2)\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
