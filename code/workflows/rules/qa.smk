# science:code
# status: workflow-owned
# science:end

# =============================================================================
# qa.smk — WP2: two-severity QA checkpoints (t037 discipline).
# Structural failures exit non-zero → the *.qa.pass sentinel is NOT written →
# the DAG halts. Distribution issues are written to the report + warnings field
# but are NOT build-fatal. Downstream rules depend on the SENTINEL, not the
# report (qa_report.md is never a strict rule output — failed-job cleanup would
# delete the evidence). (plan:0003 KD3.) Thresholds live in config.yaml `qa.*`
# (tracked as an input so a threshold change re-runs the checkpoint).
# =============================================================================

rule qa_raw_gse14577:
    input:
        gpl96=f"{PROC}/GSE14577/expr_GPL96.probe_x_sample.tsv.gz",
        gpl97=f"{PROC}/GSE14577/expr_GPL97.probe_x_sample.tsv.gz",
        meta=f"{PROC}/GSE14577/sample_metadata.tsv",
        config=CONFIGFILE,
        script=f"{SCRIPTS}/qa_checkpoint.py",
    output:
        sentinel=f"{PROC}/GSE14577/raw.qa.pass",
    params:
        # report is NOT a strict output — failed-job cleanup would delete the
        # very evidence of failure (plan:0003 KD3). The script writes it; only
        # the sentinel gates the DAG.
        report=f"{RES}/qa/GSE14577_raw.qa_report.md",
    log:
        f"{RES}/logs/qa_raw_gse14577.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --dataset gse14577 --config {input.config} "
        "--gpl96 {input.gpl96} --gpl97 {input.gpl97} --meta {input.meta} "
        "--report {params.report} --sentinel {output.sentinel} > {log} 2>&1"

rule qa_raw_gse130353:
    input:
        sheet=f"{PROC}/GSE130353/sample_sheet.tsv",
        members=f"{PROC}/GSE130353/raw_members.ok",
        contract=f"{PROC}/GSE130353/parse_contract.json",
        config=CONFIGFILE,
        script=f"{SCRIPTS}/qa_checkpoint.py",
    output:
        sentinel=f"{PROC}/GSE130353/raw.qa.pass",
    params:
        # report is NOT a strict output (see qa_raw_gse14577).
        report=f"{RES}/qa/GSE130353_raw.qa_report.md",
    log:
        f"{RES}/logs/qa_raw_gse130353.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --dataset gse130353 --config {input.config} "
        "--sheet {input.sheet} --contract {input.contract} "
        "--report {params.report} --sentinel {output.sentinel} > {log} 2>&1"


rule qa_clean_gse14577:
    input:
        expr=f"{PROC}/GSE14577/expr.gene.tsv.gz",
        audit=f"{PROC}/GSE14577/cohort_audit.json",
        config=CONFIGFILE,
        script=f"{SCRIPTS}/qa_checkpoint.py",
    output:
        sentinel=f"{PROC}/GSE14577/clean.qa.pass",
    params:
        report=f"{RES}/qa/GSE14577_clean.qa_report.md",
        expected_samples=config["qa"]["clean_matrix"]["datasets"]["gse14577"]["expected_samples"],
    log:
        f"{RES}/logs/qa_clean_gse14577.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --mode clean-matrix --dataset gse14577 --config {input.config} "
        "--expr {input.expr} --audit {input.audit} --expected-samples {params.expected_samples} "
        "--report {params.report} --sentinel {output.sentinel} > {log} 2>&1"


rule qa_clean_gse130353:
    input:
        expr=f"{PROC}/GSE130353/expr.gene.tsv.gz",
        audit=f"{PROC}/GSE130353/cohort_audit.json",
        nearzero=f"{PROC}/GSE130353/nearzero.qa.pass",
        config=CONFIGFILE,
        script=f"{SCRIPTS}/qa_checkpoint.py",
    output:
        sentinel=f"{PROC}/GSE130353/clean.qa.pass",
    params:
        report=f"{RES}/qa/GSE130353_clean.qa_report.md",
        expected_samples=config["qa"]["clean_matrix"]["datasets"]["gse130353"]["expected_samples"],
    log:
        f"{RES}/logs/qa_clean_gse130353.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --mode clean-matrix --dataset gse130353 --config {input.config} "
        "--expr {input.expr} --audit {input.audit} --expected-samples {params.expected_samples} "
        "--report {params.report} --sentinel {output.sentinel} > {log} 2>&1"


