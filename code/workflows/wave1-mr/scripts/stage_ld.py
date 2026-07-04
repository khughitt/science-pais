# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Stage the 1000G-EUR LD reference panel for local plink clumping.

plan:0007 Task 2 (first half) / dataset:1000g-eur-ld-panel. Download + extract
the MRC-IEU 1kg.v3 EUR plink bfile, SHA-256 everything, and record the
build-reconciliation decision: the panel is GRCh37, the sumstats are GRCh38, so
clumping proceeds by **rsID** (hm_rsid), which is build-independent. That is the
reconciliation; a positional join would be the hard-stop path (not used here).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tarfile
import urllib.request
from pathlib import Path

import yaml

_UA = {"User-Agent": "wave1-mr-pilot/plan-0007 (research; contact via repo)"}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while chunk := fh.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=600) as resp, open(dest, "wb") as fh:
        while chunk := resp.read(1 << 20):
            fh.write(chunk)
    return _sha256(dest)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--bfile-prefix", required=True)   # e.g. data/raw/ld/1000g-eur-phase3/EUR
    p.add_argument("--manifest", required=True)
    a = p.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text())
    ld = cfg["ld_panel"]

    prefix = Path(a.bfile_prefix)
    out_dir = prefix.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    tgz = out_dir / "1kg.v3.tgz"
    tgz_sha = download(ld["source_url"], tgz)
    with tarfile.open(tgz, "r:gz") as tf:
        tf.extractall(out_dir, filter="data")

    bfiles = {ext: prefix.with_suffix(ext) for ext in (".bed", ".bim", ".fam")}
    missing = [str(p) for p in bfiles.values() if not p.exists()]
    if missing:
        raise SystemExit(
            f"stage_ld: expected plink bfile {a.bfile_prefix}.{{bed,bim,fam}} after extract; missing {missing}"
        )

    manifest = {
        "name": ld["name"],
        "superpopulation": ld["superpopulation"],
        "build": ld["build"],
        "source_url": ld["source_url"],
        "archive_sha256": tgz_sha,
        "bfile_prefix": a.bfile_prefix,
        "bfile_sha256": {ext.lstrip("."): _sha256(p) for ext, p in bfiles.items()},
        "build_reconciliation": (
            "panel=GRCh37, sumstats=GRCh38 → clump by rsID (hm_rsid), "
            "build-independent; PASS (plan:0007 Task 2)."
        ),
    }
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    sys.stderr.write(f"stage_ld: {ld['name']} staged; archive sha256={tgz_sha[:12]}…\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
