---
id: paper:Shahbaz2025
kind: paper
title: Integrated immune, hormonal, and transcriptomic profiling reveals sex-specific
  dysregulation in long COVID patients with ME/CFS
status: active
ontology_terms:
- long COVID
- ME/CFS
- sex differences
- immune dysregulation
- sex hormones
- testosterone
- estradiol
- cortisol
- myelopoiesis
- regulatory T cells
- neuroinflammation
- gut barrier dysfunction
- transcriptomics
- post-acute infection syndrome
dataset_usage: []
source_refs:
- cite:Shahbaz2025
related:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
- question:0007-mechanism-of-female-predominance-in-pais
- question:0011-mitochondrial-basis-of-pem
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- question:0016-oxidative-stress-upstream-driver-of-bioenergetic
- topic:long-covid-immune-dysregulation
- topic:menopause-sex-hormones-and-pais-risk
created: '2026-06-21'
updated: '2026-06-21'
---
# Integrated immune, hormonal, and transcriptomic profiling reveals sex-specific dysregulation in long COVID patients with ME/CFS

- **Authors:** Shima Shahbaz, Mohammed Osman, Hussain Syed, Andrew Mason, Rhonda J. Rosychuk, Jan Willem Cohen Tervaert, Shokrollah Elahi (corresponding author)
- **Year:** 2025
- **Journal:** Cell Reports Medicine
- **DOI:** 10.1016/j.xcrm.2025.102449
- **PMID:** 41205594
- **PMCID:** PMC12711683
- **Article ID:** S2666-3791(25)00522-1
- **Published:** 2025-11-07
- **Institution:** University of Alberta, Edmonton, Canada
- **BibTeX key:** Shahbaz2025
- **Source:** Full-text XML via Europe PMC (PMC12711683), read 2026-06-21.

## Key Contribution

Multi-omic case-control study (n=140) characterizing sex-specific immune, hormonal, and transcriptomic differences in long COVID patients who met Canadian Consensus Criteria for ME/CFS, sampled approximately 12 months post-infection. The key finding is a strongly sex-dimorphic pattern: female long COVID (LCF) patients exhibit myelopoiesis shift, heightened pro-inflammatory cytokine responses, gut-barrier dysfunction markers, reduced testosterone, and neuroinflammatory transcriptomic signatures; male long COVID (LCM) patients show a milder, distinct inflammatory pattern with reduced estradiol. Both sexes show reduced cortisol. The study provides direct gonadal steroid measurements in a clinical long-COVID ME/CFS cohort, making it a second independent, non-UK Biobank corroboration that low non-dominant sex hormone (testosterone in females, estradiol in males) is associated with long COVID, consistent with the reproductive-stage immune-homeostasis framing in `hypothesis:0005`.

## Methods

**Design:** Observational cross-sectional case-control.

**Cohort:** 140 participants recruited at the Long COVID clinic, University of Alberta Hospital, Edmonton. Seventy-eight LC patients with ME/CFS (58 female [LCF], 20 male [LCM]); 62 recovered COVID-19 controls without persistent symptoms (42 female [RF], 20 male [RM]). Groups were age- and sex-matched (mean age ~49.5 years LC, ~46-48 years controls). Both LC and control groups were enrolled at approximately 12 months post-acute SARS-CoV-2 infection (371 ± 19 days LC; 370 ± 8.9 days R). The majority of participants (~60%) were infected with the original Wuhan strain; the remainder were primarily Delta or Omicron. Greater than 80% of the acute infections were mild (no hospitalization).

**Case definition:** ME/CFS by Canadian Consensus Criteria (CCC) and WHO criteria, using DePaul Symptom Questionnaire-PEM (DSQ-PEM) to assess post-exertional malaise. PEM required frequency and severity scores ≥2 for at least one of five core items.

**Exclusions:** Prior ME/CFS diagnosis unrelated to COVID-19; comorbidities with overlapping symptoms; chronic conditions (HIV, HCV, HBV, cancer, or other debilitating diseases unrelated to SARS-CoV-2). Menstrual cycle phase, menopausal status, and contraceptive use were NOT collected.

