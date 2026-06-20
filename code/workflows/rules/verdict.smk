# =============================================================================
# verdict.smk — WP6/WP7/WP8: concordance + permutation null (per pair × DB),
# specificity, theme roll-up, DB-robustness, compartment, mechanical verdict.
#
# Concordance pairs × DBs = 6 cells: primary×Hallmark = confirmatory C1;
# primary×{Reactome,GOBP} = S3; s4×{...} = S4. Each cell carries its own
# ρ + p_perm. DB-robustness applies the pre-reg theme-sign-only rule (NO
# per-DB ρ-direction gate). Verdict walks the locked resolution order → 1 label.
# Helper functions: rules/common.smk.
# =============================================================================

# --- WP6: concordance ρ + paired sample-label permutation null (per pair×DB) --
rule concordance:
    input:
        concordance_nes_inputs,
    output:
        rho=f"{PROC}/concordance/{{pair}}.{{db}}.rho.tsv",
    params:
        na=config["preprocessing"]["na_nes_handling"],   # NA NES → excluded pairwise from ρ
    log:
        f"{RES}/logs/concordance.{{pair}}.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("verdict/concordance (scipy spearmanr)")

rule permutation_null:
    input:
        # the heavy rule re-runs the full limma→fgsea→NES→ρ chain under permuted
        # SAMPLE labels; needs both prepared datasets + the DB's gene sets.
        g14577=f"{PROC}/GSE14577/expr.gene.tsv.gz",
        g130353=f"{PROC}/GSE130353/expr.gene.tsv.gz",
        sheet14577=f"{PROC}/GSE14577/sample_metadata.tsv",
        sheet130353=f"{PROC}/GSE130353/sample_sheet.tsv",
        geneset=f"{PROC}/genesets/{{db}}.rds",
    output:
        perm=f"{PROC}/perm/{{pair}}.{{db}}.perm.tsv",
    params:
        B=config["permutation"]["B"],
        seed=config["determinism"]["seed"],
        rng_kind=config["determinism"]["r_rng_kind"],
        pools=config["permutation"]["label_pools"],
    threads: 8
    log:
        f"{RES}/logs/permutation_null.{{pair}}.{{db}}.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        stub("verdict/permutation_null (permutation_null.R, HEAVY, BiocParallel)")

# --- WP7: specificity → theme roll-up → DB-robustness → compartment -----------
rule specificity:
    input:
        qfs_vs_qs=f"{PROC}/fgsea/qfs_vs_qs.{{db}}.nes.tsv",
        qs_vs_hc=f"{PROC}/fgsea/qs_vs_hc.{{db}}.nes.tsv",
        qfs_vs_hc=f"{PROC}/fgsea/qfs_vs_hc.{{db}}.nes.tsv",
    output:
        classes=f"{PROC}/specificity/{{db}}.classes.tsv",
    params:
        nominal_p=config["specificity"]["nominal_p"],
    log:
        f"{RES}/logs/specificity.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("verdict/specificity (specificity.py)")

rule theme_rollup:
    input:
        classes=f"{PROC}/specificity/{{db}}.classes.tsv",
        primary_rho=f"{PROC}/concordance/primary.{{db}}.rho.tsv",
        nes_x=f"{PROC}/fgsea/pi_cfs_vs_hc.{{db}}.nes.tsv",
        nes_y=f"{PROC}/fgsea/qfs_vs_hc.{{db}}.nes.tsv",
    output:
        themes=f"{PROC}/rollup/{{db}}.themes.tsv",
    params:
        theme_map=config["theme_map"],
    log:
        f"{RES}/logs/theme_rollup.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("verdict/theme_rollup strict-dominance (theme_rollup.py)")

rule db_robustness:
    input:
        themes=expand(f"{PROC}/rollup/{{db}}.themes.tsv", db=DBS),
        primary_rho=expand(f"{PROC}/concordance/primary.{{db}}.rho.tsv", db=DBS),
        primary_perm=expand(f"{PROC}/perm/primary.{{db}}.perm.tsv", db=DBS),
    output:
        robustness=f"{PROC}/rollup/db_robustness.tsv",
    params:
        min_dbs=config["verdict"]["db_robustness_min_dbs"],
    log:
        f"{RES}/logs/db_robustness.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("verdict/db_robustness theme-sign-only >=2 DBs (theme_rollup.py)")

rule compartment:
    input:
        primary_rho=f"{PROC}/concordance/primary.{PRIMARY_DB}.rho.tsv",
        nes_x=f"{PROC}/fgsea/pi_cfs_vs_hc.{PRIMARY_DB}.nes.tsv",
        nes_y=f"{PROC}/fgsea/qfs_vs_hc.{PRIMARY_DB}.nes.tsv",
    output:
        compartment=f"{PROC}/rollup/compartment.tsv",
    params:
        marker_regex=config["compartment_marker_regex"],
        fraction=config["verdict"]["compartment_marker_fraction"],
    log:
        f"{RES}/logs/compartment.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("verdict/compartment 50%-marker on concordance-carrying set")

# --- WP8: mechanical verdict (locked resolution order → exactly one label) ----
rule verdict:
    input:
        # C1 = primary×Hallmark; the verdict resolution order runs on these.
        primary_rho=f"{PROC}/concordance/primary.{PRIMARY_DB}.rho.tsv",
        primary_perm=f"{PROC}/perm/primary.{PRIMARY_DB}.perm.tsv",
        # mandatory sensitivities — the verdict "stands only if these run"
        # (pre-reg:0002): S3 = primary×{Reactome,GOBP}, S4 = s4×{all DBs}. Wire
        # the FULL pair×DB concordance + null surface so none dangles.
        concordance=expand(f"{PROC}/concordance/{{pair}}.{{db}}.rho.tsv", pair=PAIRS, db=DBS),
        perm=expand(f"{PROC}/perm/{{pair}}.{{db}}.perm.tsv", pair=PAIRS, db=DBS),
        specificity=expand(f"{PROC}/specificity/{{db}}.classes.tsv", db=DBS),
        themes=expand(f"{PROC}/rollup/{{db}}.themes.tsv", db=DBS),
        robustness=f"{PROC}/rollup/db_robustness.tsv",
        compartment=f"{PROC}/rollup/compartment.tsv",
        datapackage=f"{PROC}/datapackage.json",
    output:
        verdict=f"{RES}/verdict.json",
        report=f"{RES}/results.md",
    params:
        resolution_order=config["verdict"]["resolution_order"],
        alpha=config["verdict"]["p_perm_alpha"],
        precision=config["determinism"]["float_precision"],
    log:
        f"{RES}/logs/verdict.log"
    conda:
        "../envs/py.yaml"
    shell:
        stub("verdict/verdict locked resolution order → 1 label (verdict.py)")
