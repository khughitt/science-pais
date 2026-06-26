# science:code
# status: workflow-owned
# task_ids: [t035]
# science:end

# =============================================================================
# acquire.smk — WP1: reproducible acquisition (download + checksum), parse,
# extract, and emit the minimal Frictionless datapackage (discharges G1).
# Seeded by code/scripts/g1_acquire.py (the one-off curl is retired here).
#
# Scripts are declared as rule INPUTS (not bare {SCRIPTS} interpolation) so a
# code edit correctly triggers re-runs and provenance tracking is accurate
# (snakemake --lint). acquire_common.py is tracked even where not named in the
# shell, because every script imports it.
# =============================================================================

# --- downloads (no data input; verify against the LOCKED SHA-256) ------------
rule download_gse130353_tar:
    input:
        # ancient(): the payload is content-addressed by a LOCKED sha256, so a
        # fetch_url.py edit can never change the verified bytes — don't let code
        # churn trigger a 95 MB re-download (dependency still recorded for DAG).
        script=ancient(f"{SCRIPTS}/fetch_url.py"),
        srclib=ancient(f"{SCRIPTS}/acquire_common.py"),
    output:
        f"{RAW}/GSE130353_RAW.tar"
    params:
        url=config["acquisition"]["gse130353"]["raw_tar"]["url"],
        sha256=config["acquisition"]["gse130353"]["raw_tar"]["sha256"],
    log:
        f"{RES}/logs/download_gse130353_tar.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --url {params.url} --sha256 {params.sha256} "
        "--out {output} > {log} 2>&1"

rule download_gse14577_soft:
    input:
        script=ancient(f"{SCRIPTS}/fetch_url.py"),
        srclib=ancient(f"{SCRIPTS}/acquire_common.py"),
    output:
        f"{RAW}/GSE14577_family.soft.gz"
    params:
        url=config["acquisition"]["gse14577"]["soft"]["url"],
        sha256=config["acquisition"]["gse14577"]["soft"]["sha256"],
    log:
        f"{RES}/logs/download_gse14577_soft.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --url {params.url} --sha256 {params.sha256} "
        "--out {output} > {log} 2>&1"

rule download_gse130353_soft:
    input:
        script=ancient(f"{SCRIPTS}/fetch_url.py"),
        srclib=ancient(f"{SCRIPTS}/acquire_common.py"),
    output:
        f"{RAW}/GSE130353_family.soft.gz"
    params:
        url=config["acquisition"]["gse130353"]["soft"]["url"],
        sha256=config["acquisition"]["gse130353"]["soft"]["sha256"],
    log:
        f"{RES}/logs/download_gse130353_soft.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --url {params.url} --sha256 {params.sha256} "
        "--out {output} > {log} 2>&1"

# --- parse / extract ----------------------------------------------------------
rule parse_gse14577:
    input:
        soft=f"{RAW}/GSE14577_family.soft.gz",
        verify=f"{PROC}/verify/gse14577_soft.sha256.pass",   # hash-gated (finding 2)
        script=f"{SCRIPTS}/parse_gse14577.py",
        srclib=f"{SCRIPTS}/acquire_common.py",
    output:
        gpl96=f"{PROC}/GSE14577/expr_GPL96.probe_x_sample.tsv.gz",
        gpl97=f"{PROC}/GSE14577/expr_GPL97.probe_x_sample.tsv.gz",
        meta=f"{PROC}/GSE14577/sample_metadata.tsv",
        contract=f"{PROC}/GSE14577/parse_contract.json",
    params:
        out_dir=lambda wc, output: os.path.dirname(output.contract),
    log:
        f"{RES}/logs/parse_gse14577.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --soft {input.soft} "
        "--out-dir {params.out_dir} > {log} 2>&1"

rule extract_gse130353:
    input:
        tar=f"{RAW}/GSE130353_RAW.tar",
        soft=f"{RAW}/GSE130353_family.soft.gz",
        verify_tar=f"{PROC}/verify/gse130353_tar.sha256.pass",    # hash-gated (finding 2)
        verify_soft=f"{PROC}/verify/gse130353_soft.sha256.pass",
        script=f"{SCRIPTS}/extract_gse130353.py",
        srclib=f"{SCRIPTS}/acquire_common.py",
    output:
        sheet=f"{PROC}/GSE130353/sample_sheet.tsv",
        contract=f"{PROC}/GSE130353/parse_contract.json",
        members=f"{PROC}/GSE130353/raw_members.ok",   # sentinel for raw_members/
    params:
        out_dir=lambda wc, output: os.path.dirname(output.contract),
    log:
        f"{RES}/logs/extract_gse130353.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --tar {input.tar} --soft {input.soft} "
        "--out-dir {params.out_dir} > {log} 2>&1"

# --- minimal Frictionless datapackage (discharges pre-reg:0002 G1) -----------
rule emit_datapackage:
    input:
        # the three acquired payloads (recorded as resources) + both parse
        # contracts (gate the datapackage behind a successful parse/extract).
        soft14577=f"{RAW}/GSE14577_family.soft.gz",
        tar=f"{RAW}/GSE130353_RAW.tar",
        soft130353=f"{RAW}/GSE130353_family.soft.gz",
        contract14577=f"{PROC}/GSE14577/parse_contract.json",
        contract130353=f"{PROC}/GSE130353/parse_contract.json",
        verify14577=f"{PROC}/verify/gse14577_soft.sha256.pass",   # hash-gated (finding 2)
        verify_tar=f"{PROC}/verify/gse130353_tar.sha256.pass",
        verify_soft=f"{PROC}/verify/gse130353_soft.sha256.pass",
        script=f"{SCRIPTS}/emit_datapackage.py",
        srclib=f"{SCRIPTS}/acquire_common.py",
    output:
        f"{PROC}/datapackage.json",
    log:
        f"{RES}/logs/emit_datapackage.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} "
        "--payload {input.soft14577} {input.tar} {input.soft130353} "
        "--out {output} > {log} 2>&1"
