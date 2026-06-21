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
# Observed ρ + scatter from the WP5 (multilevel) NES; the locked NA-NES rule
# (excluded pairwise) is intrinsic to concordance.py. Scripts are rule INPUTS.
rule concordance:
    input:
        unpack(concordance_nes_inputs),
        script=f"{SCRIPTS}/concordance.py",
        lib=f"{SCRIPTS}/_verdict_lib.py",   # require_same_universe guard
    output:
        rho=f"{PROC}/concordance/{{pair}}.{{db}}.rho.tsv",
        scatter=f"{PROC}/concordance/{{pair}}.{{db}}.scatter.tsv",
    log:
        f"{RES}/logs/concordance.{{pair}}.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --nes-x {input.nes_x} --nes-y {input.nes_y} "
        "--pair {wildcards.pair} --db {wildcards.db} "
        "--out-rho {output.rho} --out-scatter {output.scatter} > {log} 2>&1"

rule permutation_null:
    input:
        # the heavy rule re-runs the full limma→fgsea→NES→ρ chain under permuted
        # SAMPLE labels; needs both arms' prepared matrices + the DB's gene sets.
        x_expr=lambda wc: pair_arm(wc.pair, "x")["expr"],
        x_sheet=lambda wc: pair_arm(wc.pair, "x")["sheet"],
        y_expr=lambda wc: pair_arm(wc.pair, "y")["expr"],
        y_sheet=lambda wc: pair_arm(wc.pair, "y")["sheet"],
        geneset=f"{PROC}/genesets/{{db}}.rds",
        script=f"{SCRIPTS}/permutation_null.R",
        # permutation_null.R re-implements the WP5 limma→fgsea→NES ranking under
        # permuted labels; wire the WP5 scripts as inputs so any change to the
        # ranking/NA/size-filter policy there INVALIDATES the heavy null (it must
        # not silently diverge from the observed NES). (review WP6-7, Medium.)
        limma_ref=f"{SCRIPTS}/limma_de.R",
        fgsea_ref=f"{SCRIPTS}/fgsea_enrich.R",
    output:
        perm=f"{PROC}/perm/{{pair}}.{{db}}.perm.tsv",          # io_contract perm_columns
        nulldist=f"{PROC}/perm/{{pair}}.{{db}}.nulldist.tsv",  # B permuted ρ (histogram)
    params:
        B=config["permutation"]["B"],
        nperm=config["permutation"]["null_nes"]["nperm"],
        seed=lambda wc: cell_seed(wc),                # per-(pair×DB) substream seed
        rng_kind=config["determinism"]["r_rng_kind"],
        min_size=config["genesets"]["size_filter"]["min"],
        max_size=config["genesets"]["size_filter"]["max"],
        x_case=lambda wc: pair_arm(wc.pair, "x")["case"],
        x_control=lambda wc: pair_arm(wc.pair, "x")["control"],
        x_sample_col=lambda wc: pair_arm(wc.pair, "x")["sample_col"],
        x_group_col=lambda wc: pair_arm(wc.pair, "x")["group_col"],
        y_case=lambda wc: pair_arm(wc.pair, "y")["case"],
        y_control=lambda wc: pair_arm(wc.pair, "y")["control"],
        y_sample_col=lambda wc: pair_arm(wc.pair, "y")["sample_col"],
        y_group_col=lambda wc: pair_arm(wc.pair, "y")["group_col"],
    threads: 8
    log:
        f"{RES}/logs/permutation_null.{{pair}}.{{db}}.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        "Rscript {input.script} --pair {wildcards.pair} --db {wildcards.db} "
        "--x-expr {input.x_expr} --x-sheet {input.x_sheet} "
        "--x-case {params.x_case:q} --x-control {params.x_control:q} "
        "--x-sample-col {params.x_sample_col} --x-group-col {params.x_group_col} "
        "--y-expr {input.y_expr} --y-sheet {input.y_sheet} "
        "--y-case {params.y_case:q} --y-control {params.y_control:q} "
        "--y-sample-col {params.y_sample_col} --y-group-col {params.y_group_col} "
        "--geneset {input.geneset} --B {params.B} --nperm {params.nperm} "
        "--min-size {params.min_size} --max-size {params.max_size} "
        "--seed {params.seed} --rng-kind {params.rng_kind:q} --threads {threads} "
        "--out-perm {output.perm} --out-nulldist {output.nulldist} > {log} 2>&1"

