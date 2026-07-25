---
id: dataset:msigdb-2024-1-hs-source-gmt-collections
kind: dataset
title: MSigDB 2024.1.Hs source GMT collections
status: candidate
created: "2026-06-26"
updated: "2026-06-26"
origin: external
dataset_class: reference
source_class: reference
tier: evaluate-next
license: custom
update_cadence: static
access:
  level: public
  availability: available
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-06-26'
  verified_by: agent (t065)
  source_url: https://data.broadinstitute.org/gsea-msigdb/msigdb/release/2024.1.Hs/
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: Public Broad MSigDB release — GMT collections download without credentials and rerun locally. Reference dataset. Third-party-reproducible.
accessions:
- MSigDB:2024.1.Hs
ontology_terms:
- msigdb
- gene-sets
- hallmark
- reactome
- go-biological-process
- homo-sapiens
provided_capabilities: []
related:
- task:t035
- task:t065
- pre-registration:0002-cross-trigger-pathway-overlap
- plan:0003-cross-trigger-pathway-overlap-pipeline
- question:0001-shared-molecular-signature-across-triggers
---

# MSigDB 2024.1.Hs source GMT collections

## Summary

Pinned source reference for the t035 gene-set universe: MSigDB 2024.1.Hs
Hallmark, Reactome, and GO:BP symbol GMT files. The workflow verifies each GMT
against the locked SHA-256 in `code/workflows/config.yaml` before mapping to
Ensembl and applying the t035 size filter.

## Access verification log

- 2026-06-26 (agent t065): public release landing URL and local hash-verified GMT
  acquisition path confirmed from the t035 workflow config and verify sentinels.
  License is recorded as `custom`; commons application needs policy review.

## Connections to Project

This source is not itself the project clean base. The reusable project substrate
is `dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe`, derived from these
GMT collections by the locked t035 mapping/theme recipe.
