# =============================================================================
# enrich.smk — WP5: limma DE (per contrast) + fgsea (per contrast × DB).
# 5 contrasts → moderated-t ranked gene lists; 5 × 3 DBs → NES tables.
# MMSEQ estimate is log_mu (continuous) → limma only; DESeq2/edgeR inadmissible.
# NES tables follow the locked R↔Python schema (config.io_contract).
# Helper functions: rules/common.smk.
# =============================================================================

rule limma_de:
    input:
        unpack(de_expr_input),
    output:
        ranked=f"{PROC}/de/{{contrast}}.ranked.tsv",
    params:
        spec=lambda wc: config["contrasts"][wc.contrast],
        seed=config["determinism"]["seed"],
    log:
        f"{RES}/logs/limma_de.{{contrast}}.log"
    conda:
        "envs/r-bioc.yaml"
    shell:
        stub("enrich/limma_de (limma_de.R)")

rule fgsea_enrich:
    input:
        ranked=f"{PROC}/de/{{contrast}}.ranked.tsv",
        geneset=f"{PROC}/genesets/{{db}}.rds",
    output:
        nes=f"{PROC}/fgsea/{{contrast}}.{{db}}.nes.tsv",
    params:
        size_filter=config["genesets"]["size_filter"],
        seed=config["determinism"]["seed"],
        columns=config["io_contract"]["nes_columns"],
    log:
        f"{RES}/logs/fgsea_enrich.{{contrast}}.{{db}}.log"
    conda:
        "envs/r-bioc.yaml"
    shell:
        stub("enrich/fgsea_enrich (fgsea_enrich.R)")
