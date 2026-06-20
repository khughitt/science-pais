# =============================================================================
# prepare.smk — WP4: probe→gene collapse, near-zero filter, gene-set prep.
# Verdict-affecting preprocessing is pre-reg-locked (3rd amendment): the
# near-zero log_mu filter is a contrast-blind KDE-antimode PROCEDURE with a
# build-fatal halt-if-not-bimodal guard (no silent fixed-τ fallback);
# U133A∪B genes combine by mean-of-platform-collapsed-log2. (plan:0003 KD9.)
# =============================================================================

rule prepare_gse14577:
    input:
        harmonized=f"{PROC}/GSE14577/harmonized.ensembl.tsv.gz",
        qa=f"{PROC}/GSE14577/harmonize.qa.pass",
    output:
        expr=f"{PROC}/GSE14577/expr.gene.tsv.gz",
        audit=f"{PROC}/GSE14577/cohort_audit.json",
    params:
        collapse=config["preprocessing"]["probe_collapse"],
        dual_chip=config["preprocessing"]["u133_dual_chip_combine"],
    log:
        f"{RES}/logs/prepare_gse14577.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        stub("prepare/prepare_gse14577 (collapse_probes.R)")

rule prepare_gse130353:
    input:
        harmonized=f"{PROC}/GSE130353/harmonized.ensembl.tsv.gz",
        sheet=f"{PROC}/GSE130353/sample_sheet.tsv",
        qa=f"{PROC}/GSE130353/harmonize.qa.pass",
    output:
        expr=f"{PROC}/GSE130353/expr.gene.tsv.gz",
        audit=f"{PROC}/GSE130353/cohort_audit.json",
        sentinel=f"{PROC}/GSE130353/nearzero.qa.pass",   # bimodality gate (build-fatal)
    params:
        nz=config["preprocessing"]["near_zero_filter"],
    log:
        f"{RES}/logs/prepare_gse130353.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("prepare/prepare_gse130353 near-zero KDE-antimode filter")

# KD7 — 2024.1.Hs collections are PINNED, HASHED GMT downloads (decoupled from
# the conda r-msigdbr version). download_genesets verifies each GMT against its
# config sha256; an empty/mismatched hash HALTS (fail-early). prepare_genesets
# then maps symbols→Ensembl, applies the size filter, and asserts the release.
rule download_genesets:
    output:
        gmt=f"{RAW}/genesets/{{db}}.{config['genesets']['msigdb_release']}.symbols.gmt",
    params:
        url=lambda wc: config["genesets"]["gmt_sources"][wc.db]["url"],
        sha256=lambda wc: config["genesets"]["gmt_sources"][wc.db]["sha256"],
    log:
        f"{RES}/logs/download_genesets.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("prepare/download_genesets (curl + sha256 verify; HALT on empty/mismatch)")

rule prepare_genesets:
    input:
        gmt=expand(
            f"{RAW}/genesets/{{db}}.{config['genesets']['msigdb_release']}.symbols.gmt",
            db=DBS,
        ),
    output:
        rds=expand(f"{PROC}/genesets/{{db}}.rds", db=DBS),
        theme_map=f"{PROC}/genesets/theme_map.tsv",
        release_hash=f"{PROC}/genesets/msigdb_release_hash.txt",
    params:
        release=config["genesets"]["msigdb_release"],
        size_filter=config["genesets"]["size_filter"],
        id_space=config["genesets"]["gmt_id_space"],
    log:
        f"{RES}/logs/prepare_genesets.log"
    conda:
        "../envs/r-bioc.yaml"   # symbols→Ensembl map + size filter; universe must not drift
    shell:
        stub("prepare/prepare_genesets (prepare_genesets.R)")
