# science:code
# status: workflow-owned
# task_ids: [t035]
# science:end

# =============================================================================
# common.smk — shared helper functions (kept out of rule files so each rule
# file is rules-only, per snakemake lint guidance).
# =============================================================================

def contrast_dataset(contrast):
    """Dataset that owns a given contrast (from config)."""
    return config["contrasts"][contrast]["dataset"]

# limma sheet schema per dataset: which sheet column matches the expr-matrix
# sample columns, and which carries the group label. GSE14577's expr matrix is
# per-PATIENT (U133A∪B combined) so its sample key is `patient_key` (the sheet
# has one row per chip → limma_de.R dedupes to patient level); GSE130353's expr
# columns are GSM accessions.
DE_SHEET_COLS = {
    "gse14577":  {"sample": "patient_key", "group": "group"},
    "gse130353": {"sample": "accession",   "group": "group"},
}

def de_param(wildcards, key):
    """Contrast spec field (case / control / dataset) from config."""
    return config["contrasts"][wildcards.contrast][key]

def de_sheet_col(wildcards, which):
    """Sample/group sheet column for the contrast's dataset (DE_SHEET_COLS)."""
    return DE_SHEET_COLS[contrast_dataset(wildcards.contrast)][which]

def stub(label):
    """WP0 skeleton rule body: fail loudly on a real run (no silent placeholder
    outputs); `snakemake -n` still resolves the DAG. Replaced per work package."""
    return (f"echo 'STUB {label} — not yet implemented (WP0 skeleton; see "
            f"plan:0003). Implement before running.' >&2; exit 1")

def de_expr_input(wildcards):
    """limma_de inputs: prepared expr + sample sheet for the contrast's dataset
    (both datasets gate on the clean-base QA sentinel)."""
    ds = contrast_dataset(wildcards.contrast)
    if ds == "gse130353":
        return {
            "expr": f"{PROC}/GSE130353/expr.gene.tsv.gz",
            "sheet": f"{PROC}/GSE130353/sample_sheet.tsv",
            "qa": f"{PROC}/GSE130353/clean.qa.pass",
        }
    return {
        "expr": f"{PROC}/GSE14577/expr.gene.tsv.gz",
        "sheet": f"{PROC}/GSE14577/sample_metadata.tsv",
        "qa": f"{PROC}/GSE14577/clean.qa.pass",
    }

def concordance_nes_inputs(wildcards):
    """The two contrasts' NES tables that a (pair × db) concordance compares."""
    pair = config["concordance_pairs"][wildcards.pair]
    return {
        "nes_x": f"{PROC}/fgsea/{pair['x']}.{wildcards.db}.nes.tsv",
        "nes_y": f"{PROC}/fgsea/{pair['y']}.{wildcards.db}.nes.tsv",
    }

# per-dataset prepared-matrix / sample-sheet paths (the permutation null reads
# the expr matrices + sheets directly to re-fit limma under permuted labels).
EXPR_OF = {
    "gse14577":  f"{PROC}/GSE14577/expr.gene.tsv.gz",
    "gse130353": f"{PROC}/GSE130353/expr.gene.tsv.gz",
}
EXPR_QA_OF = {
    "gse14577":  f"{PROC}/GSE14577/clean.qa.pass",
    "gse130353": f"{PROC}/GSE130353/clean.qa.pass",
}
SHEET_OF = {
    "gse14577":  f"{PROC}/GSE14577/sample_metadata.tsv",
    "gse130353": f"{PROC}/GSE130353/sample_sheet.tsv",
}

def pair_arm(pair, arm):
    """Resolve one arm ('x'|'y') of a concordance pair to its full DE spec:
    contrast name, dataset, case/control, expr+sheet paths, sheet columns."""
    cname = config["concordance_pairs"][pair][arm]
    spec = config["contrasts"][cname]
    ds = spec["dataset"]
    return {
        "contrast": cname, "dataset": ds,
        "case": spec["case"], "control": spec["control"],
        "expr": EXPR_OF[ds], "expr_qa": EXPR_QA_OF[ds], "sheet": SHEET_OF[ds],
        "sample_col": DE_SHEET_COLS[ds]["sample"],
        "group_col": DE_SHEET_COLS[ds]["group"],
    }

def cell_seed(wildcards):
    """Deterministic per-(pair×DB) substream seed: master seed offset by the
    cell's fixed index in (PAIRS × DBS) order, so every cell is independently
    reproducible regardless of execution order/worker count (plan:0003 KD10)."""
    idx = PAIRS.index(wildcards.pair) * len(DBS) + DBS.index(wildcards.db)
    return config["determinism"]["seed"] * 1000 + idx
