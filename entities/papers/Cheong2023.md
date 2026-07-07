---
id: paper:Cheong2023
kind: paper
title: Epigenetic memory of coronavirus infection in innate immune cells and their progenitors
status: active
paper_kind: ""
ontology_terms:
- epigenetic reprogramming
- trained immunity
- hematopoietic stem and progenitor cells
- chromatin accessibility
- ATAC-seq
- myelopoiesis
- monocyte hyperreactivity
- IL-6 signaling
- STAT3
- innate immune memory
- COVID-19
- convalescence
dataset_usage: []
source_refs:
- cite:Cheong2023
related:
- topic:innate-immune-memory-trained-immunity-in-pais
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i
- question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1
- hypothesis:0003-immune-exhaustion-feedback
- hypothesis:0004-acute-severity-threshold
created: "2026-07-07"
updated: "2026-07-07"
---

# Epigenetic memory of coronavirus infection in innate immune cells and their progenitors

<!--
- **Authors:** Jin-Gyu Cheong, Arjun Ravishankar, Siddhartha Sharma, Christopher N. Parkhurst, Simon A. Grassmann, Claire K. Wingert, Paoline Laurent, Sai Ma, Lucinda Paddock, Isabella C. Miranda, ..., Jason D. Buenrostro, Rachel E. Niec, Franck J. Barrat, Lindsay Lief, Joseph C. Sun, Duygu Ucar, Steven Z. Josefowicz (corresponding)
- **Year:** 2023
- **Journal:** Cell, Vol. 186, Issue 18, pp. 3882–3902.e24
- **DOI:** https://doi.org/10.1016/j.cell.2023.07.019
- **PMID:** 37597510
- **PMCID:** PMC10638861
- **BibTeX key:** Cheong2023
- **Source:** web search (Europe PMC abstract); project-entity cross-references (topic:innate-immune-memory-trained-immunity-in-pais, h0003, h0004)
-->

## Key Contribution

Severe (but not mild) SARS-CoV-2 infection durably reprograms hematopoietic stem and progenitor cells (HSPCs) at the level of chromatin accessibility, producing an epigenomic imprint that persists for months to one year and is inherited by progeny monocytes — establishing a central (bone-marrow-level), antigen-independent mechanism by which a single severe infection can sustain a hyperinflammatory myeloid state long after viral clearance. Mechanistically, acute IL-6 — not viral antigen per se — is required to establish this HSPC imprint: IL-6 blockade in a mouse coronavirus model blocked the epigenomic reprogramming. This study provides the strongest available empirical anchor for the hypothesis that acute IL-6 drives durable HSPC-level trained immunity, making it the load-bearing primary paper for `question:0026` (IL-6/STAT3 → HSPC imprinting → hyperreactive monocytes) and for `topic:innate-immune-memory-trained-immunity-in-pais`.

## Methods

**Overall design.** Multimodal single-cell epigenomic and transcriptomic profiling of peripheral blood cells, including sorted HSPCs, from COVID-19 patients and controls, combined with a mouse mechanistic arm [UNVERIFIED: specific cell-isolation protocol and mouse coronavirus strain].

**Human observational arm.** Combined single-nucleus RNA-seq (snRNA-seq) and single-nucleus ATAC-seq (snATAC-seq) applied to PBMCs and/or sorted HSPC fractions from patients with severe/hospitalized COVID-19, mild COVID-19, convalescent individuals, and healthy controls. Longitudinal sampling was performed at multiple time points, including up to 12 months post-infection. The design is observational: no randomization or intervention in the human arm. Sample sizes are not reported in the abstract [UNVERIFIED: exact n per group and time point].

**Key epigenomic readouts.** ATAC-seq chromatin accessibility profiling of HSPC populations and progeny monocytes; single-cell gene expression (snRNA-seq); transcription factor motif enrichment and footprinting analysis. The study reports differential chromatin accessibility at inflammatory gene loci — open chromatin marks associated with trained/hyperreactive innate output.

