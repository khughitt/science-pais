---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:prjna1001790-post-chikv-wholeblood
kind: dataset
title: PRJNA1001790 — Post-chikungunya whole-blood transcriptome
status: candidate
created: '2026-07-07'
updated: '2026-07-07'
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
  verified: false
  source_url: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1001790
  notes: "Raw FASTQ only (SRA: 98 BioSamples / 196 experiments = total-RNA + small-RNA library per sample); no processed per-sample expression matrix deposited. Raw reads only — needs pinned quantification (G4) before staging."
accessions:
- PRJNA1001790
ontology_terms:
- post-chikungunya
- chikungunya
- whole-blood
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: chikungunya
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# PRJNA1001790 — Post-chikungunya whole-blood transcriptome

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Design specifics below are WP1-verified against the BioProject/SRA record and the linked paper (Ramundo et al. 2025, Scientific Reports, PMC11861634) on 2026-07-08.

## What it is

Post-chikungunya whole-blood **bulk total RNA-seq** (TruSeq Stranded, PE 2×75 bp) **+ small RNA-seq** (TruSeq Small RNA, SE 75 bp); BioProject `PRJNA1001790`, 98 BioSamples / 196 SRA experiments (= one mRNA + one miRNA library per sample). **54 patients: 29 pCHIKV-CIJD cases** (developed post-chikungunya Chronic Inflammatory Joint Disease) **vs 25 CHIKV-infected controls who recovered** (did NOT chronify). The contrast is therefore **chronic-outcome vs recovered-outcome — both CHIKV-infected — NOT infected-vs-healthy** (flag for cross-trigger harmonization). Disease-phase definitions (paper): acute = up to 14 days; post-acute = 14–90 days; chronic (pCHIKV-CIJD) = symptom persistence >90 days. Whole-blood samples were **SEQUENCED at D0** (inclusion, acute phase, ≤14 d post-onset) **and D21** (post-acute, 21 days after inclusion); clinical follow-up visits also occurred at D90, but the sequenced post-acute samples were collected up to D21. Deposit is **RAW FASTQ only** — no processed per-sample matrix — so needs pinned quantification (G4) before use.

## Corpus role (t117)

- **Matrix:** **DEMOTED from strict-primary (WP1 2026-07-08).** Resolved to DEMOTE: the sequenced post-acute timepoint is D21 (~3 wk, below the ≥4-wk floor), no transcriptome exists at the D90 chronic-diagnosis visit, and the deposit is raw-FASTQ-only (G4 blocker). It **removes chikungunya as a strict-primary trigger.** Its distinctive **chronic-outcome-defined, CHIKV-recovered-control, prospective early-predictor** design is a candidate for a separate *adjacent chronification-predictor* triangulation, not the primary post-acute rank matrix.
- **onset_certainty:** documented
- **WP1 resolution:**
  - **WP1 finding (2026-07-08):** SEQUENCED whole-blood timepoints = {**D0** = inclusion (acute phase, ≤14 d post-onset), **D21** = 21 days post-inclusion (post-acute phase)}. Disease-phase defs: acute ≤14 d, post-acute 14–90 d, chronic >90 d. Clinical D90 visits occurred but sequenced post-acute samples were collected up to D21 (~3 wk post-inclusion). **≥4-wk post-acute samples: borderline → NO at the molecular level** — the sequenced post-acute timepoint is D21 (~3 wk after inclusion; roughly 3–5 wk post symptom-onset depending on inclusion day), below the clean ≥4-wk floor; **no transcriptome is confirmed at the D90 chronic-diagnosis visit.** HOWEVER cases (29) are *defined by* persistent symptoms (chronic joint disease at ≥90 d), so the D21 sample is drawn from still-symptomatic future-chronic patients — a **prospective early-predictor design**, not a ≥4-wk persistent-symptom molecular snapshot. Contrast is chronic-vs-recovered (both CHIKV+), not disease-vs-healthy.
  - Additional blocker: SRA raw-FASTQ only → the pinned raw-read quantification path (G4) must be verified before staging. (Evidence above; promotion/demotion decision left to orchestrator.)
- **Conditional/LOO flag (if promoted):** SRA-only platform axis — LOO-drop candidate; feeds the platform-LOO artifact control.

## Access / caveats

Public accession (`PRJNA1001790`); WP1 (2026-07-08) confirms **raw FASTQ only** — no processed per-sample expression matrix deposited (SRA: 98 BioSamples / 196 experiments = total-RNA + small-RNA per sample). Obtaining a per-sample matrix requires pinned raw-read quantification (G4). Assay confirmed: bulk total RNA-seq + small RNA-seq (not single-cell).
