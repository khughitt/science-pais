#!/usr/bin/env python3
"""concordance.py — WP6: observed NES rank-concordance for ONE (pair × DB) cell.

Computes the Spearman ρ of NES between the two contrasts of a concordance pair
over the **shared testable gene-set universe**, using the WP5 fgsea NES tables
(the reported/headline NES, fgsea-multilevel). A gene-set enters ρ iff its NES is
non-NA in BOTH contrasts (the locked pairwise-exclusion rule: a set whose NES is
NA/undefined in either arm is "absent" — pre-reg:0002). This is the reported
effect size + the scatter; significance comes from permutation_null.R, whose own
rho_obs is fgseaSimple-consistent with its null (≈ this value to ~1e-3).

Outputs
  rho.tsv      : pair, db, rho_obs, n_shared, n_na_x, n_na_y, n_dropped_either
  scatter.tsv  : gene_set, contrast_x, contrast_y, nes_x, nes_y  (the ρ substrate;
                 feeds the report + single-set-dominance inspection)

The join key is gene_set exact-match within the db (io_contract). Full precision
on ρ/NES (fwrite-style): rounding only happens at the final verdict (KD10).
"""
import argparse
import sys

import pandas as pd
from scipy.stats import spearmanr

from _verdict_lib import require_same_universe


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--nes-x", required=True)
    p.add_argument("--nes-y", required=True)
    p.add_argument("--pair", required=True)
    p.add_argument("--db", required=True)
    p.add_argument("--out-rho", required=True)
    p.add_argument("--out-scatter", required=True)
    return p.parse_args()


def load_nes(path, db):
    df = pd.read_csv(path, sep="\t", dtype={"gene_set": str})
    if df.empty:
        sys.exit(f"[concordance] empty NES table: {path}")
    bad = df.loc[df["db"] != db, "db"].unique()
    if len(bad):
        sys.exit(f"[concordance] {path}: db column {bad} != expected {db}")
    if df["gene_set"].duplicated().any():
        sys.exit(f"[concordance] {path}: duplicate gene_set keys")
    return df


def main():
    a = parse_args()
    x = load_nes(a.nes_x, a.db)
    y = load_nes(a.nes_y, a.db)
    contrast_x = x["contrast"].iloc[0]
    contrast_y = y["contrast"].iloc[0]
    # the pinned universe must match exactly before the ρ join (one row per set);
    # a short/truncated table is a structural error, not a silent inner-join drop.
    require_same_universe([x, y], [contrast_x, contrast_y])

    n_na_x = int(x["NES"].isna().sum())
    n_na_y = int(y["NES"].isna().sum())

    # join on the full pinned universe (same db), then keep only sets testable in
    # BOTH arms (NES non-NA in each) — the locked pairwise-exclusion rule.
    j = x[["gene_set", "NES"]].merge(
        y[["gene_set", "NES"]], on="gene_set", how="inner",
        suffixes=("_x", "_y"))
    shared = j.dropna(subset=["NES_x", "NES_y"]).reset_index(drop=True)
    n_dropped_either = int(len(j) - len(shared))

    if len(shared) < 3:
        sys.exit(f"[concordance] {a.pair} x {a.db}: only {len(shared)} shared "
                 "testable sets — Spearman ρ undefined (need >= 3)")

    rho = spearmanr(shared["NES_x"].to_numpy(), shared["NES_y"].to_numpy()).statistic

    rho_tbl = pd.DataFrame([{
        "pair": a.pair, "db": a.db, "rho_obs": rho,
        "n_shared": len(shared), "n_na_x": n_na_x, "n_na_y": n_na_y,
        "n_dropped_either": n_dropped_either,
    }])
    rho_tbl.to_csv(a.out_rho, sep="\t", index=False, na_rep="NA")

    scatter = shared.rename(columns={"NES_x": "nes_x", "NES_y": "nes_y"}).copy()
    scatter.insert(1, "contrast_x", contrast_x)
    scatter.insert(2, "contrast_y", contrast_y)
    scatter = scatter.sort_values("gene_set").reset_index(drop=True)
    scatter[["gene_set", "contrast_x", "contrast_y", "nes_x", "nes_y"]].to_csv(
        a.out_scatter, sep="\t", index=False, na_rep="NA")

    print(f"[concordance] {a.pair} x {a.db}: rho_obs={rho:.6f} over "
          f"{len(shared)} shared sets (dropped {n_dropped_either}; "
          f"NA: x={n_na_x}, y={n_na_y})", file=sys.stderr)


if __name__ == "__main__":
    main()