**Assays:**
- **Immune phenotyping:** Complete blood count (CBC); flow cytometry for T cell subsets (naive, central memory, effector memory, terminal effector CD4+/CD8+), Tregs (FOXP3+CD25+), CD39+ Tregs, CD71+ erythroid cells (CECs) in PBMCs.
- **Cytokine/chemokine profiling:** 6-plex and extended multiplex plasma analysis; ELISA. Included IL-1α, IL-6, IL-10, IL-12/IL-23p40, IL-16, IL-17a, IP-10/CXCL10, IFN-γ, TNF-α, TGF-β1, PlGF, MCP-1, MIP-1α, MDC, sFlt-1, VCAM-1, ICAM-1, CRP, SAA, eotaxin-3, VEGF-C, and others.
- **Gut-barrier biomarkers:** Plasma I-FABP, LPS-BP, sCD14, Gal-9, ARTN, Reelin.
- **6-plex hormone panel:** Testosterone, estradiol, progesterone, cortisol, growth hormone (GH), thyroid hormones (T3, T4).
- **Transcriptomics:** Bulk RNA-seq on PBMCs; DESeq2 for differential expression; pathway analysis (gene ontology and pathway enrichment); digital cytometry for in-silico cell composition; olfactory receptor (OR) gene expression assessed.

**Statistics:** Kruskal-Wallis with Dunn's multiple comparisons; two-tailed Mann-Whitney; Pearson correlations on standardized parameters.

## Key Findings

### Cohort and Clinical Severity
The female-to-male ratio in the LC group was 2.9:1 (74.4% female), consistent with prior reports from this group. Female LC patients showed significantly higher symptom burden than male LC patients across most domains: pain severity index (PSI), widespread pain index (WSP), cognitive impairment/brain fog, and post-exertional malaise (PEM). Sleep difficulties did not differ significantly between LCF and LCM.

### Immune Cell Phenotype (sex-dimorphic)
- **LCF only:** Increased absolute neutrophils and monocytes, decreased lymphocytes (CBC) — shift toward myelopoiesis at the expense of lymphopoiesis.
- **Both sexes:** Significant reduction in absolute naive CD4+ and CD8+ T cells; significant expansion of terminal effector (TE) CD4+ and CD8+ T cells (CD45RA+CCR7+CD95+CD28−), consistent with persistent T cell activation.
- **LCF only:** Significant reduction in Tregs (FOXP3+CD25+) in PBMCs; reduced frequency and intensity of CD39 expression on Tregs — implicating impaired immunoregulation.
- **LCF only:** Expanded CD71+ erythroid cells (CECs) in PBMCs; increased red cell distribution width (RDW) — dysregulated erythropoiesis. CECs are proposed to contribute to fatigue via ARTN secretion.

### Cytokines and Chemokines
- **LCF:** Broad pro-inflammatory elevation — IL-1α, IL-6, IL-12/IL-23p40, IP-10, IFN-γ, TNF-α, IL-17a, PlGF, MCP-1, MIP-1α, MDC, sFlt-1, VCAM-1, ICAM-1, CRP, SAA significantly elevated vs. RF. TGF-β1, IL-16, eotaxin-3, VEGF-C reduced. Dominant IFN-γ/IP-10 type-2 interferon signature.
- **LCM:** Narrower, more moderate pro-inflammatory elevation — IL-1α, IL-10, TNF-α, IL-17a, PlGF, MCP-1, MIP-1α, ICAM-1, sFlt-1, CRP, SAA elevated; only VEGF-C reduced. Elevated IL-10 suggests partially compensatory anti-inflammatory signaling. Dominant IL-1 signaling pattern, contrasting with LCF's IFN-γ pattern.

### Gut-Barrier Dysfunction
Significantly elevated plasma I-FABP, LPS-BP, and sCD14 in LCF vs. RF — indicative of intestinal injury and microbial translocation. These elevations were NOT observed in LCM vs. RM. Gal-9, ARTN, and Reelin were elevated in both sexes, with significantly higher levels in LCF than LCM or controls.

### Hormone Panel (6-plex)
- **Testosterone:** Significantly reduced in LCF vs. RF; no significant change in LCM vs. RM.
- **Estradiol:** Significantly reduced in LCM vs. RM; not significantly altered in LCF vs. RF.
- **Cortisol:** Significantly reduced in both LCF and LCM vs. their respective controls — the only hormone finding present in both sexes.
- **Growth hormone (GH):** Significantly elevated in LCF compared to all other groups.
- **Progesterone, T3, T4, BMI:** No significant differences between groups.

