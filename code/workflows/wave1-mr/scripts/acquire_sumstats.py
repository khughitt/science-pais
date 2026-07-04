# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Acquire the two harmonised GWAS-SSF sumstats for the Wave-1 MR pilot.

plan:0007 Task 1. The exposure (old deposit) and outcome (new deposit) use
DIFFERENT harmonised filenames, so we resolve the actual `*.h.tsv.gz` from each
harmonised directory listing rather than construct it. Download, SHA-256, stream
row count, and write a manifest. Fail loud on any failure.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml

_UA = {"User-Agent": "wave1-mr-pilot/plan-0007 (research; contact via repo)"}


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def resolve_harmonised_file(harmonised_dir: str) -> str:
    """Return the absolute URL of the single `*.h.tsv.gz` (not `-meta.yaml`)."""
    html = _get(harmonised_dir).decode("utf-8", errors="replace")
    hits = [
        h for h in re.findall(r'href="([^"]+\.h\.tsv\.gz)"', html)
        if not h.endswith("-meta.yaml")
    ]
    hits = sorted(set(hits))
    if len(hits) != 1:
        raise SystemExit(
            f"acquire: expected exactly one *.h.tsv.gz in {harmonised_dir}, found {hits}"
        )
    href = hits[0]
    return href if href.startswith("http") else harmonised_dir.rstrip("/") + "/" + href


def download(url: str, dest: Path) -> str:
    """Stream-download to dest; return SHA-256 hex."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=300) as resp, open(dest, "wb") as fh:
        while chunk := resp.read(1 << 20):
            fh.write(chunk)
            h.update(chunk)
    return h.hexdigest()


def count_rows(path: Path) -> int:
    """Data rows (excluding header), streamed — never loads the file into memory."""
    n = 0
    with gzip.open(path, "rt") as fh:
        for _ in fh:
            n += 1
    return max(0, n - 1)


def acquire_one(cfg_side: dict, dest: Path) -> dict:
    url = resolve_harmonised_file(cfg_side["harmonised_dir"])
    sha = download(url, dest)
    return {
        "accession": cfg_side["accession"],
        "name": cfg_side["name"],
        "source_url": url,
        "local_path": str(dest),
        "sha256": sha,
        "n_rows": count_rows(dest),
        "build": cfg_side["build"],
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--exposure-out", required=True)
    p.add_argument("--outcome-out", required=True)
    p.add_argument("--manifest", required=True)
    a = p.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text())

    manifest = {
        "exposure": acquire_one(cfg["exposure"], Path(a.exposure_out)),
        "outcome": acquire_one(cfg["outcome"], Path(a.outcome_out)),
    }
    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    for side, m in manifest.items():
        sys.stderr.write(f"acquire: {side} {m['accession']} rows={m['n_rows']} sha256={m['sha256'][:12]}…\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
