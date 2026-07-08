# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""reconcile_qa — roll the per-deposit stage_matrix.qa.json ingest contracts up into ONE
cross-deposit reconciliation table (task:t117 / plan:0010, project-review item #3).

stage_matrix emits a per-deposit `stage_matrix.qa.json` (the ingest contract), but nothing
aggregated them — so the heterogeneity that MATTERS before the rank step (mixed expression
scales, mixed gene-id namespaces, arm balance, covariate coverage) was only visible one
deposit at a time. This reads every supplied qa.json and emits:

  {out_tsv}   one row per deposit: verdict, handler, expression scale (+ its verdict),
              gene-id namespace + map rate, gene count, sample/arm counts, DE design,
              covariate coverage, eligibility — a single reviewable QA sheet.
  {out_json}  a machine summary: PASS/REVIEW counts, the DISTINCT expression scales and
              gene namespaces across the corpus (the modeling-risk surface), gene-count
              spread, and a `warnings` list (any deposit whose scale verdict != PASS, whose
              gene map rate is soft-low, whose required covariates are incomplete, whose
              arms are thin, or that carries a non-fatal dead selector).

Fail-early: a qa.json that is missing or unparseable is a HALT (never a silent skip — a
gap in the reconciliation must be loud). The rank pipeline pools deposits only at the NES
level, so MIXED expression scales are admissible ONLY IF each deposit's DE contrast fully
absorbs its own scale; this table surfaces the scale mix so that assumption is reviewed,
not assumed."""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path
from typing import NoReturn

# soft (advisory) gene-map-rate floor for the warnings column; the HARD fail-closed floor
# is per-deposit in stage_matrix (config.harmonization.guardrails.min_map_rate).
SOFT_MAP_RATE_WARN = 0.70

# stable column order for the reconciliation sheet
COLUMNS = [
    "dataset", "verdict", "handler", "expr_scale", "scale_verdict", "continuous_only",
    "gene_ns_source", "gene_ns_target", "map_rate", "map_rate_ok", "n_genes",
    "dup_policy", "dup_collapsed", "n_total", "n_retained", "n_dropped",
    "n_case", "n_control", "group_source", "de_design", "stock_ok",
    "required_covariates", "covariates_ok", "eligible",
]


def halt(msg: str) -> NoReturn:
    sys.exit(f"[reconcile_qa] HALT: {msg}")


def _row(qa: dict) -> dict:
    """Flatten one stage_matrix.qa.json into a reconciliation row."""
    gene = qa.get("gene_id", {})
    scale = qa.get("expression_scale", {})
    samples = qa.get("samples", {})
    elig = qa.get("contrast_eligibility", {})
    cov_present = elig.get("covariate_columns_present", {})
    return {
        "dataset": qa.get("dataset"),
        "verdict": qa.get("verdict"),
        "handler": qa.get("parser", {}).get("handler"),
        "expr_scale": scale.get("declared"),
        "scale_verdict": scale.get("verdict"),
        "continuous_only": scale.get("continuous_only"),
        "gene_ns_source": gene.get("source_namespace"),
        "gene_ns_target": gene.get("target_namespace"),
        "map_rate": gene.get("map_rate"),
        "map_rate_ok": gene.get("map_rate_ok"),
        "n_genes": gene.get("n_out"),
        "dup_policy": qa.get("duplicate_handling", {}).get("policy"),
        "dup_collapsed": qa.get("duplicate_handling", {}).get("duplicates_collapsed"),
        "n_total": samples.get("n_total"),
        "n_retained": samples.get("n_retained"),
        "n_dropped": samples.get("n_dropped"),
        "n_case": elig.get("n_case"),
        "n_control": elig.get("n_control"),
        "group_source": samples.get("group_source"),
        "de_design": elig.get("de_model_design"),
        "stock_ok": elig.get("de_model_stock_ok"),
        "required_covariates": ",".join(elig.get("required_covariates", [])) or "-",
        "covariates_ok": all(cov_present.values()) if cov_present else True,
        "eligible": elig.get("eligible"),
    }


def _warnings(qa: dict, row: dict) -> list[str]:
    """Per-deposit advisories a reviewer should see even when the verdict is PASS."""
    w = []
    if row["scale_verdict"] != "PASS":
        w.append(f"expression-scale verdict {row['scale_verdict']!r} (declared {row['expr_scale']!r})")
    mr = row["map_rate"]
    if isinstance(mr, (int, float)) and mr < SOFT_MAP_RATE_WARN:
        w.append(f"gene map_rate {mr} < soft floor {SOFT_MAP_RATE_WARN}")
    if row["covariates_ok"] is False:
        w.append(f"required covariates incomplete ({row['required_covariates']})")
    if row["eligible"] is False:
        w.append("contrast NOT eligible")
    if isinstance(row["n_case"], int) and isinstance(row["n_control"], int) \
            and min(row["n_case"], row["n_control"]) < 3:
        w.append(f"thin arm (case={row['n_case']}, control={row['n_control']})")
    dead = qa.get("samples", {}).get("group_resolution", {}).get("dead_excluded_rules", [])
    if dead:
        w.append(f"dead (non-fatal) excluded selector(s): {[d['selector'] for d in dead]}")
    if qa.get("expression_scale", {}).get("caveat"):
        w.append(f"scale caveat: {qa['expression_scale']['caveat']}")
    return w


def reconcile(qa_paths: list[Path], out_tsv: Path, out_json: Path) -> dict:
    rows, warnings = [], {}
    for p in qa_paths:
        if not p.exists():
            halt(f"qa.json {p} absent — every declared deposit must have staged before "
                 f"reconciliation (no silent gaps)")
        try:
            qa = json.loads(p.read_text())
        except json.JSONDecodeError as e:
            halt(f"qa.json {p} is unparseable: {e}")
        row = _row(qa)
        rows.append(row)
        w = _warnings(qa, row)
        if w:
            warnings[row["dataset"]] = w
    rows.sort(key=lambda r: str(r["dataset"]))

    genes = [r["n_genes"] for r in rows if isinstance(r["n_genes"], int)]
    scales: dict[str, int] = {}
    namespaces: dict[str, int] = {}
    for r in rows:
        scales[str(r["expr_scale"])] = scales.get(str(r["expr_scale"]), 0) + 1
        ns = f"{r['gene_ns_source']}->{r['gene_ns_target']}"
        namespaces[ns] = namespaces.get(ns, 0) + 1

    summary = {
        "n_deposits": len(rows),
        "verdicts": {v: sum(1 for r in rows if r["verdict"] == v)
                     for v in sorted({str(r["verdict"]) for r in rows})},
        "expression_scales": dict(sorted(scales.items())),
        "gene_namespaces": dict(sorted(namespaces.items())),
        "de_designs": sorted({str(r["de_design"]) for r in rows}),
        "group_sources": sorted({str(r["group_source"]) for r in rows}),
        "n_genes": {"min": min(genes), "max": max(genes),
                    "median": int(statistics.median(genes))} if genes else {},
        "total_case": sum(r["n_case"] for r in rows if isinstance(r["n_case"], int)),
        "total_control": sum(r["n_control"] for r in rows if isinstance(r["n_control"], int)),
        # the rank step pools deposits ONLY at the NES level, so >1 expression scale is
        # admissible IFF each deposit's DE contrast absorbs its own scale — surfaced, not assumed.
        "scale_heterogeneity": len(scales) > 1,
        "warnings": warnings,
    }

    out_tsv.parent.mkdir(parents=True, exist_ok=True)
    header = "\t".join(COLUMNS)
    body = "\n".join("\t".join(str(r.get(c, "")) for c in COLUMNS) for r in rows)
    _atomic(out_tsv, header + "\n" + body + "\n")
    _atomic(out_json, json.dumps(summary, indent=2) + "\n")
    return summary


def _atomic(path: Path, text: str) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def main() -> int:
    ap = argparse.ArgumentParser(description="reconcile per-deposit stage_matrix.qa.json into one QA sheet")
    ap.add_argument("--qa", required=True, nargs="+", type=Path, help="stage_matrix.qa.json paths")
    ap.add_argument("--out-tsv", required=True, type=Path)
    ap.add_argument("--out-json", required=True, type=Path)
    args = ap.parse_args()
    s = reconcile(args.qa, args.out_tsv, args.out_json)
    print(f"[reconcile_qa] {s['n_deposits']} deposits: verdicts={s['verdicts']}; "
          f"scales={list(s['expression_scales'])}; namespaces={list(s['gene_namespaces'])}; "
          f"case/control={s['total_case']}/{s['total_control']}; "
          f"{len(s['warnings'])} deposit(s) with advisories", file=sys.stderr)
    for ds, w in s["warnings"].items():
        print(f"[reconcile_qa]   {ds}: {'; '.join(w)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
