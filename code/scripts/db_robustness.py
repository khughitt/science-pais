# science:code
# status: exploratory
# science:end

#!/usr/bin/env python3
"""db_robustness.py — WP7: cross-DB theme robustness (pre-reg:0002 "DB-robustness —
direction-consistent recurrence").

A fatigue-specific theme "recurs across >=2 DBs" (the `shared_suggestive`
requirement) IFF it is a fatigue-specific theme in >=min_dbs of {Hallmark, Reactome,
GO-BP} AND its theme-level NES direction is the SAME SIGN in those DBs. This is a
theme-sign-only rule: there is deliberately **NO per-DB ρ-direction gate** here (the
primary ρ test lives in the concordance/permutation rules; robustness re-derives
theme classes per DB and checks recurrence + sign agreement).

Reads the three per-DB theme roll-ups (theme_rollup.py {db}.themes.tsv). For each
verdict-eligible theme that is fatigue-specific in >=1 DB, groups the fatigue-specific
DBs by theme-direction sign; the theme is db-robust iff the largest same-sign group
reaches min_dbs. (A theme fatigue-specific in 3 DBs as +,+,- is robust on +; in 2 DBs
as +,- it is not — opposite-direction recurrence is not robust biology.)

Output: db_robustness.tsv — theme, n_dbs_fatigue_specific, dbs_fatigue_specific,
fs_directions, robust_direction, db_robust.
"""
import argparse
import sys

import pandas as pd

COLUMNS = ["theme", "n_dbs_fatigue_specific", "dbs_fatigue_specific",
           "fs_directions", "robust_direction", "db_robust"]


def robustness(dirs, min_dbs):
    """Locked direction-consistent recurrence (pre-reg:0002): given the theme-level
    NES directions (+1/-1) of the DBs in which the theme is fatigue-specific, the
    theme is db-robust iff the largest same-sign group reaches min_dbs. Returns
    (db_robust: bool, robust_direction: +1/-1 or pd.NA). A 2-DB +/- conflict is NOT
    robust; a 3-DB +,+,- is robust on +."""
    pos = sum(1 for d in dirs if d > 0)
    neg = sum(1 for d in dirs if d < 0)
    if max(pos, neg) >= min_dbs:
        return True, (1 if pos >= neg else -1)
    return False, pd.NA


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--themes", nargs="+", required=True,
                   help="per-DB theme_rollup outputs ({db}.themes.tsv)")
    p.add_argument("--min-dbs", type=int, required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()


def main():
    a = parse_args()
    frames = [pd.read_csv(p, sep="\t", dtype={"theme": str}) for p in a.themes]
    allt = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

    # fatigue-specific, verdict-eligible theme occurrences only
    fs = allt[(allt["theme_class"] == "fatigue-specific")
              & (allt["verdict_eligible"] == True)] if not allt.empty else allt  # noqa: E712

    rows = []
    if not fs.empty:
        for theme, grp in fs.groupby("theme", sort=True):
            grp = grp.sort_values("db")
            dirs = grp["theme_direction"].astype(int).tolist()
            dbs = grp["db"].tolist()
            db_robust, robust_direction = robustness(dirs, a.min_dbs)
            rows.append({
                "theme": theme,
                "n_dbs_fatigue_specific": int(len(grp)),
                "dbs_fatigue_specific": ",".join(dbs),
                "fs_directions": ",".join(f"{db}:{d:+d}" for db, d in zip(dbs, dirs)),
                "robust_direction": robust_direction,
                "db_robust": db_robust,
            })

    out = pd.DataFrame(rows, columns=COLUMNS).sort_values("theme").reset_index(drop=True)
    out.to_csv(a.out, sep="\t", index=False, na_rep="NA")

    robust = out.loc[out["db_robust"] == True, "theme"].tolist()  # noqa: E712
    print(f"[db_robustness] {len(out)} fatigue-specific themes across DBs; "
          f"db-robust (>={a.min_dbs} same-sign DBs): {robust}", file=sys.stderr)


if __name__ == "__main__":
    main()
