# science:code
# status: exploratory
# science:end

#!/usr/bin/env python3
"""theme_rollup.py — WP7: strict-dominance theme roll-up for ONE DB (pre-reg:0002
"Theme roll-up", dominance rule).

Restricts to the DB's **concordance-carrying sets** (primary-concordant ∧ p<nominal
in both PI-CFS-vs-HC and QFS-vs-HC — the single locked definition in _verdict_lib),
assigns each to its locked theme (the precomputed theme_map.tsv, which mirrors the
pre-reg theme map verbatim), folds in the per-set specificity class (specificity.py),
and rolls each theme up by STRICT DOMINANCE:

  fatigue-specific theme ≡ (#fatigue-specific sets) >  (#exposure_sequela sets)
  exposure_sequela theme ≡ (#exposure_sequela sets) >= (#fatigue-specific sets) AND >=1
  unresolved theme       ≡ no fatigue-specific and no exposure_sequela set

Theme-level NES direction (locked) = sign of the QFS-vs-HC NES of the theme's
fatigue-specific concordance-carrying set with the largest |NES| (the representative
set); NA where the theme has no fatigue-specific set. The `other` catch-all theme is
ineligible to carry a verdict theme (verdict_eligible=False) but is still reported.

Output: {db}.themes.tsv — theme, db, n_carrying, n_fatigue_specific,
n_exposure_sequela, n_unresolved, theme_class, theme_direction, verdict_eligible,
rep_set. Emits a header-only file when no set is concordance-carrying.
"""
import argparse
import sys

import pandas as pd

from _verdict_lib import concordance_carrying, load_nes, primary_concordant

COLUMNS = ["theme", "db", "n_carrying", "n_fatigue_specific",
           "n_exposure_sequela", "n_unresolved", "theme_class",
           "theme_direction", "verdict_eligible", "rep_set"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--classes", required=True, help="specificity.py {db}.classes.tsv")
    p.add_argument("--nes-x", required=True, help="PI-CFS-vs-HC NES (primary x arm)")
    p.add_argument("--nes-y", required=True, help="QFS-vs-HC NES (primary y arm)")
    p.add_argument("--theme-map", required=True, help="locked theme_map.tsv")
    p.add_argument("--db", required=True)
    p.add_argument("--nominal-p", type=float, required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()


def classify_theme(n_fs, n_es):
    """Locked strict-dominance theme class (pre-reg:0002): fatigue-specific iff
    #fatigue-specific > #exposure_sequela; exposure_sequela iff #es >= #fs and >=1
    (so a tie demotes to exposure_sequela); else unresolved."""
    if n_fs > n_es:
        return "fatigue-specific"
    if n_es >= n_fs and n_es >= 1:
        return "exposure_sequela"
    return "unresolved"


def theme_direction(rows):
    """Sign of the QFS-vs-HC NES of the fatigue-specific set with the largest
    |NES| (the representative set). Returns (direction, rep_set_name) or
    (NA, NA) when the theme has no fatigue-specific carrying set."""
    fs = rows[rows["spec_class"] == "fatigue-specific"]
    if fs.empty:
        return pd.NA, pd.NA
    rep = fs.loc[fs["nes_y"].abs().idxmax()]
    return (1 if rep["nes_y"] > 0 else -1), rep["gene_set"]


def main():
    a = parse_args()
    x = load_nes(a.nes_x, a.db)
    y = load_nes(a.nes_y, a.db)
    classes = pd.read_csv(a.classes, sep="\t", dtype={"gene_set": str})
    tmap = pd.read_csv(a.theme_map, sep="\t", dtype={"gene_set": str})
    tmap = tmap[tmap["db"] == a.db][["gene_set", "theme"]]

    carrying = concordance_carrying(primary_concordant(x, y), a.nominal_p)

    if carrying.empty:
        pd.DataFrame(columns=COLUMNS).to_csv(a.out, sep="\t", index=False, na_rep="NA")
        print(f"[theme_rollup] {a.db}: 0 concordance-carrying sets — "
              "empty roll-up (compartment cannot fire; no theme carries)",
              file=sys.stderr)
        return

    # join theme + specificity class onto the carrying sets (nes_y = QFS-vs-HC NES,
    # used for the theme-direction representative).
    cc = carrying[["gene_set", "nes_y"]].merge(tmap, on="gene_set", how="left")
    cc = cc.merge(classes[["gene_set", "spec_class"]], on="gene_set", how="left")
    if cc["theme"].isna().any():
        missing = cc.loc[cc["theme"].isna(), "gene_set"].tolist()
        sys.exit(f"[theme_rollup] {a.db}: {len(missing)} carrying sets absent from "
                 f"theme_map.tsv (e.g. {missing[:3]}) — theme assignment incomplete")
    if cc["spec_class"].isna().any():
        missing = cc.loc[cc["spec_class"].isna(), "gene_set"].tolist()
        sys.exit(f"[theme_rollup] {a.db}: {len(missing)} carrying sets absent from the "
                 f"specificity classes table (e.g. {missing[:3]}) — classes truncated")

    rows = []
    for theme, grp in cc.groupby("theme", sort=True):
        n_fs = int((grp["spec_class"] == "fatigue-specific").sum())
        n_es = int((grp["spec_class"] == "exposure_sequela").sum())
        n_un = int((grp["spec_class"] == "unresolved").sum())
        theme_class = classify_theme(n_fs, n_es)
        tdir, rep = theme_direction(grp)
        rows.append({
            "theme": theme, "db": a.db, "n_carrying": int(len(grp)),
            "n_fatigue_specific": n_fs, "n_exposure_sequela": n_es,
            "n_unresolved": n_un, "theme_class": theme_class,
            "theme_direction": tdir,
            "verdict_eligible": theme != "other",
            "rep_set": rep,
        })

    out = pd.DataFrame(rows, columns=COLUMNS).sort_values("theme").reset_index(drop=True)
    out.to_csv(a.out, sep="\t", index=False, na_rep="NA")

    fs_themes = out[(out["theme_class"] == "fatigue-specific") & out["verdict_eligible"]]
    print(f"[theme_rollup] {a.db}: {len(carrying)} carrying sets over {len(out)} "
          f"themes; fatigue-specific verdict-eligible themes="
          f"{fs_themes['theme'].tolist()}", file=sys.stderr)


if __name__ == "__main__":
    main()
