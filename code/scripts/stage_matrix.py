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

kind-handlers implemented here:
  matrix    a delimited genes x samples table (csv/tsv/txt, optionally gzipped) whose
            group is resolvable from on-disk data (`column_regex` or a `companion`
            metadata payload). Gene ids are symbol/RefSeq/Ensembl (tranche b map).
  prebuilt  a gene x sample matrix ALREADY produced by the upstream microarray chain
            (parse_series_matrix/parse_gse14577 -> harmonize -> collapse_probes); this
            handler adopts it into the uniform contract, resolving group from a
            `column_regex` (patient-key prefix) or a `sheet` (the chain's samples.tsv).
            probe->gene + platform probe->Ensembl mapping happened upstream (needs the
            platform .db, not the org.Hs.eg.db symbol map).
  tar       a per-sample RAW.tar of gene-level tables — each file member is ONE sample's
            column, keyed by a sample id pulled from the member filename; group is NOT in
            the tar and comes from an external metadata sheet (SOFT / series-matrix) via
            the `sheet` group_source.
A deposit whose group source cannot yet be resolved stays fail-early (`parse.status:
deferred` names its exact blocker — e.g. a group-metadata payload) so the contract is
executable, not fabricated.
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
def _covariate_spec(gs: dict, columns: list[str]) -> list[tuple[str, str]]:
    """Normalize `covariate_cols` to (source_col, sheet_name) pairs.

    Each entry is either a plain string (metadata column kept under its own name) or a
    `{col, as}` dict (renamed to the de_model's expected covariate name — e.g. the
    GSE128078 characteristics `individual_identifier`/`timepoint_day` -> subject/timepoint
    the `de_models` contract asks for). Fails early on an absent source column."""
    specs: list[tuple[str, str]] = []
    for c in gs.get("covariate_cols", []):
        if isinstance(c, dict):
            src, dst = c["col"], c.get("as", c["col"])
        else:
            src, dst = c, c
        if src not in columns:
            halt(f"declared covariate column '{src}' absent from metadata (has {columns})")
        specs.append((src, dst))
    return specs


def _resolution_report(mode: str, selectors: list[tuple[str, str]],
                       sel_hits: dict, n_seen: int) -> dict:
    """Per-selector capture counts for `_validate_arm_partition` (and the QA record).

    `selectors` is the ORDERED list of declared (selector, group) rules; `sel_hits` maps
    a selector to how many samples it actually captured (first-match-wins). n_seen is the
    number of candidate samples/rows the derive saw."""
    return {
        "mode": mode,
        "n_seen": int(n_seen),
        "rules": [{"selector": sel, "group": grp, "n_matched": int(sel_hits.get(sel, 0))}
                  for sel, grp in selectors],
    }


def _groups_from_table(df: pd.DataFrame, gs: dict) -> tuple[dict, dict, dict]:
    """sample -> group (+ covariates) from a metadata table, plus a RESOLUTION report.

    Shared by `companion` (raw metadata payload) and `sheet` (a processed samples table
    — the microarray chain OR a parse_geo_metadata series-matrix sheet). The join key is
    `sample_col` (the metadata column whose values ARE the expr column names — often
    differs from the GSM `sample` column, e.g. GSE270045 joins on `sample_id`). Raw
    condition -> contrast arm is applied HERE (stage_matrix is the sole place that maps
    condition -> arm), never in the parser, via EITHER:
      * `condition_col` + `level_map`   exact map of a characteristic (disease_state)
      * `group_regex_col` + `group_regex`  ordered {pattern, group} regex on a column
        (for deposits whose only group signal is in a free-text column, e.g. GSE270045
        title "Healthy Control"/"Long Covid" with no disease-state characteristic).
    The resolution report records, per declared selector, how many samples it captured —
    so `_validate_arm_partition` can fail-early on an empty arm (a too-loose sibling
    pattern silently emptying the other arm via first-match-wins — the QFS/CFS trap)."""
    key = gs["sample_col"]
    if key not in df.columns:
        halt(f"metadata join column '{key}' absent (has {list(df.columns)})")
    covs = _covariate_spec(gs, list(df.columns))

    if "condition_col" in gs:
        val, level_map = gs["condition_col"], gs["level_map"]
        if val not in df.columns:
            halt(f"metadata condition column '{val}' absent (has {list(df.columns)})")
        selectors = [(str(k), g) for k, g in level_map.items()]

        def _derive(row: pd.Series) -> tuple[str | None, str | None]:
            g = level_map.get(row[val])   # unmapped condition -> excluded
            return (g, str(row[val])) if g is not None else (None, None)
    elif "group_regex_col" in gs:
        import re
        col, rules = gs["group_regex_col"], gs["group_regex"]
        if col not in df.columns:
            halt(f"metadata group_regex column '{col}' absent (has {list(df.columns)})")
        compiled = [(re.compile(r["pattern"]), r["pattern"], r["group"]) for r in rules]
        selectors = [(r["pattern"], r["group"]) for r in rules]

        def _derive(row: pd.Series) -> tuple[str | None, str | None]:
            s = str(row[col])
            for rx, pat, g in compiled:
                if rx.search(s):
                    return g, pat
            return None, None
    else:
        halt("sheet/companion group_source needs `condition_col`+`level_map` "
             "or `group_regex_col`+`group_regex`")

    # rows whose join key is NaN/blank cannot join to ANY expr column — they are
    # non-joinable metadata rows (trailing blanks, unmapped samples), NOT ambiguous
    # duplicates. Drop them (recorded) BEFORE the dup-key check so a repeated empty key
    # (e.g. the 6 blank SampleName rows in the PXD companion sheet) is not mis-flagged as
    # an ambiguous duplicate — a false HALT that hides the real, clean 1:1 join.
    key_series = df[key].astype("string")
    joinable = key_series.notna() & key_series.str.strip().ne("")
    n_nonjoinable = int((~joinable).sum())
    df = pd.DataFrame(df[joinable])   # pd.DataFrame(...) keeps the type a DataFrame (mask widens it)

    # fail-closed: the metadata sheet is the label authority, so a duplicated (real) join
    # key is ambiguous (which row's group/covariates win?) — HALT rather than let the
    # last-seen row silently overwrite.
    key_vals = list(df[key])
    dups = sorted({v for v in key_vals if key_vals.count(v) > 1})
    if dups:
        halt(f"metadata join column '{key}' has duplicate values {dups} "
             f"— cannot resolve group/covariates unambiguously")

    group_of, covariates_of, sel_hits = {}, {}, {}
    for _, row in df.iterrows():
        s = row[key]
        g, sel = _derive(row)
        if g is not None:
            group_of[s] = g
            sel_hits[sel] = sel_hits.get(sel, 0) + 1
        covariates_of[s] = {dst: row[src] for src, dst in covs}
    resolution = _resolution_report(gs["mode"], selectors, sel_hits, len(df))
    resolution["n_nonjoinable_keys_dropped"] = n_nonjoinable
    return group_of, covariates_of, resolution


def resolve_groups(samples: list[str], parse: dict, raw_dir: Path,
                   proc_dir: Path) -> tuple[dict, dict, dict]:
    """sample -> group (+ optional covariates) from the declared `group_source`.

    Returns (group_of, covariates_of, resolution). The metadata source dir depends on the
    MODE, not the handler: `companion` reads a raw payload (raw_dir); `sheet` reads a
    PROCESSED samples table (proc_dir) — either the microarray chain's samples.tsv
    (prebuilt) or a parse_geo_metadata series-matrix sheet (matrix handler, group in
    series metadata). `deferred` HALTs naming the exact missing payload. `resolution`
    carries per-selector capture counts for `_validate_arm_partition`."""
    gs = parse["group_source"]
    mode = gs["mode"]
    if mode == "deferred":
        halt(f"group source deferred: {gs.get('needs', 'metadata payload not yet staged')} "
             f"— acquire it + declare a resolvable group_source before parsing this deposit")
    elif mode == "column_regex":
        import re
        rules = gs["map"]  # ordered list of {pattern, group}
        compiled = [(re.compile(r["pattern"]), r["pattern"], r["group"]) for r in rules]
        selectors = [(r["pattern"], r["group"]) for r in rules]
        group_of: dict[str, str] = {}
        sel_hits: dict[str, int] = {}
        for s in samples:
            for rx, pat, g in compiled:
                if rx.search(s):
                    group_of[s] = g
                    sel_hits[pat] = sel_hits.get(pat, 0) + 1
                    break
        return group_of, {}, _resolution_report(mode, selectors, sel_hits, len(samples))
    elif mode == "companion":
        meta = raw_dir / f"{gs['payload']}.data"
        if not meta.exists():
            halt(f"companion metadata payload {meta} absent (acquire '{gs['payload']}' first)")
        return _groups_from_table(pd.read_csv(meta, sep=gs.get("sep", "\t"), dtype=str), gs)
    elif mode == "sheet":
        meta = proc_dir / gs["file"]
        if not meta.exists():
            halt(f"processed samples sheet {meta} absent (run the upstream parse rule "
                 f"— microarray chain or parse_geo_metadata — first)")
        return _groups_from_table(pd.read_csv(meta, sep=gs.get("sep", "\t"), dtype=str), gs)
    halt(f"unknown group_source mode '{mode}' (column_regex|companion|sheet|deferred)")


def _validate_arm_partition(resolution: dict, arms: set[str], accession: str) -> dict:
    """Fail-early on a mis-declared group source BEFORE it silently corrupts the contrast.

    The downstream eligibility check flags a too-thin arm as a REVIEW verdict, but frames
    it as 'not eligible' and can miss the ROOT CAUSE: a declared arm rule that captured
    the WRONG samples or none at all. plan:0010 review (the GSE130353 QFS/CFS trap): a
    pattern loose enough to match both arms empties the other arm via first-match-wins,
    yet the surviving arm alone still passes the non-empty retain check. So HALT when a
    declared contrast ARM matched 0 samples, naming the dead selector(s) as the
    diagnostic. Rules mapping to a deliberately-excluded (non-arm) group may legitimately
    match 0 — those are recorded as `dead_excluded_rules`, not fatal. Returns the
    resolution annotated with those non-fatal dead rules (for the QA record)."""
    rules = resolution.get("rules", [])
    empty = {}
    for a in sorted(arms):
        arm_rules = [r for r in rules if r["group"] == a]
        if sum(r["n_matched"] for r in arm_rules) == 0:
            empty[a] = arm_rules
    if empty:
        detail = "; ".join(
            f"arm {a!r}: " + (", ".join(f"{r['selector']!r}->0" for r in rs) or "no declared rule")
            for a, rs in empty.items())
        halt(f"{accession}: contrast arm(s) {sorted(empty)} matched 0 of "
             f"{resolution.get('n_seen')} samples via the declared group source "
             f"(mode={resolution.get('mode')}) — {detail}. A one-armed contrast (a "
             f"too-loose sibling pattern capturing the other arm, or a typo'd field/level) "
             f"is refused here rather than surfacing later as a silent mis-label.")
    resolution = dict(resolution)
    resolution["dead_excluded_rules"] = [
        {"selector": r["selector"], "group": r["group"]}
        for r in rules if r["group"] not in arms and r["n_matched"] == 0]
    return resolution


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


# ---------------------------------------------------------------- kind: prebuilt
def parse_prebuilt(proc_dir: Path, parse: dict, hmap: dict | None) -> tuple[pd.DataFrame, dict]:
    """Adopt a gene x sample matrix ALREADY produced by the upstream microarray chain
    (parse_series_matrix/parse_gse14577 -> harmonize -> collapse_probes) into the
    uniform contract. The probe->gene collapse + platform probe->Ensembl mapping
    happened upstream (needs the platform .db, not the org.Hs.eg.db symbol map), so
    here the feature ids are bare Ensembl genes — run the passthrough harmonizer only
    to strip versions + validate, then a defensive dup-collapse (there should be none
    post-collapse). This keeps stage_matrix the SOLE producer of expr.gene.tsv.gz."""
    blob = proc_dir / parse["prebuilt_expr"]
    if not blob.exists():
        halt(f"prebuilt expr {blob} absent — run the upstream microarray parse/harmonize/collapse rules first")
    sep = parse.get("sep", "\t")
    with open_maybe_gz(blob) as fh:
        df = pd.read_csv(fh, sep=sep, dtype=str, index_col=False)
    gene_col = df.columns[parse.get("gene_id_col", 0)]
    raw_ids = df[gene_col].tolist()
    sample_cols = [c for c in df.columns if c != gene_col]
    mat = df[sample_cols].apply(pd.to_numeric, errors="coerce")

    mapped, gene_report = harmonize_gene_ids(raw_ids, parse["gene_id_namespace"], hmap)
    mat.index = pd.Index(mapped, name="gene_id")
    n_unmapped_rows = int(mat.index.isna().sum())
    mat = mat[mat.index.notna()]
    mat, n_dup = collapse_duplicates(mat, parse.get("duplicate_policy", "mean"))
    gene_report["n_out"] = int(mat.shape[0])
    gene_report["n_unmapped_rows_dropped"] = n_unmapped_rows
    gene_report["duplicates_collapsed"] = int(n_dup)
    gene_report["duplicate_policy"] = parse.get("duplicate_policy", "mean")
    gene_report["prebuilt_expr"] = parse["prebuilt_expr"]
    return mat, gene_report


# ---------------------------------------------------------------------- kind: tar
def _resolve_col(df: pd.DataFrame, spec) -> str:
    """A member column spec is a NAME (str) or a POSITIONAL index (int). Positional is
    required for deposits whose value column is named per-sample (GSE251872 `S###`)."""
    if isinstance(spec, int):
        if not (0 <= spec < len(df.columns)):
            halt(f"member column index {spec} out of range (has {len(df.columns)} cols)")
        return str(df.columns[spec])
    if spec not in df.columns:
        halt(f"member column '{spec}' absent (has {list(df.columns)})")
    return str(spec)


def parse_tar(raw_dir: Path, payload: str, parse: dict, hmap: dict | None) -> tuple[pd.DataFrame, dict]:
    """Per-sample RAW.tar of gene-level tables -> (Ensembl x samples DataFrame, gene report).

    Each file member matching `member_glob` is ONE sample: its (member_gene_col,
    member_value_col) become that sample's column, keyed by the sample id pulled from
    the member basename via `sample_id_regex` (group 1). member_gene_col/value_col are a
    NAME or a positional int (GSE251872's value column is named per-sample). Duplicate
    gene ids WITHIN a member (cufflinks emits >1 locus per gene symbol) collapse under
    `member_agg` before the cross-member merge; the cross-deposit Ensembl collapse then
    runs on the merged matrix, same as parse_matrix. Group is NOT in the tar — it comes
    from the metadata sheet (SOFT/series-matrix) via the `sheet` group_source."""
    import fnmatch
    import io
    import re
    import tarfile

    blob = raw_dir / f"{payload}.data"
    glob = parse["member_glob"]
    sid_rx = re.compile(parse["sample_id_regex"])
    comment = parse.get("member_comment")   # e.g. "#" for MMSEQ's mapped-fragments header
    agg = parse.get("member_agg", "sum")

    series: dict[str, pd.Series] = {}
    with tarfile.open(blob, "r") as tf:
        members = sorted((m for m in tf.getmembers() if m.isfile()), key=lambda m: m.name)
        for m in members:
            base = Path(m.name).name
            if not fnmatch.fnmatch(base, glob):
                continue
            mo = sid_rx.search(base)
            if not mo:
                halt(f"tar member '{base}' does not match sample_id_regex '{parse['sample_id_regex']}'")
            sid = mo.group(1)
            if sid in series:
                halt(f"tar sample id '{sid}' (from {base}) collides with an earlier member")
            fobj = tf.extractfile(m)
            if fobj is None:
                halt(f"tar member '{base}' is not extractable")
            raw = fobj.read()
            reader = gzip.open(io.BytesIO(raw), "rt", encoding="utf-8", errors="replace") \
                if base.endswith(".gz") else io.StringIO(raw.decode("utf-8", "replace"))
            df = pd.read_csv(reader, sep=parse.get("member_sep", "\t"),
                             dtype=str, comment=comment, index_col=False)
            gcol = _resolve_col(df, parse["member_gene_col"])
            vcol = _resolve_col(df, parse["member_value_col"])
            # within-member collapse of duplicate gene ids (cufflinks multi-locus symbols)
            mv = pd.DataFrame({
                "gene": pd.Series(df[gcol]).astype(str),
                "value": pd.to_numeric(pd.Series(df[vcol]), errors="coerce"),
            })
            series[sid] = pd.Series(mv.groupby("gene")["value"].agg(agg))

    if not series:
        halt(f"tar payload matched no members for glob '{glob}'")
    mat = pd.DataFrame(series)   # outer-join on gene id; samples = columns
    n_na_cells = int(mat.isna().sum().sum())
    raw_ids = [str(x) for x in mat.index]

    mapped, gene_report = harmonize_gene_ids(raw_ids, parse["gene_id_namespace"], hmap)
    mat.index = pd.Index(mapped, name="gene_id")
    n_unmapped_rows = int(mat.index.isna().sum())
    mat = mat[mat.index.notna()]
    mat, n_dup = collapse_duplicates(mat, parse.get("duplicate_policy", "sum"))
    gene_report["n_out"] = int(mat.shape[0])
    gene_report["n_unmapped_rows_dropped"] = n_unmapped_rows
    gene_report["duplicates_collapsed"] = int(n_dup)
    gene_report["duplicate_policy"] = parse.get("duplicate_policy", "sum")
    gene_report["n_members"] = len(series)
    gene_report["n_na_cells_merged"] = n_na_cells
    return mat, gene_report


KIND_HANDLERS = {"matrix", "prebuilt", "tar"}
DEFERRED_KINDS: dict[str, str] = {}


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
    origin = load_origin(raw_dir, payload)   # provenance = the RAW payload (csv/tsv/series_matrix/soft)
    hmap = load_harmonization(cfg, parse["gene_id_namespace"])
    proc_dir = Path(cfg["paths"]["processed"]) / accession

    # --- parse into an Ensembl x samples matrix; group resolution reads from the
    #     raw dir (matrix: companion payload) or the processed dir (prebuilt: the
    #     upstream microarray chain's samples sheet).
    if handler == "matrix":
        mat, gene_report = parse_matrix(raw_dir, payload, parse, hmap)
    elif handler == "tar":
        mat, gene_report = parse_tar(raw_dir, payload, parse, hmap)
    else:  # prebuilt
        mat, gene_report = parse_prebuilt(proc_dir, parse, hmap)
    all_samples = list(mat.columns)

    # --- expression scale: assert the declared scale against the observed data
    scale_report = _scale_verdict(mat, parse)

    # --- resolve groups + retain only the contrast arms ----------------------
    # group source dir is chosen by MODE inside resolve_groups (companion->raw_dir,
    # sheet->proc_dir), so both are handed in regardless of the parse handler.
    group_of, cov_of, resolution = resolve_groups(all_samples, parse, raw_dir, proc_dir)
    case, control = parse["case_label"], parse["control_label"]
    arms = {case, control}
    # fail-early: a declared arm that captured 0 samples (a too-loose sibling pattern or
    # a typo'd field) is a mis-declared group source, not a thin-cohort REVIEW — HALT with
    # the dead selector named, before the one-armed matrix reaches eligibility.
    resolution = _validate_arm_partition(resolution, arms, accession)
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
    # bool(...) coerces numpy.bool_ (from .all()) to a JSON-serializable Python bool.
    # notna() first: a missing value stringifies to "nan" (len 3), which .str.len() would
    # wrongly count as present — so a required covariate could be incomplete yet pass.
    def _cov_complete(c: str) -> bool:
        if c not in sheet.columns:
            return False
        col = pd.Series(sheet[c])
        return bool((col.notna() & col.astype(str).str.strip().ne("")).all())
    cov_present = {c: _cov_complete(c) for c in needed_cov}
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
                   "handler": handler,
                   # for prebuilt: the upstream parse->harmonize->collapse chain that
                   # produced the adopted gene matrix (probe->gene happened there).
                   "upstream": parse.get("upstream")},
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
            "group_resolution": resolution,   # per-selector capture counts (arm-partition audit)
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

    # A stale PASS sentinel — AND a prior PASS's expr/sheet — must never survive a
    # now-failing re-run, so "qa.json only" holds even after an earlier PASS.
    out_expr.parent.mkdir(parents=True, exist_ok=True)
    out_pass.unlink(missing_ok=True)
    out_expr.unlink(missing_ok=True)
    out_sheet.unlink(missing_ok=True)
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
    has_negative = stats.get("pct_negative", 0) > 0.0
    if declared == "counts":
        ok = is_integer and not has_negative           # true integer counts (DESeq2/edgeR-admissible)
    elif declared == "estimated_counts":
        # salmon/RSEM/pseudo-alignment EM counts: non-negative, count-MAGNITUDE, but
        # legitimately fractional — transcript posterior means summed to gene can be
        # heavily fractional (multimapped reads spread thinly), so an integer-fraction
        # gate is the WRONG test: it rejects valid EM matrices (e.g. GSE270045, 43%
        # integer-like, values 1e-8..5e4, library-size-varying column sums). The real
        # invariants are non-negative + count magnitude (max well above a normalized/
        # proportion range) → continuous, limma-only.
        ok = not has_negative and stats.get("max", 0) >= 100.0
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
