# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Aggregate the six per-stratum naive-MR results into one manifest (plan:0009 Task 3).

Reads the six `harmonize_estimate.R` result JSONs + their Snakemake `benchmark:`
TSVs (wall-clock + peak RSS) + the `setup_twosamplemr` sentinel + the Task-2
`instruments_manifest.json` (instrument-count cross-ref), and writes one
`naive_mr_results.json` recording: per-stratum results, a summary (estimated vs
skipped/quarantined/weak), a bounded exposure-architecture `cross_stratum`
sign-concordance descriptor (male vs female IVW sign per trait — NOT a
sex-modification test), an `entities` cross-ref, and resource usage.

Structural completeness is a hard requirement: this is the manifest Task 5's
write-up reads, so a missing/malformed input file HARD-STOPS. As defense-in-depth
(P1) the estimator script (`harmonize_estimate.R`) is the primary gate on estimator
sanity, but this aggregator re-asserts: any record with `status: "estimated"` that
is missing a configured method or carries a non-finite `b`/`se`/`pval`/`or` also
HARD-STOPS, so a malformed record can never reach the manifest silently.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import yaml

CANONICAL_METHOD_LABELS = ("Inverse variance weighted", "MR Egger", "Weighted median")

# Fixed KD1/KD3 + naive-arm labels (plan:0009 Task 3) — carried on every output,
# independent of any single stratum's outcome, so the aggregate manifest states
# them even if every per-stratum result were skipped/weak.
LABELS = {
    "ancestry_flag": (
        "Outcome GCST90454541 is a European-dominant (~85-90%) multi-ancestry HGI "
        "broad/population meta; no EUR-only sibling. ANCESTRY-FLAGGED, NON-PRIMARY "
        "(KD1) — exploratory/robustness only, never primary evidence for "
        "hypothesis:0005 / question:0007 / question:0013."
    ),
    "bounded_sex": (
        "Male-only / female-only strata give a BOUNDED exposure-architecture read "
        "against a mixed-sex outcome (KD3) — NOT a genotype x sex "
        "effect-modification test. No sex-modification claim."
    ),
    "exposure_side": (
        "SHBG and total testosterone share Ruth instrument loci (steroid-axis "
        "pleiotropy plausible; Egger+WM only partially bound it). Female-testosterone "
        "is weakest-instrumented yet most decision-relevant."
    ),
    "sample_overlap_uncorrected": True,  # Ruth = 100% UKB, HGI pools UKB -> structural
    "naive_comparator_only": True,       # overlap NOT corrected here; MRlap is Task 4
}

# config trait -> cross_stratum output key
TRAIT_KEY = {"shbg": "shbg", "total-testosterone": "testosterone"}

ENTITIES = [
    "dataset:ruth-2020-shbg-testosterone-gwas",
    "dataset:covid19-hgi-longcovid-gwas",
]


def _stratum_from_path(path: Path, suffix: str) -> str:
    name = path.name
    if not name.endswith(suffix):
        raise SystemExit(f"aggregate_mr: filename does not end in {suffix}: {path}")
    return name[: -len(suffix)]


