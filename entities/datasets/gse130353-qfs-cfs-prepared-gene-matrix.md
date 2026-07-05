---
id: dataset:gse130353-qfs-cfs-prepared-gene-matrix
kind: dataset
title: "GSE130353 prepared QFS/CFS monocyte gene-expression clean base"
status: active
created: "2026-06-26"
updated: "2026-06-26"
origin: derived
dataset_class: deposit
source_class: observational
tier: use-now
license: unknown
update_cadence: static
datapackage: "data/processed/GSE130353/datapackage.json"
n_rows: 23546
n_cols: 40
value_dtype: float64
feature_axis: rows
row_kind: gene
col_kind: sample
species: ["Homo sapiens"]
assay: bulk-rnaseq
library_prep: "MMSEQ log_mu expression estimates from monocyte RNA-seq"
reference_genome: "Ensembl release 68 identifiers mapped to current Ensembl universe"
preprocessing_version: "t035 config 2026-06-26"
derivation:
  kind: workflow
  workflow_recipe: "workflow:t035-cross-trigger-pathway-overlap"
  recipe_lockfile: "code/workflows/config.yaml"
  inputs:
    - dataset:gse130353-qfs-cfs-monocytes
parent_dataset: dataset:gse130353-qfs-cfs-monocytes
ontology_terms: [post-q-fever-fatigue, q-fever, me-cfs, monocytes, rna-seq, transcriptomics, clean-base]
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: q-fever
    cohort_design: case-control
source_refs:
  - cite:Raijmakers2019
related:
  - task:t035
  - task:t065
  - pre-registration:0002-cross-trigger-pathway-overlap
  - plan:0003-cross-trigger-pathway-overlap-pipeline
  - question:0001-shared-molecular-signature-across-triggers
  - paper:Raijmakers2019
---

# GSE130353 prepared QFS/CFS monocyte gene-expression clean base

## Summary

Reusable clean-base output for the GSE130353 arm of `task:t035`. The datapackage
records the filtered Ensembl `log_mu` gene matrix, authoritative sample sheet,
near-zero/cohort audit, and clean-base QA sentinels produced by the t035
workflow.

## Granularity at this access level

The unit of analysis is donor/sample accession. The expression value is MMSEQ
`log_mu`, not raw counts; DESeq2/edgeR-style count models are inadmissible for
this clean base. The QFS specificity contrast depends on the SOFT `subject
status` field, not filename prefixes.

## Commons readiness

Dry-run promotion target: clean-base deposit with `bio.matrix` and `bio.rnaseq`
modality metadata. The payload is compact and reproducible, but the inherited
GEO/source license is recorded as `unknown`; apply promotion only after license
policy is accepted for commons use.

## Connections to Project

Primary use is pathway-level comparison against the GSE14577 PI-CFS arm in
`pre-registration:0002-cross-trigger-pathway-overlap`. Do not promote t035
downstream DE, fgsea, concordance, or verdict outputs as this clean-base entity.
