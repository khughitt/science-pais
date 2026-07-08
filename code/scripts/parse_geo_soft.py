# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""parse_geo_soft — GEO family SOFT -> tidy per-sample metadata sheet.

WP1b tranche (a2): the group-metadata payload for `tar` deposits whose case/control
label lives ONLY in the family SOFT (not the expr payload, and — for multi-platform
deposits — not reachable via the plain series-matrix URL, which 404s). This is the
SOFT-format sibling of `parse_geo_metadata.py`: same tidy output contract, different
input grammar. A SOFT file is a sequence of per-sample blocks:

  ^SAMPLE = GSM3736559
  !Sample_title = ...
  !Sample_platform_id = GPLxxxx
  !Sample_characteristics_ch1 = subject status: Q Fever Fatigue Syndrom
  !Sample_characteristics_ch1 = donor id: 13135

so attributes are ` = `-delimited, one per line, scoped to the current `^SAMPLE`
block (vs the series matrix's one tab-delimited line per attribute across all
samples). It emits one tidy row per sample so `stage_matrix`'s `sheet` group_source
can join it to the tar's expr columns (by the GSM the tar member filename carries) and
apply the deposit's `level_map` / `group_regex`. The parser fabricates NO group label
— it emits every characteristic verbatim; stage_matrix owns the condition->arm map.

Emits <out-samples> (TSV), one row per sample in `^SAMPLE` order:
  sample     the GSM accession (the join key; the tar member filename carries it too)
  title      `!Sample_title`
  platform   `!Sample_platform_id` (the batch axis when a deposit spans >1 platform)
  <char>     one column per distinct `!Sample_characteristics_ch1` key (normalized),
             e.g. subject_status, donor_id, disease_state.

`_norm_key` mirrors parse_geo_metadata.py (kept local — the two stay decoupled;
Composition > Inheritance).
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


def _norm_key(k: str) -> str:
    """Characteristic key -> a stable, column-safe slug (spaces/punct -> _)."""
    k = k.strip().lower()
    k = re.sub(r"[^a-z0-9]+", "_", k).strip("_")
    return k or "characteristic"


def parse(path: Path) -> tuple[list[str], dict[str, dict[str, str]]]:
    """Return (sample_order, meta[sample][col]) from the SOFT per-sample blocks.

    sample_order is the `^SAMPLE = GSM...` order. Each sample carries title + platform
    + one entry per characteristic key (a `key: value` characteristic line). A repeated
    key within a sample keeps the last value seen (SOFT rarely repeats a key)."""
    sample_order: list[str] = []
    meta: dict[str, dict[str, str]] = {}
    cur: str | None = None

    with _open_maybe_gz(path) as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.startswith("^SAMPLE = "):
                cur = line.split(" = ", 1)[1].strip()
                if cur not in meta:
                    sample_order.append(cur)
                    meta[cur] = {}
            elif cur is None:
                continue
            elif line.startswith("^"):
                # a non-SAMPLE section (^SERIES, ^PLATFORM, ...) closes the sample scope
                cur = None
            elif line.startswith("!Sample_title = "):
                meta[cur]["title"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!Sample_platform_id = "):
                meta[cur]["platform"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!Sample_characteristics_ch1 = "):
                val = line.split(" = ", 1)[1].strip()
                if ":" in val:
                    key, v = val.split(":", 1)
                    meta[cur][_norm_key(key)] = v.strip()
                # a characteristic with no "key: value" shape carries no column name -> skip

    if not sample_order:
        sys.exit("[parse_geo_soft] HALT: no '^SAMPLE =' blocks — not a GEO family SOFT")
    return sample_order, meta


def run(in_path: Path, out_samples: Path) -> None:
    if not in_path.exists():
        sys.exit(f"[parse_geo_soft] HALT: missing {in_path}")
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
    print(f"[parse_geo_soft] {len(sample_order)} samples, cols={['sample'] + meta_cols}",
          file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description="GEO family SOFT -> tidy per-sample metadata sheet")
    ap.add_argument("--in", dest="in_path", required=True, type=Path)
    ap.add_argument("--out-samples", required=True, type=Path)
    args = ap.parse_args()
    run(args.in_path, args.out_samples)
    return 0


if __name__ == "__main__":
    sys.exit(main())
