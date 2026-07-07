---
id: question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence
kind: question
title: Does HSPC epigenomic imprinting depth at 3-6 months post-infection predict
  PAIS persistence at 12+ months?
status: active
ontology_terms:
- hematopoietic stem and progenitor cells
- ATAC-seq
- H3K4me3
- trained immunity
- PAIS biomarker
- epigenetic memory
datasets: []
source_refs:
- cite:Cheong2023
- cite:Mitroulis2018
origins:
- type: assistant
  ref: research-topic
related:
- topic:innate-immune-memory-trained-immunity-in-pais
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-07-07'
updated: '2026-07-07'
added_by: "llm:claude-sonnet-4-6:research-topic"
---

# Does HSPC epigenomic imprinting depth at 3-6 months post-infection predict PAIS persistence at 12+ months?

## Summary

Cheong et al. 2023 (Cell) demonstrated that severe SARS-CoV-2 infection imprints hematopoietic stem and progenitor cell (HSPC) chromatin in a durable manner (persisting to 12 months), with progeny monocytes inheriting the hyperreactive epigenome. If this HSPC imprinting is a *causal* contributor to PAIS chronification, then imprinting depth — measurable by ATAC-seq chromatin accessibility or H3K4me3 ChIP-seq at inflammatory gene loci — should predict who develops persistent PAIS vs who recovers. This question asks whether HSPC epigenomic imprinting is a prospective biomarker of PAIS risk and a mechanistic proxy for innate-immune-training depth.

## Why It Matters

- If HSPC imprinting depth predicts PAIS chronification, it would be the first mechanistic PAIS biomarker that is (a) antigen-independent, (b) upstream of the circulating monocyte/cytokine phenotype, and (c) actionable (imprinting is in principle reversible by epigenetic agents).
- Without this test, the role of central trained immunity in PAIS remains inferential — we know the imprint exists after severe COVID, but not whether it is PAIS-specific or merely a severity correlate.
- A positive result would directly prioritize epigenetic-reprogramming approaches (BET inhibitors, itaconate supplementation, statin-class modulators) as PAIS therapeutics rather than purely anti-inflammatory or antiviral strategies.

## Current Evidence

- Supporting: Cheong2023 shows that HSPC chromatin remodeling after severe COVID persists to 12 months and is conveyed to monocyte progeny; the paper establishes the imprint is present and transmitted but does not correlate imprinting depth with PAIS symptom status or recovery trajectory.
- Supporting: HSPC-level imprinting (Mitroulis2018, β-glucan murine model) is durable over the timescale relevant to PAIS (months); the HSPC compartment renews the peripheral monocyte pool continuously.
- Gap: No study has measured HSPC epigenomic state prospectively from infection through the PAIS/recovery outcome window in a cohort with defined PAIS case definition. The Cheong2023 cohort was enriched for severe illness; long COVID is common after mild-to-moderate acute disease.
- Conflicting: The severity-selection issue in Cheong2023 means we do not know if mild/moderate COVID also imprints HSPCs at a magnitude sufficient to sustain PAIS; if imprinting requires near-hospitalization IL-6 levels, it would predict much lower long COVID rates than are observed.

## Thoughts

- Best current interpretation: HSPC imprinting depth is a biologically plausible and mechanistically motivated PAIS predictor, but no prospective data yet support or refute it. The question is answerable with existing ATAC-seq and ChIP-seq technology applied to a well-phenotyped PAIS inception cohort.
- Major remaining uncertainty: (a) whether mild/moderate infection drives meaningful HSPC imprinting; (b) whether the imprint is causally linked to symptoms vs merely reflecting acute severity; (c) whether HSPC can be accessed longitudinally from peripheral blood (circulating HSPC frequency is low) or whether bone marrow aspirates are required.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (HSPC imprinting as a candidate attractor maintenance mechanism).
- Required datasets: a prospective PAIS inception cohort with blood sampling at 3 and 12 months post-infection, PAIS case ascertainment, and sufficient HSPC cell numbers for ATAC-seq (or single-cell multiome). Large RECOVER-style biobank with sorted HSPC would be ideal.
- Required analyses: differential chromatin accessibility (ATAC-seq peaks) and H3K4me3 ChIP-seq at innate immune gene loci (NLRP3, TNF, IL6, CXCL8, IFN-stimulated genes) in HSPCs stratified by PAIS status at 12 months; regression of PAIS outcome on imprinting depth score.
- Priority level: P2 — mechanistically important but requires specialized primary data collection not currently available in public datasets.

## Related

- Topic notes: `topic:innate-immune-memory-trained-immunity-in-pais`
- Article notes: Cheong2023, Mitroulis2018.
- Methods/Datasets: RECOVER-VITAL biobank; LIINC; sorted HSPCs from peripheral blood (low frequency, requires enrichment); single-cell multiome (snRNA + ATAC-seq).
