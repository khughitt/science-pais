#!/usr/bin/env python3
"""compartment.py — WP7: cell-type-marker compartment check on the PRIMARY DB
(pre-reg:0002 `compartment_confounded`, resolution step 3).

Computes the Hallmark **concordance-carrying sets** (the single locked definition in
_verdict_lib: primary-concordant ∧ nominal p<nominal_p in both PI-CFS-vs-HC and
QFS-vs-HC) and fires `compartment_confounded` iff **>=fraction of those carrying sets
are compartment markers** by the locked marker regex (matched against the prefix-
stripped, uppercased set name, case-insensitive). If the concordance-carrying list is
empty the rule **cannot fire** (no sets to be marker-dominated) — a locked outcome,
reported as status `cannot_fire_empty_carrying`.

Output: compartment.tsv — db, n_carrying, n_marker, marker_fraction,
compartment_confounded, status, marker_sets.
"""
import argparse
import re
import sys

import pandas as pd

from _verdict_lib import concordance_carrying, load_nes, primary_concordant, strip_prefix


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--nes-x", required=True, help="PI-CFS-vs-HC NES (primary DB)")
    p.add_argument("--nes-y", required=True, help="QFS-vs-HC NES (primary DB)")
    p.add_argument("--db", required=True, help="primary DB (hallmark)")
    p.add_argument("--marker-regex", required=True)
    p.add_argument("--fraction", type=float, required=True)
    p.add_argument("--nominal-p", type=float, required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()


def main():
    a = parse_args()
    x = load_nes(a.nes_x, a.db)
    y = load_nes(a.nes_y, a.db)
    marker = re.compile(a.marker_regex, re.IGNORECASE)

    carrying = concordance_carrying(primary_concordant(x, y), a.nominal_p)
    n_carrying = int(len(carrying))

    marker_hits = [s for s in carrying["gene_set"]
                   if marker.search(strip_prefix(s))]
    n_marker = len(marker_hits)

    if n_carrying == 0:
        marker_fraction = pd.NA
        confounded = False
        status = "cannot_fire_empty_carrying"
    else:
        marker_fraction = n_marker / n_carrying
        confounded = marker_fraction >= a.fraction
        status = "fired" if confounded else "not_marker_dominated"

    out = pd.DataFrame([{
        "db": a.db, "n_carrying": n_carrying, "n_marker": n_marker,
        "marker_fraction": marker_fraction, "compartment_confounded": confounded,
        "status": status, "marker_sets": ";".join(sorted(marker_hits)),
    }])
    out.to_csv(a.out, sep="\t", index=False, na_rep="NA")

    print(f"[compartment] {a.db}: {n_marker}/{n_carrying} concordance-carrying sets "
          f"are markers → compartment_confounded={confounded} ({status})",
          file=sys.stderr)


if __name__ == "__main__":
    main()
