# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Aggregate the six per-stratum MRlap results + the Task-3 naive manifest into
one `mrlap_results.json` comparison manifest (plan:0009 Task 4).

Reads the six `run_mrlap.R` result JSONs + their Snakemake `benchmark:` TSVs
(wall-clock + peak RSS) + the `setup_mrlap` sentinel + the Task-3
`naive_mr_results.json`, and writes a per-stratum `comparison` table (naive IVW
vs MRlap observed vs MRlap corrected), a bounded `cross_stratum` sign-concordance
descriptor on the CORRECTED estimates (male-only vs female-only per trait — NOT a
sex-modification test), a `summary`, an `entities` cross-ref, and resource usage.

Structural completeness is a hard requirement: this is the manifest Task 5's
write-up reads, so a missing/malformed input file HARD-STOPS. As defense-in-depth
(re-asserting `run_mrlap.R`'s own gate) any record with `status: "corrected"` that
carries a non-finite `mrlap_corrected` b/se/pval also HARD-STOPS. A `status:
"insufficient-mrlap-ivs"` record is carried (not hard-stopped), counted in
`summary.n_insufficient_ivs`, and its `status` is carried on its `comparison`
entry so a downstream reader knows those values are non-quotable.

Naive-IVW extraction is exact-match and hard-stop: the Task-3 per-stratum record
must have `status: "estimated"` and a `methods` entry with `method == "Inverse
variance weighted"` (verbatim) — anything else (stratum absent, non-estimated
status, renamed/missing IVW entry) HALTs naming the stratum, rather than silently
emitting a null `naive_ivw` column.

The naive<->corrected comparison is SIGN/DIRECTION only: naive IVW runs on the
1000G-EUR-clumped instrument set in log-OR/SD; MRlap observed/corrected run on
MRlap's own genome-wide distance-pruned set in MRlap's standardized (SD/SD)
scale. Different scale AND different instrument set -> no OR-magnitude
comparison is ever assembled here. The one clean like-for-like delta is MRlap
observed -> corrected (same set, same std scale).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import yaml

# Fixed KD1/KD3 + overlap-correction labels (plan:0009 Task 4) — carried on every
# output, independent of any single stratum's outcome. Mirrors the per-stratum
# `labels` block `run_mrlap.R` writes into each result JSON.
LABELS = {
    "ancestry_flag": (
        "Outcome GCST90454541 is a European-dominant (~85-90%) multi-ancestry HGI "
        "broad/population meta; no EUR-only sibling. ANCESTRY-FLAGGED, NON-PRIMARY "
        "(KD1) — exploratory/robustness only, never primary evidence for "
        "hypothesis:0005 / question:0007 / question:0013. Overlap-correction does "
        "NOT lift this."
    ),
    "bounded_sex": (
        "Male-only / female-only strata give a BOUNDED exposure-architecture read "
        "against a mixed-sex outcome (KD3) — NOT a genotype x sex "
        "effect-modification test. No sex-modification claim."
    ),
    "exposure_side": (
        "SHBG and total testosterone share Ruth instrument loci (steroid-axis "
        "pleiotropy plausible). Female-testosterone is weakest-instrumented yet "
        "most decision-relevant — a wide/weak corrected estimate is informative, "
        "not a failure."
    ),
    "sample_overlap_corrected": True,
    "overlap_correction_does_not_lift_ceiling": True,
    "ldsc_ancestry_mismatch": True,
    "_ldsc_ancestry_note": (
        "MRlap cross-trait LDSC uses the EUR eur_w_ld_chr ref; the outcome is "
        "~10-15% non-European -> outcome h2/int_crosstrait (the correction driver) "
        "are ancestry-approximate. Compounds KD1."
    ),
}

# config trait -> cross_stratum output key (mirrors aggregate_mr.py TRAIT_KEY)
TRAIT_KEY = {"shbg": "shbg", "total-testosterone": "testosterone"}

ENTITIES = [
    "dataset:ruth-2020-shbg-testosterone-gwas",
    "dataset:covid19-hgi-longcovid-gwas",
    "dataset:eur-ldsc-ld-score-reference",
    "dataset:1000g-eur-ld-panel",
]

COMPARISON_NOTE = (
    "naive IVW is on the 1000G-EUR LD-clumped set (r2<0.001,10Mb) in log-OR/SD; "
    "MRlap observed+corrected are on MRlap's genome-wide distance-pruned set "
    "(MR_pruning_dist=500kb, MR_pruning_LD=0) in MRlap's STANDARDIZED scale "
    "(SD/SD). naive<->corrected therefore differ in BOTH scale and instrument "
    "set -> compare SIGN/DIRECTION only, never OR-magnitude. The one clean "
    "like-for-like delta is MRlap observed->corrected (same set, same std scale) "
    "= the overlap(+winner's-curse) correction."
)

RESULT_REQUIRED_KEYS = {
    "stratum", "accession", "trait", "sex", "exposure", "outcome",
    "exposure_n", "outcome_total_n", "status", "scale",
    "mrlap_observed", "mrlap_corrected", "difference", "m_ivs", "pruned_snps",
    "ldsc", "ldsc_ancestry_mismatch", "_ldsc_ancestry_note", "overlap_signal",
    "mrlap_params", "labels",
}


def _stratum_from_path(path: Path, suffix: str) -> str:
    name = path.name
    if not name.endswith(suffix):
        raise SystemExit(f"aggregate_mrlap: filename does not end in {suffix}: {path}")
    return name[: -len(suffix)]


def _isfinite(x) -> bool:
    try:
        return math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def _sign(x) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def load_result(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mrlap: MRlap result JSON missing: {path} — HALT")
    try:
        rec = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate_mrlap: MRlap result JSON malformed: {path} ({e}) — HALT")

    missing = RESULT_REQUIRED_KEYS - rec.keys()
    if missing:
        raise SystemExit(
            f"aggregate_mrlap: MRlap result {path} missing required key(s) {sorted(missing)} — HALT"
        )

    expected_stratum = _stratum_from_path(p, ".mrlap.json")
    if rec["stratum"] != expected_stratum:
        raise SystemExit(
            f"aggregate_mrlap: MRlap result {path} stratum field {rec['stratum']!r} != "
            f"filename-derived {expected_stratum!r} — HALT (malformed)"
        )

    status = rec["status"]
    if status not in {"corrected", "insufficient-mrlap-ivs"}:
        raise SystemExit(f"aggregate_mrlap: MRlap result {path} has unknown status {status!r} — HALT (malformed)")

    for block_name in ("mrlap_observed", "mrlap_corrected"):
        block = rec[block_name]
        for field in ("b", "se", "pval"):
            if field not in block:
                raise SystemExit(
                    f"aggregate_mrlap: MRlap result {path} {block_name} missing {field!r} — HALT (malformed)"
                )

    if "quality_flags" not in rec["ldsc"]:
        raise SystemExit(f"aggregate_mrlap: MRlap result {path} ldsc block missing 'quality_flags' — HALT (malformed)")
    if "cross_trait_ldsc_intercept" not in rec["overlap_signal"]:
        raise SystemExit(
            f"aggregate_mrlap: MRlap result {path} overlap_signal missing 'cross_trait_ldsc_intercept' — HALT (malformed)"
        )

    # Defense-in-depth: re-assert run_mrlap.R's own hard-stop on a non-finite
    # corrected estimate for any record that claims to be usably "corrected".
    if status == "corrected":
        mc = rec["mrlap_corrected"]
        if not all(_isfinite(mc[f]) for f in ("b", "se", "pval")):
            raise SystemExit(
                f"aggregate_mrlap: stratum {rec['stratum']!r} has status 'corrected' but "
                f"non-finite mrlap_corrected b/se/pval={mc!r} — HALT (technical, defense-in-depth)"
            )

    return rec


def load_benchmark(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mrlap: benchmark TSV missing: {path} — HALT")
    stratum = _stratum_from_path(p, ".benchmark.tsv")
    with p.open(newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise SystemExit(f"aggregate_mrlap: benchmark TSV {path} has no data row — HALT (malformed)")
    row = rows[-1]  # last invocation, in case of a re-run
    for col in ("s", "max_rss"):
        if col not in row or row[col] in (None, ""):
            raise SystemExit(f"aggregate_mrlap: benchmark TSV {path} missing '{col}' column/value — HALT (malformed)")
    try:
        wall_clock_s = float(row["s"])
        max_rss_mb = float(row["max_rss"])
    except ValueError as e:
        raise SystemExit(f"aggregate_mrlap: benchmark TSV {path} non-numeric s/max_rss ({e}) — HALT (malformed)")
    return {"stratum": stratum, "wall_clock_s": wall_clock_s, "max_rss_mb": max_rss_mb}


def load_setup_sentinel(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mrlap: setup_mrlap sentinel missing: {path} — HALT")
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate_mrlap: setup sentinel malformed JSON: {path} ({e}) — HALT")


def load_naive_manifest(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate_mrlap: naive manifest missing: {path} — HALT")
    try:
        manifest = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate_mrlap: naive manifest malformed JSON: {path} ({e}) — HALT")
    if "strata" not in manifest or not isinstance(manifest["strata"], list):
        raise SystemExit(f"aggregate_mrlap: naive manifest {path} missing 'strata' list — HALT (malformed)")
    return manifest


def naive_ivw_for(stratum: str, naive_by_stratum: dict) -> dict:
    """Exact-match, hard-stop extraction of the naive IVW row for `stratum`."""
    rec = naive_by_stratum.get(stratum)
    if rec is None:
        raise SystemExit(f"aggregate_mrlap: no naive-manifest entry for stratum {stratum!r} — HALT")
    if rec.get("status") != "estimated":
        raise SystemExit(
            f"aggregate_mrlap: naive-manifest entry for stratum {stratum!r} has status "
            f"{rec.get('status')!r} (not 'estimated') — HALT (naive IVW required for the comparison)"
        )
    methods = rec.get("methods")
    if not isinstance(methods, list):
        raise SystemExit(f"aggregate_mrlap: naive-manifest entry for stratum {stratum!r} has no 'methods' list — HALT")
    ivw = next((m for m in methods if m.get("method") == "Inverse variance weighted"), None)
    if ivw is None:
        raise SystemExit(
            f"aggregate_mrlap: naive-manifest entry for stratum {stratum!r} is missing the exact "
            f"'Inverse variance weighted' method entry (got {[m.get('method') for m in methods]}) — HALT"
        )
    required = ("b", "se", "pval", "or", "nsnp")
    missing = [f for f in required if f not in ivw]
    if missing:
        raise SystemExit(
            f"aggregate_mrlap: naive IVW entry for stratum {stratum!r} missing field(s) {missing} — HALT"
        )
    for f in ("b", "se", "pval", "or"):
        if not _isfinite(ivw[f]):
            raise SystemExit(
                f"aggregate_mrlap: naive IVW entry for stratum {stratum!r} has non-finite {f!r}={ivw[f]!r} — HALT"
            )
    return {
        "b": ivw["b"], "se": ivw["se"], "pval": ivw["pval"], "or": ivw["or"], "nsnp": ivw["nsnp"],
        "scale": "log-OR/SD",
    }


def build_cross_stratum(strata: list[dict]) -> dict:
    by_trait_sex: dict[tuple[str, str], dict] = {(s["trait"], s["sex"]): s for s in strata}
    out = {}
    for trait, key in TRAIT_KEY.items():
        signs = {}
        for sex in ("male", "female"):
            rec = by_trait_sex.get((trait, sex))
            if rec is None or rec["status"] != "corrected":
                signs[sex] = None
                continue
            signs[sex] = _sign(rec["mrlap_corrected"]["b"])
        male_female_concordant = (
            None if signs["male"] is None or signs["female"] is None else signs["male"] == signs["female"]
        )
        out[key] = {
            "male_corrected_sign": signs["male"],
            "female_corrected_sign": signs["female"],
            "male_female_sign_concordant": male_female_concordant,
        }
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--results", required=True, nargs="+")
    p.add_argument("--naive", required=True)
    p.add_argument("--benchmarks", required=True, nargs="+")
    p.add_argument("--setup", required=True)
    p.add_argument("--manifest", required=True)
    a = p.parse_args()

    cfg = yaml.safe_load(Path(a.config).read_text())

    strata = [load_result(r) for r in a.results]
    strata_by_name = {s["stratum"]: s for s in strata}
    if len(strata_by_name) != len(strata):
        raise SystemExit("aggregate_mrlap: duplicate stratum name across MRlap result JSONs — HALT")

    benchmarks = [load_benchmark(b) for b in a.benchmarks]
    benchmarks_by_name = {b["stratum"]: b for b in benchmarks}
    if len(benchmarks_by_name) != len(benchmarks):
        raise SystemExit("aggregate_mrlap: duplicate stratum name across benchmark TSVs — HALT")

    missing_benchmarks = set(strata_by_name) - set(benchmarks_by_name)
    if missing_benchmarks:
        raise SystemExit(f"aggregate_mrlap: no benchmark TSV for stratum/strata {sorted(missing_benchmarks)} — HALT")
    extra_benchmarks = set(benchmarks_by_name) - set(strata_by_name)
    if extra_benchmarks:
        raise SystemExit(f"aggregate_mrlap: benchmark TSV for unknown stratum/strata {sorted(extra_benchmarks)} — HALT")

    setup = load_setup_sentinel(a.setup)

    naive_manifest = load_naive_manifest(a.naive)
    naive_by_name = {s["stratum"]: s for s in naive_manifest["strata"]}

    comparison = []
    for name in sorted(strata_by_name):
        rec = strata_by_name[name]
        naive_ivw = naive_ivw_for(name, naive_by_name)
        observed = rec["mrlap_observed"]
        corrected = rec["mrlap_corrected"]
        comparison.append({
            "stratum": name,
            "trait": rec["trait"],
            "sex": rec["sex"],
            "status": rec["status"],
            "naive_ivw": naive_ivw,
            "mrlap_observed": {
                "b": observed["b"], "se": observed["se"], "pval": observed["pval"],
                "scale": "MRlap std (SD/SD)",
            },
            "mrlap_corrected": {
                "b": corrected["b"], "se": corrected["se"], "pval": corrected["pval"],
                "scale": "MRlap std (SD/SD)",
            },
            "observed_to_corrected_delta": corrected["b"] - observed["b"],
            "naive_vs_corrected": {
                "sign_concordant": _sign(naive_ivw["b"]) == _sign(corrected["b"]),
                "_note": (
                    "sign/direction ONLY — different scale (log-OR/SD vs std SD/SD) AND "
                    "different instrument set; NO magnitude/OR comparison"
                ),
            },
            "cross_trait_ldsc_intercept": rec["overlap_signal"]["cross_trait_ldsc_intercept"],
            "m_ivs": rec["m_ivs"],
            "ldsc_quality_flags": list(rec["ldsc"]["quality_flags"]),
        })

    cross_stratum = build_cross_stratum(strata)
    cross_stratum["_note"] = (
        "BOUNDED exposure-architecture descriptor (KD3) on the CORRECTED estimates — sign "
        "concordance of the male-only vs female-only corrected effect per trait against the "
        "common mixed-sex outcome. NOT a sex-modification test; no interaction is estimated. "
        "MRlap yields ONE corrected estimate per stratum, so this is IVW-vs-corrected sign "
        "concordance only, not three-method concordance."
    )

    n_corrected = sum(1 for s in strata if s["status"] == "corrected")
    n_insufficient_ivs = sum(1 for s in strata if s["status"] == "insufficient-mrlap-ivs")
    n_ldsc_flagged = sum(1 for s in strata if s["ldsc"]["quality_flags"])
    summary = {
        "n_strata": len(strata),
        "n_corrected": n_corrected,
        "n_insufficient_ivs": n_insufficient_ivs,
        "n_ldsc_flagged": n_ldsc_flagged,
    }

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
        "_note": (
            "genome-wide MRlap internal munge + cross-trait LDSC — the new, "
            "previously-untested resource step."
        ),
    }

    mrlap_params = dict(cfg["mrlap"])

    manifest = {
        "plan": "plan:0009-wave1-mr-hormone-pilot",
        "task": "t089",
        "stage": "Task 4 — MRlap overlap correction (canonicalized sumstats)",
        "labels": LABELS,
        "mrlap_params": mrlap_params,
        "setup": setup,
        "comparison": comparison,
        "comparison_note": COMPARISON_NOTE,
        "cross_stratum": cross_stratum,
        "summary": summary,
        "entities": ENTITIES,
        "resource": resource,
    }
    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    print(
        f"aggregate_mrlap: {summary['n_strata']} strata, {summary['n_corrected']} corrected, "
        f"{summary['n_insufficient_ivs']} insufficient-ivs, {summary['n_ldsc_flagged']} ldsc-flagged; "
        f"peak_rss_mb={resource['peak_rss_mb']:.1f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
