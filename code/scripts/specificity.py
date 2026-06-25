# science:code
# status: exploratory
# science:end

#!/usr/bin/env python3
"""specificity.py — WP7: per-set specificity class for ONE DB (pre-reg:0002
"Specificity metric", fully thresholded — the QFS-vs-QS presence backbone).

For every gene-set in the DB, evaluate the two locked presence predicates against
the set's **QFS-vs-HC NES direction** (the reference direction):

  S1-positive (fatigue presence, QFS-vs-QS) ≡ same-sign NES as QFS-vs-HC AND
                                              nominal fgsea p < nominal_p
  S2-positive (exposure presence, QS-vs-HC) ≡ same-sign NES as QFS-vs-HC AND
                                              nominal fgsea p < nominal_p

  per-set class: fatigue-specific ≡ S1+ AND NOT S2+
                 exposure_sequela ≡ S2+            (regardless of S1)
                 unresolved       ≡ neither

NA rule (pre-reg:0002): a set with NA QFS-vs-HC NES has no reference direction →
class `absent` (it cannot be primary-concordant, so it is never counted in the
roll-up anyway). A set with NA NES in QFS-vs-QS / QS-vs-HC simply cannot be S1/S2
positive. The class is computed for EVERY set here; the concordance-carrying
restriction that decides which classes count toward the verdict is applied
downstream (theme_rollup.py), keeping this rule's inputs to the three contrasts
it needs.

Output: {db}.classes.tsv — gene_set, db, nes_qfs_vs_hc, dir_qfs_vs_hc,
nes_qfs_vs_qs, p_qfs_vs_qs, s1_pos, nes_qs_vs_hc, p_qs_vs_hc, s2_pos, spec_class.
Full precision (rounding only at the final verdict, KD10).
"""
import argparse
import sys

import pandas as pd

from _verdict_lib import load_nes, require_same_universe


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--qfs-vs-hc", required=True, help="reference-direction contrast")
    p.add_argument("--qfs-vs-qs", required=True, help="S1 fatigue presence contrast")
    p.add_argument("--qs-vs-hc", required=True, help="S2 exposure presence contrast")
    p.add_argument("--db", required=True)
    p.add_argument("--nominal-p", type=float, required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()


def direction(nes):
    """Sign of an NES as -1/+1, or NA where NES is NA/0 (no carried direction)."""
    if pd.isna(nes) or nes == 0:
        return pd.NA
    return 1 if nes > 0 else -1


def positive(ref_dir, d, p, thr):
    """Locked presence predicate: same-sign-as-reference AND nominal p < thr. Any
    NA operand (no reference direction, NA NES, or NA p) is a clean False — never
    positive (pre-reg:0002 NA rule)."""
    if pd.isna(ref_dir) or pd.isna(d) or pd.isna(p):
        return False
    return (d == ref_dir) and (p < thr)


def spec_class(s1_pos, s2_pos, has_dir):
    """Locked per-set specificity class (pre-reg:0002): fatigue-specific ≡ S1+ ∧ ¬S2+;
    exposure_sequela ≡ S2+ (regardless of S1); unresolved ≡ neither. A set with no
    QFS-vs-HC reference direction (NA NES) is `absent` — it can never be concordant."""
    if not has_dir:
        return "absent"
    if s1_pos and not s2_pos:
        return "fatigue-specific"
    if s2_pos:
        return "exposure_sequela"
    return "unresolved"


def main():
    a = parse_args()
    ref = load_nes(a.qfs_vs_hc, a.db)
    s1 = load_nes(a.qfs_vs_qs, a.db)
    s2 = load_nes(a.qs_vs_hc, a.db)
    # all three contrasts must span the identical pinned universe before the join,
    # else a short table would misclassify (silently drop) sets (fail early).
    require_same_universe([ref, s1, s2], [a.qfs_vs_hc, a.qfs_vs_qs, a.qs_vs_hc])

    # align all three on the pinned universe (same db, identical gene_set set)
    m = ref[["gene_set", "NES"]].rename(columns={"NES": "nes_qfs_vs_hc"})
    m = m.merge(
        s1[["gene_set", "NES", "pval"]].rename(
            columns={"NES": "nes_qfs_vs_qs", "pval": "p_qfs_vs_qs"}),
        on="gene_set", how="left")
    m = m.merge(
        s2[["gene_set", "NES", "pval"]].rename(
            columns={"NES": "nes_qs_vs_hc", "pval": "p_qs_vs_hc"}),
        on="gene_set", how="left")

    rows = []
    for r in m.itertuples(index=False):
        ref_dir = direction(r.nes_qfs_vs_hc)
        s1_pos = positive(ref_dir, direction(r.nes_qfs_vs_qs),
                          r.p_qfs_vs_qs, a.nominal_p)
        s2_pos = positive(ref_dir, direction(r.nes_qs_vs_hc),
                          r.p_qs_vs_hc, a.nominal_p)

        cls = spec_class(s1_pos, s2_pos, has_dir=not pd.isna(ref_dir))

        rows.append({
            "gene_set": r.gene_set, "db": a.db,
            "nes_qfs_vs_hc": r.nes_qfs_vs_hc, "dir_qfs_vs_hc": ref_dir,
            "nes_qfs_vs_qs": r.nes_qfs_vs_qs, "p_qfs_vs_qs": r.p_qfs_vs_qs,
            "s1_pos": s1_pos,
            "nes_qs_vs_hc": r.nes_qs_vs_hc, "p_qs_vs_hc": r.p_qs_vs_hc,
            "s2_pos": s2_pos,
            "spec_class": cls,
        })

    out = pd.DataFrame(rows, columns=[
        "gene_set", "db", "nes_qfs_vs_hc", "dir_qfs_vs_hc",
        "nes_qfs_vs_qs", "p_qfs_vs_qs", "s1_pos",
        "nes_qs_vs_hc", "p_qs_vs_hc", "s2_pos", "spec_class"])
    out = out.sort_values("gene_set").reset_index(drop=True)
    out.to_csv(a.out, sep="\t", index=False, na_rep="NA")

    counts = out["spec_class"].value_counts().to_dict()
    print(f"[specificity] {a.db}: {len(out)} sets — "
          f"fatigue-specific={counts.get('fatigue-specific', 0)}, "
          f"exposure_sequela={counts.get('exposure_sequela', 0)}, "
          f"unresolved={counts.get('unresolved', 0)}, "
          f"absent={counts.get('absent', 0)}", file=sys.stderr)


if __name__ == "__main__":
    main()
