# science:code
# status: workflow-owned
# science:end

# =============================================================================
# enrich.smk — WP5: limma DE (per contrast) + fgsea (per contrast × DB).
# 5 contrasts → moderated-t ranked gene lists; 5 × 3 DBs → NES tables.
# MMSEQ estimate is log_mu (continuous) → limma only; DESeq2/edgeR inadmissible.
# NES tables follow the locked R↔Python schema (config.io_contract).
# Scripts are declared as rule INPUTS so a code edit triggers re-runs (lint).
# Helper functions: rules/common.smk.
# =============================================================================

rule limma_de:
    input:
        unpack(de_expr_input),
        script=f"{SCRIPTS}/limma_de.R",
    output:
        ranked=f"{PROC}/de/{{contrast}}.ranked.tsv",
        diag=f"{PROC}/de/{{contrast}}.diag.json",
    params:
        case=lambda wc: de_param(wc, "case"),
        control=lambda wc: de_param(wc, "control"),
        dataset=lambda wc: de_param(wc, "dataset"),
        sample_col=lambda wc: de_sheet_col(wc, "sample"),
        group_col=lambda wc: de_sheet_col(wc, "group"),
        seed=config["determinism"]["seed"],
    log:
        f"{RES}/logs/limma_de.{{contrast}}.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        "Rscript {input.script} --expr {input.expr} --sheet {input.sheet} "
        "--dataset {params.dataset} --contrast {wildcards.contrast} "
        "--sample-col {params.sample_col} --group-col {params.group_col} "
        "--case {params.case:q} --control {params.control:q} --seed {params.seed} "
        "--out-ranked {output.ranked} --out-diag {output.diag} > {log} 2>&1"

rule fgsea_enrich:
    input:
        ranked=f"{PROC}/de/{{contrast}}.ranked.tsv",
        geneset=f"{PROC}/genesets/{{db}}.rds",
        script=f"{SCRIPTS}/fgsea_enrich.R",
    output:
        nes=f"{PROC}/fgsea/{{contrast}}.{{db}}.nes.tsv",
    params:
        min_size=config["genesets"]["size_filter"]["min"],
        max_size=config["genesets"]["size_filter"]["max"],
        seed=config["determinism"]["seed"],
    log:
        f"{RES}/logs/fgsea_enrich.{{contrast}}.{{db}}.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        "Rscript {input.script} --ranked {input.ranked} --geneset {input.geneset} "
        "--db {wildcards.db} --contrast {wildcards.contrast} "
        "--min-size {params.min_size} --max-size {params.max_size} "
        "--seed {params.seed} --out-nes {output.nes} > {log} 2>&1"
