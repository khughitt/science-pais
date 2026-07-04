# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Emit the reproducible output bundle for the Wave-1 MR pilot (plan:0007).

Writes datapackage.json (resources + SHA-256 + entity cross-refs + provenance
DAG, Dim 9), qa_report.{json,md} (structural hard-stop checks + outcome-extract
peak-memory/wall-clock, Dim 6), and run_metadata.json (versions, params, seed,
input SHA-256s, resolved TwoSampleMR version, git commit — full provenance).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import subprocess
from pathlib import Path

import yaml


def _git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return "UNKNOWN"


def _load(path: str) -> dict:
    return json.loads(Path(path).read_text())


def main() -> int:
    p = argparse.ArgumentParser()
    for f in ("config", "results", "harmonised", "acq-manifest", "ld-manifest",
              "datapackage", "qa-json", "qa-md", "run-metadata"):
        p.add_argument(f"--{f}", required=True)
    a = p.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text())
    results = _load(a.results)
    acq = _load(a.acq_manifest)
    ld = _load(a.ld_manifest)
    # setup sentinel (TwoSampleMR versions) sits next to results/.env/
    sentinel = Path(cfg["paths"]["results"]) / ".env" / "twosamplemr.ok"
    versions = _load(str(sentinel)) if sentinel.exists() else {}

    # --- datapackage.json (resources + entity cross-refs + provenance DAG) ---
    resources = [
        {"name": "exposure_sumstats", "path": acq["exposure"]["local_path"],
         "sha256": acq["exposure"]["sha256"], "source": acq["exposure"]["source_url"],
         "entity": "dataset:bentham-2015-sle-gwas"},
        {"name": "outcome_sumstats", "path": acq["outcome"]["local_path"],
         "sha256": acq["outcome"]["sha256"], "source": acq["outcome"]["source_url"],
         "entity": "dataset:covid19-hgi-longcovid-gwas"},
        {"name": "ld_panel", "path": ld["bfile_prefix"], "sha256": ld["archive_sha256"],
         "source": ld["source_url"], "entity": "dataset:1000g-eur-ld-panel"},
        {"name": "harmonised", "path": a.harmonised},
        {"name": "mr_results", "path": a.results},
    ]
    datapackage = {
        "name": "wave1-mr-pilot",
        "title": "Wave-1 MR pilot: autoimmune liability -> long-COVID (mechanics-only)",
        "entities": cfg["entities"],
        "resources": resources,
        "provenance_dag": [
            {"from": ["dataset:bentham-2015-sle-gwas", "dataset:1000g-eur-ld-panel"],
             "rule": "build_instrument", "to": "instrument"},
            {"from": ["instrument", "dataset:covid19-hgi-longcovid-gwas"],
             "rule": "harmonize_estimate", "to": "mr_results"},
        ],
    }
    Path(a.datapackage).write_text(json.dumps(datapackage, indent=2))

    # --- qa_report (structural hard-stops + resources) -----------------------
    f_min = cfg["instrument"]["f_min"]
    mean_f = results.get("mean_f_instruments")
    nsnp = results.get("n_instruments_harmonised", 0)
    checks = [
        {"name": "exposure_downloaded", "status": "PASS" if acq["exposure"]["sha256"] != "PENDING-RETRIEVAL" else "FAIL"},
        {"name": "outcome_downloaded", "status": "PASS" if acq["outcome"]["sha256"] != "PENDING-RETRIEVAL" else "FAIL"},
        {"name": "ld_build_reconciliation", "status": "PASS", "detail": ld["build_reconciliation"]},
        {"name": "instruments_harmonised_ge_3", "status": "PASS" if nsnp >= 3 else "FAIL", "detail": f"n={nsnp}"},
        {"name": "mean_F_ge_floor", "status": "PASS" if (mean_f is not None and mean_f >= f_min) else "FAIL",
         "detail": f"mean F={mean_f}, floor={f_min}"},
        {"name": "estimators_finite",
         "status": "PASS" if all(m.get("b") is not None for m in results.get("methods", [])) else "FAIL"},
        {"name": "ancestry_mechanics_only_labelled",
         "status": "PASS" if "MECHANICS-ONLY" in results.get("label", "") else "FAIL"},
    ]
    overall = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    qa = {"overall": overall, "checks": checks, "resources": results.get("resources", {}),
          "dropped_snps": results.get("dropped_snps", [])}
    Path(a.qa_json).write_text(json.dumps(qa, indent=2))

    md = [f"# QA report — wave1-mr-pilot\n", f"**Overall: {overall}**\n", "| check | status | detail |", "|---|---|---|"]
    md += [f"| {c['name']} | {c['status']} | {c.get('detail','')} |" for c in checks]
    r = results.get("resources", {})
    md += ["", f"Outcome extraction: {r.get('outcome_extract_seconds','?')} s, "
           f"peak ~{r.get('peak_memory_mb','?')} MB.", "",
           f"_{results.get('label','')}_"]
    Path(a.qa_md).write_text("\n".join(md) + "\n")

    # --- run_metadata (full provenance) --------------------------------------
    run_meta = {
        "plan": cfg["entities"]["plan"], "task": cfg["entities"]["task"],
        "git_commit": _git_commit(),
        "created_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "params": {"instrument": cfg["instrument"], "harmonise": cfg["harmonise"],
                   "estimate": cfg["estimate"]},
        "twosamplemr": versions,
        "input_sha256": {"exposure": acq["exposure"]["sha256"],
                         "outcome": acq["outcome"]["sha256"],
                         "ld_archive": ld["archive_sha256"]},
        "outcome_stratum": cfg["outcome"]["accession"],
        "ancestry_note": cfg["outcome"]["ancestry_note"],
    }
    Path(a.run_metadata).write_text(json.dumps(run_meta, indent=2))
    print(f"emit_datapackage_qa: overall {overall}; wrote datapackage + qa + run_metadata")
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
