---
id: workflow:t035-cross-trigger-pathway-overlap
type: workflow
title: "t035 cross-trigger pathway-overlap Snakemake workflow"
status: active
method: "snakemake"
outputs:
  - slug: gse14577-pi-cfs-prepared-gene-matrix
    title: "GSE14577 prepared PI-CFS gene-expression clean base"
    resource_names: [expr-gene-tsv-gz, sample-metadata-tsv, cohort-audit-json, clean-qa-pass]
    ontology_terms: [post-infectious-cfs, me-cfs, microarray, transcriptomics]
  - slug: gse130353-qfs-cfs-prepared-gene-matrix
    title: "GSE130353 prepared QFS/CFS monocyte gene-expression clean base"
    resource_names: [expr-gene-tsv-gz, sample-sheet-tsv, cohort-audit-json, nearzero-qa-pass, clean-qa-pass]
    ontology_terms: [post-q-fever-fatigue, me-cfs, rna-seq, transcriptomics]
  - slug: msigdb-2024-1-hs-mapped-pais-gene-set-universe
    title: "MSigDB 2024.1.Hs mapped PAIS gene-set universe"
    resource_names: [hallmark-rds, reactome-rds, gobp-rds, theme-map-tsv, theme-spec-json, msigdb-release-hash-txt, clean-qa-pass]
    ontology_terms: [msigdb, gene-sets, homo-sapiens]
created: "2026-06-26"
updated: "2026-06-26"
related:
  - task:t035
  - task:t065
  - pre-registration:0002-cross-trigger-pathway-overlap
  - plan:0003-cross-trigger-pathway-overlap-pipeline
  - question:0001-shared-molecular-signature-across-triggers
---

## Purpose

Snakemake recipe for the t035 cross-trigger pathway-overlap analysis. This
workflow prepares two reusable public expression clean bases and one mapped
gene-set universe, then runs project-specific pathway-overlap analyses and
verdict generation.

## Location

- **Snakefile:** `code/workflows/Snakefile`
- **Config:** `code/workflows/config.yaml`
- **Rules:** `code/workflows/rules/`

## Steps

| Step | Rule | Purpose |
|------|------|---------|
| acquisition | `emit_datapackage` | Record raw GEO payload provenance. |
| source QA | `qa_raw_*` | Verify raw payload parse and hash contracts. |
| clean-base prep | `prepare_gse14577`, `prepare_gse130353`, `prepare_genesets` | Produce workflow-ready expression matrices and mapped gene sets. |
| clean-base QA | `qa_clean_*` | Gate prepared matrices and gene-set universe. |
| clean-base manifests | `clean_base_datapackages` | Emit runtime datapackages for reusable clean-base substrates. |
| analysis | `limma_de`, `fgsea_enrich`, `concordance`, `permutation_null`, `specificity`, `theme_rollup` | Produce t035 project-specific result tables. |
| result QA | `qa_results`, `results_datapackage` | Gate and package the final result bundle. |

## Inputs

- `dataset:gse14577-pi-cfs-pbmc-microarray`
- `dataset:gse130353-qfs-cfs-monocytes`
- `dataset:msigdb-2024-1-hs-source-gmt-collections`

## Outputs

Reusable clean-base outputs:

- `dataset:gse14577-pi-cfs-prepared-gene-matrix`
- `dataset:gse130353-qfs-cfs-prepared-gene-matrix`
- `dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe`

Project-specific t035 outputs are described by `results/datapackage.json` and
should not be promoted as clean-base commons datasets.
