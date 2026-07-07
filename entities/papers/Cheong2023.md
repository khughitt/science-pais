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
dataset_usage:
- id: geo:GSE196990
  role: reanalysis-candidate
  notes: "snRNA/ATAC-seq (PBMC-PIE workflow) across 168 enrolled participants — severe
    COVID-19 convalescent (Early + Late), nonCoV critically ill, healthy; raw + processed
    data deposited; analysis code at Zenodo 10.5281/zenodo.8097411"
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
upgrade_notes: "2026-07-07: upgraded from abstract-only to PDF full text (PMC author
  manuscript). All six [UNVERIFIED] markers resolved. cGAS-STING and NLRP3 peak links
  explicitly dropped (not in paper). STAT3 occupancy verdict: motif-accessibility-inferred,
  not ChIP/CUT&RUN. Human tocilizumab comparison confirmed in cohort. Mouse strain
  MHV-1 / female A/J confirmed. GEO GSE196990 recorded."
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
- **Source:** PDF full text (PMC author manuscript / NIHMS, read 2026-07-07); project-entity cross-references (topic:innate-immune-memory-trained-immunity-in-pais, h0003, h0004)
-->

## Key Contribution

Severe SARS-CoV-2 infection durably reprograms hematopoietic stem and progenitor cells (HSPCs) at the level of chromatin accessibility, producing an epigenomic imprint that persists for months to one year and is inherited by progeny monocytes — establishing a central (bone-marrow-level), antigen-independent mechanism by which a single severe infection can sustain a hyperinflammatory myeloid state long after viral clearance. Mild COVID-19 samples were collected but excluded from differential analyses; the authors explicitly note that whether mild disease induces similar programs is an open question. Mechanistically, acute IL-6 — not viral antigen per se — is required to establish this HSPC imprint, demonstrated in a mouse coronavirus model (MHV-1 / A/J, anti-IL-6R blockade) and in a human quasi-natural experiment (Tocilizumab-treated vs. untreated patients during the Spring 2020 NYC surge). This study provides the strongest available empirical anchor for the hypothesis that acute IL-6 drives durable HSPC-level trained immunity, making it the load-bearing primary paper for `question:0026` (IL-6/STAT3 → HSPC imprinting → hyperreactive monocytes) and for `topic:innate-immune-memory-trained-immunity-in-pais`.

## Methods

**Overall design.** Multimodal single-cell epigenomic and transcriptomic profiling of peripheral blood cells, including sorted HSPCs, from COVID-19 patients and controls, combined with a mouse mechanistic arm. The key methodological innovation is the PBMC Progenitor Input Enrichment (PBMC-PIE) platform: circulating CD34+ HSPCs (~0.05% of PBMC) are enriched ~200-fold by CD34 magnetic bead selection, then FACS-sorted and mixed back with bulk PBMC at 1:5–1:20 ratios for combined snRNA/ATAC-seq, giving simultaneous access to rare HSPCs and their myeloid progeny from standard blood draws without bone-marrow biopsy. Paired BM and peripheral blood HSPC samples from the same donors confirmed that circulating CD34+ cells accurately capture the transcriptomic and epigenomic diversity of bone-marrow HSPC subtypes. Mouse model: female A/J mice (6 weeks old, Jackson Laboratories) infected intranasally with murine hepatitis virus 1 (MHV-1, 5,000 PFU) — NOT a mouse-adapted SARS-CoV-2; MHV-1 in A/J was chosen because it mimics many aspects of severe COVID-19 and convalescence in humans (ref 68 in paper).

