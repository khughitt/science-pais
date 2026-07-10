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
- cite:Corces2017
- cite:Desoutter2019
- cite:Horwitz2023
- cite:Lacerda2018
origins:
- type: assistant
  ref: research-topic
related:
- topic:innate-immune-memory-trained-immunity-in-pais
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-07-07'
updated: '2026-07-10'
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
- Required datasets (revised per t107 → `interpretation:0040`, which showed the HSPC-first framing is not the feasible opportunistic route):
  - **Primary opportunistic readout — CD14⁺ monocyte ATAC-seq on banked PBMC.** A longitudinal PAIS cohort with cryopreserved *viable* PBMC, PAIS case ascertainment, and coverage of the **full acute-severity spectrum**; monocytes (~10–20% of PBMC) give ample cells on any platform, and carry the *transmitted* imprint (Cheong2023). Realistic sources: **RECOVER** (open BAC application, longitudinal to ~4 y [@Horwitz2023]) and the **UK ME/CFS Biobank** (open cost-reimbursement, ~20 PBMC vials/contact [@Lacerda2018]).
  - **Definitive source-localization — marrow HSPC ATAC-seq.** Same-compartment as Cheong2023, but the only *identified* banked PAIS source is **LIINC's bone-marrow tissue arm** (consortium/LCRC-mediated access).
  - Direct circulating-CD34⁺ HSPC ATAC from banked PBMC is *marginal* (~0.05% of PBMC ⇒ single-vial bulk Omni-ATAC only [@Corces2017], CD34-preferential thaw loss [@Desoutter2019]) and compartment-mismatched — not the recommended primary.
- Required analyses:
  - **Primary:** differential chromatin accessibility (ATAC-seq peaks) at innate-immune gene loci (NLRP3, TNF, IL6, CXCL8, IFN-stimulated genes) in **CD14⁺ monocytes**, **severity-stratified**, within-trigger (PAIS-persistent vs infected-recovered); regression of PAIS persistence on a monocyte imprint-depth score with acute severity modeled, not adjusted post hoc.
  - **Definitive (LIINC marrow arm):** the same accessibility/H3K4me3 contrast in sorted marrow HSPCs, as the fidelity check localizing whether a monocyte difference originates in the HSPC compartment.
- Priority level: P2 — mechanistically important but requires specialized primary data collection not currently available in public datasets.

## Related

- Topic notes: `topic:innate-immune-memory-trained-immunity-in-pais`
- Article notes: Cheong2023, Mitroulis2018.
- Methods/Datasets: RECOVER-VITAL biobank; LIINC; sorted HSPCs from peripheral blood (low frequency, requires enrichment); single-cell multiome (snRNA + ATAC-seq).

## Notes

- 2026-07-10: **Opportunistic-feasibility triage done (t107 → `interpretation:0040-t107-hspc-epigenomics-feasibility-banked-pbmc`): CONDITIONAL GO, but the direct test is buildable on banked PAIS blood only after a target pivot.** The literal route — circulating CD34⁺ HSPC ATAC-seq from archived PBMC — is *marginal* (CD34⁺ ≈ 0.01–0.1% of PBMC → only ~a few hundred–2,000 usable HSPCs per frozen vial after CD34-preferential thaw apoptosis [@Desoutter2019] + sort loss ⇒ bulk low-input/Omni-ATAC single-vial only [@Corces2017]; scATAC/Multiome need multi-vial pooling) *and* compartment-mismatched to the **bone-marrow** HSPCs Cheong2023 imprinted. The **feasible, high-leverage** readout is instead **monocyte-progeny (CD14⁺) ATAC-seq** — abundant (~10–20% of PBMC, all-platform), and the imprint's *transmitted* readout + q0026 effector locus per Cheong2023, so a faithful (not fallback) target. The **definitive same-compartment** test needs **LIINC's banked bone marrow** (consortium/LCRC access). Access is *not* the binding constraint: RECOVER (open BAC application, viable PBMC, longitudinal to ~4 y, full acute-severity spectrum [@Horwitz2023]) and the UK ME/CFS Biobank (open cost-reimbursement, ~20 PBMC vials/contact [@Lacerda2018]) are realistically obtainable — cell-number/compartment and severity-selection (Cheong2023 severe-only) are. Recommended form: severity-stratified, within-trigger (PAIS-persistent vs infected-recovered) monocyte-ATAC on RECOVER + UK-ME/CFS PBMC, LIINC marrow as the fidelity check.
