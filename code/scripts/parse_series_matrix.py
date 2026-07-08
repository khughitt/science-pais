# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""parse_series_matrix — GEO series-matrix -> probe x sample table + inline samples.

WP1b tranche (c), microarray path. A GEO `*_series_matrix.txt.gz` carries BOTH the
per-sample metadata (as `!Sample_*` header lines) and the normalized probe x sample
value table (between `!series_matrix_table_begin/_end`) in ONE file, so — unlike the
per-sample RAW.tar deposits — its case/control grouping is resolvable INLINE with no
extra metadata payload. This parser is config-agnostic: it emits EVERY sample
characteristic verbatim as its own column (normalized key) so the downstream
`stage_matrix` prebuilt handler applies the deposit's `level_map` (raw condition ->
contrast arm) — the parser fabricates no group label.

Writes, into the deposit's processed dir:
  <out-expr>     probe x sample, as-deposited (probe ID_REF rows, sample columns);
                 NO probe->gene collapse / normalization (that is harmonize+collapse).
  <out-samples>  one row per sample: sample, title, platform, + one column per
                 distinct `!Sample_characteristics_ch1` key (e.g. twin_pair, sex,
                 diagnonsis[sic]). Column order = the value-table header order.

Deterministic gzip (mtime=0, no embedded name) so re-runs are byte-identical (KD10).
"""
from __future__ import annotations

import argparse
import gzip
import re
import sys
from pathlib import Path


def _open_maybe_gz(path: Path):
    with path.open("rb") as fh:
        magic = fh.read(2)
    if magic == b"\x1f\x8b":
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return path.open("rt", encoding="utf-8", errors="replace")


def _unquote(cells: list[str]) -> list[str]:
    return [c[1:-1] if len(c) >= 2 and c[0] == '"' and c[-1] == '"' else c for c in cells]


def _norm_key(k: str) -> str:
    """Characteristic key -> a stable, filesystem/column-safe slug (spaces/punct -> _)."""
    k = k.strip().lower()
    k = re.sub(r"[^a-z0-9]+", "_", k).strip("_")
    return k or "characteristic"


def parse(path: Path) -> tuple[list[str], dict[str, dict[str, str]], list[str], list[list[str]]]:
    """Return (sample_order, meta[sample][col], probe_header, probe_rows).

    meta carries title/platform + one entry per characteristic key. sample_order is
    taken from the value-table header (the authoritative expr column order); the
    `!Sample_geo_accession` order is asserted to match it."""
    titles: list[str] = []
    platforms: list[str] = []
    geo_acc: list[str] = []
    char_lines: list[list[str]] = []   # each: per-sample "key: value" cells
    probe_header: list[str] = []
    probe_rows: list[list[str]] = []
    in_table = False

    with _open_maybe_gz(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("!Sample_title\t"):
                titles = _unquote(line.split("\t")[1:])
            elif line.startswith("!Sample_geo_accession\t"):
                geo_acc = _unquote(line.split("\t")[1:])
            elif line.startswith("!Sample_platform_id\t"):
                platforms = _unquote(line.split("\t")[1:])
            elif line.startswith("!Sample_characteristics_ch1\t"):
                char_lines.append(_unquote(line.split("\t")[1:]))
            elif line.startswith("!series_matrix_table_begin"):
                in_table = True
            elif line.startswith("!series_matrix_table_end"):
                in_table = False
            elif in_table:
                cells = _unquote(line.split("\t"))
                if not probe_header:
                    probe_header = cells
                else:
                    probe_rows.append(cells)

    if not probe_header:
        sys.exit("[parse_series_matrix] HALT: no value table found (!series_matrix_table_begin)")
    sample_order = probe_header[1:]   # drop the ID_REF label
    if geo_acc and geo_acc != sample_order:
        sys.exit("[parse_series_matrix] HALT: !Sample_geo_accession order != value-table header order "
                 "— cannot align metadata to expression columns")

    n = len(sample_order)
    meta: dict[str, dict[str, str]] = {s: {} for s in sample_order}
    for i, s in enumerate(sample_order):
        meta[s]["title"] = titles[i] if i < len(titles) else ""
        meta[s]["platform"] = platforms[i] if i < len(platforms) else ""
    # characteristics: one column per distinct key; detect key from the "key: value" cells
    for cells in char_lines:
        if len(cells) != n:
            continue   # ragged characteristic line — skip rather than misalign
        keys = [c.split(":", 1)[0].strip() for c in cells if ":" in c]
        if not keys:
            continue
        key = _norm_key(max(set(keys), key=keys.count))   # modal key on the line
        for i, s in enumerate(sample_order):
            cell = cells[i]
            val = cell.split(":", 1)[1].strip() if ":" in cell else cell.strip()
            meta[s][key] = val
    return sample_order, meta, probe_header, probe_rows


def _write_gz(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as gz:
        gz.write(text.encode("utf-8"))


def run(in_path: Path, out_expr: Path, out_samples: Path) -> None:
    if not in_path.exists():
        sys.exit(f"[parse_series_matrix] HALT: missing {in_path}")
    sample_order, meta, _probe_header, probe_rows = parse(in_path)

    # probe x sample matrix (as-deposited)
    lines = ["\t".join(["ID_REF"] + sample_order) + "\n"]
    for row in probe_rows:
        lines.append("\t".join(row) + "\n")
    _write_gz(out_expr, "".join(lines))

    # samples sheet: sample + every metadata column (stable column order)
    meta_cols: list[str] = []
    for s in sample_order:
        for k in meta[s]:
            if k not in meta_cols:
                meta_cols.append(k)
    out_samples.parent.mkdir(parents=True, exist_ok=True)
    with out_samples.open("w", encoding="utf-8") as w:
        w.write("\t".join(["sample"] + meta_cols) + "\n")
        for s in sample_order:
            w.write("\t".join([s] + [meta[s].get(c, "") for c in meta_cols]) + "\n")

    print(f"[parse_series_matrix] {in_path.name}: {len(probe_rows)} probes x {len(sample_order)} samples; "
          f"characteristics={[c for c in meta_cols if c not in ('title', 'platform')]}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description="parse a GEO series-matrix into probe x sample + samples sheet")
    ap.add_argument("--in", dest="in_path", required=True, type=Path)
    ap.add_argument("--out-expr", required=True, type=Path)
    ap.add_argument("--out-samples", required=True, type=Path)
    args = ap.parse_args()
    run(args.in_path, args.out_expr, args.out_samples)
    return 0


if __name__ == "__main__":
    sys.exit(main())
