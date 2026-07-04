# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Emit the reproducible output bundle for the Wave-1 MR pilot.

plan:0007 Outputs contract. Writes:
- datapackage.json  — Frictionless descriptor: every input+output resource with
  SHA-256 + source, PLUS entity cross-references (config.entities: plan, task,
  the three datasets) and a provenance DAG linking outputs to inputs (Dim 9).
- qa_report.{json,md} — structural hard-stop checks (columns, row counts, allele
  coding, instrument count, mean F, palindromic drops, ancestry/build
  reconciliation) AND the outcome-extraction peak-memory + wall-clock (Dim 6).
- run_metadata.json — tool + R-package versions, all params (incl. clump
  thresholds, MHC window, harmonise action, weighted-median RNG seed), input
  SHA-256s, resolved TwoSampleMR version, retrieval date, producing git commit.

STUB — not yet implemented (WP0 skeleton).
"""
from __future__ import annotations

import argparse
import sys


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--results", required=True)
    p.add_argument("--harmonised", required=True)
    p.add_argument("--acq-manifest", required=True)
    p.add_argument("--ld-manifest", required=True)
    p.add_argument("--datapackage", required=True)
    p.add_argument("--qa-json", required=True)
    p.add_argument("--qa-md", required=True)
    p.add_argument("--run-metadata", required=True)
    p.parse_args()
    sys.stderr.write("emit_datapackage_qa.py: STUB not implemented (plan:0007 Outputs contract)\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
