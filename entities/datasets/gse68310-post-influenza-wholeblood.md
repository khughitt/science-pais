---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse68310-post-influenza-wholeblood
kind: dataset
title: GSE68310 — Post-influenza whole-blood (FLU09 convalescent)
status: candidate
created: "2026-07-07"
updated: "2026-07-07"
consumed_by:
- plan:0010-crosspais-pathway-response-rank-estimation
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-07-08'
  verified_by: agent (t117 WP1)
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE68310
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: GEO Series Matrix (TXT) + GSE68310_non-normalized.txt.gz (241.5 MB) + GSE68310_SubjectPhenotypes1.txt.gz; staging to disk deferred to workflow execution.
accessions:
- GSE68310
ontology_terms:
- post-influenza
- influenza
- whole-blood
- microarray
provided_capabilities:
- data_product: data-product:gene-expression-microarray
  qualifiers:
    cohort_design: case-control
    trigger: influenza
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE68310 — Post-influenza whole-blood (FLU09 convalescent)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Design specifics below are WP1-verified against the GEO record and the FLU09 paper (Zhai et al. 2015, PLoS Pathogens, PMC4466531) on 2026-07-08.

## What it is

Post-influenza / acute-respiratory-viral-infection whole-blood **MICROARRAY** (GPL10558, Illumina HumanHT-12 V4.0 BeadChip; 880 arrays from 133 individuals). FLU09 prospective cohort. Sampling timepoints (7): **enrollment/baseline** (pre-illness) → **day 0** (within 48 h of ARI symptom onset) → **day 2** → **day 4** → **day 6** → **day 21** (convalescent) → a **spring end-of-year** return visit (recovered subjects, ~5–6 months later). The latest *within-illness* sample is **day 21 (3 weeks)** — below the ≥4-week floor — and the paper states "by day 21 the gene expression pattern was indistinguishable from baseline." The only >4-week samples are the spring end-of-year visits, which are return-to-health/second-baseline collections from **recovered (asymptomatic) subjects**, not persistently-symptomatic post-acute sampling. Per-sample matrix downloadable (Series Matrix TXT + `GSE68310_non-normalized.txt.gz` + `GSE68310_SubjectPhenotypes1.txt.gz`). Case-vs-control contrast is available (influenza-positive vs other-ARI/baseline).

## Corpus role (t117)

- **Matrix:** **DEMOTED (WP1 2026-07-08) — acute/early-convalescent decoy (specificity layer), NOT primary.** The provisional promote/demote is resolved to DEMOTE: no ≥4-wk persistently-symptomatic sample exists (latest within-illness = day 21, and by day 21 expression is back to baseline per the FLU09 paper). It **removes influenza as a strict-primary trigger**. Its within-illness day-0→6 arc can serve the acute-decoy specificity layer only.
- **onset_certainty:** documented
- **WP1 resolution:**
  - **WP1 finding (2026-07-08):** sampling timepoints = {enrollment/baseline, day 0 (≤48 h post-onset), day 2, day 4, day 6, day 21 (convalescent), spring end-of-year (~5–6 mo)}. Latest within-illness sample = **day 21 (3 wk)**, below the ≥4-wk floor; paper states "by day 21 the gene expression pattern was indistinguishable from baseline." **≥4-wk post-acute samples with persistent symptoms present: NO** — the only >4-wk timepoint (spring end-of-year) is a return-to-health second-baseline from recovered, asymptomatic subjects. No persistently-symptomatic ≥4-wk sampling exists in this deposit.
  - Prior gating note: promote into the strict count only if later post-acute *symptomatic* samples were verified; otherwise demote to the early-convalescent decoy/specificity layer. (Evidence above; promotion/demotion decision left to orchestrator.)
- **Conditional/LOO flag (if promoted):** microarray platform — LOO-drop candidate; feeds the platform-LOO artifact control.

## Access / caveats

Public accession (`GSE68310`); per-sample expression matrix confirmed downloadable (WP1, 2026-07-08): Series Matrix (TXT) + `GSE68310_non-normalized.txt.gz` (241.5 MB) + `GSE68310_SubjectPhenotypes1.txt.gz`. Microarray assay confirmed (GPL10558).