**Mouse mechanistic arm.** Mouse coronavirus infection model with pharmacological IL-6 receptor blockade (or anti-IL-6 antibody treatment) administered during acute infection, followed by ATAC-seq on bone-marrow HSPCs post-infection. This arm tests IL-6 necessity, not just correlation: blocking IL-6 during the acute phase prevented the establishment of the HSPC epigenomic imprint observed in unblocked infected animals [UNVERIFIED: specific agent, dose, timing, and extent of blockade].

**Transmission test.** The study explicitly tracked whether the HSPC epigenomic program is conveyed to peripheral daughter monocytes through differentiation — a key design element establishing the central-to-peripheral inheritance of the trained phenotype.

## Key Findings

**HSPC epigenomic reprogramming after severe COVID-19.** Severe SARS-CoV-2 infection induces durable differential chromatin accessibility in HSPCs at inflammatory gene loci, with distinct transcription factor activities and altered regulation of inflammatory programs. This reprogramming is not observed (or is markedly attenuated) after mild COVID-19 — establishing a severity-dependent threshold for the imprinting event.

**Persistence to 12 months.** The HSPC epigenomic alterations persist for months to approximately one year following severe COVID-19. This duration exceeds the half-life of circulating monocytes (~1–7 days) by orders of magnitude, confirming that the imprint must reside in self-renewing progenitors to be maintained at this timescale.

**Transmission to progeny monocytes.** The altered HSPC epigenomic programs are conveyed, through differentiation, to peripheral innate immune cells (monocytes). This is the key step establishing that central HSPC training continuously supplies a hyperreactive myeloid output to the circulation — an antigen-independent, self-replenishing source of inflammatory cells.

**Durable myelopoiesis skewing.** Severe COVID-19 is associated with durable increases in myelopoiesis — a bias in HSPC fate decisions toward inflammatory myeloid output — that persists into convalescence. This myelopoiesis skewing is both a consequence of and a contributor to the inflammatory epigenomic state.

**IL-6 as mechanistically required imprinting signal (mouse arm).** In a mouse coronavirus model, pharmacological blockade of IL-6 signaling during acute infection prevented the establishment of the HSPC epigenomic imprint. This positions acute IL-6 — not virus-specific antigen recognition, not direct viral cytopathic effects — as the central driver that writes the bone-marrow-level epigenetic memory. The proposed signaling chain, consistent with the mechanistic arm, is: IL-6 → JAK1/2 → STAT3 → epigenetic remodeling at inflammatory gene promoters and enhancers in HSPCs [UNVERIFIED: whether STAT3 occupancy was directly demonstrated vs. inferred from IL-6-blockade rescue].

**Scope (what the study does not measure).** The paper is an acute-to-convalescent imprinting study. It characterizes the HSPC epigenomic state and its myeloid output through up to 12 months; it does not report correlations between HSPC imprinting depth and PAIS symptom burden, long-COVID diagnosis, or post-acute sequelae outcomes. The link from "durable myeloid imprint" to "PAIS symptoms" is mechanistically plausible but inferential and outside this paper's scope.

## Relevance

**`question:0026` (IL-6/STAT3 HSPC imprinting) — direct empirical anchor.** This paper is the primary empirical support for the claim that acute IL-6 drives durable HSPC central training after a PAIS-relevant infection. The IL-6-blockade mouse arm directly tests, and confirms, the mechanistic requirement. The human arm provides the observational evidence that this imprinting occurs in severe COVID-19 convalescents and persists at the timescales relevant to PAIS chronification.

**`topic:innate-immune-memory-trained-immunity-in-pais` — load-bearing anchor paper.** The topic was structured around this result as the most direct human epigenomic evidence for central trained immunity in a PAIS-relevant context. The antigen-independent-persistence hook — the core mechanistic claim of the topic — rests on the transmission of the HSPC imprint to continuously replenished monocytes independent of ongoing viral presence.

**`hypothesis:0004` (acute-severity threshold) — molecular candidate for the threshold mechanism.** HSPC central training via IL-6 is a plausible molecular substrate for why severe COVID-19 (high IL-6, high inflammatory insult) produces a qualitatively different long-term myeloid state than mild disease. However, Cheong2023 demonstrates this only in the severe/hospitalized tier — it does not establish whether or how the same mechanism operates in the mild-disease onset PAIS cases that constitute the majority of long COVID and ME/CFS. The severity-bounded nature of this finding narrows the threshold model: the relevant threshold may be "sufficient acute IL-6 to imprint HSPCs," not "infection per se." See `hypothesis:0004` Current Uncertainty for the existing treatment of this point (t095).