# --- WP7: specificity → theme roll-up → DB-robustness → compartment -----------
# nominal_p is the SINGLE locked fgsea-p floor (config specificity.nominal_p): it
# gates the S1/S2 presence predicates AND the concordance-carrying p<0.05 rule, so
# both legs share one knob. The locked concordance-carrying definition lives ONCE in
# _verdict_lib.py (wired as an input so its edits retrigger theme_rollup/compartment).
rule specificity:
    input:
        qfs_vs_qs=f"{PROC}/fgsea/qfs_vs_qs.{{db}}.nes.tsv",
        qs_vs_hc=f"{PROC}/fgsea/qs_vs_hc.{{db}}.nes.tsv",
        qfs_vs_hc=f"{PROC}/fgsea/qfs_vs_hc.{{db}}.nes.tsv",
        script=f"{SCRIPTS}/specificity.py",
        lib=f"{SCRIPTS}/_verdict_lib.py",
    output:
        classes=f"{PROC}/specificity/{{db}}.classes.tsv",
    params:
        nominal_p=config["specificity"]["nominal_p"],
    log:
        f"{RES}/logs/specificity.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --qfs-vs-hc {input.qfs_vs_hc} "
        "--qfs-vs-qs {input.qfs_vs_qs} --qs-vs-hc {input.qs_vs_hc} "
        "--db {wildcards.db} --nominal-p {params.nominal_p} "
        "--out {output.classes} > {log} 2>&1"

rule theme_rollup:
    input:
        classes=f"{PROC}/specificity/{{db}}.classes.tsv",
        nes_x=f"{PROC}/fgsea/pi_cfs_vs_hc.{{db}}.nes.tsv",
        nes_y=f"{PROC}/fgsea/qfs_vs_hc.{{db}}.nes.tsv",
        theme_map=f"{PROC}/genesets/theme_map.tsv",   # locked per-set theme assignment
        script=f"{SCRIPTS}/theme_rollup.py",
        lib=f"{SCRIPTS}/_verdict_lib.py",
    output:
        themes=f"{PROC}/rollup/{{db}}.themes.tsv",
    params:
        nominal_p=config["specificity"]["nominal_p"],
    log:
        f"{RES}/logs/theme_rollup.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --classes {input.classes} "
        "--nes-x {input.nes_x} --nes-y {input.nes_y} "
        "--theme-map {input.theme_map} --db {wildcards.db} "
        "--nominal-p {params.nominal_p} --out {output.themes} > {log} 2>&1"

# theme-sign-only recurrence — NO per-DB ρ-direction gate (pre-reg:0002 lock), so
# the concordance/perm tables are deliberately NOT inputs here.
rule db_robustness:
    input:
        themes=expand(f"{PROC}/rollup/{{db}}.themes.tsv", db=DBS),
        script=f"{SCRIPTS}/db_robustness.py",
    output:
        robustness=f"{PROC}/rollup/db_robustness.tsv",
    params:
        min_dbs=config["verdict"]["db_robustness_min_dbs"],
    log:
        f"{RES}/logs/db_robustness.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --themes {input.themes} "
        "--min-dbs {params.min_dbs} --out {output.robustness} > {log} 2>&1"

rule compartment:
    input:
        nes_x=f"{PROC}/fgsea/pi_cfs_vs_hc.{PRIMARY_DB}.nes.tsv",
        nes_y=f"{PROC}/fgsea/qfs_vs_hc.{PRIMARY_DB}.nes.tsv",
        script=f"{SCRIPTS}/compartment.py",
        lib=f"{SCRIPTS}/_verdict_lib.py",
    output:
        compartment=f"{PROC}/rollup/compartment.tsv",
    params:
        marker_regex=config["compartment_marker_regex"],
        fraction=config["verdict"]["compartment_marker_fraction"],
        nominal_p=config["specificity"]["nominal_p"],
        db=PRIMARY_DB,
    log:
        f"{RES}/logs/compartment.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --nes-x {input.nes_x} --nes-y {input.nes_y} "
        "--db {params.db} --marker-regex {params.marker_regex:q} "
        "--fraction {params.fraction} --nominal-p {params.nominal_p} "
        "--out {output.compartment} > {log} 2>&1"

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
