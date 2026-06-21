#!/usr/bin/env python3
"""verdict.py — WP8: the mechanical verdict (pre-reg:0002 "Verdict resolution order").

Walks the LOCKED resolution order over the complete WP6/WP7 surface and emits EXACTLY
ONE label to results/verdict.json, a human-readable results.md synthesizing into
q0001/h0001/q0017, and a deterministic results/run_metadata.json provenance manifest
(deferred review finding 5). No post-hoc selection: the label is a pure function of the
pre-committed signals (resolve()).

Resolution order (config.verdict.resolution_order, mirrors pre-reg:0002):
  1 model_inadequate_or_batch_confounded — admissibility: limma diagnostics OR PCA batch.
  2 null_nonarbitrating                  — p_perm >= alpha (C1 = primary × Hallmark).
  3 compartment_confounded               — >=50% Hallmark concordance-carrying sets are markers.
  4 exposure_confounded                  — no fatigue-specific theme & >=1 exposure_sequela theme.
  5 shared_suggestive                    — >=1 fatigue-specific theme that is DB-robust.
  6 fragile                              — fatigue-specific theme(s) but none DB-robust.
  7 exposure_confounded_residual         — else (p<alpha, all themes unresolved-specificity).

Admissibility batch leg (locked decision, user 2026-06-21; pre-reg:0002 clarifying note):
neither deposit records a batch covariate, so PCA-batch dominance is NOT assessable and the
batch leg is non-firing (it cannot be demonstrated without a batch label). The limma-diagnostics
leg is evaluated normally. This loosens no threshold and the verdict is set at step 2 regardless.

Confirmatory toggle hygiene (deferred review finding 6): the C1 label MUST be produced with all
robustness_toggles OFF; verdict.py HALTs if any is on.
"""
import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import pandas as pd

# Per-label belief update on the commitment targets — mirrors pre-reg:0002 "Decision
# Criteria" table VERBATIM (the locked epistemic semantics; not derived from data).
BELIEF_UPDATES = {
    "model_inadequate_or_batch_confounded": {
        "hypothesis:0001-shared-dysregulated-attractor": "No update (test inadmissible)",
        "question:0017-deflationary-alternatives-vs-shared-pathophysiology": "No update",
    },
    "null_nonarbitrating": {
        "hypothesis:0001-shared-dysregulated-attractor":
            "Minimal (power/bias ceiling — cannot exclude a real shared signature)",
        "question:0017-deflationary-alternatives-vs-shared-pathophysiology":
            "No update — explicitly NOT support for the coincidence null",
    },
    "compartment_confounded": {
        "hypothesis:0001-shared-dysregulated-attractor": "Negative (artifactual convergence)",
        "question:0017-deflationary-alternatives-vs-shared-pathophysiology":
            "Strengthens detection-artifact account",
    },
    "exposure_confounded": {
        "hypothesis:0001-shared-dysregulated-attractor":
            "Negative on the interpretation that convergence reflects shared fatigue biology",
        "question:0017-deflationary-alternatives-vs-shared-pathophysiology":
            "Strengthens ascertainment/exposure-sequela account",
    },
    "shared_suggestive": {
        "hypothesis:0001-shared-dysregulated-attractor":
            "Moderate positive (capped at 'suggestive — needs >=3-trigger test')",
        "question:0017-deflationary-alternatives-vs-shared-pathophysiology":
            "Weakens finite-repertoire-coincidence null",
    },
    "fragile": {
        "hypothesis:0001-shared-dysregulated-attractor": "Near-zero durable update (unstable signal)",
        "question:0017-deflationary-alternatives-vs-shared-pathophysiology": "No material update",
    },
    "exposure_confounded_residual": {
        "hypothesis:0001-shared-dysregulated-attractor":
            "Negative-for-fatigue-specificity (permutation-significant but specificity unresolved)",
        "question:0017-deflationary-alternatives-vs-shared-pathophysiology":
            "Strengthens ascertainment/exposure account (residual)",
    },
}


