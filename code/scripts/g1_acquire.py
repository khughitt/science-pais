#!/usr/bin/env python3
"""G1/G2 acquisition seed orchestrator for t035 (post-WP1 refactor).

This was the original one-off acquisition script; in WP1 its logic was split
into rule-callable modules and it is KEPT as the integration seed — a single
offline command that reproduces every acquisition artifact and writes the
roll-up `acquisition_manifest.json` (hashes of every raw payload + both parse
contracts). The Snakemake rules (rules/acquire.smk) call the SAME module
functions, so this seed and the pipeline can never diverge.

  parse_gse14577.run()    -> data/processed/GSE14577/*  (+ contract)
  extract_gse130353.run() -> data/processed/GSE130353/* (+ contract)  [if tar present]

Bounded by pre-registration:0002 G1/G2: acquire + hash + parse contract ONLY —
no DE, fgsea, concordance, or pathway result. Re-runnable; GSE14577 proceeds
offline, GSE130353 activates once the tar is on disk.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import extract_gse130353
import parse_gse14577
from acquire_common import SOURCE_URLS, sha256_path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"


def main() -> int:
    PROC.mkdir(parents=True, exist_ok=True)

    raw_hashes = {}
    for p in sorted(RAW.iterdir()):
        if p.is_file() and p.name != ".gitkeep":
            raw_hashes[p.name] = {
                "sha256": sha256_path(p),
                "bytes": p.stat().st_size,
                "source_url": SOURCE_URLS.get(p.name, "unknown"),
            }

    soft14577 = RAW / "GSE14577_family.soft.gz"
    g14577 = (
        parse_gse14577.run(soft14577, PROC / "GSE14577")
        if soft14577.exists()
        else {"status": "missing", "file": soft14577.name}
    )

    tar = RAW / "GSE130353_RAW.tar"
    soft130353 = RAW / "GSE130353_family.soft.gz"
    if tar.exists() and soft130353.exists():
        g130353 = extract_gse130353.run(tar, soft130353, PROC / "GSE130353")
    else:
        g130353 = {
            "dataset": "GSE130353",
            "status": "PENDING_DOWNLOAD",
            "needed_file": "GSE130353_RAW.tar",
            "source_url": SOURCE_URLS["GSE130353_RAW.tar"],
            "note": "RAW.tar must be fetched directly (geo adapter is series-matrix-only). "
                    "Run the download rule (or fetch_url.py) then re-run this seed.",
        }

    manifest = {
        "task": "t035",
        "gate": "G1 acquisition + integrity; G2 scale/header smoke check",
        "pre_registration": "pre-registration:0002-cross-trigger-pathway-overlap",
        "scope": "acquire + hash + parse contract ONLY -- no DE/fgsea/concordance",
        "raw_file_hashes": raw_hashes,
        "GSE14577": g14577,
        "GSE130353": g130353,
    }
    man_path = PROC / "acquisition_manifest.json"
    man_path.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"[g1] wrote {man_path.relative_to(ROOT)}")
    print(f"[g1] raw files hashed: {list(raw_hashes)}")
    print(f"[g1] GSE14577 status={g14577.get('status')}")
    print(f"[g2] GSE130353 status={g130353.get('status')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