Testosterone levels in LCF showed moderate inverse correlations with IL-6, TNF-α, IL-1α, IFN-γ, MCP-1, IL-17a, and IP-10, and weak inverse correlations with Reelin, VCAM-1, and RDW. This suggests testosterone may have anti-inflammatory or neuroprotective roles inversely associated with the inflammatory burden in LCF patients.

### Transcriptomics (bulk RNA-seq, PBMCs)
- **LCF vs. RF top upregulated genes:** ZNF469 (>6.7-fold, neuronal differentiation), BRINP2 (>5.8-fold, neurological development), FEZF2 (>5.5-fold, deep-layer neuron development), HOXC12 (>5.1-fold, HSC renewal), ZFHX3 (>4.8-fold, neuronal differentiation and ECM remodeling), Reln (>4-fold, synaptic plasticity and cognitive function). Neuroinflammatory/cognitive-dysfunction signature predominates in LCF.
- **LCF top downregulated genes:** WDR62, NRXN2, GMPR, MUC12, SYCE1/SYCE1L, FOXO4.
- **LCM vs. RM:** Upregulation of FCγR1-BP, PALB2, DSCC1, EPSTI1, CASP5, MCC — immune responses, vascular function, cellular stress. Downregulation of genes related to immune dysregulation and endothelial dysfunction.
- **Sex hormone receptor expression (LCF):** Upregulation of ESR1, ESR2, ESRRG, AR (androgen receptor), NR3C1 (glucocorticoid receptor). Authors interpret this as heightened sensitivity to estrogen/androgen/glucocorticoid signaling in the setting of reduced circulating hormones.
- **Pathway enrichment (LCF upregulated):** Cell-cycle regulation, amino acid metabolism, protein synthesis, neuroinflammation, oxidative stress response, tissue repair.
- **Pathway enrichment (LCF downregulated):** Neutrophil degranulation, phagosome formation, integrin signaling, macrophage alternative activation, CD27 signaling, myelination, Rho-GTPase signaling, extracellular matrix degradation.
- **Pathway enrichment (LCM upregulated):** Oxidative phosphorylation and respiratory electron transport (enhanced mitochondrial activity), cellular stress response, immune activation, tissue repair.
- **Olfactory receptor (OR) gene upregulation:** Elevated in both sexes, more prominent in LCF; interpreted as ectopic sensory/neuroinflammatory dysregulation.

### Biomarker-Symptom Correlations
Correlations between plasma biomarkers and clinical symptom scores (PSI, WSP, cognitive impairment, PEM) were more pronounced in LCF than LCM. Elevated biomarkers in LCF correlate with greater symptom burden.

## Relevance

### To hypothesis:0005 (Reproductive-Stage Immune Homeostatic Margin)
This is a **second independent, non-UK Biobank, non-AlcaldeHerraiz corroboration** of low non-dominant sex hormone associated with long COVID. The hormone pattern — reduced testosterone in females, reduced estradiol in males — mirrors what has been reported in the UK Biobank cohort (AlcaldeHerraiz2025), but arises from an entirely different setting: a clinical case-control at the University of Alberta (Elahi group), using direct plasma hormone immunoassay rather than SHBG-inferred or questionnaire-based exposure. The inverse correlation between testosterone and inflammatory cytokines in LCF supports a mechanistic hypothesis that low testosterone contributes to dysregulated inflammation in female patients.

However, **reverse causation remains unresolved**: the study is cross-sectional, so it cannot determine whether low testosterone/estradiol precedes long COVID onset or is suppressed downstream by the chronic inflammatory/neuroendocrine state (HPG axis disruption, partial adrenal insufficiency, altered glucocorticoid metabolism, or negative feedback). Authors acknowledge this explicitly. This finding does NOT establish pre-infection causal direction.

