---
id: evidence-line:0061-aid2025-persistent-jakstat-il6-exhaustion-supports-0025
type: evidence-line
title: "Aid2025 multi-cohort: persistent JAK-STAT/IL-6/IFN/complement activation +\
  \ CD8 exhaustion >180d with no circulating virus — supports the persistent-inflammatory-activation\
  \ state"
status: active
stance: supports
target: proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
source: paper:Aid2025
strength: moderate
independence: independent
independence_group: aid2025-masscpr-recover-lc-multiomics
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: observational
related:
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- hypothesis:0003-immune-exhaustion-feedback
source_refs:
- paper:Aid2025
created: '2026-06-24'
updated: '2026-06-24'
---
# Evidence Line: Aid2025 multi-cohort: persistent JAK-STAT/IL-6/IFN/complement activation + CD8 exhaustion >180d with no circulating virus — supports the persistent-inflammatory-activation state

## What this line shows

Aid2025 (*Nat Immunol*) multi-omically profiled two independent cohorts — a 2020–2021 discovery cohort
(n=142; 28 LC) and a 2023–2024 NIH RECOVER validation cohort (n=38; 18 LC). PBMC bulk RNA-seq + Olink
proteomics show **IL-6, IL-6-JAK-STAT3, JAK-STAT, JAK1, type-II IFN (IFNγ), and complement** pathways
persistently enriched at day 90–180 **and beyond 180 days** (GSEA, FDR q<0.05), with **IL-6R protein
validated** by ELISA/MSD across both cohorts, co-occurring with **CD8+ T-cell exhaustion** (PDCD1, IFI44,
PRDM1) and **no detectable plasma SARS-CoV-2** (genomic + subgenomic RT-PCR). Pathway scores correlate with
fatigue, dyspnoea, and cognitive complaints. This directly supports `proposition:0025`'s persistent-
inflammatory-activation arm (and the no-circulating-virus clause).

## Why it is independent

`independent` under `independence_group: aid2025-masscpr-recover-lc-multiomics`. Internally cross-validated
across two separately recruited cohorts (MassCPR/BIDMC discovery + NIH RECOVER validation), distinct from
the Ryan2022 whole-blood line (`evidence-line:0062`) in cohort, compartment (PBMC vs whole blood), and
assay (GSEA pathway enrichment + Olink vs whole-blood DEG/ISG).

## Caveats / scope

`direct_test`, **moderate** — bounded by: (1) small, demographically skewed cohorts (discovery LC 85.7%
female, 100% Hispanic/Latino, 72% unvaccinated; validation n=18); (2) **bulk** PBMC RNA-seq cannot resolve
the cell source of the IL-6/JAK-STAT signal (`question:0006`); (3) **observational/cross-sectional within
time-windows** — co-activation with symptoms is associative, establishing the *state* but not that it
*drives* symptoms (that is `proposition:0026`); (4) no-virus is shown in **blood**, not tissue, so it
does not exclude a tissue reservoir feeding the loop (`hypothesis:0002`); (5) pre-Omicron/largely
unvaccinated. Supports the descriptive state, not the causal-loop claim.