**Human observational arm.** Combined snRNA-seq and snATAC-seq (Multiome 10x Genomics) applied to PBMC-PIE samples from four clinical groups enrolled at Weill Cornell Medicine/NYP Hospital (March 2020–March 2021): (1) healthy volunteer donors, (2) recovered severe COVID-19 (WHO score 6–7, requiring ICU/mechanical ventilation) partitioned into Early convalescent (2–4 months post-admission) and Late convalescent (4–12 months post-admission), and (3) recovered non-COVID-19 critically ill (nonCoV, required ICU). Total enrolled: **n=168 participants**. Main ATAC-seq analysis cohort: **n=57** across the four groups (Healthy, nonCoV, Early, Late). Multiome cohort: **n=30** study participants; differential accessibility analysis used n=70 (CD14+ monocytes) and n=49 (CD34+ HSPC) good-quality bulk/pseudo-bulk samples. Mild COVID-19 samples were collected but **excluded from differential analyses** — the per-group Ns within the severe convalescent groups are in Table S1. Participants were infected with 614D/614G variants, enrolled prior to COVID-19 vaccine rollout. The design is observational in the human arm; no randomization was performed (but see tocilizumab quasi-natural-experiment below).

**Key epigenomic readouts.** ATAC-seq chromatin accessibility profiling of HSPC populations and progeny monocytes; single-cell gene expression (snRNA-seq); transcription factor motif enrichment and footprinting analysis. The study reports differential chromatin accessibility at inflammatory gene loci — open chromatin marks associated with trained/hyperreactive innate output.

**Mouse mechanistic arm.** Female A/J mice infected with MHV-1 (5,000 PFU intranasal on day 0). IL-6 receptor blockade: mouse anti-IL-6R blocking antibody (InVivoMab, 2 µg/µL, 100 µL total) injected on day 0 together with virus. Mice cleared virus within two weeks and regained weight by day 30. At day 30 post-infection, bone marrow was harvested (tibia + femur), lineage-depleted, and profiled by snRNA/ATAC-seq (Multiome 10x). Three groups: naïve mice, MHV-1-recovered mice (untreated), MHV-1-recovered mice that received anti-IL-6R. This arm tests IL-6 necessity, not just correlation: anti-IL-6R treatment during the acute phase significantly reduced GMP frequencies and STAT3 motif accessibility in bone-marrow HSC/MPP at day 30, preventing the epigenomic imprint observed in untreated recovered animals.

**Human IL-6 blockade comparison (quasi-natural experiment).** A subset of Late-group severe COVID-19 participants received Tocilizumab (anti-IL-6R) during acute hospitalization at NYP Hospital during the Spring/Summer 2020 NYC surge. Because Tocilizumab administration was near-random at that time (no discernible clinical or demographic differences between treated and untreated participants per Table S1), the study exploited this as a quasi-natural experiment. Late-group untreated patients had significantly higher GMP frequencies (the key HSPC imprinting readout) at 4–12 months compared to both healthy controls and the tocilizumab-treated Late group. This provides direct human evidence — not only mouse evidence — that acute-phase IL-6R signaling is required to establish the durable HSPC imprint.

**Transmission test.** The study explicitly tracked whether the HSPC epigenomic program is conveyed to peripheral daughter monocytes through differentiation — a key design element establishing the central-to-peripheral inheritance of the trained phenotype.

## Key Findings

**HSPC epigenomic reprogramming after severe COVID-19.** Severe SARS-CoV-2 infection induces durable differential chromatin accessibility in HSPCs at inflammatory gene loci, with distinct transcription factor activities and altered regulation of inflammatory programs. This reprogramming is not observed (or is markedly attenuated) after mild COVID-19 — establishing a severity-dependent threshold for the imprinting event.

**Persistence to 12 months.** The HSPC epigenomic alterations persist for months to approximately one year following severe COVID-19. This duration exceeds the half-life of circulating monocytes (~1–7 days) by orders of magnitude, confirming that the imprint must reside in self-renewing progenitors to be maintained at this timescale.

**Transmission to progeny monocytes.** The altered HSPC epigenomic programs are conveyed, through differentiation, to peripheral innate immune cells (monocytes). This is the key step establishing that central HSPC training continuously supplies a hyperreactive myeloid output to the circulation — an antigen-independent, self-replenishing source of inflammatory cells.