**What it adds to t032 (corpus-independence gate for SHBG/sex-hormone prior):** This paper is author-independent (Elahi/Alberta vs. AlcaldeHerraiz/Barcelona) and data-source-independent (clinical immunology cohort vs. UK Biobank questionnaire). It measures **gonadal steroids directly**, not SHBG. It corroborates the directional pattern (reduced non-dominant sex hormone in LC) with a different instrument and population. This materially upgrades the sex-hormone signal from single-source background toward a replicated association, though it does not resolve causal direction and does not measure SHBG.

**What it does NOT provide for t036 (hormone-panel triangulation to positively test H0005):** The study is cross-sectional at ~12 months, so it captures the LC state but not the hormone trajectory from before infection through recovery. It lacks menopausal status, FSH, LH, AMH, and contraceptive use. It cannot test whether hormone levels mediate the path from reproductive stage to failed recovery — the precise positive-test criterion for H0005.

### To question:0007 (Mechanism of Female Predominance in PAIS)
The 2.9:1 female-to-male ratio in the LC ME/CFS cohort is consistent with published literature. The sex-dimorphic immune, hormonal, and transcriptomic profiles provide mechanistic specificity: the female excess may reflect myelopoiesis shift, Treg depletion, gut-barrier dysfunction, and neuroinflammatory transcriptional programming — not just reporting bias or case-definition artifact. However, menopausal status was not collected, so age-by-reproductive-stage decomposition is not possible.

### To question:0013 (Reproductive Stage and Failed Immune Recovery)
The paper confirms direct measurement of sex hormones in a long-COVID ME/CFS population with the low-non-dominant-sex-hormone signal, but explicitly lacks menstrual cycle phase and menopausal status. It provides supporting evidence that gonadal steroids are measurably perturbed in long COVID but cannot speak to whether a specific reproductive-stage transition increased risk.

### To question:0011 (Mitochondrial Basis of PEM) and question:0016 (Oxidative Stress)
In LCM patients, upregulation of oxidative phosphorylation and respiratory electron transport pathways suggests elevated mitochondrial metabolic demand — potentially consistent with cellular stress rather than impaired capacity. In LCF, upregulation of oxidative stress response and amino acid metabolism pathways may reflect cellular adaptation. These transcriptomic signatures are indirect and need cell-type resolution (bulk RNA-seq limitation) but add to the picture of metabolic dysregulation in ME/CFS.

### To hypothesis:0003 (Immune Exhaustion Feedback)
The expansion of terminal effector T cells (TE CD4+/CD8+) in both sexes, reduction in naive T cells, and Treg depletion in LCF, combined with the pro-inflammatory cytokine milieu, are consistent with persistent immune activation and failure to resolve — the immune exhaustion/sustained activation loop.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| ME/CFS by Canadian Consensus Criteria (CCC) | Post-acute infection syndrome (ME/CFS phenotype) | CCC is the most stringent widely used ME/CFS case definition; signals greater phenotypic specificity than WHO long-COVID alone |
| Myelopoiesis shift (↑ neutrophils/monocytes, ↓ lymphocytes) | Innate-adaptive imbalance; persistent innate activation | Female-predominant in this cohort |
| Treg depletion, reduced CD39+ Tregs | Immune exhaustion / failed resolution; impaired immunoregulation | Specifically in LCF; connects to hypothesis:0003 |
| TE CD4+/CD8+ expansion | T cell terminal differentiation / exhaustion | Both sexes; consistent with antigen-driven chronic activation |
| CD71+ erythroid cell (CEC) expansion | Stress hematopoiesis; immunosuppression mechanism | LCF-specific; proposed to secrete ARTN contributing to fatigue |
| Reduced testosterone (LCF), reduced estradiol (LCM) | Non-dominant sex hormone depletion | Key link to hypothesis:0005; cross-sectional only |
| Reduced cortisol (both sexes) | HPA axis dysregulation | Both sexes; HPG axis disruption not distinguished from adrenal insufficiency or altered feedback |
| Gut-barrier dysfunction (I-FABP, LPS-BP, sCD14) | Microbial translocation; gut-barrier integrity | LCF-predominant; connects to microbial dysbiosis mechanism |
| Neuroinflammatory transcriptional signature (LCF) | Neuroinflammation / cognitive dysfunction | Brain fog mechanistic plausibility |
| Upregulated sex hormone receptors (ESR1, ESR2, AR, NR3C1 in LCF) | Compensatory receptor upregulation under hormone depletion | Suggests tissue sensitivity may be adaptive; metabolic and immune consequences |