**`hypothesis:0003` (immune exhaustion feedback) — antigen-independent complement.** Trained HSPC imprinting provides a candidate antigen-independent maintenance mechanism for the inflammatory state that h0003 attributes to a T-cell exhaustion / persistent antigen loop. The two are not mutually exclusive: bone-marrow-derived trained monocytes can sustain innate inflammatory output even after adaptive exhaustion has blunted T-cell effector function. This supports the tolerance/training dual-compartment interpretation noted in h0003 (t095). The PAIS-specific causal evidence for this complement is absent — it is inferential from the Cheong2023 imprinting data and the Bomans2018 post-sepsis parallel.

**`question:0023` (cGAS-STING → IFN-I) and `question:0024` (NLRP3/inflammasome) — indirect connections.** HSPC-trained chromatin accessibility is elevated at broad categories of inflammatory gene loci; cGAS/STING pathway genes and NLRP3/pro-IL-1β promoters may be among the loci primed by HSPC training, making trained monocytes hyperresponsive to cytoplasmic DNA (cGAS-STING) and DAMP (NLRP3) signals. However, Cheong2023 does not specifically report priming at cGAS, STING, or NLRP3 loci, so these connections remain mechanistically inferred from the broader trained-immunity framework, not demonstrated in this paper [UNVERIFIED: whether differential ATAC-seq peaks at cGAS/STING/NLRP3 loci were reported].

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| HSPC epigenomic reprogramming (ATAC-seq differential accessibility) | Central trained immunity / bone-marrow-level imprint | Durable because in self-renewing progenitors, not in short-lived monocytes |
| Persistence to 12 months post-infection | Antigen-independent PAIS chronification mechanism | The imprint outlasts both viral clearance and monocyte turnover |
| Imprint transmitted to progeny monocytes | Continuously replenished hyperreactive myeloid output | Mechanistic link from progenitor training to circulating effector phenotype |
| Durable myelopoiesis skewing | Myeloid bias as a sustained-inflammation substrate | Inflammatory myeloid cell numbers elevated beyond normal homeostatic setpoint |
| IL-6 required (mouse blockade arm) | IL-6/STAT3 as imprinting signal (q0026) | Identifies the cytokine driver; opens intervention target at the acute-phase window |
| Severity-dependent (severe >> mild COVID-19) | Acute-severity threshold (h0004) | Bounds the imprinting mechanism to high-severity illness; consistent with h0004 but does not explain mild-disease PAIS |
| No PAIS symptom correlation | Inferential gap between myeloid imprint and PAIS outcomes | The causal-to-symptoms link is the key missing empirical step |

## Limitations

**1. Severity selection — the primary PAIS extrapolation caveat.** The HSPC epigenomic reprogramming was demonstrated in severe/hospitalized COVID-19 patients. Long COVID prevalence peaks after severe acute illness but the majority of long COVID and ME/CFS cases follow mild-to-moderate acute infection. Whether mild COVID-19 induces comparable central HSPC imprinting at clinically relevant depths is not established by this study. Extrapolating the trained-immunity mechanism from this paper to the broad PAIS population requires severity-stratified replication that has not yet been performed.

**2. Imprinting study, not PAIS outcome study.** The paper characterizes the epigenomic state of HSPCs and monocytes in COVID-19 convalescents. It does not report whether participants with deeper HSPC imprinting are more likely to develop long-COVID symptoms, or whether the imprint depth predicts PAIS duration or severity. The connection between the myeloid imprint and post-acute symptoms is inferential — supported by mechanistic plausibility and the parallel with sepsis-trained immunity, but not empirically demonstrated in this cohort.

**3. Human arm is observational.** The epigenomic profiling of human HSPCs and monocytes is cross-sectional or longitudinal observational data. Causality for the transmission chain (IL-6 → HSPC imprint → trained monocyte output → inflammation) is supported by the mouse mechanistic arm, but the human observational arm cannot by itself establish causal direction.

