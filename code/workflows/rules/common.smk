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
    (GSE130353 also gates on the near-zero bimodality sentinel)."""
    ds = contrast_dataset(wildcards.contrast)
    if ds == "gse130353":
        return {
            "expr": f"{PROC}/GSE130353/expr.gene.tsv.gz",
            "sheet": f"{PROC}/GSE130353/sample_sheet.tsv",
            "qa": f"{PROC}/GSE130353/nearzero.qa.pass",
        }
    return {
        "expr": f"{PROC}/GSE14577/expr.gene.tsv.gz",
        "sheet": f"{PROC}/GSE14577/sample_metadata.tsv",
    }

def concordance_nes_inputs(wildcards):
    """The two contrasts' NES tables that a (pair × db) concordance compares."""
    pair = config["concordance_pairs"][wildcards.pair]
    return [
        f"{PROC}/fgsea/{pair['x']}.{wildcards.db}.nes.tsv",
        f"{PROC}/fgsea/{pair['y']}.{wildcards.db}.nes.tsv",
    ]