**Durable myelopoiesis skewing.** Severe COVID-19 is associated with durable increases in myelopoiesis — a bias in HSPC fate decisions toward inflammatory myeloid output — that persists into convalescence. This myelopoiesis skewing is both a consequence of and a contributor to the inflammatory epigenomic state.

**IL-6 as mechanistically required imprinting signal (mouse + human arms).** In the MHV-1 mouse model, anti-IL-6R treatment on day 0 prevented the HSPC epigenomic imprint at day 30 (reduced GMP frequencies, reduced STAT3/IRF/CEBP motif accessibility in HSC/MPP). In the human cohort, Tocilizumab-treated patients showed significantly lower Late-group GMP frequencies than untreated patients (quasi-natural experiment). This positions acute IL-6 — not virus-specific antigen recognition — as the central driver of bone-marrow-level epigenetic memory.

**STAT3 occupancy — motif-accessibility-inferred, not directly demonstrated.** STAT3 involvement is supported by chromatin accessibility at STAT3 motifs measured by two methods: (1) chromVAR chromatin-variation scores (per-cell TF motif activity from snATAC-seq) and (2) HINT-based TF footprinting (genome-wide ATAC-seq read-depth profiles at motif instances). Both showed elevated STAT3 motif accessibility in post-COVID-19 HSPC and monocytes, reduced by anti-IL-6R in both humans and mice. Direct STAT3 protein occupancy assays (ChIP-seq, CUT&RUN, or CUT&TAG) were NOT performed. The IL-6 → STAT3 → epigenetic remodeling chain is inferred from motif accessibility plus functional rescue, not confirmed by a direct STAT3-binding assay. For q0026 purposes: the IL-6 requirement is demonstrated; STAT3 as the proximal transcriptional effector is strongly supported but not occupancy-confirmed.

**Scope (what the study does not measure).** The paper is an acute-to-convalescent imprinting study. It characterizes the HSPC epigenomic state and its myeloid output through up to 12 months; it does not report correlations between HSPC imprinting depth and PAIS symptom burden, long-COVID diagnosis, or post-acute sequelae outcomes. The link from "durable myeloid imprint" to "PAIS symptoms" is mechanistically plausible but inferential and outside this paper's scope.

## Relevance

**`question:0026` (IL-6/STAT3 HSPC imprinting) — direct empirical anchor.** This paper is the primary empirical support for the claim that acute IL-6 drives durable HSPC central training after a PAIS-relevant infection. IL-6 necessity is established by BOTH the MHV-1 mouse anti-IL-6R arm AND the human tocilizumab quasi-natural experiment — making this a two-species, convergent demonstration. The STAT3 link specifically is inferred from ATAC-seq motif accessibility (chromVAR + HINT footprinting) and functional rescue, not from a direct ChIP-seq/CUT&RUN occupancy assay. Strength of claim for q0026: IL-6 requirement = demonstrated (human + mouse, functional rescue); STAT3 as proximal effector = strongly supported (motif accessibility + anti-IL-6R attenuation) but not protein-occupancy confirmed.

**`topic:innate-immune-memory-trained-immunity-in-pais` — load-bearing anchor paper.** The topic was structured around this result as the most direct human epigenomic evidence for central trained immunity in a PAIS-relevant context. The antigen-independent-persistence hook — the core mechanistic claim of the topic — rests on the transmission of the HSPC imprint to continuously replenished monocytes independent of ongoing viral presence.

**`hypothesis:0004` (acute-severity threshold) — molecular candidate for the threshold mechanism.** HSPC central training via IL-6 is a plausible molecular substrate for why severe COVID-19 (high IL-6, high inflammatory insult) produces a qualitatively different long-term myeloid state than mild disease. However, Cheong2023 demonstrates this only in the severe/hospitalized tier — it does not establish whether or how the same mechanism operates in the mild-disease onset PAIS cases that constitute the majority of long COVID and ME/CFS. The severity-bounded nature of this finding narrows the threshold model: the relevant threshold may be "sufficient acute IL-6 to imprint HSPCs," not "infection per se." See `hypothesis:0004` Current Uncertainty for the existing treatment of this point (t095).

