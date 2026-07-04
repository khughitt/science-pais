# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Aggregate the six per-stratum instrument sidecars into one manifest (plan:0009 Task 2).

Reads the six `build_instrument.R` JSON sidecars + their Snakemake `benchmark:`
TSVs (wall-clock + peak RSS, F3) + the `setup_twosamplemr` sentinel, and writes
one `instruments_manifest.json` recording, per stratum: attrition counts,
instrument counts, mean/min/max F, `eligible_for_mr` + reasons, quality flags,
and resource usage — plus a cross-stratum summary (n eligible/quarantined) and
the resolved TwoSampleMR/ieugwasr versions (F1).

Structural completeness is a hard requirement: this is the single artifact
Task 3/4 read to decide which strata to use, so a missing or malformed sidecar
or benchmark TSV HARD-STOPS rather than silently degrading the manifest.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import yaml


def _stratum_from_benchmark_path(path: Path) -> str:
    name = path.name
    suffix = ".benchmark.tsv"
    if not name.endswith(suffix):
        raise SystemExit(f"aggregate: benchmark filename does not end in {suffix}: {path}")
    return name[: -len(suffix)]


def load_sidecar(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate: sidecar missing: {path} — HALT")
    try:
        rec = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate: sidecar malformed JSON: {path} ({e}) — HALT")
    required = {
        "stratum", "accession", "trait", "sex", "attrition", "n_genomewide_sig",
        "n_instruments", "mean_F", "min_F", "max_F", "clump", "mhc_excluded",
        "eligible_for_mr", "eligibility_reasons", "quality_flags", "instrument_tsv",
    }
    missing = required - rec.keys()
    if missing:
        raise SystemExit(f"aggregate: sidecar {path} missing required key(s) {sorted(missing)} — HALT")
    return rec


def load_benchmark(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate: benchmark TSV missing: {path} — HALT")
    stratum = _stratum_from_benchmark_path(p)
    with p.open(newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise SystemExit(f"aggregate: benchmark TSV {path} has no data row — HALT (malformed)")
    row = rows[-1]  # last invocation, in case of a re-run
    for col in ("s", "max_rss"):
        if col not in row or row[col] in (None, ""):
            raise SystemExit(f"aggregate: benchmark TSV {path} missing '{col}' column/value — HALT (malformed)")
    try:
        wall_clock_s = float(row["s"])
        max_rss_mb = float(row["max_rss"])
    except ValueError as e:
        raise SystemExit(f"aggregate: benchmark TSV {path} non-numeric s/max_rss ({e}) — HALT (malformed)")
    return {"stratum": stratum, "wall_clock_s": wall_clock_s, "max_rss_mb": max_rss_mb}


def load_setup_sentinel(path: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"aggregate: setup_twosamplemr sentinel missing: {path} — HALT")
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"aggregate: setup sentinel malformed JSON: {path} ({e}) — HALT")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--sidecars", required=True, nargs="+")
    p.add_argument("--benchmarks", required=True, nargs="+")
    p.add_argument("--setup", required=True)
    p.add_argument("--manifest", required=True)
    a = p.parse_args()

    cfg = yaml.safe_load(Path(a.config).read_text())
    instrument_params = dict(cfg["instrument"])
    instrument_params.setdefault("mhc_exclude", None)  # absent in config == off (plan:0009 Task 2)

    strata = [load_sidecar(s) for s in a.sidecars]
    strata_by_name = {s["stratum"]: s for s in strata}
    if len(strata_by_name) != len(strata):
        raise SystemExit("aggregate: duplicate stratum name across sidecars — HALT")

    benchmarks = [load_benchmark(b) for b in a.benchmarks]
    benchmarks_by_name = {b["stratum"]: b for b in benchmarks}
    if len(benchmarks_by_name) != len(benchmarks):
        raise SystemExit("aggregate: duplicate stratum name across benchmark TSVs — HALT")

    missing_benchmarks = set(strata_by_name) - set(benchmarks_by_name)
    if missing_benchmarks:
        raise SystemExit(f"aggregate: no benchmark TSV for stratum/strata {sorted(missing_benchmarks)} — HALT")
    extra_benchmarks = set(benchmarks_by_name) - set(strata_by_name)
    if extra_benchmarks:
        raise SystemExit(f"aggregate: benchmark TSV for unknown stratum/strata {sorted(extra_benchmarks)} — HALT")

    setup = load_setup_sentinel(a.setup)

    eligible = [s["stratum"] for s in strata if s["eligible_for_mr"]]
    quarantined = [
        {"stratum": s["stratum"], "reasons": s["eligibility_reasons"]}
        for s in strata if not s["eligible_for_mr"]
    ]
    summary = {
        "n_strata": len(strata),
        "n_eligible": len(eligible),
        "n_quarantined": len(quarantined),
        "quarantined": quarantined,
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
    }

    manifest = {
        "plan": "plan:0009-wave1-mr-hormone-pilot",
        "task": "t089",
        "stage": "Task 2 — hormone instruments",
        "instrument_params": instrument_params,
        "strata": strata,
        "summary": summary,
        "twosamplemr_setup": setup,
        "resource": resource,
    }
    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    print(
        f"aggregate_instruments: {summary['n_strata']} strata, "
        f"{summary['n_eligible']} eligible, {summary['n_quarantined']} quarantined; "
        f"peak_rss_mb={resource['peak_rss_mb']:.1f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