rule qa_clean_genesets:
    input:
        rds=expand(f"{PROC}/genesets/{{db}}.rds", db=DBS),
        theme_map=f"{PROC}/genesets/theme_map.tsv",
        release_hash=f"{PROC}/genesets/msigdb_release_hash.txt",
        script=f"{SCRIPTS}/qa_genesets.R",
    output:
        sentinel=f"{PROC}/genesets/clean.qa.pass",
    params:
        report=f"{RES}/qa/genesets_clean.qa_report.md",
        dbs=",".join(DBS),
        rds=lambda wc, input: ",".join(input.rds),
        release=config["genesets"]["msigdb_release"],
        sha256s=",".join(config["genesets"]["gmt_sources"][db]["sha256"] for db in DBS),
        min_size=config["genesets"]["size_filter"]["min"],
        max_size=config["genesets"]["size_filter"]["max"],
    log:
        f"{RES}/logs/qa_clean_genesets.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        "Rscript {input.script} --dbs {params.dbs} --rds {params.rds} "
        "--theme-map {input.theme_map} --release-hash {input.release_hash} "
        "--expected-release {params.release} --expected-sha256s {params.sha256s} "
        "--min-size {params.min_size} --max-size {params.max_size} "
        "--report {params.report} --sentinel {output.sentinel} > {log} 2>&1"


rule qa_results:
    input:
        ranked=expand(f"{PROC}/de/{{contrast}}.ranked.tsv", contrast=CONTRASTS),
        diag=expand(f"{PROC}/de/{{contrast}}.diag.json", contrast=CONTRASTS),
        nes=expand(f"{PROC}/fgsea/{{contrast}}.{{db}}.nes.tsv", contrast=CONTRASTS, db=DBS),
        rho=expand(f"{PROC}/concordance/{{pair}}.{{db}}.rho.tsv", pair=PAIRS, db=DBS),
        scatter=expand(f"{PROC}/concordance/{{pair}}.{{db}}.scatter.tsv", pair=PAIRS, db=DBS),
        perm=expand(f"{PROC}/perm/{{pair}}.{{db}}.perm.tsv", pair=PAIRS, db=DBS),
        nulldist=expand(f"{PROC}/perm/{{pair}}.{{db}}.nulldist.tsv", pair=PAIRS, db=DBS),
        specificity=expand(f"{PROC}/specificity/{{db}}.classes.tsv", db=DBS),
        themes=expand(f"{PROC}/rollup/{{db}}.themes.tsv", db=DBS),
        robustness=f"{PROC}/rollup/db_robustness.tsv",
        compartment=f"{PROC}/rollup/compartment.tsv",
        verdict=f"{RES}/verdict.json",
        report=f"{RES}/results.md",
        metadata=f"{RES}/run_metadata.json",
        config=CONFIGFILE,
        script=f"{SCRIPTS}/qa_results.py",
    output:
        sentinel=f"{RES}/qa/t035_results.qa.pass",
    params:
        report=f"{RES}/qa/t035_results.qa_report.md",
        processed=PROC,
        results=RES,
    log:
        f"{RES}/logs/qa_results.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --processed {params.processed} --results {params.results} "
        "--config {input.config} --report {params.report} "
        "--sentinel {output.sentinel} > {log} 2>&1"


rule qa_all:
    input:
        f"{PROC}/GSE14577/raw.qa.pass",
        f"{PROC}/GSE130353/raw.qa.pass",
        f"{PROC}/GSE14577/clean.qa.pass",
        f"{PROC}/GSE130353/clean.qa.pass",
        f"{PROC}/genesets/clean.qa.pass",
        f"{RES}/qa/t035_results.qa.pass",