**`hypothesis:0003` (immune exhaustion feedback) — antigen-independent complement.** Trained HSPC imprinting provides a candidate antigen-independent maintenance mechanism for the inflammatory state that h0003 attributes to a T-cell exhaustion / persistent antigen loop. The two are not mutually exclusive: bone-marrow-derived trained monocytes can sustain innate inflammatory output even after adaptive exhaustion has blunted T-cell effector function. This supports the tolerance/training dual-compartment interpretation noted in h0003 (t095). The PAIS-specific causal evidence for this complement is absent — it is inferential from the Cheong2023 imprinting data and the Bomans2018 post-sepsis parallel.

**`question:0023` (cGAS-STING → IFN-I) and `question:0024` (NLRP3/inflammasome) — NOT supported by this paper's data (cross-links dropped).** The full text was examined for differential ATAC-seq accessibility peaks or pathway enrichment at cGAS (*MB21D1*), *STING1*, *NLRP3*, *CASP1*, or *GSDMD* loci. None were reported. The cGAS-STING (Domizio 2022, Nature) and inflammasome (Sefik 2022, Nature) papers are cited in the introduction as background references for acute COVID-19 immunopathology, but play no role in the paper's own results, ATAC-seq peak clusters, GO enrichments, or TF activity analyses. The GO enrichment terms reported are "myeloid cell activation," "cytokine production," "differentiation," and "cell migration" — not innate-sensing pathway terms. **Cheong2023 should not be listed as a supporting reference for q0023 or q0024.** These cross-links rest entirely on the general trained-immunity framework; a separate paper that directly profiles cGAS/STING or NLRP3 locus accessibility in post-COVID-19 trained monocytes would be needed to ground them.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| HSPC epigenomic reprogramming (ATAC-seq differential accessibility) | Central trained immunity / bone-marrow-level imprint | Durable because in self-renewing progenitors, not in short-lived monocytes |
| Persistence to 12 months post-infection | Antigen-independent PAIS chronification mechanism | The imprint outlasts both viral clearance and monocyte turnover |
| Imprint transmitted to progeny monocytes | Continuously replenished hyperreactive myeloid output | Mechanistic link from progenitor training to circulating effector phenotype |
| Durable myelopoiesis skewing | Myeloid bias as a sustained-inflammation substrate | Inflammatory myeloid cell numbers elevated beyond normal homeostatic setpoint |
| IL-6 required (MHV-1 mouse anti-IL-6R arm + human tocilizumab quasi-natural experiment) | IL-6/STAT3 as imprinting signal (q0026) | Two-species convergent demonstration; STAT3 inferred via motif accessibility, not ChIP/CUT&RUN; opens acute-phase intervention window |
| Severe-COVID-19-specific design (mild samples collected but excluded from differential analysis) | Acute-severity threshold (h0004) | Imprint demonstrated only in severe/ICU tier; whether mild disease produces comparable imprinting is an explicit open question acknowledged by the authors |
| No PAIS symptom correlation | Inferential gap between myeloid imprint and PAIS outcomes | The causal-to-symptoms link is the key missing empirical step |

## Limitations

**1. Severity selection — the primary PAIS extrapolation caveat.** The HSPC epigenomic reprogramming was demonstrated in severe/hospitalized COVID-19 patients (WHO score 6–7, ICU/mechanical-ventilation). Mild COVID-19 samples were collected but explicitly excluded from differential analyses. The authors themselves flag "understanding if mild COVID-19 induces similar programs is an important topic for future work" (Discussion). Long COVID prevalence peaks after severe acute illness, but the majority of long COVID and ME/CFS cases follow mild-to-moderate acute infection — precisely the severity tier this paper does not characterize. Whether mild COVID-19 induces comparable central HSPC imprinting is not established here, and a direct severe-vs-mild epigenomic comparison has not been published. Extrapolating the trained-immunity mechanism to the broad PAIS population requires severity-stratified replication.

