---
id: topic:biomarkers-and-objective-endpoints
type: topic
title: Biomarkers and Objective Endpoints for Post-Acute Infection Syndromes
status: active
ontology_terms:
- biomarker
- serum proteomics
- immune profiling
- objective endpoint
- post-exertional malaise
- polysomnography
- reproducibility
- post-acute infection syndrome
related:
- topic:mecfs-long-covid-convergence
- question:0001-shared-molecular-signature-across-triggers
source_refs:
- cite:Patrascu2025
- cite:Talla2023
- cite:CerviaHasler2024
- cite:Klein2023
- cite:Peppercorn2023
- cite:Hoel2026
- cite:Che2025
- cite:Moldofsky2011
created: '2026-06-11'
updated: '2026-06-11'
---
# Biomarkers and Objective Endpoints for Post-Acute Infection Syndromes

## Summary

PAIS research is bottlenecked by measurement: without objective, reproducible biomarkers and endpoints, the syndromes cannot be reliably diagnosed, stratified, or used as trial outcomes, and computational subphenotyping has nothing stable to learn from. Several candidate molecular signatures now exist — serum proteomic inflammatory subtypes in long COVID (Talla2023), a high-AUC multi-omic immune-profiling panel (Klein2023), a complement/thromboinflammation signature with quantitative biomarker ratios (CerviaHasler2024), a PBMC proteome overlapping ME/CFS (Peppercorn2023), the largest ME/CFS serum proteome to date (Hoel2026), and an exercise-challenge multi-omics model of post-exertional malaise (Che2025) — alongside an objective neurophysiological endpoint in post-SARS sleep architecture (Moldofsky2011) and a review-level synthesis of the biomarker landscape (Patrascu2025). The recurring problem is *reproducibility and heterogeneity*: signatures replicate at the level of biological domains (inflammation, mitochondrial/energy, vascular, neuro) more reliably than at the level of individual analytes, and patient heterogeneity fractures most single-marker panels. Establishing objective, reproducible endpoints is therefore the prerequisite for credible trials and for the project's subphenotyping aims.

## Key Concepts

**Serum/plasma proteomic signatures.** Talla2023 (Olink, 1,472 proteins) shows long COVID is biologically heterogeneous: ~65% of patients fall into two inflammatory subclusters (IFN-gamma/NF-kB/TNF dominated; the second adding neutrophil-activation/NETosis and type I IFN), ~35% have no distinguishable inflammatory signature, and a 3-protein panel (CCL7, CD40LG, S100A12) reaches AUROC 0.79-0.87 with independent (INCOV) replication. CerviaHasler2024 (SomaScan, >6,500 proteins) identifies a persistent complement/thromboinflammation signature with C5bC6/C7 and vWF/ADAMTS13 ratios as top machine-learning biomarkers. Hoel2026 (SomaScan 7k, largest ME/CFS serum proteome: 50 vs 29) maps multisystem secretome changes (elevated complement, coagulation, chemokines; reduced neutrophil-derived proteins) supporting failed immune/metabolic homeostasis.

**Immune-profiling signatures.** Klein2023 (MY-LC, 275 individuals) integrates flow cytometry, plasma proteomics, antibody profiling, and viral serology via machine learning into a LASSO classifier with AUC 0.94, with markedly reduced systemic cortisol as the single strongest predictor (AUC 0.96 alone), plus non-conventional monocyte and EBV-reactivation features — the highest-AUC long-COVID panel in the project's literature, though derived in one trigger.

**Intracellular / PBMC proteome.** Peppercorn2023 (SWATH MS on PBMCs) finds the long COVID immune-cell proteome overlaps the ME/CFS proteome in immune and mitochondrial pathways despite very different illness durations (~1 vs ~16 years) — molecular support for cross-syndrome convergence, while also reporting direction-of-effect discordances for some proteins.

**Functional / exercise-provoked endpoints.** Che2025 measures plasma metabolomics, proteomics, and ex-vivo immune responses before and 24 h after a standardized cardiopulmonary exercise test, capturing the *provoked* state (post-exertional malaise) rather than a single resting snapshot — a design that turns PEM into a measurable, reproducible perturbation and points to a heightened innate-immune response as a candidate trigger.

**Objective neurophysiology.** Moldofsky2011 demonstrates an objective polysomnographic abnormality (alpha-EEG sleep anomaly, cyclical alternating pattern, nonrestorative sleep) in chronic post-SARS syndrome — an early example of a non-self-report, instrument-based endpoint for a PAIS, and a template for objective measurement beyond blood biomarkers.

**Synthesis of the biomarker landscape.** Patrascu2025 reviews established (CRP, IL-6, D-dimer, ferritin, ESR) and novel (suPAR, NETs/Cit-H3, NfL, GFAP, KL-6, SP-D, I-FABP, zonulin) markers organized by organ system, and argues for biomarker-guided, longitudinal, multi-omics-plus-AI approaches — the measurement framework the project's computational track depends on.

## Current State of Knowledge

### What the evidence supports

