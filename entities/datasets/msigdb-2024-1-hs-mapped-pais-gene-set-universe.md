---
id: dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe
type: dataset
title: "MSigDB 2024.1.Hs mapped PAIS gene-set universe"
status: active
created: "2026-06-26"
updated: "2026-06-26"
origin: derived
dataset_class: deposit
source_class: reference
tier: use-now
license: custom
update_cadence: static
datapackage: "data/processed/genesets/datapackage.json"
member_key_column: set_key
members_resource: members-tsv
n_sets: 5355
set_size_summary: {min: 15, median: 43, max: 500}
identifier_space:
  tier: gene
  namespace: ensembl
  resolution_status: declared_unresolved
derivation:
  kind: workflow
  workflow_recipe: "workflow:t035-cross-trigger-pathway-overlap"
  recipe_lockfile: "code/workflows/config.yaml"
  inputs:
    - dataset:msigdb-2024-1-hs-source-gmt-collections
parent_dataset: dataset:msigdb-2024-1-hs-source-gmt-collections
ontology_terms: [msigdb, gene-sets, hallmark, reactome, go-biological-process, homo-sapiens, clean-base]
provided_capabilities:
  - modality: gene-sets
    trigger: not-applicable
related:
  - task:t035
  - task:t065
  - task:t069
  - pre-registration:0002-cross-trigger-pathway-overlap
  - plan:0003-cross-trigger-pathway-overlap-pipeline
  - question:0001-shared-molecular-signature-across-triggers
---

# MSigDB 2024.1.Hs mapped PAIS gene-set universe

## Summary

Reusable t035 gene-set clean base: MSigDB 2024.1.Hs Hallmark, Reactome, and
GO:BP collections mapped from symbols to Ensembl, size-filtered, and assigned to
the locked PAIS theme map.

## Granularity at this access level

The resources are workflow-ready RDS gene-set objects, a normalized
`members.tsv` table for `bio.geneset` promotion, plus the theme-map and
release-hash sidecars. This entity is a reusable reference substrate for the
t035 analysis, not a project result bundle.

## Commons readiness

Dry-run promotion target: clean-base deposit with the `bio.geneset` extension.
The generated `members.tsv` resource has one row per retained set
(`set_key = <db>:<gene_set>`) and semicolon-delimited Ensembl `member_ids`.
Actual commons application remains blocked on MSigDB custom-license policy.

## Connections to Project

Primary use is the t035 Hallmark confirmatory analysis and Reactome/GO:BP
sensitivity analyses. Do not promote downstream fgsea/NES, concordance, or
verdict tables as this clean-base entity.