**2. Imprinting study, not PAIS outcome study.** The paper characterizes the epigenomic state of HSPCs and monocytes in COVID-19 convalescents. It does not report whether participants with deeper HSPC imprinting are more likely to develop long-COVID symptoms, or whether the imprint depth predicts PAIS duration or severity. The connection between the myeloid imprint and post-acute symptoms is inferential — supported by mechanistic plausibility and the parallel with sepsis-trained immunity, but not empirically demonstrated in this cohort.

**3. Human arm is observational.** The epigenomic profiling of human HSPCs and monocytes is cross-sectional or longitudinal observational data. Causality for the transmission chain (IL-6 → HSPC imprint → trained monocyte output → inflammation) is supported by the mouse mechanistic arm, but the human observational arm cannot by itself establish causal direction.

**4. Mouse-to-human mechanistic translation — substantially bridged by in-cohort tocilizumab comparison.** The paper includes BOTH the MHV-1 mouse arm AND a human quasi-natural experiment: during the Spring/Summer 2020 NYC surge, Tocilizumab administration was near-random and the study compared Late-group HSPC phenotypes between treated and untreated patients. Tocilizumab-treated patients had significantly lower GMP frequencies at 4–12 months, with no discernible confounding clinical or demographic differences (Table S1). This two-species convergent demonstration substantially bridges the mouse-to-human gap for the IL-6-requirement claim. Residual limitation: GMP frequency is a surrogate biomarker, not a PAIS-symptom endpoint; the Tocilizumab sub-group Ns within the Late group are small; and this is not a randomized trial. Whether acute-phase IL-6 blockade reduces subsequent PAIS incidence in practice remains unproven.

**5. Non-COVID PAIS generalizability.** The study is specific to coronavirus infection. Whether Borrelia, Coxiella burnetti, EBV, influenza, or other PAIS-defining infections produce comparable HSPC-level central training is entirely inferred from mechanistic analogy and the post-sepsis Bomans2018 parallel. The IL-6-dependence claim predicts that pathogens generating lower IL-6 peaks during acute infection would produce weaker HSPC imprinting — a testable corollary.

**6. No long-term fate or reversibility data beyond 12 months.** The study tracks HSPC imprinting up to 12 months. Whether the imprint spontaneously erodes beyond that timepoint, or whether it is maintained indefinitely, is unknown. The half-life of SARS-CoV-2-specific HSPC training is not established; β-glucan-induced murine trained immunity reverses over months, but COVID-specific human imprinting kinetics may differ.

## Model / Tool Availability

**Data:** All raw and processed data are deposited at GEO under accession **GSE196990**. This is a reanalysis candidate (snRNA/ATAC-seq across 168 enrolled participants, four clinical groups) — see `dataset_usage` frontmatter.

**Code:** Analysis scripts at GitHub (https://github.com/sharmasiddhartha231/Final_Covid19_Scripts) and archived at Zenodo (10.5281/zenodo.8097411). Snakemake used for bulk RNA-seq workflow (STAR + DESeq2).

**Interactive viewer:** Multiome data queryable at https://buenrostlab.shinyapps.io/covid_myeloid/ (myeloid cells), covid_pbmc, and covid_hspc shiny apps.

**Supplemental data:** Mendeley Data (10.17632/pfwyrmffdp.1).

**Novel software:** The PBMC-PIE workflow (PBMC Progenitor Input Enrichment for CD34+ HSPC from peripheral blood) is described in detail and could be applied to other disease cohorts without bone-marrow biopsy. No new software packages are released. Standard pipelines used: Cell Ranger ARC (Multiome), Seurat/Signac, ArchR, HOMER, HINT (footprinting), cinaR (differential accessibility), Snakemake.

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
