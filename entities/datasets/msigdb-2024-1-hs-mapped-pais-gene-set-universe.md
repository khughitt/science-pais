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
derivation:
  kind: workflow
  workflow_recipe: "workflow:t035-cross-trigger-pathway-overlap"
  recipe_lockfile: "code/workflows/config.yaml"
  inputs:
    - dataset:msigdb-2024-1-hs-source-gmt-collections
parent_dataset: dataset:msigdb-2024-1-hs-source-gmt-collections
ontology_terms: [msigdb, gene-sets, hallmark, reactome, go-biological-process, homo-sapiens, clean-base]
related:
  - task:t035
  - task:t065
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

The resources are workflow-ready RDS gene-set objects plus the theme-map and
release-hash sidecars. This entity is a reusable reference substrate for the
t035 analysis, not a project result bundle.

## Commons readiness

Dry-run promotion target: clean-base deposit without `bio.geneset` extension.
Actual commons application is blocked on MSigDB license policy. The current
datapackage is workflow-ready RDS plus a theme index, not a normalized long
membership table with a `set_key` column; add that table before applying the
`bio.geneset` mixin.

## Connections to Project

Primary use is the t035 Hallmark confirmatory analysis and Reactome/GO:BP
sensitivity analyses. Do not promote downstream fgsea/NES, concordance, or
verdict tables as this clean-base entity.