- Multiple independent platforms detect persistent, objectively measurable molecular abnormalities months to years post-infection (Talla2023, Klein2023, CerviaHasler2024, Hoel2026), distinguishing failed recovery from delayed recovery.
- Small, validated panels can stratify patients: the 3-protein inflammatory panel (Talla2023) and the cortisol-anchored multi-omic classifier (Klein2023) both replicate or reach high AUC.
- Objective, non-self-report endpoints exist beyond blood: polysomnographic sleep anomalies (Moldofsky2011) and provoked exercise-challenge readouts (Che2025).
- Domain-level convergence (inflammation, mitochondrial/energy, vascular/complement, neuro) recurs across long COVID and ME/CFS (Peppercorn2023, Hoel2026, CerviaHasler2024), supporting cross-PAIS endpoints.

### What is contested or unresolved

- **Reproducibility and heterogeneity.** Talla2023 shows ~35% of patients have no inflammatory signature at all, and symptom categories do not map onto molecular clusters; single-analyte panels frequently fail to transfer across cohorts, platforms (Olink vs SomaScan vs MS), variants, and vaccination eras.
- **No validated surrogate endpoint.** The field still lacks a single, prospectively validated biomarker of disease burden that responds to treatment — the prerequisite for efficient trials.
- **Trigger and platform specificity.** Klein2023's high-AUC panel is COVID-derived and untested across triggers; cross-platform NPX comparison is discouraged (Talla2023), complicating meta-analysis.
- **Cohort size and selection.** Many signatures rest on modest, often referral-biased, mostly unvaccinated, ancestral-strain or single-center cohorts (Talla2023, Peppercorn2023, Moldofsky2011, CerviaHasler2024).

### Tensions between papers

Klein2023 elevates a multi-domain *immune + endocrine* signature (cortisol, monocytes, EBV) as near-diagnostic, whereas Talla2023 emphasizes that a large minority of patients have no inflammatory signature — i.e. no single panel will capture all of PAIS. Peppercorn2023 reports cross-syndrome proteome convergence but also analyte-level discordances, cautioning against treating overlap as equivalence (the same caution Hanson2023 raises elsewhere in the project). Resting-snapshot proteomics (Talla2023, Klein2023, Hoel2026) and provoked/functional measurement (Che2025, Moldofsky2011) may be measuring different things, and the field has not settled which is the more reproducible endpoint.

## Controversies and Open Questions

- Which candidate signatures are reproducible across cohorts, platforms, triggers, and variant/vaccination eras, versus cohort-specific artefacts (Talla2023, Klein2023, CerviaHasler2024)?
- Is there a single validated surrogate endpoint of disease burden that tracks treatment response, or must endpoints be domain- or subphenotype-specific (Patrascu2025, Talla2023)?
- Do provoked/functional endpoints (exercise challenge, polysomnography) outperform resting biomarkers for diagnosis and trial outcomes (Che2025, Moldofsky2011)?
- Do long COVID-derived panels transfer to ME/CFS and other PAIS, as required for a cross-trigger PAIS-specific signature (Peppercorn2023, Hoel2026, Klein2023)?
- How should heterogeneity be handled — as noise to average over, or as the signal that defines subphenotypes for stratified trials (Talla2023)?

## Relevance to This Project

Objective, reproducible endpoints are the prerequisite for everything the project wants to do downstream: diagnose PAIS, run credible interventional trials, and perform computational subphenotyping that distinguishes shared from trigger-specific biology. This topic directly operationalizes `question:0001-shared-molecular-signature-across-triggers` by inventorying the candidate signatures and exposing the reproducibility/heterogeneity problem that question hinges on, and it supports `topic:mecfs-long-covid-convergence` by assembling the molecular evidence (Peppercorn2023, Hoel2026, Che2025) for and against cross-syndrome equivalence at the analyte level. It also supplies the measurement substrate for the vascular subphenotype work (CerviaHasler2024) and for any pre-registered analysis: the harmonized, multi-platform, multi-trigger comparison with recovered controls that the project's central question demands.

## Key References

- Patrascu2025 — narrative synthesis of established and novel PASC biomarkers by organ system; argues for longitudinal multi-omics + AI.
- Talla2023 — serum proteomic inflammatory subtypes of long COVID; 3-protein panel (CCL7, CD40LG, S100A12) with INCOV replication; ~35% non-inflammatory.
- CerviaHasler2024 — complement/thromboinflammation signature; C5bC6/C7 and vWF/ADAMTS13 as top biomarkers (Science adg7942).
- Klein2023 — MY-LC multi-omic immune-profiling classifier (AUC 0.94); cortisol as strongest single predictor.
- Peppercorn2023 — PBMC proteome overlap between long COVID and ME/CFS; immune + mitochondrial pathways; some discordances.
- Hoel2026 — largest ME/CFS serum proteome (SomaScan 7k); multisystem secretome changes; failed immune/metabolic homeostasis.
- Che2025 — exercise-challenge multi-omics model of post-exertional malaise; heightened innate immunity as candidate trigger.
- Moldofsky2011 — objective polysomnographic sleep anomaly in chronic post-SARS syndrome; early non-self-report PAIS endpoint.