## Limitations

1. **Cross-sectional design:** No pre-infection baseline; cannot determine causal direction for hormone changes. Reverse causation (LC suppressing HPG axis via chronic inflammation, antigen persistence, or altered HPA/HPG feedback) is entirely plausible and unresolved.
2. **Missing reproductive covariates:** Menstrual cycle phase, menopausal status, and contraceptive use were NOT collected. This is explicitly flagged by the authors. Without these, sex-hormone findings cannot be attributed to pre-existing reproductive-stage differences vs. LC-induced hormonal disruption.
3. **Sex imbalance:** 58 female vs. 20 male LC patients; 42 female vs. 20 male controls. Unequal sex-group sizes reduce power for male-specific analyses; DESeq2 used to adjust for transcriptomic analyses, but immunological comparisons in LCM remain underpowered relative to LCF.
4. **SHBG not measured:** The study measures gonadal steroid hormones directly but does NOT measure sex hormone binding globulin (SHBG), which is the mediator-specific exposure tested in the AlcaldeHerraiz/UK Biobank work. The two datasets are therefore complementary but not directly comparable on the SHBG-protection hypothesis.
5. **Bulk RNA-seq:** Cannot resolve cell-type-specific transcriptional changes. Neuroinflammatory signatures from PBMCs may reflect circulating immune cell gene expression rather than central nervous system processes.
6. **No PEM-stratified vs. non-PEM LC comparison:** All patients met ME/CFS criteria including PEM; there is no comparison arm of long COVID without PEM, limiting ability to isolate PEM-specific biology.
7. **Single time point (~12 months post-infection):** Immune and hormone profiles at one time point cannot speak to trajectory (worsening, plateau, or partial recovery).
8. **Predominantly mild acute infection:** >80% mild acute COVID reduces confounding by acute severity but limits generalizability to post-hospitalization cohorts.
9. **Strain heterogeneity:** ~60% Wuhan, remainder Delta/Omicron — potential strain-specific immune effects not stratified.
10. **Exclusion of menopause confounders not confirmed:** Because menopausal status was not collected, the testosterone reduction in females could partly reflect higher average menopausal prevalence in the LC group (though mean ages were matched at ~49.5 years).

## Model / Tool Availability

No model or tool released. RNA-seq data are stated to be available via a data and code availability statement (specific repository not specified in the extracted text). [UNVERIFIED: confirm GEO/SRA accession number from full paper methods.]

## Follow-up

### Immediate reads
- AlcaldeHerraiz2025 — UK Biobank SHBG/sex-hormone x long COVID (the single-source prior this paper independently corroborates directionally).
- Shah2025 — sex as a long-COVID risk factor in large registry/biobank (no hormone measurement; complementary).
- Averyanova2022 — mechanistic review of sex hormones and immune modulation (provides mechanistic context for testosterone-cytokine inverse correlations).
- Klein2023 — sex differences in acute COVID immune responses (prior work this paper builds on for the sex-dimorphic immune signature).

### Open questions raised
- **Does the testosterone depletion in LCF reflect pre-infection vulnerability (a constitutional or reproductive-stage state) or downstream suppression by chronic inflammation?** A longitudinal design with pre- and post-infection sampling is required to answer this.
- **What is the menopausal status distribution in LCF vs. RF?** At mean age 49.5 years, a substantial fraction of female participants may be peri- or postmenopausal. An FSH/AMH-stratified analysis or self-reported menopausal status would substantially sharpen the interpretation.
- **Is the Treg depletion mechanistically upstream or downstream of low testosterone in LCF?** The inverse testosterone-IL-6/TNF-α correlation is suggestive but correlational only.
- **Do the neuroinflammatory transcriptomic findings (ZNF469, BRINP2, Reln upregulation) reflect activation of circulating monocytes/lymphocytes or contamination with brain-derived extracellular vesicles?** Single-cell RNA-seq of PBMCs or direct CNS sampling would be needed.
- **Can the hormone-immune correlations be reproduced in non-ME/CFS long COVID?** All patients met CCC; the relevance to the broader LC population without PEM is unknown.
