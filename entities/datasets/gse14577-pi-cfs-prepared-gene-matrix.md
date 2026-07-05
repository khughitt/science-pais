---
id: dataset:gse14577-pi-cfs-prepared-gene-matrix
kind: dataset
title: "GSE14577 prepared PI-CFS gene-expression clean base"
status: active
created: "2026-06-26"
updated: "2026-06-26"
origin: derived
dataset_class: deposit
source_class: observational
tier: use-now
license: unknown
update_cadence: static
datapackage: "data/processed/GSE14577/datapackage.json"
n_rows: 18371
n_cols: 15
value_dtype: float64
feature_axis: rows
row_kind: gene
col_kind: patient
derivation:
  kind: workflow
  workflow_recipe: "workflow:t035-cross-trigger-pathway-overlap"
  recipe_lockfile: "code/workflows/config.yaml"
  inputs:
    - dataset:gse14577-pi-cfs-pbmc-microarray
parent_dataset: dataset:gse14577-pi-cfs-pbmc-microarray
ontology_terms: [post-infectious-cfs, me-cfs, pbmc, microarray, transcriptomics, clean-base]
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: mixed
    cohort_design: case-control
source_refs:
  - cite:Gow2009
related:
  - task:t035
  - task:t065
  - pre-registration:0002-cross-trigger-pathway-overlap
  - plan:0003-cross-trigger-pathway-overlap-pipeline
  - question:0001-shared-molecular-signature-across-triggers
  - paper:Gow2009
---

# GSE14577 prepared PI-CFS gene-expression clean base

## Summary

Reusable clean-base output for the GSE14577 arm of `task:t035`. The datapackage
records the patient-level Ensembl gene matrix, sample metadata, cohort audit,
and clean-base QA sentinel produced by the t035 workflow.

## Granularity at this access level

The unit of analysis is patient. The workflow collapses U133A/U133B probe-level
data to Ensembl gene identifiers by the locked t035 preprocessing recipe. This
entity is not the raw GEO deposit and should not be used as evidence for
platform-level probe details.

## Commons readiness

Dry-run promotion target: clean-base deposit with `bio.matrix` modality. The
payload is compact and reproducible, but the inherited GEO/source license is
recorded as `unknown`; apply promotion only after license policy is accepted for
commons use.

## Connections to Project

Primary use is pathway-level comparison against the Q-fever/CFS monocyte arm in
`pre-registration:0002-cross-trigger-pathway-overlap`. Do not promote t035
downstream DE, fgsea, concordance, or verdict outputs as this clean-base entity.
