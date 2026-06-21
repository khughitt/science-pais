# =============================================================================
# prepare.smk — WP4: probe→gene collapse, near-zero filter, gene-set prep.
# Verdict-affecting preprocessing is pre-reg-locked (3rd amendment): the
# near-zero log_mu filter is a contrast-blind KDE-antimode PROCEDURE with a
# build-fatal halt-if-not-bimodal guard (no silent fixed-τ fallback);
# U133A∪B genes combine by mean-of-platform-collapsed-log2. (plan:0003 KD9.)
# Scripts are declared as rule INPUTS so a code edit triggers re-runs (lint).
# =============================================================================

rule prepare_gse14577:
    input:
        harmonized=f"{PROC}/GSE14577/harmonized.ensembl.tsv.gz",
        qa=f"{PROC}/GSE14577/harmonize.qa.pass",
        script=f"{SCRIPTS}/collapse_probes.R",
    output:
        expr=f"{PROC}/GSE14577/expr.gene.tsv.gz",
        audit=f"{PROC}/GSE14577/cohort_audit.json",
    params:
        collapse=config["preprocessing"]["probe_collapse"],
        dual_chip=config["preprocessing"]["u133_dual_chip_combine"],
    log:
        f"{RES}/logs/prepare_gse14577.log"
    conda:
        "../envs/r-bioc.yaml"
    shell:
        "Rscript {input.script} --harmonized {input.harmonized} "
        "--out-expr {output.expr} --out-audit {output.audit} "
        "--collapse {params.collapse} --dual-chip {params.dual_chip} > {log} 2>&1"

rule prepare_gse130353:
    input:
        harmonized=f"{PROC}/GSE130353/harmonized.ensembl.tsv.gz",
        sheet=f"{PROC}/GSE130353/sample_sheet.tsv",
        qa=f"{PROC}/GSE130353/harmonize.qa.pass",
        script=f"{SCRIPTS}/near_zero_filter.py",
    output:
        expr=f"{PROC}/GSE130353/expr.gene.tsv.gz",
        audit=f"{PROC}/GSE130353/cohort_audit.json",
        sentinel=f"{PROC}/GSE130353/nearzero.qa.pass",   # bimodality gate (build-fatal)
    params:
        method=config["preprocessing"]["near_zero_filter"]["method"],
        bandwidth=config["preprocessing"]["near_zero_filter"]["kde_bandwidth"],
        min_donors=config["preprocessing"]["near_zero_filter"]["min_donors"],
        require_interior=config["preprocessing"]["near_zero_filter"]["bimodality"]["require_interior_antimode"],
        min_sep=config["preprocessing"]["near_zero_filter"]["bimodality"]["min_mode_separation"],
        min_mass=config["preprocessing"]["near_zero_filter"]["bimodality"]["min_antimode_mass_fraction"],
    log:
        f"{RES}/logs/prepare_gse130353.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --harmonized {input.harmonized} "
        "--out-expr {output.expr} --out-audit {output.audit} --sentinel {output.sentinel} "
        "--min-donors {params.min_donors} --method {params.method} "
        "--kde-bandwidth {params.bandwidth} --require-interior-antimode {params.require_interior} "
        "--min-mode-separation {params.min_sep} "
        "--min-antimode-mass-fraction {params.min_mass} > {log} 2>&1"

# KD7 — 2024.1.Hs collections are PINNED, HASHED GMT downloads (decoupled from
# the conda r-msigdbr version). download_genesets verifies each GMT against its
# config sha256; an empty/mismatched hash HALTS (fail-early). prepare_genesets
# then maps symbols→Ensembl, applies the size filter, and asserts the release.
rule download_genesets:
    input:
        # ancient(): GMT is content-addressed by a LOCKED sha256 — a fetch_url.py
        # edit can't change the verified bytes (see acquire.smk downloads).
        script=ancient(f"{SCRIPTS}/fetch_url.py"),
        srclib=ancient(f"{SCRIPTS}/acquire_common.py"),
    output:
        gmt=f"{RAW}/genesets/{{db}}.{config['genesets']['msigdb_release']}.symbols.gmt",
    params:
        url=lambda wc: config["genesets"]["gmt_sources"][wc.db]["url"],
        sha256=lambda wc: config["genesets"]["gmt_sources"][wc.db]["sha256"],
    log:
        f"{RES}/logs/download_genesets.{{db}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        # empty sha256 (reactome/gobp TBD-at-ingest) -> fetch_url.py HALTs.
        "python {input.script} --url {params.url} --sha256 {params.sha256} "
        "--out {output.gmt} > {log} 2>&1"

# Serialize the LOCKED theme map (PCRE) from config → JSON so prepare_genesets.R
# applies it verbatim (the r-bioc env has no r-yaml). config is the source — and
# NOT ancient(): theme_spec.json carries the verdict-relevant theme/compartment
# regexes, so a config amendment to either MUST rerun this (and theme_map.tsv
# downstream), never silently leave them stale (review WP4-5, Medium).
rule emit_theme_spec:
    input:
        config=CONFIGFILE,
        script=f"{SCRIPTS}/emit_theme_spec.py",
    output:
        f"{PROC}/genesets/theme_spec.json",
    log:
        f"{RES}/logs/emit_theme_spec.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --config {input.config} --out {output} > {log} 2>&1"

rule prepare_genesets:
    input:
        gmt=expand(
            f"{RAW}/genesets/{{db}}.{config['genesets']['msigdb_release']}.symbols.gmt",
            db=DBS,
        ),
        verify=expand(f"{PROC}/verify/{{db}}_gmt.sha256.pass", db=DBS),  # hash-gated (finding 2)
        theme_spec=f"{PROC}/genesets/theme_spec.json",
        script=f"{SCRIPTS}/prepare_genesets.R",
    output:
        rds=expand(f"{PROC}/genesets/{{db}}.rds", db=DBS),
        theme_map=f"{PROC}/genesets/theme_map.tsv",
        release_hash=f"{PROC}/genesets/msigdb_release_hash.txt",
    params:
        # comma-joined parallel lists (DBS-ordered) — avoids shell-quoting regexes
        # and the pairwise arg parser's single-value limit.
        gmts=lambda wc, input: ",".join(input.gmt),
        dbs=",".join(DBS),
        sha256s=",".join(config["genesets"]["gmt_sources"][db]["sha256"] for db in DBS),
        out_rds=lambda wc, output: ",".join(output.rds),
        release=config["genesets"]["msigdb_release"],
        min_size=config["genesets"]["size_filter"]["min"],
        max_size=config["genesets"]["size_filter"]["max"],
        id_space=config["genesets"]["gmt_id_space"],
        multimap=config["harmonization"]["multimap_policy"],
    log:
        f"{RES}/logs/prepare_genesets.log"
    conda:
        "../envs/r-bioc.yaml"   # symbols→Ensembl map + size filter; universe must not drift
    shell:
        "Rscript {input.script} --gmts {params.gmts} --dbs {params.dbs} "
        "--sha256s {params.sha256s} --out-rds {params.out_rds} "
        "--theme-spec {input.theme_spec} --out-theme-map {output.theme_map} "
        "--out-release-hash {output.release_hash} --release {params.release} "
        "--min-size {params.min_size} --max-size {params.max_size} "
        "--id-space {params.id_space} --multimap {params.multimap} > {log} 2>&1"