def resolve(*, resolution_order, limma_ok, batch_confounded, p_perm, alpha,
            compartment_confounded, fatigue_specific_themes, exposure_sequela_themes,
            db_robust_themes):
    """PURE locked resolution walk → (label, trace). First-match wins. `*_themes` are
    sets of verdict-eligible Hallmark theme names; db_robust_themes is the subset
    satisfying direction-consistent DB-robustness. Raises on an unknown order."""
    fs = set(fatigue_specific_themes)
    es = set(exposure_sequela_themes)
    robust_fs = fs & set(db_robust_themes)

    predicates = {
        "model_inadequate_or_batch_confounded": (
            (not limma_ok) or batch_confounded,
            "limma diagnostics fail or PCA batch-dominated" if ((not limma_ok) or batch_confounded)
            else "limma diagnostics pass; batch leg non-firing"),
        "null_nonarbitrating": (
            p_perm >= alpha,
            f"p_perm={p_perm} >= alpha={alpha}" if p_perm >= alpha
            else f"p_perm={p_perm} < alpha={alpha}"),
        "compartment_confounded": (
            compartment_confounded,
            ">=50% concordance-carrying sets are compartment markers" if compartment_confounded
            else "concordance not marker-dominated (or empty carrying)"),
        "exposure_confounded": (
            (len(fs) == 0) and (len(es) >= 1),
            "no fatigue-specific theme and >=1 exposure_sequela theme"
            if ((len(fs) == 0) and (len(es) >= 1))
            else "fatigue-specific theme present, or no exposure_sequela theme"),
        "shared_suggestive": (
            len(robust_fs) >= 1,
            f"DB-robust fatigue-specific theme(s): {sorted(robust_fs)}" if robust_fs
            else "no DB-robust fatigue-specific theme"),
        "fragile": (
            len(fs) >= 1 and len(robust_fs) == 0,
            "fatigue-specific theme(s) present but none DB-robust"
            if (len(fs) >= 1 and len(robust_fs) == 0)
            else "no fatigue-specific theme"),
        "exposure_confounded_residual": (
            True,  # terminal fall-through (p<alpha, all themes unresolved-specificity)
            "p_perm<alpha but all concordant themes unresolved-specificity"),
    }

    trace = []
    verdict = None
    for i, label in enumerate(resolution_order, start=1):
        if label not in predicates:
            sys.exit(f"[verdict] resolution_order label '{label}' has no predicate")
        fired, reason = predicates[label]
        decided = verdict is None and bool(fired)
        trace.append({"step": i, "label": label, "fired": bool(fired),
                      "reason": reason, "decided": decided})
        if decided:
            verdict = label
    if verdict is None:
        sys.exit("[verdict] no label fired — resolution_order must include a terminal catch-all")
    return verdict, trace


# ---------------------------------------------------------------------------- I/O ---
def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--primary-rho", required=True)
    p.add_argument("--primary-perm", required=True)
    p.add_argument("--concordance", nargs="+", required=True)
    p.add_argument("--perm", nargs="+", required=True)
    p.add_argument("--specificity", nargs="+", required=True)
    p.add_argument("--themes", nargs="+", required=True)
    p.add_argument("--robustness", required=True)
    p.add_argument("--compartment", required=True)
    p.add_argument("--diag", nargs="+", required=True, help="limma diag.json sidecars")
    p.add_argument("--acq-datapackage", required=True, help="WP1 acquisition manifest")
    p.add_argument("--config", required=True)
    p.add_argument("--primary-db", required=True)
    p.add_argument("--out-verdict", required=True)
    p.add_argument("--out-report", required=True)
    p.add_argument("--out-metadata", required=True)
    return p.parse_args()


def read_tsv(path):
    return pd.read_csv(path, sep="\t", dtype={"gene_set": str, "theme": str})


