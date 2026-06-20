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
