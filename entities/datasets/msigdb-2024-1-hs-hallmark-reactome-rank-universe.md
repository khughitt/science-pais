---
id: dataset:msigdb-2024-1-hs-hallmark-reactome-rank-universe
kind: dataset
title: "MSigDB 2024.1.Hs Hallmark+Reactome rank-estimation universe (t117)"
status: active
created: "2026-07-08"
updated: "2026-07-08"
consumed_by:
- plan:0010-crosspais-pathway-response-rank-estimation
origin: derived
dataset_class: deposit
source_class: reference
tier: use-now
license: custom
update_cadence: static
datapackage: "data/processed/genesets/pais_universe.datapackage.json"
n_sets: 1153
set_size_summary: {min: 15, median: 42, max: 478}
identifier_space:
  tier: gene
  namespace: ensembl
  resolution_status: declared_unresolved
derivation:
  kind: workflow
  workflow_recipe: "workflow:t117-crosspais-rank"
  recipe_lockfile: "code/workflows/t117-crosspais-rank/config.yaml"
  inputs:
    - dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe
parent_dataset: dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe
ontology_terms: [msigdb, gene-sets, hallmark, reactome, homo-sapiens, effective-rank]
provided_capabilities:
  - modality: gene-sets
    trigger: not-applicable
related:
  - task:t117
  - plan:0010-crosspais-pathway-response-rank-estimation
  - dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe
  - interpretation:0037-t116-power-bias-floor-shared-axis-sim
---

# MSigDB 2024.1.Hs Hallmark+Reactome rank-estimation universe (t117)

## Summary

The **single pinned gene-set universe** for the cross-PAIS pathway-response
effective-rank estimand (`task:t117` / `plan:0010`). It is the union of the
plan:0003 mapped clean base's **Hallmark** (50 sets) and **Reactome** (1103 sets)
per-DB objects — Ensembl-mapped, size-filtered 15–500 — combined into **one**
named-list `.rds` (1153 sets). GO:BP is **deliberately dropped**: its ~4200
highly-overlapping ontology terms would flood the pathway × contrast matrix with
correlated rows and inflate apparent low-rank structure, the exact shared-artifact
confound the t117 artifact/compartment battery guards against (universe decision,
2026-07-08).

## Provenance / reproducibility

Built by `code/scripts/combine_universe.R` from the two **hash-locked** clean-base
`.rds` inputs (`hallmark.rds`, `reactome.rds`); set names carry `HALLMARK_` /
`REACTOME_` prefixes so the union is collision-free. The artifact is written with
`compress = FALSE` (no gzip mtime) and stable name ordering, so its sha256 is a
pure function of the inputs and reproducible on re-build:

- `universe_rds`: `data/processed/genesets/pais_universe.2024.1.Hs.rds`
- `sha256`: `2a782ac5f1fa9824fbc1ee174542c601da969bc0be762c7d8ac0d5a0eee9b07b`
- `bytes`: 1927734
- source `hallmark.rds` sha256: `115b739df1219c57f17365411c590fa202cbdc90097326b4960dd80ad3b7f8d0`
- source `reactome.rds` sha256: `c49cc75b4725e4771f2bd77ac90988c87e063597f40c5fe678aafd82ad97b090`

The locked hash is pinned in the workflow config (`genesets.universe_sha256`) and
re-verified before consumption by the `verify_universe` rule.

## Connections to Project

Every t117 contrast meets only at the NES level over this one universe (expression
is never merged across deposits). It is the `plan:0010` Stage-2 enrichment target
and the substrate for the Stage-3 rank battery. Derived from — and does not
replace — `dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe` (the full
Hallmark+Reactome+GO:BP clean base), which remains the t035 substrate.
