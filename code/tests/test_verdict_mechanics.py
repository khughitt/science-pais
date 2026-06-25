# science:code
# status: library
# science:end

#!/usr/bin/env python3
"""Branch tests for the WP6/WP7 verdict mechanics (review WP6-7, Low finding).

Pytest-free by project convention (see test_qa_checkpoint.py): a plain script with
its own assertion counter that exits non-zero on any failure. Exercises the locked
decision logic at its boundaries — the cheap unit checks that the coherent
full-pipeline outputs alone do NOT prove:

  * missing-universe fail-fast (require_same_universe)            [Finding 1]
  * concordance-carrying p<0.05 boundary + concordant requirement
  * empty carrying set (no carrying → empty roll-up / cannot-fire)
  * S1/S2 presence predicate p-boundary + NA/sign handling
  * mixed-theme tie demotion (strict dominance)
  * direction-conflict DB-robustness
  * compartment marker 50% threshold

Run:  uv run --frozen --group pipeline python code/tests/test_verdict_mechanics.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from _verdict_lib import (  # noqa: E402
    concordance_carrying, primary_concordant, require_same_universe, strip_prefix,
)
from specificity import positive, spec_class  # noqa: E402
from theme_rollup import classify_theme  # noqa: E402
from db_robustness import robustness  # noqa: E402
from compartment import fire  # noqa: E402
from verdict import resolve, theme_sets_across_dbs  # noqa: E402

# locked resolution order (config.verdict.resolution_order / pre-reg:0002)
ORDER = [
    "model_inadequate_or_batch_confounded", "null_nonarbitrating",
    "compartment_confounded", "exposure_confounded", "shared_suggestive",
    "fragile", "exposure_confounded_residual",
]

_PASS = 0
_FAIL = 0


def expect(label: str, cond: bool) -> None:
    global _PASS, _FAIL
    if cond:
        _PASS += 1
        print(f"  ok   {label}")
    else:
        _FAIL += 1
        print(f"  FAIL {label}")


def raises_systemexit(fn) -> bool:
    try:
        fn()
        return False
    except SystemExit:
        return True


def nes_frame(contrast, rows):
    """rows: list of (gene_set, NES, pval) → a minimal io_contract NES frame."""
    return pd.DataFrame(
        [{"gene_set": g, "db": "hallmark", "contrast": contrast,
          "NES": n, "pval": p} for g, n, p in rows])


# --- Finding 1: universe equality fail-fast --------------------------------------
def test_universe_guard():
    a = nes_frame("x", [("S1", 1.0, 0.01), ("S2", 1.0, 0.01)])
    b = nes_frame("y", [("S1", 1.0, 0.01), ("S2", 1.0, 0.01)])
    short = nes_frame("y", [("S1", 1.0, 0.01)])  # missing S2
    expect("equal universes pass",
           require_same_universe([a, b], ["x", "y"]) is None)
    expect("short table exits (one row per pinned set)",
           raises_systemexit(lambda: require_same_universe([a, short], ["x", "y"])))
    # primary_concordant enforces it internally
    expect("primary_concordant fails fast on universe mismatch",
           raises_systemexit(lambda: primary_concordant(a, short)))


# --- concordance-carrying: p<0.05 boundary + concordant requirement --------------
def test_concordance_carrying():
    x = nes_frame("pi_cfs_vs_hc", [
        ("CONC_SIG",  1.5, 0.01),   # same sign as y, sig both → carrying
        ("CONC_BORD", 1.5, 0.05),   # p == 0.05 exactly → NOT < 0.05 → excluded
        ("ANTI",      1.5, 0.01),   # opposite sign in y → not concordant
        ("CONC_NSY",  1.5, 0.01),   # concordant but y not sig
    ])
    y = nes_frame("qfs_vs_hc", [
        ("CONC_SIG",  2.0, 0.02),
        ("CONC_BORD", 2.0, 0.01),
        ("ANTI",     -2.0, 0.01),
        ("CONC_NSY",  2.0, 0.20),
    ])
    carrying = set(concordance_carrying(primary_concordant(x, y), 0.05)["gene_set"])
    expect("carrying = sig-both same-sign only", carrying == {"CONC_SIG"})
    expect("p==0.05 excluded (strict <)", "CONC_BORD" not in carrying)
    expect("anti-concordant excluded", "ANTI" not in carrying)
    expect("one-arm-nonsig excluded", "CONC_NSY" not in carrying)
    # empty carrying when every set sign-flips vs x (all-positive) → none concordant
    allneg = nes_frame("qfs_vs_hc", [("CONC_SIG", -2.0, 0.02), ("CONC_BORD", -2.0, 0.01),
                                     ("ANTI", -2.0, 0.01), ("CONC_NSY", -2.0, 0.20)])
    expect("anti-correlated → empty carrying",
           concordance_carrying(primary_concordant(x, allneg), 0.05).empty)


# --- S1/S2 presence predicate + per-set class ------------------------------------
def test_specificity():
    expect("positive: same sign, p<0.05", positive(1, 1, 0.049, 0.05) is True)
    expect("positive: p==0.05 boundary is False", positive(1, 1, 0.05, 0.05) is False)
    expect("positive: opposite sign is False", positive(1, -1, 0.001, 0.05) is False)
    expect("positive: NA p is False", positive(1, 1, pd.NA, 0.05) is False)
    expect("positive: NA ref dir is False", positive(pd.NA, 1, 0.001, 0.05) is False)
    expect("class fatigue-specific = S1 ∧ ¬S2",
           spec_class(True, False, True) == "fatigue-specific")
    expect("class exposure_sequela = S2 (even if S1)",
           spec_class(True, True, True) == "exposure_sequela")
    expect("class unresolved = neither", spec_class(False, False, True) == "unresolved")
    expect("class absent = no direction", spec_class(True, False, False) == "absent")


# --- theme roll-up strict dominance (mixed-theme tie demotion) --------------------
def test_theme_rollup():
    expect("fs>es → fatigue-specific", classify_theme(2, 1) == "fatigue-specific")
    expect("fs==es tie → exposure_sequela (demote)",
           classify_theme(2, 2) == "exposure_sequela")
    expect("es>fs → exposure_sequela", classify_theme(1, 3) == "exposure_sequela")
    expect("no fs/es → unresolved", classify_theme(0, 0) == "unresolved")
    expect("single fs, zero es → fatigue-specific", classify_theme(1, 0) == "fatigue-specific")


# --- DB-robustness direction-consistent recurrence -------------------------------
def test_db_robustness():
    r, d = robustness([1, 1], 2)
    expect("2 DBs same sign → robust(+)", r is True and d == 1)
    r, d = robustness([1, -1], 2)
    expect("2 DBs opposite sign → NOT robust", r is False and pd.isna(d))
    r, d = robustness([1, 1, -1], 2)
    expect("3 DBs +,+,- → robust on +", r is True and d == 1)
    r, _ = robustness([1], 2)
    expect("1 DB → not robust (below min_dbs)", r is False)
    r, d = robustness([-1, -1, -1], 2)
    expect("3 DBs all - → robust on -", r is True and d == -1)


# --- compartment marker 50% threshold --------------------------------------------
def test_compartment():
    conf, status, _ = fire(0, 0, 0.50)
    expect("empty carrying → cannot fire", conf is False and status == "cannot_fire_empty_carrying")
    conf, status, _ = fire(4, 2, 0.50)
    expect("exactly 50% → fires (>=)", conf is True and status == "fired")
    conf, status, _ = fire(4, 1, 0.50)
    expect("25% → not marker-dominated", conf is False and status == "not_marker_dominated")


# --- strip_prefix ----------------------------------------------------------------
def test_strip_prefix():
    expect("HALLMARK_ stripped + upper", strip_prefix("HALLMARK_GLYCOLYSIS") == "GLYCOLYSIS")
    expect("REACTOME_ stripped", strip_prefix("REACTOME_TCA_CYCLE") == "TCA_CYCLE")
    expect("GOBP_ stripped", strip_prefix("GOBP_INNATE_IMMUNE_RESPONSE") == "INNATE_IMMUNE_RESPONSE")
    expect("non-collection prefix untouched", strip_prefix("KEGG_FOO") == "KEGG_FOO")


# --- WP8 resolution walk: exercise EACH label path (plan:0003 WP8 DoD) -----------
def resolve_full(**kw):
    base = dict(resolution_order=ORDER, limma_ok=True, batch_confounded=False,
                p_perm=0.01, alpha=0.05, compartment_confounded=False,
                fatigue_specific_themes=set(), exposure_sequela_themes=set(),
                db_robust_themes=set())
    base.update(kw)
    return resolve(**base)


def resolve_label(**kw):
    label, trace = resolve_full(**kw)
    n_decided = sum(1 for t in trace if t["decided"])
    return label, n_decided


def test_resolution_paths():
    # step 1 — both legs
    lab, n = resolve_label(limma_ok=False)
    expect("limma fail → model_inadequate", lab == "model_inadequate_or_batch_confounded" and n == 1)
    lab, _ = resolve_label(batch_confounded=True)
    expect("batch → model_inadequate", lab == "model_inadequate_or_batch_confounded")
    # step 2 — the actual t035 outcome (p_perm >= alpha)
    lab, n = resolve_label(p_perm=0.949)
    expect("p_perm>=alpha → null_nonarbitrating (exactly one decided)",
           lab == "null_nonarbitrating" and n == 1)
    # step 3
    lab, _ = resolve_label(compartment_confounded=True)
    expect("marker-dominated → compartment_confounded", lab == "compartment_confounded")
    # step 4
    lab, _ = resolve_label(exposure_sequela_themes={"innate/IFN"})
    expect("no fs + exposure theme → exposure_confounded", lab == "exposure_confounded")
    # step 5
    lab, _ = resolve_label(fatigue_specific_themes={"mitochondrial/OXPHOS"},
                           db_robust_themes={"mitochondrial/OXPHOS"})
    expect("DB-robust fatigue theme → shared_suggestive", lab == "shared_suggestive")
    # step 6
    lab, _ = resolve_label(fatigue_specific_themes={"mitochondrial/OXPHOS"})
    expect("fatigue theme not DB-robust → fragile", lab == "fragile")
    # step 7 — terminal fall-through
    lab, _ = resolve_label()  # p<alpha, no compartment, no fs/es themes
    expect("all unresolved → exposure_confounded_residual",
           lab == "exposure_confounded_residual")
    # compartment precedes exposure (ordering): both true → compartment wins
    lab, _ = resolve_label(compartment_confounded=True,
                           exposure_sequela_themes={"innate/IFN"})
    expect("compartment precedes exposure (step order)", lab == "compartment_confounded")


def test_trace_honesty():
    # the t035 run: null_nonarbitrating decides at step 2; later steps must be
    # NOT reached and NOT fired — esp. the terminal residual must not spuriously
    # report fired:true with a 'p_perm<alpha' reason (review WP8 Medium-1).
    _, trace = resolve_full(p_perm=0.949)
    by = {t["label"]: t for t in trace}
    expect("step 2 decided", by["null_nonarbitrating"]["decided"] is True)
    expect("residual NOT fired after decision",
           by["exposure_confounded_residual"]["fired"] is False)
    expect("residual NOT reached after decision",
           by["exposure_confounded_residual"]["reached"] is False)
    expect("exactly one step fired", sum(1 for t in trace if t["fired"]) == 1)
    expect("no fired step is unreached",
           all(t["reached"] for t in trace if t["fired"]))
    expect("post-decision reason says not reached",
           "not reached" in by["compartment_confounded"]["reason"])


def test_cross_db_theme_sets():
    import pandas as pd
    # a theme fatigue-specific ONLY in Reactome+GO-BP (not Hallmark) must still be
    # captured — the union must not be Hallmark-narrowed (review WP8 Medium-2).
    df = pd.DataFrame([
        {"theme": "mitochondrial/OXPHOS", "db": "reactome",
         "theme_class": "fatigue-specific", "verdict_eligible": True},
        {"theme": "mitochondrial/OXPHOS", "db": "gobp",
         "theme_class": "fatigue-specific", "verdict_eligible": True},
        {"theme": "innate/IFN", "db": "hallmark",
         "theme_class": "exposure_sequela", "verdict_eligible": True},
        {"theme": "other", "db": "gobp",
         "theme_class": "fatigue-specific", "verdict_eligible": False},  # ineligible
    ])
    fs, es = theme_sets_across_dbs(df)
    expect("cross-DB: Reactome+GO-BP-only fatigue theme captured",
           fs == {"mitochondrial/OXPHOS"})
    expect("cross-DB: exposure theme captured", es == {"innate/IFN"})
    expect("'other' (ineligible) excluded from fatigue set", "other" not in fs)
    fs0, es0 = theme_sets_across_dbs(pd.DataFrame())
    expect("empty themes → empty sets", fs0 == set() and es0 == set())


def main() -> int:
    for t in (test_universe_guard, test_concordance_carrying, test_specificity,
              test_theme_rollup, test_db_robustness, test_compartment, test_strip_prefix,
              test_resolution_paths, test_trace_honesty, test_cross_db_theme_sets):
        print(f"\n[{t.__name__}]")
        t()
    print(f"\n{_PASS} passed, {_FAIL} failed")
    return 1 if _FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
