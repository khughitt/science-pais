# science:code
# status: workflow-owned
# task_ids: [t139]
# science:end
"""Parse GSE157007 series matrix -> donor map for the t139 pseudobulk (Step 2).

Emits donor_map.tsv (one row per GEO sample) with the fields the pseudobulk rule
needs: gsm, title, subject_id (donor), group, modality, and — for the scRNA GEX
samples — the in-tar barcodes/features/matrix basenames and the matrix format
(`tsv` for the F0xx submission, `mtx` for the later OH submission).

GEO messiness handled: the `!Sample_characteristics_ch1` rows are NOT key-aligned
across sample columns (subject-id / age-group / assay appear in different row
positions per sample), so each sample's characteristic cells are scanned for
`key: value` prefixes rather than read by row position.

Group/modality mapping (frozen): age group 'Frail' -> frail (case, 5 donors);
'Old' -> healthy-old (control, 6 donors); 'Young'/'Cord blood' -> dropped. Assay
'single-cell RNA' -> scRNA-GEX (kept [A1]); 'single-cell TCR'/'surface protein'
-> dropped. No PAIS/target data is touched here.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import os
import sys
from pathlib import Path

GROUP_MAP = {"frail": "frail", "old": "healthy-old"}          # kept groups
GEX_SUFFIX = "_scrna"   # scRNA GEX only [A1]; title suffix is the reliable marker
                        # (the later OH submission omits the `assay` characteristic,
                        # so assay-based filtering misclassifies its _vdj libraries)


def _cells(line: str) -> list[str]:
    """Split a !Sample_* line into unquoted cells (drop the leading key token)."""
    parts = line.rstrip("\n").split("\t")
    return [p.strip().strip('"') for p in parts[1:]]


def parse(series_matrix: Path) -> list[dict]:
    titles: list[str] = []
    gsms: list[str] = []
    char_rows: list[list[str]] = []
    suppl_rows: list[list[str]] = []

    with gzip.open(series_matrix, "rt") as fh:
        for line in fh:
            if line.startswith("!Sample_title\t"):
                titles = _cells(line)
            elif line.startswith("!Sample_geo_accession\t"):
                gsms = _cells(line)
            elif line.startswith("!Sample_characteristics_ch1\t"):
                char_rows.append(_cells(line))
            elif line.startswith("!Sample_supplementary_file"):
                suppl_rows.append(_cells(line))

    n = len(titles)
    if not (n and len(gsms) == n):
        raise SystemExit("parse: title/accession columns missing or misaligned")

    rows: list[dict] = []
    for i in range(n):
        # per-sample characteristics dict (scan all char rows for 'key: value')
        chars: dict[str, str] = {}
        for row in char_rows:
            if i < len(row) and ":" in row[i]:
                k, _, v = row[i].partition(":")
                chars[k.strip().lower()] = v.strip()
        # per-sample supplementary basenames (in-tar names are GSM-prefixed)
        suppl = [row[i] for row in suppl_rows if i < len(row) and row[i]]
        suppl_names = [os.path.basename(u) for u in suppl if u.upper() != "NONE"]

        age = chars.get("age group", "").strip().lower()
        assay = chars.get("assay", "").strip().lower()
        group = GROUP_MAP.get(age, "")
        title_l = titles[i].strip().lower()
        is_gex = title_l.endswith(GEX_SUFFIX)
        modality = "scRNA-GEX" if is_gex else (assay or title_l.split("_")[-1])

        def _find(token: str) -> str:
            hits = [s for s in suppl_names if token in s]
            return hits[0] if hits else ""

        matrix = _find("matrix")
        fmt = "mtx" if matrix.endswith(".mtx.gz") else ("tsv" if matrix.endswith(".tsv.gz") else "")

        rows.append({
            "gsm": gsms[i],
            "title": titles[i],
            "subject_id": chars.get("subject id", "") or titles[i].split("_")[0],
            "age_group": chars.get("age group", ""),
            "assay": assay,
            "group": group,
            "modality": modality,
            "barcodes_file": _find("barcodes"),
            "features_file": _find("features"),
            "matrix_file": matrix,
            "matrix_format": fmt,
            "keep": "1" if (is_gex and group in ("frail", "healthy-old")) else "0",
        })
    return rows


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--series-matrix", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    a = p.parse_args()

    rows = parse(a.series_matrix)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["gsm", "title", "subject_id", "age_group", "assay", "group",
            "modality", "barcodes_file", "features_file", "matrix_file",
            "matrix_format", "keep"]
    with a.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    kept = [r for r in rows if r["keep"] == "1"]
    frail = [r for r in kept if r["group"] == "frail"]
    old = [r for r in kept if r["group"] == "healthy-old"]
    fmts = sorted({r["matrix_format"] for r in kept})
    sys.stderr.write(
        f"[parse] {len(rows)} samples; kept {len(kept)} scRNA-GEX "
        f"({len(frail)} frail, {len(old)} healthy-old); matrix formats={fmts}\n"
    )
    # Fail early if the verified donor counts are not reproduced.
    if not (len(frail) == 5 and len(old) == 6):
        raise SystemExit(
            f"[parse] HALT: expected 5 frail / 6 healthy-old GEX donors, "
            f"got {len(frail)}/{len(old)} (metadata drift — re-verify before proceeding)."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
