# science:code
# status: exploratory
# task_ids: [t035]
# science:end

#!/usr/bin/env python3
"""Shared acquisition helpers for the t035 pipeline (WP1).

These were factored out of the original one-off `g1_acquire.py` so the
Snakemake acquisition rules (rules/acquire.smk) and the seed orchestrator
share ONE implementation of hashing, scale stats, and the authoritative GEO
source URLs / group map. Nothing here writes files or reads config — callers
pass explicit paths (the pipeline's single source of truth is config.yaml).

Bounded by pre-registration:0002 G1/G2 (acquisition + integrity + scale parse).
"""
from __future__ import annotations

import gzip
import hashlib
import statistics
from pathlib import Path

# Authoritative GEO source URLs, keyed by on-disk basename. These MIRROR
# config.yaml `acquisition.*.url`; kept here only so the datapackage/manifest
# can label a payload by its filename without re-plumbing config.
SOURCE_URLS = {
    "GSE14577_family.soft.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE14nnn/GSE14577/soft/GSE14577_family.soft.gz",
    "GSE130353_family.soft.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE130nnn/GSE130353/soft/GSE130353_family.soft.gz",
    "GSE130353_series_matrix.txt.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE130nnn/GSE130353/matrix/GSE130353_series_matrix.txt.gz",
    "GSE130353_RAW.tar": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE130nnn/GSE130353/suppl/GSE130353_RAW.tar",
}

# pre-reg:0002 G4 — group code is derived from the SOFT `subject status`, NOT
# the filename prefix (QS files are prefixed "PQ"; CFS titles carry CSF/FCS
# typos). First substring match wins.
GSE130353_GROUP_MAP = {
    "Healthy control": "HC",
    "Chronic Fatigue Syndrome": "CFS",
    "Q Fever Fatigue Syndrom": "QFS",
    "Q fever seropositive controls": "QS",
}


def sha256_path(p: Path) -> str:
    """Streaming SHA-256 of a file (1 MiB chunks; handles the 95 MB tar)."""
    h = hashlib.sha256()
    with Path(p).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def scale_stats(values: list[float]) -> dict:
    """Universal scale check: confirm log-scale vs counts (pre-reg:0002 G2)."""
    n = len(values)
    if n == 0:
        return {"n": 0}
    integer_like = sum(1 for v in values if abs(v - round(v)) < 1e-9)
    negative = sum(1 for v in values if v < 0)
    return {
        "n": n,
        "min": round(min(values), 6),
        "max": round(max(values), 6),
        "mean": round(statistics.fmean(values), 6),
        "median": round(statistics.median(values), 6),
        "pct_integer_like": round(100 * integer_like / n, 3),
        "pct_negative": round(100 * negative / n, 3),
    }


def inspect_mmseq(name: str, gz_bytes: bytes) -> dict:
    """G2: lock the column/scale facts for one MMSEQ file from the data itself."""
    text = gzip.decompress(gz_bytes).decode("utf-8", errors="replace")
    lines = text.splitlines()
    comments = [ln for ln in lines[:40] if ln.startswith("#")]
    data_lines = [ln for ln in lines if ln and not ln.startswith("#")]
    header = data_lines[0].split("\t") if data_lines else []
    body = data_lines[1:] if len(data_lines) > 1 else []
    col_stats = {}
    sample_rows = body[: min(len(body), 5000)]
    for ci, cname in enumerate(header):
        vals = []
        for ln in sample_rows:
            parts = ln.split("\t")
            if ci < len(parts):
                try:
                    vals.append(float(parts[ci]))
                except ValueError:
                    pass
        if len(vals) >= max(10, int(0.5 * len(sample_rows))):
            col_stats[cname] = scale_stats(vals)
    return {
        "file": name,
        "n_comment_lines": len(comments),
        "comment_preview": comments[:8],
        "header_columns": header,
        "n_data_rows": len(body),
        "first_data_row": body[0].split("\t") if body else [],
        "numeric_column_scale_stats": col_stats,
    }
