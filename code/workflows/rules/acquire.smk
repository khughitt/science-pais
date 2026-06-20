# =============================================================================
# acquire.smk — WP1: reproducible acquisition (download + checksum), parse,
# extract, and emit the minimal Frictionless datapackage (discharges G1).
# Seeded by code/scripts/g1_acquire.py (the one-off curl is retired here).
# =============================================================================

# --- downloads (no Snakemake input; verify against the LOCKED SHA-256) --------
rule download_gse130353_tar:
    output:
        f"{RAW}/GSE130353_RAW.tar"
    params:
        url=config["acquisition"]["gse130353"]["raw_tar"]["url"],
        sha256=config["acquisition"]["gse130353"]["raw_tar"]["sha256"],
    log:
        f"{RES}/logs/download_gse130353_tar.log"
    conda:
        "envs/py.yaml"
    shell:
        stub("acquire/download_gse130353_tar")   # curl + sha256 verify (WP1)

rule download_gse14577_soft:
    output:
        f"{RAW}/GSE14577_family.soft.gz"
    params:
        url=config["acquisition"]["gse14577"]["soft"]["url"],
        sha256=config["acquisition"]["gse14577"]["soft"]["sha256"],
    log:
        f"{RES}/logs/download_gse14577_soft.log"
    conda:
        "envs/py.yaml"
    shell:
        stub("acquire/download_gse14577_soft")

rule download_gse130353_soft:
    output:
        f"{RAW}/GSE130353_family.soft.gz"
    params:
        url=config["acquisition"]["gse130353"]["soft"]["url"],
        sha256=config["acquisition"]["gse130353"]["soft"]["sha256"],
    log:
        f"{RES}/logs/download_gse130353_soft.log"
    conda:
        "envs/py.yaml"
    shell:
        stub("acquire/download_gse130353_soft")

# --- parse / extract ----------------------------------------------------------
rule parse_gse14577:
    input:
        soft=f"{RAW}/GSE14577_family.soft.gz",
    output:
        gpl96=f"{PROC}/GSE14577/expr_GPL96.probe_x_sample.tsv.gz",
        gpl97=f"{PROC}/GSE14577/expr_GPL97.probe_x_sample.tsv.gz",
        meta=f"{PROC}/GSE14577/sample_metadata.tsv",
        contract=f"{PROC}/GSE14577/parse_contract.json",
    log:
        f"{RES}/logs/parse_gse14577.log"
    conda:
        "envs/py.yaml"
    shell:
        stub("acquire/parse_gse14577 (parse_gse14577.py)")

rule extract_gse130353:
    input:
        tar=f"{RAW}/GSE130353_RAW.tar",
        soft=f"{RAW}/GSE130353_family.soft.gz",
    output:
        sheet=f"{PROC}/GSE130353/sample_sheet.tsv",
        contract=f"{PROC}/GSE130353/parse_contract.json",
        members=f"{PROC}/GSE130353/raw_members.ok",   # sentinel for raw_members/
    log:
        f"{RES}/logs/extract_gse130353.log"
    conda:
        "envs/py.yaml"
    shell:
        stub("acquire/extract_gse130353 (extract_gse130353.py)")

# --- minimal Frictionless datapackage (discharges pre-reg:0002 G1) -----------
rule emit_datapackage:
    input:
        f"{RAW}/GSE14577_family.soft.gz",
        f"{RAW}/GSE130353_RAW.tar",
        f"{RAW}/GSE130353_family.soft.gz",
        f"{PROC}/GSE14577/parse_contract.json",
        f"{PROC}/GSE130353/parse_contract.json",
    output:
        f"{PROC}/datapackage.json",
    log:
        f"{RES}/logs/emit_datapackage.log"
    conda:
        "envs/py.yaml"
    shell:
        stub("acquire/emit_datapackage (emit_datapackage.py)")
