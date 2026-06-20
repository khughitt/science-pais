---
id: question:0001-shared-molecular-signature-across-triggers
type: question
title: Is there a molecular signature that is both shared across PAIS triggers (SARS-CoV-2,
  Borrelia, EBV, dengue) and specific to failed recovery versus full recovery?
status: active
ontology_terms:
- biomarker
- immune dysregulation
- post-acute infection syndrome
- proteomics
datasets: []
source_refs:
- cite:Klein2023
- cite:Komaroff2023
- cite:Peppercorn2023
- cite:Galbraith2011
- cite:Patterson2024
- cite:Raijmakers2021
- cite:Shankar2025
- cite:Sommen2026
- cite:Chowdhury2026
related:
- topic:shared-failure-mode-across-pais
- topic:mecfs-long-covid-convergence
- discussion:0002-cross-pathogen-pais-signature-convergence
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-11'
updated: '2026-06-20'
---

# Is there a molecular signature that is both shared across PAIS triggers (SARS-CoV-2, Borrelia, EBV, dengue) and specific to failed recovery versus full recovery?

## Summary

The project's central claim is that distinct infectious triggers converge on a shared post-infectious failure mode. Symptom-level convergence is well documented (Komaroff2023, Bai2023), but a *molecular* signature that is simultaneously (a) shared across triggers and (b) specific to failed recovery versus full recovery has not been demonstrated. This question asks whether such a signature exists, because it is the decisive empirical test separating a genuine shared mechanism from a coincidental convergence onto a finite repertoire of organ-system failures.

## Why It Matters

- Decides whether PAIS should be treated and trialed as one entity (shared-mechanism therapeutics) or as trigger-specific syndromes — the project's core scope decision.
- If unanswered, cross-PAIS reasoning risks conflating symptom overlap with biological equivalence (the trap Hanson2023 warns against), and biomarker panels derived in one trigger may not transfer.

## Current Evidence

- Supporting (shared biology): Peppercorn2023 finds overlapping immune+mitochondrial PBMC proteomes between long COVID and ME/CFS despite very different durations; Klein2023 builds a high-AUC long-COVID signature (low cortisol, non-conventional monocytes, EBV markers) that is a candidate panel to test cross-trigger; Komaroff2023 documents shared abnormalities across seven domains.
- Conflicting / cautionary: Peppercorn2023 also finds direction-of-effect *discordances* (HLA-E, S100A4 opposite between LC and ME/CFS); Cruz2025 shows even within SARS-CoV-2 the immune signature is not unitary; Hanson2023 argues classical ME/CFS is enterovirus-specific.
- **Provenance audit (2026-06-20 cross-pathogen search → `discussion:0002`):** the apparent convergence is almost entirely **assembled from separate single-trigger studies**. The few genuine **head-to-head** designs are sparse and, after the 2026-06-20 full-read pass, **uniformly fail to demonstrate a shared *positive* molecular signature**: Galbraith2011 (Dubbo EBV/Ross-River/Q-fever) found that, by qPCR, **none of the differentially expressed genes were consistent across all three triggers** in PBMCs (full text read 2026-06-20; corrects the earlier "bulk blood" framing and an even earlier "partial shared → supports" reading); Raijmakers2021 finds a shared *negative* (no TSPO neuroinflammation in ME/CFS or QFS — ambiguous); Patterson2024 *separates* long COVID from chronic Lyme by cytokine hubs (disputes). **No study runs harmonized multi-omics across ≥3 infectious triggers with full-recovery controls** — the decisive test does not yet exist. The strongest surviving convergence is at the **physiological/functional** level (Joseph2023 invasive-CPET in both ME/CFS and PASC; Liu2026 patient-IgG disrupting energetics across post-infectious subgroups), not the shared-analyte level. **2026-06-20 addition:** genuine *within-study* head-to-head molecular comparisons have now appeared, but all are **long COVID vs ME/CFS** (two fatigue phenotypes, not ≥3 distinct infectious triggers): Shankar2025 (PNAS) finds a **shared mitochondrial/oxidative-stress signature** across both (a positive pathway-level convergence), and Sommen2026 finds a **shared terminal-NK signature** that is trigger-agnostic; conversely Chowdhury2026 finds the 3-month plasma proteome distinguishes PCC from recovery by only **2 proteins** (a near-null for a *PCC-specific* analyte signature). So pathway-level LC↔ME/CFS convergence is now genuinely supported, while a recovery-discriminating specific-analyte signature and the ≥3-trigger test remain unmet; post-dengue and QFS omics are essentially absent, so the question stays *unanswerable* for several of the project's own named triggers.

## Thoughts

- Best current interpretation: convergence is robust at the level of biological *domains* (immune, mitochondrial, neurocognitive) but unproven at the level of specific shared molecules; a true cross-trigger PAIS-specific signature most plausibly lives in pathway-level features (e.g. mitochondrial/energy stress, innate non-resolution) rather than individual analytes.
- Major uncertainty: no study has yet run a head-to-head multi-omics comparison across ≥3 triggers with full-recovery controls; disease stage and duration are major confounders.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0003-immune-exhaustion-feedback`.
- Required data or analyses: harmonized multi-omics (proteomics/metabolomics/transcriptomics) across SARS-CoV-2, Borrelia, EBV/ME-CFS, dengue cohorts with matched recovered controls; pathway-level rather than analyte-level comparison.
- Priority level: P1 — directly operationalizes the research question.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`, `topic:mecfs-long-covid-convergence`, `topic:long-covid-immune-dysregulation`.
- Article notes: Klein2023, Komaroff2023, Peppercorn2023, Cruz2025, Hanson2023.
- Methods/Datasets: MY-LC, INCOV, and ME/CFS proteomic datasets are candidate inputs.
