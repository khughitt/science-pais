# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""stage_matrix — WP1b per-deposit parse of a VERIFIED raw payload into the ONE
uniform expression contract (task:t117 / plan:0010).

Turns each heterogeneous, hash-verified raw payload (`<payload>.data` + its
`<payload>.origin.json` sidecar) into a BRUTALLY UNIFORM per-deposit output so
every downstream contrast meets the identical schema:

  {PROC}/{acc}/expr.gene.tsv.gz     genes (Ensembl, no version) x retained samples
  {PROC}/{acc}/sample_sheet.tsv     one row per retained sample: sample, group, + covariates
  {PROC}/{acc}/clean.qa.pass        sentinel (only written after a PASS contract)
  {PROC}/{acc}/stage_matrix.qa.json the per-deposit INGEST CONTRACT (review Finding F,
                                    pulled forward from WP2): records source payload,
                                    parser + kind-handler, gene-id namespace (source ->
                                    Ensembl), expression scale (declared vs observed),
                                    samples retained/dropped + reasons, duplicate handling,
                                    and contrast eligibility (arms + de_model covariates).

Design authority is config.yaml — this script HARD-CODES NOTHING about a deposit.
It reads the deposit's `parse:` block (ingest contract) + `de_models` entry (the
covariate columns the sample sheet must carry) + `acquisition` block (payload
provenance) from the config it is handed. Fail-early / no silent fallback
(AGENTS.md, plan:0003 review finding 6): an unresolved gene-id namespace, a scale
mismatch, a missing group source, or a de_model covariate the sheet cannot carry
is a HALT with a precise message — never a guessed label or a partial output.

kind-handlers implemented here (WP1b tranche 1): the `matrix` family — a delimited
genes x samples table (csv/tsv/txt, optionally gzipped) whose group is resolvable
from on-disk data (`column_regex` or a `companion` metadata payload). The microarray
(`series_matrix`, `soft`) + per-sample `tar` handlers and the symbol/RefSeq -> Ensembl
harmonization map are declared but fail-early (their `parse.status: deferred` names
the exact missing piece) so the contract is executable, not fabricated.
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path
from typing import NoReturn

import pandas as pd
import yaml

from acquire_common import scale_stats, sha256_path

SCRIPT_VERSION = "t117-stage_matrix/1"


# --------------------------------------------------------------------------- io
def halt(msg: str) -> NoReturn:
    sys.exit(f"[stage_matrix] HALT: {msg}")


