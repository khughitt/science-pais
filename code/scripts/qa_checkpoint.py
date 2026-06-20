#!/usr/bin/env python3
"""Two-severity raw-data QA checkpoint for t035 (WP2; t037 discipline).

ONE generic checkpoint, config-driven (config.yaml `qa.<dataset>`), dispatched
per dataset. Two severities:

  STRUCTURAL  (build-fatal) — donor-unique key, required group codes/counts,
              gene-id column present, exact G1-observed dims, G2 estimate column.
              ANY failure -> the script exits non-zero and the *.qa.pass sentinel
              is NOT written, so the Snakemake DAG halts.
  DISTRIBUTION (surfaced)   — log-scale bounds, % missing, feature-universe size,
              % integer. Reported as warnings; never blocks the build.

The qa_report.md is always written (even on failure) and is NOT a strict
Snakemake output, so failed-job cleanup cannot delete the evidence (plan:0003
KD3). Reports are timestamp-free so they diff cleanly across runs.
"""
from __future__ import annotations

import argparse
import gzip
import json
import statistics
import sys
from pathlib import Path

import yaml


# ----------------------------------------------------------------- helpers ---
def read_tsv(path: Path) -> tuple[list[str], list[list[str]]]:
    rows = path.read_text(encoding="utf-8").splitlines()
    header = rows[0].split("\t") if rows else []
    body = [r.split("\t") for r in rows[1:] if r]
    return header, body


def matrix_stats(path: Path, gene_id_column: str) -> dict:
    """Header columns, dims, and value distribution for a probe×sample matrix."""
    vals: list[float] = []
    missing = 0
    n_rows = 0
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        samples = header[1:]
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            n_rows += 1
            for cell in parts[1:]:
                if cell == "" or cell.upper() == "NA":
                    missing += 1
                else:
                    try:
                        vals.append(float(cell))
                    except ValueError:
                        missing += 1
    total_cells = n_rows * len(samples)
    return {
        "first_column": header[0] if header else "",
        "gene_id_ok": bool(header) and header[0] == gene_id_column,
        "n_probes": n_rows,
        "n_samples": len(samples),
        "samples": samples,
        "min": round(min(vals), 6) if vals else None,
        "max": round(max(vals), 6) if vals else None,
        "median": round(statistics.median(vals), 6) if vals else None,
        "pct_missing": round(100 * missing / total_cells, 4) if total_cells else 0.0,
    }


# --------------------------------------------------------------- GSE14577 ----
def check_gse14577(spec: dict, args) -> tuple[list, list, dict]:
    failures, warnings, facts = [], [], {}
    gene_col = spec["gene_id_column"]

    # per-platform matrix structural + distribution
    plat_paths = {"GPL96": Path(args.gpl96), "GPL97": Path(args.gpl97)}
    dist = spec["distribution"]
    for plat, path in plat_paths.items():
        st = matrix_stats(path, gene_col)
        facts[plat] = st
        exp = spec["platforms"][plat]
        if not st["gene_id_ok"]:
            failures.append(f"{plat}: first column is '{st['first_column']}', expected gene-id column '{gene_col}'")
        if st["n_probes"] != exp["n_probes"]:
            failures.append(f"{plat}: {st['n_probes']} probes, expected {exp['n_probes']} (parse damage?)")
        if st["n_samples"] != exp["n_samples"]:
            failures.append(f"{plat}: {st['n_samples']} samples, expected {exp['n_samples']}")
        # distribution (surfaced)
        if st["min"] is not None and st["min"] < dist["log2_min_floor"]:
            warnings.append(f"{plat}: min {st['min']} < log2 floor {dist['log2_min_floor']}")
        if st["max"] is not None and st["max"] > dist["log2_max_ceiling"]:
            warnings.append(f"{plat}: max {st['max']} > log2 ceiling {dist['log2_max_ceiling']}")
        if st["pct_missing"] > dist["max_pct_missing"]:
            warnings.append(f"{plat}: {st['pct_missing']}% missing > {dist['max_pct_missing']}%")

    # metadata structural: required groups + donor-unique key (chips per patient)
    header, body = read_tsv(Path(args.meta))
    col = {name: i for i, name in enumerate(header)}
    for need in ("group", "patient_key", "chip"):
        if need not in col:
            failures.append(f"metadata missing required column '{need}'")
    if not failures:
        groups_present = {r[col["group"]] for r in body}
        for g in spec["required_groups"]:
            if g not in groups_present:
                failures.append(f"metadata missing required group code '{g}'")
        # donor-unique key: each patient_key carries exactly chips_per_patient distinct chips
        chips_by_patient: dict[str, set] = {}
        for r in body:
            chips_by_patient.setdefault(r[col["patient_key"]], set()).add(r[col["chip"]])
        bad = {p: sorted(c) for p, c in chips_by_patient.items()
               if len(c) != spec["chips_per_patient"]}
        if bad:
            failures.append(f"{len(bad)} patient_key(s) not paired into {spec['chips_per_patient']} "
                            f"distinct chips: {dict(list(bad.items())[:5])}")
        facts["n_unique_patients"] = len(chips_by_patient)
        facts["group_counts_samples"] = {
            g: sum(1 for r in body if r[col["group"]] == g) for g in sorted(groups_present)
        }
    return failures, warnings, facts


