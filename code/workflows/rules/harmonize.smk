# science:code
# status: workflow-owned
# task_ids: [t035]
# science:end

# =============================================================================
# harmonize.smk — WP3 (gate G3): probe/ENSG → canonical Ensembl gene id.
# Writes mapped/unmapped fractions + Hallmark-gene coverage. QA severity locked
# to the pre-reg: build-fatal IFF the harmonized universe OR the mapped-Hallmark
# intersection is empty; coverage below hallmark_coverage_warn is distribution-
# severity (surfaced, not fatal). Retired ENSG (rel68→current) are logged, not
# silently dropped. (plan:0003 KD5.) harmonize_report.json is a params path (NOT
# a strict output) so a build-fatal failure keeps the evidence (KD3); the
# *.qa.pass sentinel is the gating output.
# =============================================================================

# --- G3 coverage reference (shared) ------------------------------------------
# One r-bioc step maps the pinned Hallmark GMT (symbols) → Ensembl and emits the
# current Ensembl universe (org.Hs.eg.db) used by BOTH harmonize rules for the
# coverage gate + the rel68→current lift. (plan:0003 KD7.)
rule harmonize_reference:
    input:
        gmt=f"{RAW}/genesets/hallmark.{config['genesets']['msigdb_release']}.symbols.gmt",
        verify=f"{PROC}/verify/hallmark_gmt.sha256.pass",   # hash-gated (finding 2)
        script=f"{SCRIPTS}/genesets_reference.R",
    output:
        f"{PROC}/genesets/harmonize_reference.json",
    params:
        release=config["genesets"]["msigdb_release"],
        gmt_sha256=config["genesets"]["gmt_sources"]["hallmark"]["sha256"],
        multimap=config["harmonization"]["multimap_policy"],
    log:
        f"{RES}/logs/harmonize_reference.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        "Rscript {input.script} --gmt {input.gmt} --release {params.release} "
        "--gmt_sha256 {params.gmt_sha256} --multimap {params.multimap} --out {output} > {log} 2>&1"

rule harmonize_gse14577:
    input:
        gpl96=f"{PROC}/GSE14577/expr_GPL96.probe_x_sample.tsv.gz",
        gpl97=f"{PROC}/GSE14577/expr_GPL97.probe_x_sample.tsv.gz",
        meta=f"{PROC}/GSE14577/sample_metadata.tsv",
        reference=f"{PROC}/genesets/harmonize_reference.json",
        qa=f"{PROC}/GSE14577/raw.qa.pass",
        script=f"{SCRIPTS}/harmonize_gse14577.R",
    output:
        harmonized=f"{PROC}/GSE14577/harmonized.ensembl.tsv.gz",
        sentinel=f"{PROC}/GSE14577/harmonize.qa.pass",
    params:
        # report is NOT a strict output (KD3) — survives a build-fatal failure.
        report=f"{PROC}/GSE14577/harmonize_report.json",
        coverage_warn=config["harmonization"]["hallmark_coverage_warn"],
        multimap=config["harmonization"]["multimap_policy"],
    log:
        f"{RES}/logs/harmonize_gse14577.log"
    conda:
        "../envs/r-bioc.yaml"   # hgu133a.db / hgu133b.db probe→Ensembl mapping
    shell:
        "Rscript {input.script} --gpl96 {input.gpl96} --gpl97 {input.gpl97} "
        "--meta {input.meta} --reference {input.reference} "
        "--out-harmonized {output.harmonized} --out-report {params.report} "
        "--sentinel {output.sentinel} --coverage-warn {params.coverage_warn} "
        "--multimap {params.multimap} > {log} 2>&1"

rule harmonize_gse130353:
    input:
        members=f"{PROC}/GSE130353/raw_members.ok",
        sheet=f"{PROC}/GSE130353/sample_sheet.tsv",
        reference=f"{PROC}/genesets/harmonize_reference.json",
        qa=f"{PROC}/GSE130353/raw.qa.pass",
        script=f"{SCRIPTS}/harmonize_gse130353.py",
    output:
        harmonized=f"{PROC}/GSE130353/harmonized.ensembl.tsv.gz",
        sentinel=f"{PROC}/GSE130353/harmonize.qa.pass",
    params:
        report=f"{PROC}/GSE130353/harmonize_report.json",
        # raw_members.ok sentinel -> the raw_members/ dir it guards (strip .ok)
        members_dir=lambda wc, input: os.path.splitext(input.members)[0],
        coverage_warn=config["harmonization"]["hallmark_coverage_warn"],
    log:
        f"{RES}/logs/harmonize_gse130353.log"
    conda:
        "../envs/py.yaml"   # MMSEQ feature_id already ENSG (rel68) → lift to current
    shell:
        "python {input.script} --members-dir {params.members_dir} --sheet {input.sheet} "
        "--reference {input.reference} --out-harmonized {output.harmonized} "
        "--out-report {params.report} --sentinel {output.sentinel} "
        "--coverage-warn {params.coverage_warn} > {log} 2>&1"
