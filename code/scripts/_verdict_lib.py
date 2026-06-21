#!/usr/bin/env python3
"""_verdict_lib.py — WP7 shared primitives for the verdict-bearing set-level
definitions, kept in ONE place so the locked rules cannot drift between scripts.

The load-bearing definition here is the **concordance-carrying set** (pre-reg:0002
"Concordance-carrying set", set-level — replaces the gene-level leading-edge term):
within one DB, a set is concordance-carrying iff it is **primary-concordant**
(same-sign NES in *both* PI-CFS-vs-HC and QFS-vs-HC, both non-NA) AND is
**nominally significant (fgsea p < nominal_p) in both** contrasts. It is the
denominator for the compartment 50%-marker rule (compartment.py) and the substrate
for theme roll-up (theme_rollup.py); both import it from here.

NA rule (pre-reg:0002 "NA / undefined NES handling"): a set with NA NES in a
contrast is *absent* — it cannot be primary-concordant and cannot be
concordance-carrying.
"""
from __future__ import annotations

import re
import sys

import pandas as pd

# collection prefixes stripped before theme/marker regex matching (pre-reg:0002
# "uppercased, collection prefix … stripped"). Hallmark/Reactome/GO-BP only.
_PREFIX_RE = re.compile(r"^(HALLMARK|REACTOME|GOBP)_")


def load_nes(path: str, db: str) -> pd.DataFrame:
    """Read one (contrast × DB) NES table (io_contract nes_columns), validating
    the db column and gene_set uniqueness. Returns the frame unchanged (NA NES
    preserved as NaN)."""
    df = pd.read_csv(path, sep="\t", dtype={"gene_set": str})
    if df.empty:
        sys.exit(f"[verdict_lib] empty NES table: {path}")
    bad = df.loc[df["db"] != db, "db"].unique()
    if len(bad):
        sys.exit(f"[verdict_lib] {path}: db column {bad} != expected {db}")
    if df["gene_set"].duplicated().any():
        sys.exit(f"[verdict_lib] {path}: duplicate gene_set keys")
    return df


def strip_prefix(set_name: str) -> str:
    """Uppercase a set name and strip its MSigDB collection prefix, the form the
    locked theme/marker regexes match against."""
    return _PREFIX_RE.sub("", set_name.upper())


def require_same_universe(frames, labels) -> None:
    """Fail-fast guard on the locked "one row per pinned set" contract: every NES
    table that feeds a verdict-bearing join MUST carry the IDENTICAL gene_set set
    (NES values may be NA, but no row may be missing). A truncated/short table
    here would otherwise silently drop or misclassify sets under an inner/left
    join — pre-reg:0002 fixes the universe, so a mismatch is a structural error,
    not something to paper over (Explicit > Defensive; fail early)."""
    base = frozenset(frames[0]["gene_set"])
    for lab, f in zip(labels[1:], frames[1:]):
        u = frozenset(f["gene_set"])
        if u != base:
            only_a = sorted(base - u)
            only_b = sorted(u - base)
            sys.exit(
                f"[verdict_lib] gene_set universe mismatch ({labels[0]} vs {lab}): "
                f"{len(only_a)} only in {labels[0]} (e.g. {only_a[:3]}), "
                f"{len(only_b)} only in {lab} (e.g. {only_b[:3]}) — the pinned "
                "'one row per set' contract is violated")


def primary_concordant(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    """Join two contrasts' NES tables (the x=PI-CFS-vs-HC, y=QFS-vs-HC arms) on the
    pinned universe and flag primary-concordant sets: same-sign NES in BOTH arms,
    both non-NA. NES == 0 carries no direction → not concordant. Returns one row
    per shared gene_set with nes_x/pval_x/nes_y/pval_y and a `concordant` bool."""
    require_same_universe([x, y], [x["contrast"].iloc[0], y["contrast"].iloc[0]])
    j = x[["gene_set", "NES", "pval"]].merge(
        y[["gene_set", "NES", "pval"]], on="gene_set", how="inner",
        suffixes=("_x", "_y"))
    same_sign = ((j["NES_x"] > 0) & (j["NES_y"] > 0)) | \
                ((j["NES_x"] < 0) & (j["NES_y"] < 0))
    j["concordant"] = same_sign.fillna(False)
    return j.rename(columns={
        "NES_x": "nes_x", "pval_x": "pval_x",
        "NES_y": "nes_y", "pval_y": "pval_y"})


def concordance_carrying(j: pd.DataFrame, nominal_p: float) -> pd.DataFrame:
    """Concordance-carrying subset of a primary_concordant() join: primary-concordant
    AND nominal fgsea p < nominal_p in BOTH contrasts. NA pval fails the gate."""
    sig_both = (j["pval_x"] < nominal_p) & (j["pval_y"] < nominal_p)
    carrying = j[j["concordant"] & sig_both.fillna(False)]
    return carrying.reset_index(drop=True)  # type: ignore[return-value]
