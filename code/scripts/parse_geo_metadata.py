# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""parse_geo_metadata — GEO series-matrix -> tidy per-sample metadata sheet.

WP1b tranche (a): the group-metadata payload for RNA-seq deposits whose case/control
label lives in the series-matrix `!Sample_*` header (NOT in the expr payload's column
names). Unlike the microarray path (`parse_series_matrix.py`), this parser reads ONLY
the header block — an RNA-seq series matrix carries an EMPTY value table (the counts
ship as a separate suppl file), so there is no probe×sample matrix to emit. It writes
one tidy metadata row per sample so `stage_matrix`'s `sheet` group_source can join it
to the expr columns and apply the deposit's `level_map` / `group_regex` (raw condition
-> contrast arm). The parser fabricates NO group label — it emits every characteristic
verbatim and stage_matrix owns the condition->arm mapping.

Emits <out-samples> (TSV), one row per sample in `!Sample_geo_accession` order:
  sample     the GSM accession (stable identity; not necessarily the expr column name)
  title      `!Sample_title` (often the expr column name, e.g. GSE128078 "Sample_G1-1")
  platform   `!Sample_platform_id` (the batch axis when a deposit spans >1 platform)
  <char>     one column per distinct `!Sample_characteristics_ch1` key (normalized),
             e.g. sample_id (GSE270045 expr column), disease_state, timepoint_day.

`_unquote`/`_norm_key` mirror parse_series_matrix.py (kept local: this is the
header-only sibling, so the two stay decoupled — Composition > Inheritance).
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
    """Characteristic key -> a stable, column-safe slug (spaces/punct -> _)."""
    k = k.strip().lower()
    k = re.sub(r"[^a-z0-9]+", "_", k).strip("_")
    return k or "characteristic"


def parse(path: Path) -> tuple[list[str], dict[str, dict[str, str]]]:
    """Return (sample_order, meta[sample][col]) from the series-matrix header block.

    sample_order comes from `!Sample_geo_accession` (the authoritative sample axis for
    an RNA-seq series matrix, whose value table is empty). Each sample carries title +
    platform + one entry per characteristic key."""
    titles: list[str] = []
    platforms: list[str] = []
    geo_acc: list[str] = []
    char_lines: list[list[str]] = []

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

    if not geo_acc:
        sys.exit("[parse_geo_metadata] HALT: no !Sample_geo_accession header — not a GEO series matrix")
    sample_order = geo_acc
    n = len(sample_order)

    meta: dict[str, dict[str, str]] = {s: {} for s in sample_order}
    for i, s in enumerate(sample_order):
        meta[s]["title"] = titles[i] if i < len(titles) else ""
        meta[s]["platform"] = platforms[i] if i < len(platforms) else ""
    # characteristics: one column per distinct key; key detected from the "key: value" cells.
    for cells in char_lines:
        if len(cells) != n:
            # fail-closed: a series matrix must carry exactly one characteristics cell
            # per sample. A ragged line means the file is truncated/corrupt or our split
            # is wrong — silently skipping it is invisible provenance loss.
            sys.exit(f"[parse_geo_metadata] HALT: ragged !Sample_characteristics_ch1 line "
                     f"({len(cells)} cells, expected {n}) — malformed series matrix")
        keys = [c.split(":", 1)[0].strip() for c in cells if ":" in c]
        if not keys:
            continue
        key = _norm_key(max(set(keys), key=keys.count))   # modal key on the line
        for i, s in enumerate(sample_order):
            cell = cells[i]
            val = cell.split(":", 1)[1].strip() if ":" in cell else cell.strip()
            meta[s][key] = val
    return sample_order, meta


def run(in_path: Path, out_samples: Path) -> None:
    if not in_path.exists():
        sys.exit(f"[parse_geo_metadata] HALT: missing {in_path}")
    sample_order, meta = parse(in_path)

    meta_cols: list[str] = []
    for s in sample_order:
        for k in meta[s]:
            if k not in meta_cols:
                meta_cols.append(k)
    out_samples.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_samples.with_name(out_samples.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as w:
        w.write("\t".join(["sample"] + meta_cols) + "\n")
        for s in sample_order:
            w.write("\t".join([s] + [meta[s].get(c, "") for c in meta_cols]) + "\n")
    tmp.replace(out_samples)

    print(f"[parse_geo_metadata] {in_path.name}: {len(sample_order)} samples; "
          f"characteristics={[c for c in meta_cols if c not in ('title', 'platform')]}",
          file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description="parse a GEO series-matrix header into a per-sample metadata sheet")
    ap.add_argument("--in", dest="in_path", required=True, type=Path)
    ap.add_argument("--out-samples", required=True, type=Path)
    args = ap.parse_args()
    run(args.in_path, args.out_samples)
    return 0


if __name__ == "__main__":
    sys.exit(main())