def _atomic_text(path: Path, text: str) -> None:
    """Write text via a temp sibling + rename so a partial write never satisfies an output."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def load_origin(raw_dir: Path, payload: str) -> dict:
    p = raw_dir / f"{payload}.origin.json"
    if not p.exists():
        halt(f"missing origin sidecar {p} (was the payload acquired?)")
    return json.loads(p.read_text())


def open_maybe_gz(path: Path):
    """Text handle for a payload blob whose real kind (gz or not) is in origin.json."""
    with path.open("rb") as fh:
        magic = fh.read(2)
    if magic == b"\x1f\x8b":
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return path.open("rt", encoding="utf-8", errors="replace")


# ----------------------------------------------------------------- gene-id map
MAP_NAMESPACES = {"symbol", "alias", "refseq"}


def load_harmonization(cfg: dict, source_ns: str) -> dict | None:
    """Load + hash-verify the org.Hs.eg.db harmonization map for a non-Ensembl ns.

    Returns None for the Ensembl namespaces (no map needed). For symbol/alias/refseq
    it verifies the map file against the LOCKED config hash (empty => HALT, same
    fail-early discipline as the payloads) and returns {maps, guardrails, source}.
    The map is built by build_gene_id_map.R from the SAME org.Hs.eg.db the gene sets
    used — commensurability is a contract, not a coincidence."""
    if source_ns in ("ensembl", "ensembl_versioned"):
        return None
    if source_ns not in MAP_NAMESPACES:
        halt(f"gene-id namespace '{source_ns}' unknown (ensembl|ensembl_versioned|symbol|alias|refseq)")
    h = cfg.get("harmonization")
    if not h:
        halt("config.harmonization missing but a deposit declares a non-Ensembl gene-id namespace")
    map_tsv = Path(h["map_tsv"])
    if not map_tsv.exists():
        halt(f"harmonization map {map_tsv} absent — run build_gene_id_map (conda r-bioc) first")
    locked = h.get("map_sha256", "")
    if not locked:
        halt(f"config.harmonization.map_sha256 empty — pin it from the canonical "
             f"org.Hs.eg.db build (build_gene_id_map) before consuming {map_tsv}")
    got = sha256_path(map_tsv)
    if got != locked:
        halt(f"harmonization map sha256 mismatch (expected {locked}, got {got}) — "
             f"re-pin from a deliberate rebuild, never auto-accept")
    # maps[ns][source_id] = (ensembl_gene, n_targets); n_targets>=2 => ambiguous "first" pick
    maps: dict[str, dict[str, tuple[str, int]]] = {}
    with map_tsv.open() as fh:
        header = next(fh).rstrip("\n").split("\t")
        if header[:4] != ["source_id", "source_ns", "ensembl_gene", "n_targets"]:
            halt(f"harmonization map header {header} != expected "
                 f"[source_id, source_ns, ensembl_gene, n_targets] — rebuild build_gene_id_map")
        for line in fh:
            sid, ns, ens, n_targets = line.rstrip("\n").split("\t")
            maps.setdefault(ns, {})[sid] = (ens, int(n_targets))
    return {"maps": maps, "guardrails": h.get("guardrails", {}), "source": h.get("source", "")}


def harmonize_gene_ids(ids: list[str], source_ns: str,
                       hmap: dict | None) -> tuple[list[str], dict]:
    """Map the raw feature ids to the target Ensembl-gene axis.

    `ensembl` (bare ENSG passthrough) / `ensembl_versioned` (strip .version) map
    with no external table. `symbol` / `alias` / `refseq` resolve through the
    hash-verified org.Hs.eg.db map (`hmap`). Returns (mapped_ids, report);
    mapped_ids has one entry per input row (None where unmappable) so the caller
    collapses/drops deterministically. The report carries `map_rate` +
    `map_rate_ok` (fail-closed guardrail) so a deposit dominated by unmappable /
    wrong-namespace ids is marked ineligible, not emitted as a thin matrix."""
    report = {"source_namespace": source_ns, "target_namespace": "ensembl_gene",
              "n_in": len(ids), "version_stripped": False, "n_unmapped": 0}
    if source_ns in ("ensembl", "ensembl_versioned"):
        out, stripped, unmapped = [], False, 0
        for x in ids:
            x = str(x)
            if "." in x and x.split(".")[0].startswith("ENSG"):
                x = x.split(".")[0]
                stripped = True
            if not x.startswith("ENSG"):
                out.append(None); unmapped += 1
            else:
                out.append(x)
        report.update(version_stripped=stripped, n_unmapped=unmapped,
                      map_rate=round(1 - unmapped / max(len(ids), 1), 4), map_rate_ok=True)
        return out, report

    assert hmap is not None
    table = hmap["maps"].get(source_ns, {})
    gr = hmap["guardrails"]
    out, unmapped, looks_ensembl, ambiguous_mapped = [], 0, 0, 0
    for x in ids:
        x = str(x).split(".")[0] if source_ns == "refseq" else str(x)  # NM_x.v -> NM_x
        if x.startswith("ENSG"):
            looks_ensembl += 1
        hit = table.get(x)
        if hit is None:
            out.append(None); unmapped += 1
        else:
            ens, n_targets = hit
            out.append(ens)
            if n_targets >= 2:
                ambiguous_mapped += 1   # id resolves to >=2 ENSG; "first" picked one
    n = max(len(ids), 1)
    n_mapped = n - unmapped
    map_rate = round(n_mapped / n, 4)
    mixed_ns_frac = round(looks_ensembl / n, 4)   # declared non-Ensembl but ids look Ensembl
    ambiguous_frac = round(ambiguous_mapped / max(n_mapped, 1), 4)  # of the MAPPED ids
    min_map_rate = gr.get("min_map_rate", 0.6)
    max_mixed = gr.get("max_mixed_namespace_frac", 0.05)
    max_ambiguous = gr.get("max_ambiguous_mapped_frac", 0.20)
    report.update(
        n_unmapped=unmapped, map_rate=map_rate, min_map_rate=min_map_rate,
        mixed_namespace_frac=mixed_ns_frac, max_mixed_namespace_frac=max_mixed,
        ambiguous_mapped_frac=ambiguous_frac, max_ambiguous_mapped_frac=max_ambiguous,
        harmonization_source=hmap["source"])
    # fail closed on ANY of: too few mapped, wrong namespace, or mapped-but-mostly-ambiguous.
    report["map_rate_ok"] = (map_rate >= min_map_rate
                             and mixed_ns_frac <= max_mixed
                             and ambiguous_frac <= max_ambiguous)
    return out, report


def collapse_duplicates(df: pd.DataFrame, policy: str) -> tuple[pd.DataFrame, int]:
    """Collapse rows sharing an Ensembl id under a declared policy.

    `sum` (counts) / `mean` (continuous) / `max_total` (keep the highest-total row).
    Deterministic; returns (collapsed, n_collapsed_groups)."""
    dup_mask = df.index.duplicated(keep=False)
    n_dup_groups = int(df.index[dup_mask].nunique())
    if n_dup_groups == 0:
        return df, 0
    if policy == "sum":
        out = df.groupby(level=0, sort=True).sum()
    elif policy == "mean":
        out = df.groupby(level=0, sort=True).mean()
    elif policy == "max_total":
        order = df.sum(axis=1).groupby(level=0).idxmax()
        out = df.loc[order.values]
        out.index = order.index
        out = out.sort_index()
    else:
        halt(f"unknown duplicate_policy '{policy}' (sum|mean|max_total)")
    return out, n_dup_groups


# ----------------------------------------------------------------- group source
def resolve_groups(samples: list[str], parse: dict, raw_dir: Path) -> tuple[dict, dict]:
    """sample -> group (+ optional covariates) from the declared `group_source`.

    Returns (group_of, covariates_of). Only the two on-disk-resolvable modes are
    implemented; `deferred` HALTs naming the exact missing payload."""
    gs = parse["group_source"]
    mode = gs["mode"]
    if mode == "deferred":
        halt(f"group source deferred: {gs.get('needs', 'metadata payload not yet staged')} "
             f"— acquire it + declare a resolvable group_source before parsing this deposit")
    elif mode == "column_regex":
        import re
        rules = gs["map"]  # ordered list of {pattern, group}
        group_of: dict[str, str] = {}
        for s in samples:
            for rule in rules:
                if re.search(rule["pattern"], s):
                    group_of[s] = rule["group"]
                    break
        return group_of, {}
    elif mode == "companion":
        meta = raw_dir / f"{gs['payload']}.data"
        if not meta.exists():
            halt(f"companion metadata payload {meta} absent (acquire '{gs['payload']}' first)")
        df = pd.read_csv(meta, sep=gs.get("sep", "\t"), dtype=str)
        key, val = gs["sample_col"], gs["condition_col"]
        if key not in df.columns or val not in df.columns:
            halt(f"companion metadata missing column(s) {key}/{val}; has {list(df.columns)}")
        level_map = gs["level_map"]  # raw condition -> group
        group_of, covariates_of = {}, {}
        cov_cols = gs.get("covariate_cols", [])
        for _, row in df.iterrows():
            s = row[key]
            cond = row[val]
            if cond in level_map:
                group_of[s] = level_map[cond]
            covariates_of[s] = {c: row[c] for c in cov_cols if c in df.columns}
        return group_of, covariates_of
    halt(f"unknown group_source mode '{mode}' (column_regex|companion|deferred)")


# ------------------------------------------------------------------- kind: matrix
def parse_matrix(raw_dir: Path, payload: str, parse: dict, hmap: dict | None) -> tuple[pd.DataFrame, dict]:
    """Delimited genes x samples table -> (Ensembl x samples DataFrame, gene report)."""
    blob = raw_dir / f"{payload}.data"
    sep = parse.get("sep", "\t")
    with open_maybe_gz(blob) as fh:
        df = pd.read_csv(fh, sep=sep, dtype=str, index_col=False)
    gene_col = df.columns[parse.get("gene_id_col", 0)]
    drop = [df.columns[i] for i in parse.get("annotation_cols", [])]
    drop = [c for c in drop if c != gene_col]
    raw_ids = df[gene_col].tolist()
    sample_cols = [c for c in df.columns if c != gene_col and c not in drop]
    mat = df[sample_cols].apply(pd.to_numeric, errors="coerce")

    mapped, gene_report = harmonize_gene_ids(raw_ids, parse["gene_id_namespace"], hmap)
    mat.index = pd.Index(mapped, name="gene_id")
    n_unmapped_rows = mat.index.isna().sum()
    mat = mat[mat.index.notna()]
    mat, n_dup = collapse_duplicates(mat, parse.get("duplicate_policy", "sum"))
    gene_report["n_out"] = int(mat.shape[0])
    gene_report["n_unmapped_rows_dropped"] = int(n_unmapped_rows)
    gene_report["duplicates_collapsed"] = int(n_dup)
    gene_report["duplicate_policy"] = parse.get("duplicate_policy", "sum")
    return mat, gene_report


KIND_HANDLERS = {"matrix"}
DEFERRED_KINDS = {
    "series_matrix": "microarray series-matrix handler (probe->gene collapse via collapse_probes.R) — WP1b tranche 2",
    "soft": "GEO SOFT microarray handler (reuse parse_gse14577.py pattern) — WP1b tranche 2",
    "tar": "per-sample RAW.tar handler (reuse extract_gse130353.py pattern) — WP1b tranche 2",
}


# ------------------------------------------------------------------------- main
def run(config_path: Path, accession: str, out_expr: Path, out_sheet: Path,
        out_qa: Path, out_pass: Path) -> None:
    cfg = yaml.safe_load(config_path.read_text())
    raw_dir = Path(cfg["paths"]["raw"]) / accession
    if accession not in cfg.get("parse", {}):
        halt(f"no parse contract for {accession} in config.parse")
    parse = cfg["parse"][accession]
    de_model = _de_model_for(cfg, accession)

    handler = parse["handler"]
    if handler in DEFERRED_KINDS or parse.get("status") == "deferred":
        reason = parse.get("deferred_reason") or DEFERRED_KINDS.get(handler, "handler deferred")
        halt(f"{accession}: parse deferred — {reason}")
    if handler not in KIND_HANDLERS:
        halt(f"{accession}: unknown parse handler '{handler}'")

    payload = parse["payload"]
    origin = load_origin(raw_dir, payload)
    hmap = load_harmonization(cfg, parse["gene_id_namespace"])

    # --- parse the payload into an Ensembl x samples matrix ------------------
    mat, gene_report = parse_matrix(raw_dir, payload, parse, hmap)
    all_samples = list(mat.columns)

    # --- expression scale: assert the declared scale against the observed data
    scale_report = _scale_verdict(mat, parse)

    # --- resolve groups + retain only the contrast arms ----------------------
    group_of, cov_of = resolve_groups(all_samples, parse, raw_dir)
    case, control = parse["case_label"], parse["control_label"]
    arms = {case, control}
    retained, dropped = [], []
    for s in all_samples:
        g = group_of.get(s)
        if g in arms:
            retained.append(s)
        else:
            dropped.append({"sample": s, "reason": f"group={g!r} not in contrast arms {sorted(arms)}"})
    if not retained:
        halt(f"{accession}: no sample maps to the contrast arms {sorted(arms)} "
             f"(resolved groups: {sorted(set(group_of.values()))})")

    mat_out = mat[retained]

    # --- sample sheet: sample, group, + de_model covariates ------------------
    sheet_cols = parse.get("sheet_columns", ["sample", "group"])
    sheet_rows = []
    for s in retained:
        row = {"sample": s, "group": group_of[s]}
        row.update(cov_of.get(s, {}))
        sheet_rows.append(row)
    sheet = pd.DataFrame(sheet_rows)
    for c in sheet_cols:
        if c not in sheet.columns:
            sheet[c] = ""  # declared covariate the source could not supply -> visible blank
    sheet = sheet[[c for c in sheet_cols if c in sheet.columns]
                  + [c for c in sheet.columns if c not in sheet_cols]]

    # --- contrast eligibility (arms + de_model covariate coverage) -----------
    n_case = int((sheet["group"] == case).sum())
    n_control = int((sheet["group"] == control).sum())
    needed_cov = de_model.get("covariates", [])
    cov_present = {c: (c in sheet.columns and sheet[c].astype(str).str.len().gt(0).all())
                   for c in needed_cov}
    eligibility = {
        "de_model_design": de_model.get("design"),
        "de_model_stock_ok": de_model.get("stock_ok"),
        "required_covariates": needed_cov,
        "covariate_columns_present": cov_present,
        "n_case": n_case,
        "n_control": n_control,
        "both_arms_present": n_case >= 1 and n_control >= 1,
        "min_per_arm_ok": min(n_case, n_control) >= parse.get("min_per_arm", 2),
        # fail-closed gene-identity guardrail: a deposit whose ids map too poorly to
        # Ensembl (or are the wrong namespace) is NOT commensurable — mark ineligible
        # rather than let a thin matrix reach the rank code as if comparable.
        "gene_map_rate_ok": gene_report.get("map_rate_ok", True),
    }
    eligibility["eligible"] = (
        eligibility["both_arms_present"]
        and eligibility["min_per_arm_ok"]
        and all(cov_present.values())
        and eligibility["gene_map_rate_ok"]
    )

    # --- decide verdict BEFORE writing any expr/sheet (no-partial-output contract)
    mat_out = mat_out.sort_index()
    verdict = "PASS" if eligibility["eligible"] and scale_report["verdict"] == "PASS" else "REVIEW"
    qa = {
        "dataset": accession,
        "parser": {"script": "code/scripts/stage_matrix.py", "version": SCRIPT_VERSION,
                   "handler": handler},
        "source_payload": {
            "payload": payload,
            "original_filename": origin.get("original_filename"),
            "kind": origin.get("kind"),
            "url": origin.get("url"),
            "sha256": origin.get("sha256"),
            "bytes": origin.get("bytes"),
        },
        "gene_id": gene_report,
        "expression_scale": scale_report,
        "samples": {
            "n_total": len(all_samples),
            "n_retained": len(retained),
            "n_dropped": len(dropped),
            "group_counts": {g: int((sheet["group"] == g).sum()) for g in sorted(arms)},
            "dropped": dropped,
            "group_source": parse["group_source"]["mode"],
        },
        "duplicate_handling": {
            "policy": gene_report["duplicate_policy"],
            "duplicates_collapsed": gene_report["duplicates_collapsed"],
        },
        "contrast_eligibility": eligibility,
        "expr_out": {"rows": int(mat_out.shape[0]), "cols": int(mat_out.shape[1]),
                     "written": verdict == "PASS",
                     "sha256_note": "hash emitted by the datapackage step, not here"},
        "verdict": verdict,
    }

    # A stale PASS sentinel must never survive a now-failing re-run.
    out_expr.parent.mkdir(parents=True, exist_ok=True)
    out_pass.unlink(missing_ok=True)
    # qa.json is the DIAGNOSTIC — always emitted (atomically) so a REVIEW is inspectable.
    _atomic_text(out_qa, json.dumps(qa, indent=2) + "\n")

    if verdict != "PASS":
        # no expr/sheet/pass written -> no thin matrix can leak into a direct run.
        halt(f"{accession}: contract not PASS "
             f"(eligibility={eligibility['eligible']}, scale={scale_report['verdict']}) "
             f"— see {out_qa}; resolve before writing clean.qa.pass")

    # PASS: emit the matrix + sheet atomically, THEN the sentinel (write-order = gate).
    tmp_expr = out_expr.with_name(out_expr.name + ".tmp")
    mat_out.to_csv(tmp_expr, sep="\t", index=True, index_label="gene_id", compression="gzip")
    tmp_expr.replace(out_expr)
    _atomic_text(out_sheet, sheet.to_csv(sep="\t", index=False))
    out_pass.write_text(
        f"OK {accession} expr={mat_out.shape[0]}x{mat_out.shape[1]} "
        f"case={n_case} control={n_control} handler={handler}\n")
    print(f"[stage_matrix] {accession}: {mat_out.shape[0]} genes x {mat_out.shape[1]} samples "
          f"(case={n_case} control={n_control}); scale={scale_report['verdict']} "
          f"eligible={eligibility['eligible']}", file=sys.stderr)


def _de_model_for(cfg: dict, accession: str) -> dict:
    """The de_models entry for the contrast owning this accession (else default)."""
    for cname, c in cfg["contrasts"].items():
        if c["accession"] == accession:
            return cfg["de_models"].get(cname, cfg["de_models"]["default"])
    return cfg["de_models"]["default"]


def _scale_verdict(mat: pd.DataFrame, parse: dict) -> dict:
    """Assert the declared expression scale against the data (t035 G2 pattern)."""
    declared = parse["expression_scale"]
    sample_vals = mat.iloc[:, : min(mat.shape[1], 8)].to_numpy().ravel()
    vals = [float(v) for v in sample_vals if v == v][:200000]  # drop NaN
    stats = scale_stats(vals)
    is_integer = stats.get("pct_integer_like", 0) > 95.0
    is_count_scale = stats.get("pct_integer_like", 0) >= 50.0  # count-magnitude, allows EM fractions
    has_negative = stats.get("pct_negative", 0) > 0.0
    if declared == "counts":
        ok = is_integer and not has_negative           # true integer counts (DESeq2/edgeR-admissible)
    elif declared == "estimated_counts":
        # salmon/RSEM EM counts: non-negative, count-magnitude, but fractional
        # (transcript-level posterior means summed to gene) → continuous, limma-only.
        ok = is_count_scale and not has_negative
    elif declared in ("cpm", "fpkm", "tpm"):
        ok = not has_negative and not is_integer       # non-negative normalized continuous
    elif declared in ("log2_intensity", "log_mu"):
        ok = True                                      # continuous, sign-agnostic
    else:
        halt(f"unknown declared expression_scale '{declared}' "
             f"(counts|estimated_counts|cpm|fpkm|tpm|log2_intensity|log_mu)")
    out = {"declared": declared, "observed": stats,
           "continuous_only": declared != "counts",   # limma-only where not true integer counts
           "verdict": "PASS" if ok else "MISMATCH"}
    caveat = parse.get("scale_caveat")
    if caveat:
        out["caveat"] = caveat   # e.g. FPKM isoform->gene sum only approximately additive (sensitivity-only)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="parse a verified raw payload into the uniform expr contract")
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--accession", required=True)
    ap.add_argument("--out-expr", required=True, type=Path)
    ap.add_argument("--out-sheet", required=True, type=Path)
    ap.add_argument("--out-qa", required=True, type=Path)
    ap.add_argument("--qa-pass", required=True, type=Path)
    args = ap.parse_args()
    run(args.config, args.accession, args.out_expr, args.out_sheet, args.out_qa, args.qa_pass)
    return 0


if __name__ == "__main__":
    sys.exit(main())
