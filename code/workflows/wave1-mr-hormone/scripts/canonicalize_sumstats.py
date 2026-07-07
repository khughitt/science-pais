# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Canonicalize a raw harmonised GWAS-SSF sumstat to the lean MRlap schema (plan:0009 Task 4).

Streams one `*.h.tsv.gz` (stdlib `gzip` + `csv`, tab-delimited; no full load, no
pandas) through a source-family column map, injects the resolved total N as a
constant column, and writes a lean 8-column gz (`rsid chr pos a1 a2 beta se N`)
plus a `{out}.canonical.json` provenance sidecar. Dropping the ~15 unused
harmonised-SSF columns here means MRlap (which does its own strand/allele/NA
munging internally) never has to see them.

Two source families, each with a fixed column map onto the canonical schema:

  RUTH_MAP  — hm_-prefixed GWAS-Catalog harmonised SSF (Ruth SHBG/testosterone
              exposures). SE is flip-invariant, so the non-hm `standard_error`
              column is the correct pairing alongside the hm_ effect/allele
              columns (there is no `hm_standard_error`).
  HGI_MAP   — non-hm GWAS-Catalog harmonised SSF (HGI long-COVID outcome).

Three hard-stops, all loud non-zero exits (never a silent fallback):
  1. missing column  — any mapped source column absent from the raw header.
  2. unresolved N    — N not resolvable from config, non-integer, or <= 0.
  3. empty output    — 0 usable data rows survive dropping unusable rows (the drop
                        count, incl. the NA-rsid subcount, is always logged).

The adapter does no row-level QC beyond dropping unusable rows — a row whose rsid,
beta, or se is missing or an NA token ("NA"/"NaN"/"."/...) is dropped (see
_NA_TOKENS). MRlap munges the remaining strand/allele handling internally.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
from pathlib import Path

import yaml

RUTH_MAP = {  # hm_-prefixed GWAS-Catalog harmonised SSF (Ruth continuous traits)
    "rsid": "hm_rsid", "chr": "hm_chrom", "pos": "hm_pos",
    "a1": "hm_effect_allele", "a2": "hm_other_allele",  # a1 = effect allele (beta's ref)
    "beta": "hm_beta", "se": "standard_error",          # SE is flip-invariant; non-hm col is correct
}
HGI_MAP = {  # non-hm GWAS-Catalog harmonised SSF (HGI long-COVID outcome)
    "rsid": "rsid", "chr": "chromosome", "pos": "base_pair_location",
    "a1": "effect_allele", "a2": "other_allele",
    "beta": "beta", "se": "standard_error",
}
SOURCE_MAPS = {"ruth-exposure": RUTH_MAP, "hgi-outcome": HGI_MAP}
CANONICAL_COLUMNS = ("rsid", "chr", "pos", "a1", "a2", "beta", "se", "N")
_MAP_ORDER = ("rsid", "chr", "pos", "a1", "a2", "beta", "se")  # canonical order sans N

# Tokens that must NOT survive as an rsid/beta/se value. Harmonised GWAS-SSF writes
# the literal string "NA" for variants it could not map to an rsID; data.table::fread
# then reads "NA" -> real NA, and MRlap's run_MR does dplyr::inner_join(exposure,
# outcome, by="rsid") with na_matches="na" (NA matches NA) — so NA rsIDs surviving on
# BOTH sides would cartesian-explode the join (a genome-wide OOM). Dropping them here
# keeps the join clean and removes junk rows MRlap would process then discard.
_NA_TOKENS = {"", "na", "nan", ".", "none", "null"}


def _is_na(value: str) -> bool:
    return value.strip().lower() in _NA_TOKENS