def _isfinite(x) -> bool:
    try:
        return math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def load_result(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mr: result JSON missing: {path} — HALT")
    try:
        rec = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate_mr: result JSON malformed: {path} ({e}) — HALT")

    required = {"stratum", "status", "trait", "sex", "exposure", "outcome"}
    missing = required - rec.keys()
    if missing:
        raise SystemExit(f"aggregate_mr: result {path} missing required key(s) {sorted(missing)} — HALT")

    expected_stratum = _stratum_from_path(p, ".mr_results.json")
    if rec["stratum"] != expected_stratum:
        raise SystemExit(
            f"aggregate_mr: result {path} stratum field {rec['stratum']!r} != filename-derived "
            f"{expected_stratum!r} — HALT (malformed)"
        )

    status = rec["status"]
    if status not in {"estimated", "skipped-quarantined", "insufficient-harmonised-instruments"}:
        raise SystemExit(f"aggregate_mr: result {path} has unknown status {status!r} — HALT (malformed)")

    if status == "estimated":
        methods = rec.get("methods")
        if not isinstance(methods, list) or not methods:
            raise SystemExit(f"aggregate_mr: estimated result {path} has no methods — HALT (technical)")
        got_names = [m.get("method") for m in methods]
        for canonical in CANONICAL_METHOD_LABELS:
            if not any(canonical in (name or "") for name in got_names):
                raise SystemExit(
                    f"aggregate_mr: estimated result {path} is missing method {canonical!r} "
                    f"(got {got_names}) — HALT (technical)"
                )
        for m in methods:
            for field in ("b", "se", "pval", "or"):
                if field not in m or not _isfinite(m[field]):
                    raise SystemExit(
                        f"aggregate_mr: estimated result {path} method {m.get('method')!r} has "
                        f"non-finite/missing {field!r}={m.get(field)!r} — HALT (technical)"
                    )
    return rec


def load_benchmark(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mr: benchmark TSV missing: {path} — HALT")
    stratum = _stratum_from_path(p, ".benchmark.tsv")
    with p.open(newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise SystemExit(f"aggregate_mr: benchmark TSV {path} has no data row — HALT (malformed)")
    row = rows[-1]  # last invocation, in case of a re-run
    for col in ("s", "max_rss"):
        if col not in row or row[col] in (None, ""):
            raise SystemExit(f"aggregate_mr: benchmark TSV {path} missing '{col}' column/value — HALT (malformed)")
    try:
        wall_clock_s = float(row["s"])
        max_rss_mb = float(row["max_rss"])
    except ValueError as e:
        raise SystemExit(f"aggregate_mr: benchmark TSV {path} non-numeric s/max_rss ({e}) — HALT (malformed)")
    return {"stratum": stratum, "wall_clock_s": wall_clock_s, "max_rss_mb": max_rss_mb}


def load_setup_sentinel(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mr: setup_twosamplemr sentinel missing: {path} — HALT")
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate_mr: setup sentinel malformed JSON: {path} ({e}) — HALT")


def load_instruments_manifest(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mr: instruments manifest missing: {path} — HALT")
    try:
        manifest = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate_mr: instruments manifest malformed JSON: {path} ({e}) — HALT")
    if "strata" not in manifest or not isinstance(manifest["strata"], list):
        raise SystemExit(f"aggregate_mr: instruments manifest {path} missing 'strata' list — HALT (malformed)")
    return manifest


def _sign(x) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def build_cross_stratum(strata: list[dict]) -> dict:
    by_trait_sex: dict[tuple[str, str], dict] = {(s["trait"], s["sex"]): s for s in strata}
    out = {}
    for trait, key in TRAIT_KEY.items():
        signs = {}
        for sex in ("combined", "male", "female"):
            rec = by_trait_sex.get((trait, sex))
            if rec is None or rec["status"] != "estimated":
                signs[sex] = None
                continue
            ivw_beta = rec.get("concordance", {}).get("ivw_beta")
            signs[sex] = _sign(ivw_beta) if ivw_beta is not None else None
        male_female_concordant = (
            None
            if signs["male"] is None or signs["female"] is None
            else signs["male"] == signs["female"]
        )
        out[key] = {
            "combined_ivw_sign": signs["combined"],
            "male_ivw_sign": signs["male"],
            "female_ivw_sign": signs["female"],
            "male_female_sign_concordant": male_female_concordant,
        }
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--results", required=True, nargs="+")
    p.add_argument("--benchmarks", required=True, nargs="+")
    p.add_argument("--setup", required=True)
    p.add_argument("--instruments", required=True)
    p.add_argument("--manifest", required=True)
    a = p.parse_args()

    cfg = yaml.safe_load(Path(a.config).read_text())

    strata = [load_result(r) for r in a.results]
    strata_by_name = {s["stratum"]: s for s in strata}
    if len(strata_by_name) != len(strata):
        raise SystemExit("aggregate_mr: duplicate stratum name across result JSONs — HALT")

    benchmarks = [load_benchmark(b) for b in a.benchmarks]
    benchmarks_by_name = {b["stratum"]: b for b in benchmarks}
    if len(benchmarks_by_name) != len(benchmarks):
        raise SystemExit("aggregate_mr: duplicate stratum name across benchmark TSVs — HALT")

    missing_benchmarks = set(strata_by_name) - set(benchmarks_by_name)
    if missing_benchmarks:
        raise SystemExit(f"aggregate_mr: no benchmark TSV for stratum/strata {sorted(missing_benchmarks)} — HALT")
    extra_benchmarks = set(benchmarks_by_name) - set(strata_by_name)
    if extra_benchmarks:
        raise SystemExit(f"aggregate_mr: benchmark TSV for unknown stratum/strata {sorted(extra_benchmarks)} — HALT")

    setup = load_setup_sentinel(a.setup)

    instruments_manifest = load_instruments_manifest(a.instruments)
    instr_by_name = {s["stratum"]: s for s in instruments_manifest["strata"]}
    missing_instr = set(strata_by_name) - set(instr_by_name)
    if missing_instr:
        raise SystemExit(f"aggregate_mr: no instruments-manifest entry for stratum/strata {sorted(missing_instr)} — HALT")
    for name, rec in strata_by_name.items():
        n_input = rec.get("n_instruments_input")
        n_manifest = instr_by_name[name].get("n_instruments")
        if n_input is not None and n_manifest is not None and int(n_input) != int(n_manifest):
            raise SystemExit(
                f"aggregate_mr: stratum {name!r} n_instruments_input={n_input} != "
                f"instruments_manifest n_instruments={n_manifest} — HALT (malformed)"
            )

    n_estimated = sum(1 for s in strata if s["status"] == "estimated")
    skipped = []
    for s in strata:
        if s["status"] == "estimated":
            continue
        if s["status"] == "skipped-quarantined":
            reasons = list(s.get("eligibility_reasons") or [])
        else:  # insufficient-harmonised-instruments
            reasons = [f"insufficient-harmonised-instruments: n_harmonised={s.get('n_harmonised')}"]
        skipped.append({"stratum": s["stratum"], "reasons": reasons})
    summary = {
        "n_strata": len(strata),
        "n_estimated": n_estimated,
        "n_skipped": len(skipped),
        "skipped": skipped,
    }

    cross_stratum = build_cross_stratum(strata)
    cross_stratum["_note"] = (
        "BOUNDED exposure-architecture descriptor (KD3) — sign concordance of the "
        "male-only vs female-only IVW estimate for each trait against the common "
        "mixed-sex outcome. NOT a sex-modification test; no interaction is estimated."
    )

    per_stratum_resource = [
        {
            "stratum": name,
            "wall_clock_s": benchmarks_by_name[name]["wall_clock_s"],
            "max_rss_mb": benchmarks_by_name[name]["max_rss_mb"],
        }
        for name in sorted(strata_by_name)
    ]
    resource = {
        "per_stratum": per_stratum_resource,
        "peak_rss_mb": max(r["max_rss_mb"] for r in per_stratum_resource),
        "total_wall_clock_s": sum(r["wall_clock_s"] for r in per_stratum_resource),
    }

    estimate_params = {
        "methods": list(cfg["estimate"]["methods"]),
        "weighted_median_seed": cfg["estimate"]["weighted_median_seed"],
        "weighted_median_bootstrap_n": cfg["estimate"]["weighted_median_bootstrap_n"],
        "harmonise_action": cfg["harmonise"]["action"],
    }

    manifest = {
        "plan": "plan:0009-wave1-mr-hormone-pilot",
        "task": "t089",
        "stage": "Task 3 — naive MR comparator (IVW / Egger / weighted-median)",
        "labels": LABELS,
        "estimate_params": estimate_params,
        "strata": strata,
        "summary": summary,
        "cross_stratum": cross_stratum,
        "twosamplemr_setup": setup,
        "entities": ENTITIES,
        "resource": resource,
    }
    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    print(
        f"aggregate_mr: {summary['n_strata']} strata, {summary['n_estimated']} estimated, "
        f"{summary['n_skipped']} skipped; peak_rss_mb={resource['peak_rss_mb']:.1f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