# -------------------------------------------------------------- GSE130353 ----
def check_gse130353(spec: dict, args) -> tuple[list, list, dict]:
    failures, warnings, facts = [], [], {}

    # sample sheet structural: group counts, donor uniqueness, member presence
    header, body = read_tsv(Path(args.sheet))
    col = {name: i for i, name in enumerate(header)}
    for need in ("group", "donor_id", "member_present"):
        if need not in col:
            failures.append(f"sample_sheet missing required column '{need}'")
    if not any("missing required column" in f for f in failures):
        observed = {}
        for r in body:
            observed[r[col["group"]]] = observed.get(r[col["group"]], 0) + 1
        facts["observed_group_counts"] = observed
        if observed != spec["required_group_counts"]:
            failures.append(f"group counts {observed} != required {spec['required_group_counts']}")
        donors = {r[col["donor_id"]] for r in body}
        facts["n_donors"] = len(donors)
        if len(donors) != spec["n_donors"]:
            failures.append(f"{len(donors)} distinct donors, expected {spec['n_donors']}")
        if len(body) != spec["n_members"]:
            failures.append(f"{len(body)} sheet rows, expected {spec['n_members']} members")
        if spec.get("require_all_members_present"):
            unmatched = [r[col["accession"]] if "accession" in col else "?"
                         for r in body if r[col["member_present"]].lower() != "true"]
            if unmatched:
                failures.append(f"{len(unmatched)} sample(s) not matched to a tar member: {unmatched[:5]}")

    # parse contract structural: G2 estimate column + verdict + feature universe
    contract = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    g2 = contract.get("g2_verdict", {})
    insp = (contract.get("g2_mmseq_inspection") or [{}])[0]
    cols = insp.get("header_columns", [])
    est = spec["estimate_column"]
    facts["mmseq_columns"] = cols
    facts["g2_verdict"] = g2.get("verdict")
    facts["n_members_contract"] = contract.get("n_members")
    if est not in cols:
        failures.append(f"MMSEQ estimate column '{est}' absent from {cols}")
    if spec.get("require_g2_pass") and g2.get("verdict") != "PASS":
        failures.append(f"contract G2 verdict is {g2.get('verdict')}, expected PASS")
    if contract.get("n_members") != spec["n_members"]:
        failures.append(f"contract n_members {contract.get('n_members')} != {spec['n_members']}")

    # distribution (surfaced): feature universe + continuity of log_mu
    dist = spec["distribution"]
    n_features = insp.get("n_data_rows", 0)
    facts["n_features"] = n_features
    if n_features < dist["min_feature_universe"]:
        warnings.append(f"feature universe {n_features} < {dist['min_feature_universe']}")
    est_stats = insp.get("numeric_column_scale_stats", {}).get(est, {})
    pct_int = est_stats.get("pct_integer_like")
    facts["log_mu_scale"] = est_stats
    if pct_int is not None and pct_int > dist["max_pct_integer"]:
        warnings.append(f"{est} is {pct_int}% integer-like > {dist['max_pct_integer']}% (counts, not log_mu?)")
    return failures, warnings, facts


CHECKERS = {"gse14577": check_gse14577, "gse130353": check_gse130353}


# ----------------------------------------------------------------- report ----
def write_report(path: Path, dataset: str, failures, warnings, facts) -> None:
    verdict = "PASS" if not failures else "FAIL (structural)"
    lines = [
        f"# Raw QA report — {dataset}",
        "",
        f"**Verdict:** {verdict}  ",
        f"**Structural failures:** {len(failures)}  ",
        f"**Distribution warnings:** {len(warnings)}",
        "",
        "## Structural checks (build-fatal)",
        "",
    ]
    if failures:
        lines += [f"- ❌ {f}" for f in failures]
    else:
        lines.append("- ✅ all structural checks passed")
    lines += ["", "## Distribution checks (surfaced, not fatal)", ""]
    if warnings:
        lines += [f"- ⚠️ {w}" for w in warnings]
    else:
        lines.append("- ✅ no distribution warnings")
    lines += ["", "## Observed facts", "", "```json",
              json.dumps(facts, indent=2, sort_keys=True), "```", ""]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="two-severity raw-data QA checkpoint")
    ap.add_argument("--dataset", required=True, choices=sorted(CHECKERS))
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--report", required=True, type=Path)
    ap.add_argument("--sentinel", required=True, type=Path)
    # gse14577 inputs
    ap.add_argument("--gpl96", type=Path)
    ap.add_argument("--gpl97", type=Path)
    ap.add_argument("--meta", type=Path)
    # gse130353 inputs
    ap.add_argument("--sheet", type=Path)
    ap.add_argument("--contract", type=Path)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    spec = cfg["qa"][args.dataset]
    failures, warnings, facts = CHECKERS[args.dataset](spec, args)

    write_report(args.report, args.dataset, failures, warnings, facts)

    for w in warnings:
        print(f"[qa:{args.dataset}] WARN {w}", file=sys.stderr)
    if failures:
        for f in failures:
            print(f"[qa:{args.dataset}] STRUCTURAL FAIL {f}", file=sys.stderr)
        print(f"[qa:{args.dataset}] HALT: {len(failures)} structural failure(s); "
              f"sentinel withheld -> DAG stops. See {args.report}", file=sys.stderr)
        return 1

    # structural pass -> write the sentinel (the only strict Snakemake output)
    args.sentinel.parent.mkdir(parents=True, exist_ok=True)
    args.sentinel.write_text(
        f"PASS {args.dataset}: {len(warnings)} distribution warning(s). See {args.report}\n",
        encoding="utf-8",
    )
    print(f"[qa:{args.dataset}] PASS ({len(warnings)} warning(s)) -> {args.sentinel}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