def resolve_n(cfg: dict, source_family: str, stratum: str) -> int:
    """Resolve the total N to inject, per source family. HALTs on any ambiguity."""
    if source_family == "ruth-exposure":
        matches = [e for e in cfg.get("exposures", []) or [] if e.get("name") == stratum]
        if not matches:
            raise SystemExit(
                f"canonicalize: no exposures[] entry with name == {stratum!r} in config "
                f"— HALT (unresolved N)"
            )
        n = matches[0].get("n")
    elif source_family == "hgi-outcome":
        n = (cfg.get("outcome") or {}).get("total_n")
    else:
        raise SystemExit(f"canonicalize: unknown --source-family {source_family!r} — HALT")

    if n is None or isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise SystemExit(
            f"canonicalize: unresolved N for source-family={source_family!r} "
            f"stratum={stratum!r} (got {n!r}) — HALT (unresolved N)"
        )
    return n


def _cell(row: list[str], i: int) -> str:
    return row[i] if i < len(row) else ""


def canonicalize(source_family: str, stratum: str, in_path: str, out_path: str, cfg: dict) -> dict:
    colmap = SOURCE_MAPS.get(source_family)
    if colmap is None:
        raise SystemExit(f"canonicalize: unknown --source-family {source_family!r} — HALT")

    n_injected = resolve_n(cfg, source_family, stratum)

    with gzip.open(in_path, "rt", newline="") as in_fh:
        reader = csv.reader(in_fh, delimiter="\t")
        try:
            header = next(reader)
        except StopIteration:
            raise SystemExit(f"canonicalize: {in_path} is empty (no header row) — HALT")

        header_index = {name: i for i, name in enumerate(header)}
        missing = [src for src in colmap.values() if src not in header_index]
        if missing:
            raise SystemExit(
                f"canonicalize: source-family={source_family!r} stratum={stratum!r} is "
                f"missing column(s) {missing} in {in_path} header — HALT (missing column)"
            )
        idx = {canon: header_index[src] for canon, src in colmap.items()}

        n_rows_in = 0
        n_rows_out = 0
        n_dropped = 0
        n_dropped_na_rsid = 0
        out_p = Path(out_path)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(out_p, "wt", newline="") as out_fh:
            writer = csv.writer(out_fh, delimiter="\t", lineterminator="\n")
            writer.writerow(CANONICAL_COLUMNS)
            for row in reader:
                if not row:
                    continue
                n_rows_in += 1
                rsid = _cell(row, idx["rsid"])
                beta = _cell(row, idx["beta"])
                se = _cell(row, idx["se"])
                # Drop rows unusable as MR instruments: a missing/NA-token rsid (join
                # key), or a missing/NA-token beta/se (effect). See _NA_TOKENS above.
                if _is_na(rsid):
                    n_dropped += 1
                    n_dropped_na_rsid += 1
                    continue
                if _is_na(beta) or _is_na(se):
                    n_dropped += 1
                    continue
                out_row = [_cell(row, idx[c]) for c in _MAP_ORDER]
                out_row.append(str(n_injected))
                writer.writerow(out_row)
                n_rows_out += 1

    if n_rows_out == 0:
        out_p.unlink(missing_ok=True)  # never leave a silent empty artifact behind
        raise SystemExit(
            f"canonicalize: 0 usable data rows survived for {in_path} "
            f"(n_rows_in={n_rows_in}, n_dropped={n_dropped}) — HALT (empty output)"
        )

    sidecar = {
        "source_family": source_family,
        "stratum": stratum,
        "n_injected": n_injected,
        "n_rows_in": n_rows_in,
        "n_rows_out": n_rows_out,
        "n_dropped": n_dropped,
        "n_dropped_na_rsid": n_dropped_na_rsid,
        "columns_mapped": colmap,
    }
    Path(f"{out_path}.canonical.json").write_text(json.dumps(sidecar, indent=2))
    print(
        f"canonicalize: {stratum} ({source_family}) rows_in={n_rows_in} "
        f"rows_out={n_rows_out} dropped={n_dropped} (na_rsid={n_dropped_na_rsid}) N={n_injected}"
    )
    return sidecar


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--source-family", required=True, choices=sorted(SOURCE_MAPS))
    p.add_argument("--stratum", required=True)
    p.add_argument("--in", dest="in_path", required=True)
    p.add_argument("--out", dest="out_path", required=True)
    a = p.parse_args()

    cfg = yaml.safe_load(Path(a.config).read_text())
    canonicalize(a.source_family, a.stratum, a.in_path, a.out_path, cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
