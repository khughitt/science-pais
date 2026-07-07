# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Emit the plan:0009 reproducible bundle from the three run-of-record manifests
(plan:0009 Task 5).

Reads the Task-1 `staging_manifest.json`, the Task-3 `naive_mr_results.json`, and
the Task-4 `mrlap_results.json` (plus `config.yaml` for the pinned params, sample
sizes, and package pins) and writes four bundle artifacts beside them:

  * `datapackage.json`   — entity cross-refs + input SHA-256 resources + provenance DAG
  * `qa_report.json`     — structural hard-stop checks (mechanics GO gate), machine form
  * `qa_report.md`       — the same checks as a human table
  * `run_metadata.json`  — seeds / versions / pinned MRlap+GenomicSEM commits / input SHA-256s

The scientific write-up (`results.md`) is authored by hand — this script emits only
the machine-checkable bundle. Every QA check is computed from the manifests, not
hard-coded: a check that cannot be satisfied from the manifests reports FAIL, so the
bundle honestly reflects the run rather than asserting success. Missing/malformed
input manifests HARD-STOP (this is a provenance artifact — a partial bundle is worse
than none).

All labels/scale caveats are re-derived from the manifests the upstream stages
already stamped (KD1 ancestry flag, KD3 bounded-sex, naive↔corrected sign-only) so
the bundle carries the same ceilings as every other output.
"""
from __future__ import annotations

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import yaml


def _load_json(path: str, what: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"emit_bundle: {what} missing: {path} — HALT")
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        raise SystemExit(f"emit_bundle: {what} malformed JSON: {path} ({e}) — HALT")


def _isfinite(x) -> bool:
    try:
        return math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


# --- QA checks ---------------------------------------------------------------
# Each check returns (name, status, detail). status ∈ {PASS, WARN, FAIL}.
# Overall is FAIL if any FAIL, else WARN if any WARN, else PASS. The check set
# mirrors plan:0009 "Decision criteria" (mechanics GO) + "Validation".

def check_staging(staging: dict) -> list[tuple]:
    checks = []
    exposures = staging["sumstats"]["exposures"]
    outcome = staging["sumstats"]["outcome"]
    exp_ok = all(e.get("sha256_pin_verified") is True and e.get("sha256") for e in exposures)
    checks.append((
        "exposures_staged_sha_verified",
        "PASS" if (len(exposures) == 6 and exp_ok) else "FAIL",
        f"{len(exposures)}/6 Ruth strata staged, sha256_pin_verified all True={exp_ok}",
    ))
    out_ok = bool(outcome.get("sha256"))
    checks.append((
        "outcome_staged_sha_present",
        "PASS" if out_ok else "FAIL",
        f"{outcome.get('accession')} sha256 present={out_ok}",
    ))
    ldsc = staging.get("ldsc_reference", {})
    ldsc_ok = bool(ldsc.get("eur_w_ld_chr", {}).get("archive_sha256")) and bool(ldsc.get("hm3"))
    checks.append((
        "ldsc_reference_staged_checksummed",
        "PASS" if ldsc_ok else "FAIL",
        f"eur_w_ld_chr archive_sha256 + hm3 present={ldsc_ok}; doi="
        f"{ldsc.get('eur_w_ld_chr', {}).get('doi')}",
    ))
    ld = staging.get("ld_panel", {})
    ld_ok = bool(ld.get("archive_sha256"))
    checks.append((
        "ld_panel_staged_checksummed",
        "PASS" if ld_ok else "FAIL",
        f"1000G-EUR archive_sha256 present={ld_ok}; doi={ld.get('doi')}",
    ))
    recon = ldsc.get("build_reconciliation", "")
    checks.append((
        "ld_build_reconciliation",
        "PASS" if recon.strip().endswith("PASS.") or "PASS" in recon else "FAIL",
        "GRCh38 sumstats vs GRCh37 references reconciled by rsID (build-independent).",
    ))
    return checks


def check_naive(naive: dict, cfg: dict) -> list[tuple]:
    checks = []
    strata = naive["strata"]
    f_min = cfg["instrument"]["f_min"]
    min_iv = cfg["instrument"]["min_instruments_mr"]

    f_vals = {s["stratum"]: s["mean_f_instruments"] for s in strata}
    f_ok = all(v >= f_min for v in f_vals.values())
    checks.append((
        "mean_F_ge_floor",
        "PASS" if f_ok else "FAIL",
        f"min mean-F={min(f_vals.values()):.1f} over 6 strata, floor={f_min}",
    ))

    iv_ok = all(s["n_harmonised"] >= min_iv for s in strata)
    checks.append((
        "instruments_harmonised_ge_floor",
        "PASS" if iv_ok else "FAIL",
        f"min n_harmonised={min(s['n_harmonised'] for s in strata)}, floor={min_iv}",
    ))

    finite_ok = True
    for s in strata:
        if s.get("status") != "estimated":
            finite_ok = False
            break
        for m in s["methods"]:
            if not all(_isfinite(m[f]) for f in ("b", "se", "pval")):
                finite_ok = False
    checks.append((
        "naive_estimators_finite",
        "PASS" if finite_ok else "FAIL",
        "IVW / MR-Egger / weighted-median all finite for all 6 strata.",
    ))

    seed_ok = naive["estimate_params"].get("weighted_median_seed") is not None
    checks.append((
        "weighted_median_seed_recorded",
        "PASS" if seed_ok else "FAIL",
        f"weighted_median_seed={naive['estimate_params'].get('weighted_median_seed')}",
    ))
    return checks


def check_mrlap(mrlap: dict, cfg: dict) -> list[tuple]:
    checks = []
    summ = mrlap["summary"]
    comp = mrlap["comparison"]

    mrlap_ok = (
        summ["n_strata"] == 6 and summ["n_corrected"] == 6 and summ["n_insufficient_ivs"] == 0
    )
    checks.append((
        "mrlap_ran_all_strata_corrected",
        "PASS" if mrlap_ok else "FAIL",
        f"n_strata={summ['n_strata']}, n_corrected={summ['n_corrected']}, "
        f"n_insufficient_ivs={summ['n_insufficient_ivs']}",
    ))

    overlap_ok = all(_isfinite(c.get("cross_trait_ldsc_intercept")) for c in comp)
    checks.append((
        "overlap_signal_recorded",
        "PASS" if overlap_ok else "FAIL",
        "cross-trait LDSC intercept (overlap driver) present + finite for all 6 strata.",
    ))

    scale_ok = all(
        c["mrlap_observed"]["scale"] == "MRlap std (SD/SD)"
        and c["mrlap_corrected"]["scale"] == "MRlap std (SD/SD)"
        and c["naive_ivw"]["scale"] == "log-OR/SD"
        and set(c["naive_vs_corrected"].keys()) == {"sign_concordant", "_note"}
        for c in comp
    )
    checks.append((
        "native_scale_labelled_no_cross_scale_merge",
        "PASS" if scale_ok else "FAIL",
        "MRlap std (SD/SD) vs naive log-OR/SD labelled; naive↔corrected is sign-only "
        "(no OR-magnitude merge).",
    ))

    params = mrlap["mrlap_params"]
    pinned = all(k in params for k in ("MR_threshold", "MR_pruning_dist", "MR_pruning_LD", "MR_reverse", "seed"))
    checks.append((
        "mrlap_instrument_params_pinned",
        "PASS" if pinned else "FAIL",
        f"MR_threshold={params.get('MR_threshold')} MR_pruning_dist={params.get('MR_pruning_dist')} "
        f"MR_pruning_LD={params.get('MR_pruning_LD')} MR_reverse={params.get('MR_reverse')} "
        f"seed={params.get('seed')} (naive↔MRlap instrument sets differ — delta ≠ pure overlap bias).",
    ))

    res = mrlap["resource"]
    res_ok = _isfinite(res.get("peak_rss_mb")) and _isfinite(res.get("total_wall_clock_s"))
    checks.append((
        "genomewide_resource_recorded",
        "PASS" if res_ok else "FAIL",
        f"peak_rss={res.get('peak_rss_mb'):.0f} MB, total_wall_clock={res.get('total_wall_clock_s'):.0f} s "
        f"(genome-wide MRlap munge + cross-trait LDSC).",
    ))

    setup = mrlap["setup"]
    gsem_ok = setup.get("genomicsem_sha") == cfg["mrlap_env"]["genomicsem_ref"]
    mrlap_ref_ok = setup.get("mrlap_ref_expected") == cfg["mrlap_env"]["mrlap_ref"]
    ver_ok = (
        setup.get("twosamplemr_version") == cfg["mrlap_env"]["twosamplemr_version_expected"]
        and setup.get("ieugwasr_version") == cfg["mrlap_env"]["ieugwasr_version_expected"]
    )
    checks.append((
        "packages_pinned",
        "PASS" if (gsem_ok and mrlap_ref_ok and ver_ok) else "FAIL",
        f"GenomicSEM sha matches ref={gsem_ok}; MRlap pinned to {setup.get('mrlap_ref_expected')} "
        f"(install={setup.get('mrlap_install_method')}); TwoSampleMR={setup.get('twosamplemr_version')} "
        f"ieugwasr={setup.get('ieugwasr_version')} match expected={ver_ok}. No Python-ldsc env "
        "(MRlap+GenomicSEM are the internal LDSC engine).",
    ))

    labels = mrlap["labels"]
    labels_ok = (
        bool(labels.get("ancestry_flag"))
        and bool(labels.get("bounded_sex"))
        and labels.get("overlap_correction_does_not_lift_ceiling") is True
    )
    checks.append((
        "ancestry_flag_nonprimary_bounded_sex_labels",
        "PASS" if labels_ok else "FAIL",
        "KD1 ancestry-flag/non-primary + KD3 bounded-sex + overlap-does-not-lift-ceiling stamped.",
    ))

    n_flag = summ.get("n_ldsc_flagged", 0)
    checks.append((
        "ldsc_quality_flags",
        "PASS" if n_flag == 0 else "WARN",
        f"n_ldsc_flagged={n_flag}",
    ))
    return checks


def overall_status(checks: list[tuple]) -> str:
    statuses = {c[1] for c in checks}
    if "FAIL" in statuses:
        return "FAIL"
    if "WARN" in statuses:
        return "WARN"
    return "PASS"


# --- emitters ----------------------------------------------------------------

def emit_qa(checks: list[tuple], mrlap: dict, outdir: Path) -> str:
    overall = overall_status(checks)
    qa_json = {
        "workflow": "wave1-mr-hormone-pilot",
        "plan": "plan:0009-wave1-mr-hormone-pilot",
        "task": "t089",
        "overall": overall,
        "checks": [{"check": n, "status": s, "detail": d} for (n, s, d) in checks],
        "labels": mrlap["labels"],
    }
    (outdir / "qa_report.json").write_text(json.dumps(qa_json, indent=2))

    lines = [
        "# QA report — wave1-mr-hormone-pilot (plan:0009 Task 4/5)",
        "",
        f"**Overall: {overall}**",
        "",
        "| check | status | detail |",
        "|---|---|---|",
    ]
    for (n, s, d) in checks:
        lines.append(f"| {n} | {s} | {d} |")
    res = mrlap["resource"]
    lines += [
        "",
        f"Genome-wide MRlap resource: peak ~{res['peak_rss_mb']:.0f} MB RSS, "
        f"{res['total_wall_clock_s']:.0f} s total wall-clock over six strata "
        f"(single-thread; `-c1`).",
        "",
        "_ANCESTRY-FLAGGED, NON-PRIMARY (KD1) — outcome GCST90454541 is a European-dominant "
        "multi-ancestry HGI meta with no EUR-only sibling; overlap-correction does NOT lift this. "
        "Male/female strata are a BOUNDED exposure-architecture read against a mixed-sex outcome "
        "(KD3) — NOT a sex-modification test. No result is primary evidence for hypothesis:0005 / "
        "question:0007 / question:0013._",
        "",
    ]
    (outdir / "qa_report.md").write_text("\n".join(lines))
    return overall


def emit_datapackage(staging: dict, outdir: Path) -> None:
    exposures = staging["sumstats"]["exposures"]
    outcome = staging["sumstats"]["outcome"]
    ldsc = staging["ldsc_reference"]
    ld = staging["ld_panel"]

    resources = []
    for e in exposures:
        resources.append({
            "name": f"exposure_{e['name']}",
            "path": e["local_path"],
            "sha256": e["sha256"],
            "source": e["source_url"],
            "entity": "dataset:ruth-2020-shbg-testosterone-gwas",
        })
    resources.append({
        "name": "outcome_sumstats",
        "path": outcome["local_path"],
        "sha256": outcome["sha256"],
        "source": outcome["source_url"],
        "entity": "dataset:covid19-hgi-longcovid-gwas",
    })
    resources.append({
        "name": "ldsc_ld_score_reference",
        "path": ldsc["eur_w_ld_chr"]["ld_folder"],
        "sha256": ldsc["eur_w_ld_chr"]["archive_sha256"],
        "source": f"https://doi.org/{ldsc['eur_w_ld_chr']['doi']}",
        "entity": "dataset:eur-ldsc-ld-score-reference",
    })
    resources.append({
        "name": "ld_panel",
        "path": ld["bfile_prefix"],
        "sha256": ld["archive_sha256"],
        "source": ld["source_url"],
        "entity": "dataset:1000g-eur-ld-panel",
    })
    for name, path in [
        ("staging_manifest", "results/wave1-mr-hormone-pilot/staging_manifest.json"),
        ("naive_mr_results", "results/wave1-mr-hormone-pilot/naive_mr_results.json"),
        ("mrlap_results", "results/wave1-mr-hormone-pilot/mrlap_results.json"),
        ("qa_report", "results/wave1-mr-hormone-pilot/qa_report.json"),
        ("run_metadata", "results/wave1-mr-hormone-pilot/run_metadata.json"),
        ("results_note", "results/wave1-mr-hormone-pilot/results.md"),
    ]:
        resources.append({"name": name, "path": path})

    dp = {
        "name": "wave1-mr-hormone-pilot",
        "title": (
            "Wave-1 MR Arm-B hormone pilot: sex-hormone liability → long-COVID "
            "(overlap-corrected, ancestry-flagged exploratory)"
        ),
        "entities": {
            "plan": "plan:0009-wave1-mr-hormone-pilot",
            "task": "task:t089",
            "datasets": [
                "dataset:ruth-2020-shbg-testosterone-gwas",
                "dataset:covid19-hgi-longcovid-gwas",
                "dataset:eur-ldsc-ld-score-reference",
                "dataset:1000g-eur-ld-panel",
            ],
        },
        "resources": resources,
        "provenance_dag": [
            {
                "from": ["dataset:ruth-2020-shbg-testosterone-gwas", "dataset:1000g-eur-ld-panel"],
                "rule": "build_instrument",
                "to": "instruments (6 strata: SHBG/testosterone × combined/male/female)",
            },
            {
                "from": ["instruments", "dataset:covid19-hgi-longcovid-gwas"],
                "rule": "naive_mr (IVW / MR-Egger / weighted-median)",
                "to": "naive_mr_results",
            },
            {
                "from": [
                    "dataset:ruth-2020-shbg-testosterone-gwas",
                    "dataset:covid19-hgi-longcovid-gwas",
                    "dataset:eur-ldsc-ld-score-reference",
                ],
                "rule": "canonicalize_sumstats + run_mrlap (internal munge + cross-trait LDSC + overlap correction)",
                "to": "mrlap_results",
            },
            {
                "from": ["staging_manifest", "naive_mr_results", "mrlap_results"],
                "rule": "emit_bundle",
                "to": "datapackage + qa_report + run_metadata",
            },
        ],
    }
    (outdir / "datapackage.json").write_text(json.dumps(dp, indent=2))


def emit_run_metadata(staging: dict, mrlap: dict, cfg: dict,
                      git_commit: str, outdir: Path) -> None:
    exposures = staging["sumstats"]["exposures"]
    outcome = staging["sumstats"]["outcome"]
    ldsc = staging["ldsc_reference"]
    ld = staging["ld_panel"]
    setup = mrlap["setup"]

    meta = {
        "plan": "plan:0009-wave1-mr-hormone-pilot",
        "task": "task:t089",
        "git_commit": git_commit,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "params": {
            "instrument": {
                "p_threshold": cfg["instrument"]["p_threshold"],
                "clump_r2": cfg["instrument"]["clump_r2"],
                "clump_kb": cfg["instrument"]["clump_kb"],
                "mhc_exclude": None,  # hormones are not HLA-dominated (plan:0009 Approach)
                "f_min": cfg["instrument"]["f_min"],
            },
            "harmonise": {"action": cfg["harmonise"]["action"]},
            "naive_estimate": {
                "methods": cfg["estimate"]["methods"],
                "weighted_median_seed": cfg["estimate"]["weighted_median_seed"],
                "weighted_median_bootstrap_n": cfg["estimate"]["weighted_median_bootstrap_n"],
            },
            "mrlap": {
                "MR_threshold": cfg["mrlap"]["MR_threshold"],
                "MR_pruning_dist": cfg["mrlap"]["MR_pruning_dist"],
                "MR_pruning_LD": cfg["mrlap"]["MR_pruning_LD"],
                "MR_reverse": cfg["mrlap"]["MR_reverse"],
                "seed": cfg["mrlap"]["seed"],
            },
        },
        "packages": {
            "r_version": setup.get("r_version"),
            "twosamplemr_version": setup.get("twosamplemr_version"),
            "ieugwasr_version": setup.get("ieugwasr_version"),
            "mrlap_version": setup.get("sessionInfo_pkgs", {}).get("MRlap"),
            "genomicsem_version": setup.get("sessionInfo_pkgs", {}).get("GenomicSEM"),
            "mrlap_ref": setup.get("mrlap_ref_expected"),
            "mrlap_install_method": setup.get("mrlap_install_method"),
            "mrlap_tarball_sha256": setup.get("mrlap_tarball_sha256"),
            "genomicsem_sha": setup.get("genomicsem_sha"),
            "genomicsem_ref": setup.get("genomicsem_ref_expected"),
            "github_install_methods": setup.get("github_install_methods"),
        },
        "input_sha256": {
            **{e["name"]: e["sha256"] for e in exposures},
            "outcome": outcome["sha256"],
            "ldsc_eur_w_ld_chr_archive": ldsc["eur_w_ld_chr"]["archive_sha256"],
            "ld_panel_archive": ld["archive_sha256"],
        },
        "sample_sizes": {
            **{e["name"]: e["n"] for e in cfg["exposures"]},
            "outcome_total_n": cfg["outcome"]["total_n"],
            "_note": (
                "KD-scale contract: exposure N is the continuous-trait N; outcome N is TOTAL "
                "(case+control, observed scale), NOT effective N."
            ),
        },
        "outcome_stratum": outcome["accession"],
        "scale_note": (
            "Naive IVW/Egger/WM are log-OR/SD on the 1000G-EUR-clumped instrument set; MRlap "
            "observed+corrected are MRlap-standardized (SD/SD) on MRlap's genome-wide "
            "distance-pruned set. Cross-arm comparison is SIGN/DIRECTION only."
        ),
        "ancestry_note": mrlap["labels"]["ancestry_flag"],
    }
    (outdir / "run_metadata.json").write_text(json.dumps(meta, indent=2))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--staging", required=True)
    p.add_argument("--naive", required=True)
    p.add_argument("--mrlap", required=True)
    p.add_argument("--outdir", required=True)
    p.add_argument("--git-commit", default="UNKNOWN")
    a = p.parse_args()

    cfg = yaml.safe_load(Path(a.config).read_text())
    staging = _load_json(a.staging, "staging manifest")
    naive = _load_json(a.naive, "naive-MR manifest")
    mrlap = _load_json(a.mrlap, "MRlap manifest")

    outdir = Path(a.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    checks = check_staging(staging) + check_naive(naive, cfg) + check_mrlap(mrlap, cfg)
    overall = emit_qa(checks, mrlap, outdir)
    emit_datapackage(staging, outdir)
    emit_run_metadata(staging, mrlap, cfg, a.git_commit, outdir)

    print(f"emit_bundle: QA overall={overall}; wrote datapackage.json, qa_report.{{json,md}}, "
          f"run_metadata.json to {outdir}")
    if overall == "FAIL":
        raise SystemExit("emit_bundle: QA overall=FAIL — bundle emitted but mechanics gate FAILED — HALT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