**4. Mouse-to-human mechanistic translation.** The IL-6 necessity result comes from a mouse coronavirus model, not from a human interventional study or a natural experiment (e.g., COVID-19 patients treated with tocilizumab during acute illness). The transferability of this specific mechanism to human SARS-CoV-2 infection requires verification via human cohorts that include acute-phase anti-IL-6 treatment (some ICU cohorts used tocilizumab; whether their HSPCs were profiled is not known from this paper). [UNVERIFIED: whether any human IL-6-blockade comparison was included.]

**5. Non-COVID PAIS generalizability.** The study is specific to coronavirus infection. Whether Borrelia, Coxiella burnetti, EBV, influenza, or other PAIS-defining infections produce comparable HSPC-level central training is entirely inferred from mechanistic analogy and the post-sepsis Bomans2018 parallel. The IL-6-dependence claim predicts that pathogens generating lower IL-6 peaks during acute infection would produce weaker HSPC imprinting — a testable corollary.

**6. No long-term fate or reversibility data beyond 12 months.** The study tracks HSPC imprinting up to 12 months. Whether the imprint spontaneously erodes beyond that timepoint, or whether it is maintained indefinitely, is unknown. The half-life of SARS-CoV-2-specific HSPC training is not established; β-glucan-induced murine trained immunity reverses over months, but COVID-specific human imprinting kinetics may differ.

## Model / Tool Availability

No computational tools, models, or public datasets are associated with this paper as research artifacts for reuse. Raw sequencing data are deposited [UNVERIFIED: GEO/dbGaP accession number]. The ATAC-seq and RNA-seq workflows are standard single-cell pipelines (e.g., STAR, Seurat/Signac or ArchR for snATAC), not novel software. No therapeutic agents or clinical instruments are released.

## Follow-up

**Papers to read next or already in project:**

- `paper:Mitroulis2018` (Cell) — β-glucan-driven HSPC training in mouse and human; establishes myelopoiesis modulation as the substrate for durable (not just short-lived peripheral) trained immunity; mechanistic foundation for Cheong2023's central-training interpretation.
- `paper:Bomans2018` (Frontiers Immunology) — post-sepsis parallel: sepsis induces HSPC-level central training alongside peripheral monocyte tolerance; the tolerance/training dual-compartment model that may apply to PAIS.
- `paper:Gu2023` (Frontiers Immunology) — synthesis review explicitly linking the Cheong2023 IL-6/STAT3-HSPC axis to long COVID inflammatory burden; read as secondary contextualization of this paper's claims.
- `paper:Humer2025` (Frontiers Immunology) — advocacy for trained immunity in ME/CFS; bridges Cheong2023 to non-COVID PAIS but is conceptual, not empirical.

**Questions this paper grounds or raises for the project:**

1. **`question:0026` grounding:** Does the IL-6/STAT3 → HSPC imprinting mechanism detected in severe COVID-19 generalize across PAIS triggers (Borrelia, Coxiella, EBV, influenza, dengue)? The IL-6 dependence predicts trigger-specific gradients in imprinting depth that could be tested in cross-PAIS biobank epigenomic studies.

2. **`question:0055` (HSPC imprinting depth as PAIS biomarker):** Can ATAC-seq or H3K4me3 ChIP-seq in peripheral blood HSPCs at 3–6 months post-infection predict who develops persistent PAIS vs full recovery? The Cheong2023 design profiles convalescents but does not link imprinting depth to symptom outcomes — this is the critical missing experiment.

3. **`question:0056` (pharmacological reversal):** Do epigenetic-reprogramming agents (BET inhibitors, DNMT inhibitors, statins, itaconate) reverse the COVID-specific HSPC imprint? If IL-6 is the initiating signal, does acute-phase IL-6 blockade (tocilizumab at the time of hospitalization) prevent subsequent PAIS, as this paper's mouse arm predicts?

4. **h0004 severity threshold — mechanistic test:** Is there a measurable IL-6 threshold during acute COVID-19 above which HSPC central training is established and below which it is not? If so, this provides a single molecular mediator connecting acute severity to PAIS risk — the most direct molecular substrate for the threshold model.
