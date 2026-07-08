---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse68310-post-influenza-wholeblood
kind: dataset
title: GSE68310 — Post-influenza whole-blood (FLU09 convalescent)
status: candidate
created: '2026-07-07'
updated: '2026-07-07'
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: false
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE68310
accessions:
- GSE68310
ontology_terms:
- post-influenza
- influenza
- whole-blood
- microarray
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: influenza
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE68310 — Post-influenza whole-blood (FLU09 convalescent)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Post-influenza convalescent whole-blood microarray. Convalescent sampling window is short (≈3 weeks [UNVERIFIED]), near/under the ≥4-week post-acute floor.

## Corpus role (t117)

- **Matrix:** strict-primary **(PROVISIONAL — floor-gated)**. The ≈3 wk convalescent window is *inside* the plan's ≥4 wk post-acute floor, so this deposit is **NOT counted in the strict trigger/K total** and does not enter the primary matrix on the discovery-sweep timepoint. `matrix: strict-primary` stands only as a *target* pending the WP1 timepoint check.
- **onset_certainty:** documented
- **WP1 resolution:** promote into the strict count **only if** later post-acute *symptomatic* samples are verified; otherwise **demote** to the early-convalescent decoy/specificity layer (not a primary arm).
- **Conditional/LOO flag (if promoted):** microarray platform — LOO-drop candidate; feeds the platform-LOO artifact control.

## Access / caveats

Public accession (`GSE68310`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
