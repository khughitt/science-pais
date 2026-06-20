# =============================================================================
# harmonize.smk — WP3 (gate G3): probe/ENSG → canonical Ensembl gene id.
# Writes mapped/unmapped fractions + Hallmark-gene coverage. QA severity locked
# to the pre-reg: build-fatal IFF the mapped Hallmark set is empty; coverage
# below hallmark_coverage_warn is distribution-severity (surfaced, not fatal).
# Retired ENSG (rel68→current) are logged, not silently dropped. (plan:0003 KD5.)
# =============================================================================

rule harmonize_gse14577:
    input:
        gpl96=f"{PROC}/GSE14577/expr_GPL96.probe_x_sample.tsv.gz",
        gpl97=f"{PROC}/GSE14577/expr_GPL97.probe_x_sample.tsv.gz",
        qa=f"{PROC}/GSE14577/raw.qa.pass",
    output:
        harmonized=f"{PROC}/GSE14577/harmonized.ensembl.tsv.gz",
        report=f"{PROC}/GSE14577/harmonize_report.json",
        sentinel=f"{PROC}/GSE14577/harmonize.qa.pass",
    params:
        coverage_warn=config["harmonization"]["hallmark_coverage_warn"],
    log:
        f"{RES}/logs/harmonize_gse14577.log"
    conda:
        "envs/r-bioc.yaml"   # hgu133a.db / hgu133b.db probe→Ensembl mapping
    shell:
        stub("harmonize/harmonize_gse14577 (harmonize_geneids.py)")

rule harmonize_gse130353:
    input:
        members=f"{PROC}/GSE130353/raw_members.ok",
        sheet=f"{PROC}/GSE130353/sample_sheet.tsv",
        qa=f"{PROC}/GSE130353/raw.qa.pass",
    output:
        harmonized=f"{PROC}/GSE130353/harmonized.ensembl.tsv.gz",
        report=f"{PROC}/GSE130353/harmonize_report.json",
        sentinel=f"{PROC}/GSE130353/harmonize.qa.pass",
    params:
        coverage_warn=config["harmonization"]["hallmark_coverage_warn"],
    log:
        f"{RES}/logs/harmonize_gse130353.log"
    conda:
        "envs/py.yaml"   # MMSEQ feature_id already ENSG (rel68) → lift to current
    shell:
        stub("harmonize/harmonize_gse130353 (harmonize_geneids.py)")