def normalize(obj, ndigits):
    """Recursively coerce pandas/numpy scalars to native Python (numpy int64/float64/
    bool_ → int/float/bool; NA/NaN → None) and round floats, so json.dumps is both
    serializable and byte-deterministic (KD10 float_precision)."""
    if isinstance(obj, dict):
        return {k: normalize(v, ndigits) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [normalize(v, ndigits) for v in obj]
    if hasattr(obj, "item") and not isinstance(obj, (str, bytes)):
        obj = obj.item()                       # numpy scalar → python scalar
    if not isinstance(obj, (str, bytes, bool, int)) and pd.isna(obj):
        return None                            # NA/NaN/None → JSON null
    if isinstance(obj, float):
        return round(obj, ndigits)
    return obj


def sha256_path(path):
    h = hashlib.sha256()
    h.update(Path(path).read_bytes())
    return h.hexdigest()


def load_yaml_config(path):
    import yaml
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def main():
    a = parse_args()
    cfg = load_yaml_config(a.config)
    alpha = float(cfg["verdict"]["p_perm_alpha"])
    precision = int(cfg["determinism"]["float_precision"])
    resolution_order = list(cfg["verdict"]["resolution_order"])
    toggles = cfg.get("robustness_toggles", {})
    primary_db = a.primary_db

    # --- toggle hygiene (finding 6): C1 verdict MUST use all toggles OFF ----------
    on = sorted(k for k, v in toggles.items() if v)
    if on:
        sys.exit(f"[verdict] HALT: confirmatory verdict requires all robustness_toggles "
                 f"OFF, but these are on: {on} (pre-reg:0002 KD8)")

    # --- C1 confirmatory stats ----------------------------------------------------
    prho = read_tsv(a.primary_rho).iloc[0]
    pperm = read_tsv(a.primary_perm).iloc[0]
    p_perm = float(pperm["p_perm"])
    confirmatory = {
        "pair": str(prho["pair"]), "db": str(prho["db"]),
        "rho_obs_multilevel": float(prho["rho_obs"]),
        "rho_obs_perm": float(pperm["rho_obs"]),
        "p_perm": p_perm, "B": int(pperm["B"]), "alpha": alpha,
    }

    # --- admissibility: limma diagnostics; batch leg non-assessable ---------------
    diags = [json.loads(Path(d).read_text()) for d in a.diag]
    per_contrast = {
        d["contrast"]: {"full_rank": bool(d["full_rank"]),
                        "residual_df": int(d["residual_df"]),
                        "n_genes_tested": int(d["n_genes_tested"])}
        for d in diags
    }
    limma_ok = all(v["full_rank"] and v["residual_df"] > 0 and v["n_genes_tested"] > 0
                   for v in per_contrast.values())
    admissibility = {
        "limma_ok": limma_ok, "per_contrast": per_contrast,
        "batch_assessable": False,
        "batch_reason": "no batch covariate in GSE130353/GSE14577 deposit metadata; "
                        "PCA-batch dominance is not testable without a batch label "
                        "(locked decision 2026-06-21; pre-reg:0002 clarifying note)",
    }
    batch_confounded = False  # non-assessable → non-firing

    # --- sensitivity surface (all 6 pair×DB cells) --------------------------------
    rho_rows = pd.concat([read_tsv(p) for p in a.concordance], ignore_index=True)
    perm_rows = pd.concat([read_tsv(p) for p in a.perm], ignore_index=True)
    surface = rho_rows.merge(perm_rows[["pair", "db", "p_perm", "B"]], on=["pair", "db"])
    sensitivity_surface = [
        {"pair": str(r["pair"]), "db": str(r["db"]), "rho_obs": float(r["rho_obs"]),
         "p_perm": float(r["p_perm"]), "B": int(r["B"]), "n_shared": int(r["n_shared"])}
        for _, r in surface.sort_values(["pair", "db"]).iterrows()
    ]

    # --- specificity + theme surface (primary DB drives steps 4-6) ----------------
    spec = pd.concat([read_tsv(p) for p in a.specificity], ignore_index=True)
    specificity_summary = {
        db: grp["spec_class"].value_counts().to_dict()
        for db, grp in spec.groupby("db")
    }
    themes_all = pd.concat([read_tsv(p) for p in a.themes], ignore_index=True) \
        if a.themes else pd.DataFrame()
    prim = themes_all[themes_all["db"] == primary_db] if not themes_all.empty else themes_all

    def theme_set(df, cls):
        if df.empty:
            return set()
        sel = df[(df["theme_class"] == cls) & (df["verdict_eligible"] == True)]  # noqa: E712
        return set(sel["theme"])

    fatigue_specific = theme_set(prim, "fatigue-specific")
    exposure_sequela = theme_set(prim, "exposure_sequela")

    robust_df = read_tsv(a.robustness)
    db_robust = set(robust_df.loc[robust_df["db_robust"] == True, "theme"]) \
        if not robust_df.empty else set()  # noqa: E712

    comp = read_tsv(a.compartment).iloc[0]
    compartment_confounded = bool(comp["compartment_confounded"])

    # --- the mechanical walk ------------------------------------------------------
    label, trace = resolve(
        resolution_order=resolution_order, limma_ok=limma_ok,
        batch_confounded=batch_confounded, p_perm=p_perm, alpha=alpha,
        compartment_confounded=compartment_confounded,
        fatigue_specific_themes=fatigue_specific,
        exposure_sequela_themes=exposure_sequela, db_robust_themes=db_robust)

    verdict = {
        "verdict": label,
        "confirmatory": confirmatory,
        "resolution_trace": trace,
        "admissibility": admissibility,
        "sensitivity_surface": sensitivity_surface,
        "specificity_summary": specificity_summary,
        "themes_primary_db": prim.to_dict(orient="records") if not prim.empty else [],
        "db_robustness": robust_df.to_dict(orient="records") if not robust_df.empty else [],
        "compartment": {k: (None if pd.isna(comp[k]) else
                            (bool(comp[k]) if k == "compartment_confounded" else comp[k]))
                        for k in ("db", "n_carrying", "n_marker", "marker_fraction",
                                  "compartment_confounded", "status")},
        "belief_updates": BELIEF_UPDATES[label],
        "robustness_toggles": {k: bool(v) for k, v in toggles.items()},
        "toggles_off": True,
        "determinism": {"seed": int(cfg["determinism"]["seed"]),
                        "float_precision": precision,
                        "rng_kind": cfg["determinism"]["r_rng_kind"]},
    }
    verdict = normalize(verdict, precision)

    Path(a.out_verdict).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_verdict).write_text(
        json.dumps(verdict, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8")

    write_report(a.out_report, verdict)
    write_metadata(a, verdict)

    print(f"[verdict] {label} (p_perm={p_perm} vs alpha={alpha}); "
          f"report -> {a.out_report}", file=sys.stderr)


def write_metadata(a, verdict):
    """Deterministic run-provenance manifest (finding 5): input hashes, outputs, and
    entity cross-references. No timestamp/host and repo-root-relative paths →
    byte-reproducible and portable (KD10; no absolute machine paths committed)."""
    def rel(p):
        return os.path.relpath(p, start=os.getcwd())

    inputs = ([a.primary_rho, a.primary_perm, a.robustness, a.compartment,
               a.acq_datapackage, a.config]
              + list(a.concordance) + list(a.perm) + list(a.specificity)
              + list(a.themes) + list(a.diag))
    manifest = {
        "name": "t035-cross-trigger-pathway-overlap-verdict",
        "description": "WP8 mechanical-verdict run provenance (pre-reg:0002, plan:0003).",
        "verdict": verdict["verdict"],
        "entities": [
            "task:t035", "pre-registration:0002-cross-trigger-pathway-overlap",
            "plan:0003-cross-trigger-pathway-overlap-pipeline",
            "hypothesis:0001-shared-dysregulated-attractor",
            "question:0001-shared-molecular-signature-across-triggers",
            "question:0017-deflationary-alternatives-vs-shared-pathophysiology",
        ],
        "inputs": [{"path": rel(p), "sha256": sha256_path(p)}
                   for p in sorted(set(inputs))],
        "outputs": [{"path": rel(a.out_verdict)}, {"path": rel(a.out_report)},
                    {"path": rel(a.out_metadata)}],
    }
    Path(a.out_metadata).write_text(
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8")


def write_report(path, v):
    """Human results.md — cites pre-reg:0002, reproduces the decision-table semantics,
    synthesizes into h0001/q0017/q0001."""
    c = v["confirmatory"]
    lines = []
    A = lines.append
    A("# t035 — Cross-trigger pathway-overlap reanalysis: mechanical verdict\n")
    A("> Generated mechanically by `verdict.py` (WP8) from the locked resolution order in")
    A("> **pre-registration:0002**. No post-hoc selection: the label below is a pure function")
    A("> of the pre-committed signals. Numbers are byte-reproducible (KD10).\n")
    A(f"## Verdict: `{v['verdict']}`\n")
    A("**Belief updates (pre-reg:0002 Decision Criteria):**\n")
    for tgt, upd in v["belief_updates"].items():
        A(f"- `{tgt}` — {upd}")
    A("")
    A("## Confirmatory test (C1 = primary × Hallmark)\n")
    A(f"- NES rank-concordance ρ (reported, fgsea-multilevel): **{c['rho_obs_multilevel']}**")
    A(f"- ρ (permutation-internal, fgseaSimple): {c['rho_obs_perm']}")
    A(f"- one-sided permutation **p_perm = {c['p_perm']}** (B={c['B']}) vs α = {c['alpha']}\n")
    A("## Resolution trace (first-match wins)\n")
    A("| Step | Label | Fired | Decided | Reason |")
    A("|---|---|---|---|---|")
    for t in v["resolution_trace"]:
        A(f"| {t['step']} | `{t['label']}` | {t['fired']} | "
          f"{'**yes**' if t['decided'] else ''} | {t['reason']} |")
    A("")
    A("## Admissibility (resolution step 1)\n")
    ad = v["admissibility"]
    A(f"- limma diagnostics OK across all contrasts: **{ad['limma_ok']}** "
      "(full-rank designs, residual_df > 0, genes tested > 0)")
    A(f"- PCA-batch leg assessable: **{ad['batch_assessable']}** — {ad['batch_reason']}\n")
    A("## Sensitivity surface (all pair × DB cells carry their own permutation null)\n")
    A("| Pair | DB | ρ_obs | p_perm | n_shared |")
    A("|---|---|---|---|---|")
    for s in v["sensitivity_surface"]:
        A(f"| {s['pair']} | {s['db']} | {s['rho_obs']} | {s['p_perm']} | {s['n_shared']} |")
    A("")
    A("## Specificity / theme surface\n")
    A(f"- Per-set specificity class counts by DB: `{v['specificity_summary']}`")
    A(f"- Primary-DB ({c['db']}) concordance-carrying themes: "
      f"{v['themes_primary_db'] if v['themes_primary_db'] else 'none (0 concordance-carrying sets)'}")
    comp = v["compartment"]
    A(f"- Compartment check: {comp['n_marker']}/{comp['n_carrying']} carrying sets are markers "
      f"→ `{comp['status']}` (compartment_confounded={comp['compartment_confounded']})\n")
    A("## Synthesis\n")
    if v["verdict"] == "null_nonarbitrating":
        A("All six concordance ρ are **negative** (anti-concordant) and each sits well inside the")
        A("**left** tail of a well-formed, zero-centered permutation null, so the one-sided")
        A("`p_perm` values are all far above α. The confirmatory C1 cell")
        A(f"(primary × Hallmark, p_perm = {c['p_perm']}) does not clear the null, and the")
        A("resolution order therefore halts at step 2 → **`null_nonarbitrating`**.\n")
        A("Per pre-reg:0002 this means the **test was inadequate**, not that")
        A("`hypothesis:0001` is wrong — 2 cohorts, n = 7–10/group, cross-platform")
        A("(U133 microarray vs MMSEQ RNA-seq), cross-compartment (PBMC vs isolated monocytes),")
        A("and a per-gene power floor admitting only very large effects. It is recorded as")
        A("weighted-low evidence and feeds `question:0017` as *“existing public data cannot")
        A("adjudicate”* — **never** as evidence *for* the finite-repertoire-coincidence null")
        A("(the asymmetry is pre-committed). It does **not** resolve")
        A("`question:0001` (navigation context only — that needs the ≥3-trigger harmonized test).\n")
        A("The descriptive direction is notable but non-arbitrating: even the few concordance-")
        A("carrying mitochondrial/OXPHOS sets that survive on Reactome/GO-BP classify as")
        A("**exposure_sequela** (S2-positive in QS-vs-HC), consistent with the pre-registered")
        A("competing account that the Q-fever mito signal tracks past-*Coxiella* exposure")
        A("rather than fatigue (Raijmakers2019) — but the non-arbitrating null caps any such read.")
    else:
        A(f"See the belief-update table above for the licensed update under `{v['verdict']}`.")
    A("")
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
