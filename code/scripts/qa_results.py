# science:code
# status: exploratory
# task_ids: [t035, t063]
# science:end

#!/usr/bin/env python3
"""Build-fatal result QA for the t035 pathway-overlap workflow.

This checkpoint validates downstream substrates and the terminal verdict surface:
tables must satisfy their schema/key/numeric contracts, expected contrast/pair/db
cardinality must be complete, and verdict.json must trace back to the generated
rho/perm/diagnostic/specificity/roll-up artifacts.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


FLOAT_TOL = 1e-6


class ResultQA:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.facts: dict[str, Any] = {}

    def check(self, condition: bool, message: str) -> None:
        if not condition:
            self.failures.append(message)

    def warn(self, condition: bool, message: str) -> None:
        if not condition:
            self.warnings.append(message)


def read_tsv(path: Path, qa: ResultQA, label: str) -> pd.DataFrame:
    if not path.exists():
        qa.failures.append(f"{label}: missing file {path}")
        return pd.DataFrame()
    try:
        return pd.read_csv(path, sep="\t")
    except Exception as exc:  # pragma: no cover - defensive parsing context.
        qa.failures.append(f"{label}: could not parse TSV {path}: {exc}")
        return pd.DataFrame()


def read_json(path: Path, qa: ResultQA, label: str) -> dict[str, Any]:
    if not path.exists():
        qa.failures.append(f"{label}: missing file {path}")
        return {}
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive parsing context.
        qa.failures.append(f"{label}: could not parse JSON {path}: {exc}")
        return {}
    if not isinstance(obj, dict):
        qa.failures.append(f"{label}: JSON root must be an object")
        return {}
    return obj


def require_columns(df: pd.DataFrame, cols: list[str], qa: ResultQA, label: str) -> bool:
    missing = [c for c in cols if c not in df.columns]
    qa.check(not missing, f"{label}: missing required column(s): {missing}")
    return not missing


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def non_na_numeric(series: pd.Series) -> pd.Series:
    vals = numeric(series)
    return vals[~vals.isna()]


def check_finite(df: pd.DataFrame, cols: list[str], qa: ResultQA, label: str) -> None:
    for col in cols:
        vals = numeric(df[col])
        qa.check(vals.notna().all(), f"{label}: {col} must be numeric and non-NA")
        qa.check(vals.map(math.isfinite).all(), f"{label}: {col} must be finite")


def check_probability(df: pd.DataFrame, cols: list[str], qa: ResultQA, label: str) -> None:
    for col in cols:
        vals = non_na_numeric(df[col])
        qa.check(((vals >= 0.0) & (vals <= 1.0)).all(), f"{label}: {col} must be in [0, 1]")


def check_signed_unit(df: pd.DataFrame, cols: list[str], qa: ResultQA, label: str) -> None:
    for col in cols:
        vals = non_na_numeric(df[col])
        qa.check(((vals >= -1.0) & (vals <= 1.0)).all(), f"{label}: {col} must be in [-1, 1]")


def bool_values(series: pd.Series) -> set[bool]:
    out: set[bool] = set()
    for value in series.dropna():
        if isinstance(value, bool):
            out.add(value)
        elif str(value) == "True":
            out.add(True)
        elif str(value) == "False":
            out.add(False)
    return out


def bool_mask(series: pd.Series) -> pd.Series:
    return series.map(lambda value: value is True or str(value) == "True")


def as_float(value: Any) -> float:
    if value is None or pd.isna(value):
        return math.nan
    return float(value)


def approx_equal(left: Any, right: Any, tol: float = FLOAT_TOL) -> bool:
    lf = as_float(left)
    rf = as_float(right)
    if math.isnan(lf) and math.isnan(rf):
        return True
    return math.isfinite(lf) and math.isfinite(rf) and abs(lf - rf) <= tol


def check_de(processed: Path, contrasts: list[str], qa: ResultQA) -> dict[str, dict[str, Any]]:
    diags: dict[str, dict[str, Any]] = {}
    ranked_cols = ["gene_id", "logFC", "t", "P.Value", "adj.P.Val"]
    for contrast in contrasts:
        label = f"DE {contrast}"
        ranked = read_tsv(processed / "de" / f"{contrast}.ranked.tsv", qa, label)
        if require_columns(ranked, ranked_cols, qa, label):
            qa.check(not ranked.empty, f"{label}: ranked table is empty")
            qa.check(not ranked["gene_id"].duplicated().any(), f"{label}: duplicate gene_id keys")
            check_finite(ranked, ["logFC", "t"], qa, label)
            check_probability(ranked, ["P.Value", "adj.P.Val"], qa, label)

        diag = read_json(processed / "de" / f"{contrast}.diag.json", qa, f"DE diag {contrast}")
        if diag:
            diags[contrast] = diag
            qa.check(diag.get("contrast") == contrast, f"DE diag {contrast}: contrast field mismatch")
            qa.check(isinstance(diag.get("full_rank"), bool), f"DE diag {contrast}: full_rank must be boolean")
            qa.check(as_float(diag.get("residual_df")) > 0, f"DE diag {contrast}: residual_df must be > 0")
            qa.check(as_float(diag.get("n_genes_tested")) > 0, f"DE diag {contrast}: n_genes_tested must be > 0")
            if not ranked.empty and "gene_id" in ranked.columns:
                qa.check(
                    int(diag.get("n_genes_tested", -1)) == len(ranked),
                    f"DE diag {contrast}: n_genes_tested must equal ranked row count",
                )
    qa.facts["de_contrasts_checked"] = len(contrasts)
    return diags


def check_fgsea(processed: Path, contrasts: list[str], dbs: list[str], qa: ResultQA) -> None:
    cols = ["gene_set", "db", "contrast", "NES", "pval", "padj", "size"]
    universe_by_db: dict[str, set[str]] = {}
    for contrast in contrasts:
        for db in dbs:
            label = f"fgsea {contrast} x {db}"
            df = read_tsv(processed / "fgsea" / f"{contrast}.{db}.nes.tsv", qa, label)
            if not require_columns(df, cols, qa, label):
                continue
            qa.check(not df.empty, f"{label}: NES table is empty")
            qa.check(not df["gene_set"].duplicated().any(), f"{label}: duplicate gene_set keys")
            qa.check((df["db"] == db).all(), f"{label}: db column mismatch")
            qa.check((df["contrast"] == contrast).all(), f"{label}: contrast column mismatch")
            check_probability(df, ["pval", "padj"], qa, label)
            vals = non_na_numeric(df["NES"])
            qa.check(vals.map(math.isfinite).all(), f"{label}: NES values must be finite or NA")
            sizes = non_na_numeric(df["size"])
            qa.check((sizes > 0).all(), f"{label}: size must be > 0 where present")
            observed = set(df["gene_set"].astype(str))
            prior = universe_by_db.setdefault(db, observed)
            qa.check(observed == prior, f"{label}: gene-set universe differs within db")
    qa.facts["fgsea_cells_checked"] = len(contrasts) * len(dbs)


def check_concordance_and_perm(
    processed: Path,
    pairs: dict[str, dict[str, str]],
    dbs: list[str],
    expected_b: int,
    qa: ResultQA,
) -> tuple[dict[tuple[str, str], dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    rho_rows: dict[tuple[str, str], dict[str, Any]] = {}
    perm_rows: dict[tuple[str, str], dict[str, Any]] = {}
    rho_cols = ["pair", "db", "rho_obs", "n_shared", "n_na_x", "n_na_y", "n_dropped_either"]
    scatter_cols = ["gene_set", "contrast_x", "contrast_y", "nes_x", "nes_y"]
    perm_cols = ["pair", "db", "rho_obs", "p_perm", "B"]
    null_cols = ["perm_index", "rho_perm"]
    for pair, arms in pairs.items():
        for db in dbs:
            key = (pair, db)
            label = f"concordance {pair} x {db}"
            rho = read_tsv(processed / "concordance" / f"{pair}.{db}.rho.tsv", qa, label)
            if require_columns(rho, rho_cols, qa, label):
                qa.check(len(rho) == 1, f"{label}: rho table must have exactly one row")
                if len(rho) == 1:
                    row = rho.iloc[0].to_dict()
                    rho_rows[key] = row
                    qa.check(row["pair"] == pair, f"{label}: pair column mismatch")
                    qa.check(row["db"] == db, f"{label}: db column mismatch")
                    check_signed_unit(rho, ["rho_obs"], qa, label)
                    for col in ["n_shared", "n_na_x", "n_na_y", "n_dropped_either"]:
                        vals = numeric(rho[col])
                        qa.check((vals >= 0).all(), f"{label}: {col} must be >= 0")
                    qa.check(int(row["n_shared"]) > 0, f"{label}: n_shared must be > 0")

            scatter = read_tsv(processed / "concordance" / f"{pair}.{db}.scatter.tsv", qa, f"scatter {pair} x {db}")
            if require_columns(scatter, scatter_cols, qa, f"scatter {pair} x {db}"):
                qa.check(not scatter["gene_set"].duplicated().any(), f"scatter {pair} x {db}: duplicate gene_set keys")
                qa.check((scatter["contrast_x"] == arms["x"]).all(), f"scatter {pair} x {db}: contrast_x mismatch")
                qa.check((scatter["contrast_y"] == arms["y"]).all(), f"scatter {pair} x {db}: contrast_y mismatch")
                check_finite(scatter, ["nes_x", "nes_y"], qa, f"scatter {pair} x {db}")
                if key in rho_rows:
                    qa.check(len(scatter) == int(rho_rows[key]["n_shared"]), f"scatter {pair} x {db}: row count != n_shared")

            perm = read_tsv(processed / "perm" / f"{pair}.{db}.perm.tsv", qa, f"perm {pair} x {db}")
            if require_columns(perm, perm_cols, qa, f"perm {pair} x {db}"):
                qa.check(len(perm) == 1, f"perm {pair} x {db}: perm table must have exactly one row")
                if len(perm) == 1:
                    row = perm.iloc[0].to_dict()
                    perm_rows[key] = row
                    qa.check(row["pair"] == pair, f"perm {pair} x {db}: pair column mismatch")
                    qa.check(row["db"] == db, f"perm {pair} x {db}: db column mismatch")
                    check_signed_unit(perm, ["rho_obs"], qa, f"perm {pair} x {db}")
                    check_probability(perm, ["p_perm"], qa, f"perm {pair} x {db}")
                    b_eff = int(row["B"])
                    qa.check(0 < b_eff <= expected_b, f"perm {pair} x {db}: B_eff must be in 1..{expected_b}")

            null = read_tsv(processed / "perm" / f"{pair}.{db}.nulldist.tsv", qa, f"nulldist {pair} x {db}")
            if require_columns(null, null_cols, qa, f"nulldist {pair} x {db}"):
                qa.check(not null["perm_index"].duplicated().any(), f"nulldist {pair} x {db}: duplicate perm_index")
                check_signed_unit(null, ["rho_perm"], qa, f"nulldist {pair} x {db}")
                if key in perm_rows:
                    qa.check(len(null) == int(perm_rows[key]["B"]), f"nulldist {pair} x {db}: row count != B_eff")
    qa.facts["concordance_cells_checked"] = len(pairs) * len(dbs)
    return rho_rows, perm_rows


def check_specificity(processed: Path, dbs: list[str], qa: ResultQA) -> dict[str, dict[str, int]]:
    summaries: dict[str, dict[str, int]] = {}
    cols = [
        "gene_set", "db", "nes_qfs_vs_hc", "dir_qfs_vs_hc",
        "nes_qfs_vs_qs", "p_qfs_vs_qs", "s1_pos",
        "nes_qs_vs_hc", "p_qs_vs_hc", "s2_pos", "spec_class",
    ]
    allowed = {"fatigue-specific", "exposure_sequela", "unresolved", "absent"}
    for db in dbs:
        label = f"specificity {db}"
        df = read_tsv(processed / "specificity" / f"{db}.classes.tsv", qa, label)
        if not require_columns(df, cols, qa, label):
            continue
        qa.check(not df["gene_set"].duplicated().any(), f"{label}: duplicate gene_set keys")
        qa.check((df["db"] == db).all(), f"{label}: db column mismatch")
        check_probability(df, ["p_qfs_vs_qs", "p_qs_vs_hc"], qa, label)
        check_signed_unit(df, ["dir_qfs_vs_hc"], qa, label)
        qa.check(set(df["spec_class"]).issubset(allowed), f"{label}: invalid spec_class value")
        qa.check(bool_values(df["s1_pos"]).issubset({True, False}), f"{label}: s1_pos must be boolean-like")
        qa.check(bool_values(df["s2_pos"]).issubset({True, False}), f"{label}: s2_pos must be boolean-like")
        summaries[db] = {str(k): int(v) for k, v in df["spec_class"].value_counts().to_dict().items()}
    return summaries


def check_rollups(processed: Path, dbs: list[str], primary_db: str, qa: ResultQA) -> tuple[set[str], set[str], set[str], dict[str, Any]]:
    fatigue_specific: set[str] = set()
    exposure_sequela: set[str] = set()
    theme_cols = [
        "theme", "db", "n_carrying", "n_fatigue_specific",
        "n_exposure_sequela", "n_unresolved", "theme_class",
        "theme_direction", "verdict_eligible", "rep_set",
    ]
    class_allowed = {"fatigue-specific", "exposure_sequela", "unresolved"}
    for db in dbs:
        label = f"theme rollup {db}"
        df = read_tsv(processed / "rollup" / f"{db}.themes.tsv", qa, label)
        if not require_columns(df, theme_cols, qa, label):
            continue
        if df.empty:
            continue
        qa.check((df["db"] == db).all(), f"{label}: db column mismatch")
        qa.check(not df["theme"].duplicated().any(), f"{label}: duplicate theme keys")
        qa.check(set(df["theme_class"]).issubset(class_allowed), f"{label}: invalid theme_class")
        check_signed_unit(df, ["theme_direction"], qa, label)
        for col in ["n_carrying", "n_fatigue_specific", "n_exposure_sequela", "n_unresolved"]:
            vals = numeric(df[col])
            qa.check((vals >= 0).all(), f"{label}: {col} must be >= 0")
        sums = numeric(df["n_fatigue_specific"]) + numeric(df["n_exposure_sequela"]) + numeric(df["n_unresolved"])
        qa.check((numeric(df["n_carrying"]) == sums).all(), f"{label}: n_carrying must equal class count sum")
        eligible = bool_mask(df["verdict_eligible"])
        fatigue_specific.update(df.loc[(df["theme_class"] == "fatigue-specific") & eligible, "theme"].astype(str))
        exposure_sequela.update(df.loc[(df["theme_class"] == "exposure_sequela") & eligible, "theme"].astype(str))

    robust = read_tsv(processed / "rollup/db_robustness.tsv", qa, "db robustness")
    robust_themes: set[str] = set()
    robust_cols = [
        "theme", "n_dbs_fatigue_specific", "dbs_fatigue_specific",
        "fs_directions", "robust_direction", "db_robust",
    ]
    if require_columns(robust, robust_cols, qa, "db robustness") and not robust.empty:
        qa.check(not robust["theme"].duplicated().any(), "db robustness: duplicate theme keys")
        vals = numeric(robust["n_dbs_fatigue_specific"])
        qa.check((vals >= 0).all(), "db robustness: n_dbs_fatigue_specific must be >= 0")
        check_signed_unit(robust, ["robust_direction"], qa, "db robustness")
        robust_themes = set(robust.loc[bool_mask(robust["db_robust"]), "theme"].astype(str))

    comp = read_tsv(processed / "rollup/compartment.tsv", qa, "compartment")
    comp_row: dict[str, Any] = {}
    comp_cols = [
        "db", "n_carrying", "n_marker", "marker_fraction",
        "compartment_confounded", "status", "marker_sets",
    ]
    if require_columns(comp, comp_cols, qa, "compartment"):
        qa.check(len(comp) == 1, "compartment: table must have exactly one row")
        if len(comp) == 1:
            comp_row = comp.iloc[0].to_dict()
            qa.check(comp_row["db"] == primary_db, "compartment: db must equal primary_db")
            for col in ["n_carrying", "n_marker"]:
                qa.check(as_float(comp_row[col]) >= 0, f"compartment: {col} must be >= 0")
            frac = as_float(comp_row["marker_fraction"])
            qa.check(math.isnan(frac) or 0.0 <= frac <= 1.0, "compartment: marker_fraction must be in [0, 1] or NA")
    return fatigue_specific, exposure_sequela, robust_themes, comp_row


def check_verdict(
    results: Path,
    config: dict[str, Any],
    diags: dict[str, dict[str, Any]],
    rho_rows: dict[tuple[str, str], dict[str, Any]],
    perm_rows: dict[tuple[str, str], dict[str, Any]],
    spec_summary: dict[str, dict[str, int]],
    fatigue_specific: set[str],
    exposure_sequela: set[str],
    robust_themes: set[str],
    comp_row: dict[str, Any],
    qa: ResultQA,
) -> None:
    verdict = read_json(results / "verdict.json", qa, "verdict")
    qa.check((results / "results.md").exists(), "results.md: missing terminal report")
    qa.check((results / "run_metadata.json").exists(), "run_metadata.json: missing run metadata")
    if not verdict:
        return

    primary_db = config["genesets"]["primary_db"]
    primary_key = ("primary", primary_db)
    confirm = verdict.get("confirmatory", {})
    qa.check(confirm.get("pair") == "primary", "verdict confirmatory: pair must be primary")
    qa.check(confirm.get("db") == primary_db, "verdict confirmatory: db must equal primary_db")
    if primary_key in rho_rows:
        qa.check(approx_equal(confirm.get("rho_obs_multilevel"), rho_rows[primary_key]["rho_obs"]),
                 "verdict confirmatory rho_obs_multilevel does not match primary rho table")
    if primary_key in perm_rows:
        qa.check(approx_equal(confirm.get("rho_obs_perm"), perm_rows[primary_key]["rho_obs"]),
                 "verdict confirmatory rho_obs_perm does not match primary perm table")
        qa.check(approx_equal(confirm.get("p_perm"), perm_rows[primary_key]["p_perm"]),
                 "verdict confirmatory p_perm does not match primary perm table")
        qa.check(int(confirm.get("B", -1)) == int(perm_rows[primary_key]["B"]),
                 "verdict confirmatory B does not match primary perm table")
    qa.check(approx_equal(confirm.get("alpha"), config["verdict"]["p_perm_alpha"]),
             "verdict confirmatory alpha does not match config")

    got_surface = {
        (str(r.get("pair")), str(r.get("db"))): r
        for r in verdict.get("sensitivity_surface", [])
    }
    expected_keys = set(rho_rows)
    qa.check(set(got_surface) == expected_keys, "verdict sensitivity_surface pair/db keys do not match rho surface")
    for key in expected_keys & set(got_surface):
        row = got_surface[key]
        qa.check(approx_equal(row.get("rho_obs"), rho_rows[key]["rho_obs"]), f"verdict sensitivity rho mismatch for {key}")
        qa.check(approx_equal(row.get("p_perm"), perm_rows[key]["p_perm"]), f"verdict sensitivity p_perm mismatch for {key}")
        qa.check(int(row.get("B", -1)) == int(perm_rows[key]["B"]), f"verdict sensitivity B mismatch for {key}")
        qa.check(int(row.get("n_shared", -1)) == int(rho_rows[key]["n_shared"]), f"verdict sensitivity n_shared mismatch for {key}")

    per_contrast = verdict.get("admissibility", {}).get("per_contrast", {})
    qa.check(set(per_contrast) == set(diags), "verdict admissibility per_contrast keys do not match diag files")
    for contrast, diag in diags.items():
        if contrast not in per_contrast:
            continue
        got = per_contrast[contrast]
        for col in ["full_rank", "residual_df", "n_genes_tested"]:
            qa.check(got.get(col) == diag.get(col), f"verdict admissibility {contrast}.{col} does not match diag")

    qa.check(verdict.get("specificity_summary", {}) == spec_summary,
             "verdict specificity_summary does not match specificity tables")
    theme_sets = verdict.get("theme_sets", {})
    qa.check(set(theme_sets.get("fatigue_specific_any_db", [])) == fatigue_specific,
             "verdict theme_sets.fatigue_specific_any_db does not match rollups")
    qa.check(set(theme_sets.get("exposure_sequela_any_db", [])) == exposure_sequela,
             "verdict theme_sets.exposure_sequela_any_db does not match rollups")
    qa.check(set(theme_sets.get("db_robust", [])) == robust_themes,
             "verdict theme_sets.db_robust does not match robustness table")

    comp = verdict.get("compartment", {})
    if comp_row:
        for col in ["db", "status"]:
            qa.check(comp.get(col) == comp_row[col], f"verdict compartment {col} does not match compartment table")
        for col in ["n_carrying", "n_marker", "marker_fraction"]:
            qa.check(approx_equal(comp.get(col), comp_row[col]), f"verdict compartment {col} does not match table")
        qa.check(bool(comp.get("compartment_confounded")) in bool_values(pd.Series([comp_row["compartment_confounded"]])),
                 "verdict compartment_confounded does not match table")

    trace_labels = [step.get("label") for step in verdict.get("resolution_trace", [])]
    qa.check(trace_labels == config["verdict"]["resolution_order"],
             "verdict resolution_trace labels do not match config resolution_order")


def write_report(path: Path, qa: ResultQA) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# t035 result QA report", ""]
    if qa.failures:
        lines += ["## Structural failures", ""]
        lines += [f"- {failure}" for failure in qa.failures]
    else:
        lines += ["## Structural failures", "", "- all structural checks passed"]
    if qa.warnings:
        lines += ["", "## Warnings", ""]
        lines += [f"- {warning}" for warning in qa.warnings]
    lines += ["", "## Observed facts", "", "```json"]
    lines += [json.dumps(qa.facts, indent=2, sort_keys=True), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def check_results(
    *,
    processed: Path,
    results: Path,
    config: dict[str, Any],
    report: Path,
    sentinel: Path,
) -> int:
    qa = ResultQA()
    contrasts = list(config["contrasts"])
    dbs = list(config["genesets"]["databases"])
    pairs = dict(config["concordance_pairs"])
    expected_b = int(config["permutation"]["B"])

    diags = check_de(processed, contrasts, qa)
    check_fgsea(processed, contrasts, dbs, qa)
    rho_rows, perm_rows = check_concordance_and_perm(processed, pairs, dbs, expected_b, qa)
    spec_summary = check_specificity(processed, dbs, qa)
    fatigue_specific, exposure_sequela, robust_themes, comp_row = check_rollups(
        processed, dbs, str(config["genesets"]["primary_db"]), qa)
    check_verdict(
        results, config, diags, rho_rows, perm_rows, spec_summary,
        fatigue_specific, exposure_sequela, robust_themes, comp_row, qa)

    qa.facts["dbs_checked"] = len(dbs)
    qa.facts["result_root"] = str(results)
    qa.facts["processed_root"] = str(processed)
    write_report(report, qa)
    if qa.failures:
        if sentinel.exists():
            sentinel.unlink()
        return 1
    sentinel.parent.mkdir(parents=True, exist_ok=True)
    sentinel.write_text("PASS t035 result QA\n", encoding="utf-8")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="QA t035 downstream analysis results")
    parser.add_argument("--processed", required=True, type=Path)
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--sentinel", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    return check_results(
        processed=args.processed,
        results=args.results,
        config=config,
        report=args.report,
        sentinel=args.sentinel,
    )


if __name__ == "__main__":
    raise SystemExit(main())
