# =============================================================================
# common.smk — shared helper functions (kept out of rule files so each rule
# file is rules-only, per snakemake lint guidance).
# =============================================================================

def contrast_dataset(contrast):
    """Dataset that owns a given contrast (from config)."""
    return config["contrasts"][contrast]["dataset"]

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
