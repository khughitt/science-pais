# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Stage the 1000G-EUR LD reference panel for local plink clumping (naive arm).

plan:0009 Task 1 / dataset:1000g-eur-ld-panel (reused from plan:0007). Downloads
the three EUR plink files from the HARDENED source — Zenodo 6614170 (https,
DOI-archival, CC-BY-4.0), verifying each published md5 (hard-stop on mismatch) and
recording SHA-256. The panel is GRCh37; the sumstats are GRCh38, so naive-arm
clumping proceeds by rsID (hm_rsid), which is build-independent. (Self-contained
copy of the plan:0007 stager: this isolated hormone-pilot workflow does not reach
into the frozen wave1-mr run-of-record.)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

import yaml

_UA = {"User-Agent": "wave1-mr-hormone/plan-0009 (research; contact via repo)"}


def _hash_download(url: str, dest: Path) -> tuple[str, str]:
    """Stream-download; return (md5_hex, sha256_hex)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    md5, sha = hashlib.md5(), hashlib.sha256()
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=600) as resp, open(dest, "wb") as fh:
        while chunk := resp.read(1 << 20):
            fh.write(chunk)
            md5.update(chunk)
            sha.update(chunk)
    return md5.hexdigest(), sha.hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--bfile-prefix", required=True)
    p.add_argument("--manifest", required=True)
    a = p.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text())
    ld = cfg["ld_panel"]

    prefix = Path(a.bfile_prefix)
    sha_by_ext: dict[str, str] = {}
    for ext, spec in ld["files"].items():
        dest = prefix.with_suffix(f".{ext}")
        got_md5, sha = _hash_download(spec["url"], dest)
        if got_md5 != spec["md5"]:
            raise SystemExit(
                f"stage_ld: md5 mismatch for {dest.name}: expected {spec['md5']}, got {got_md5} — HALT"
            )
        sha_by_ext[ext] = sha
        sys.stderr.write(f"stage_ld: {dest.name} md5 OK ({got_md5[:12]}…) sha256={sha[:12]}…\n")

    manifest = {
        "name": ld["name"],
        "superpopulation": ld["superpopulation"],
        "build": ld["build"],
        "doi": ld["doi"],
        "license": ld["license"],
        "bfile_prefix": a.bfile_prefix,
        "file_md5": {ext: spec["md5"] for ext, spec in ld["files"].items()},
        "file_sha256": sha_by_ext,
        "archive_sha256": sha_by_ext["bed"],
        "source_url": f"https://doi.org/{ld['doi']}",
        "build_reconciliation": (
            "panel=GRCh37, sumstats=GRCh38 → clump by rsID (hm_rsid), "
            "build-independent; PASS (naive arm only)."
        ),
    }
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    sys.stderr.write(f"stage_ld: {ld['name']} staged from {ld['doi']} (md5-verified)\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
