---
id: paper:George2022
type: paper
title: A persistent neutrophil-associated immune signature characterizes post-COVID-19
  pulmonary sequelae
status: active
ontology_terms:
  - post-acute sequelae of SARS-CoV-2 infection
  - neutrophil extracellular traps
  - pulmonary fibrosis
  - interstitial lung disease
  - plasma proteomics
  - neutrophil-associated inflammation
  - type I interferon signaling
  - phosphoproteomics
dataset_usage: []
datasets: []
source_refs:
- cite:George2022
related:
- paper:Cruz2025
- paper:Vreeman2025
- paper:Ryan2022
- paper:Parotto2023
created: '2026-06-11'
updated: '2026-06-11'
---
# A persistent neutrophil-associated immune signature characterizes post-COVID-19 pulmonary sequelae

- **Authors:** Peter M. George, Anna Reed, Sujal R. Desai, Anand Devaraj, Tasnim Shahridan Faiez, Sarah Laverty, Amama Kanwal, Camille Esneau, Michael K.C. Liu, Faisal Kamal, William D.-C. Man, Sundeep Kaul, Suveer Singh, Georgia Lamb, Fatima K. Faizi, Michael Schuliga, Jane Read, Thomas Burgoyne, Andreia L. Pinto, Jake Micallef, Emilie Bauwens, Julie Candiracci, Mhammed Bougoussa, Marielle Herzog, Lavanya Raman, Blerina Ahmetaj-Shala, Stuart Turville, Anupriya Aggarwal, Hugo A. Farne, Alessia Dalla Pria, Andrew D. Aswani, Francesca Patella, Weronika E. Borek, Jane A. Mitchell, Nathan W. Bartlett, Arran Dokal, Xiao-Ning Xu, Peter Kelleher, Anand Shah, Aran Singanayagam
- **Year:** 2022
- **Journal:** Science Translational Medicine, vol. 14, no. 671, p. eabo5795
- **DOI:** 10.1126/scitranslmed.abo5795
- **BibTeX key:** George2022
- **Source:** PDF

## Key Contribution

This study identifies a persistent, systemic and mucosal neutrophil-associated inflammatory immune signature in individuals who develop post-COVID-19 interstitial lung changes (ILC), present at 3-6 months after hospital discharge, characterized by up-regulated plasma chemokines, proteases, and markers of neutrophil extracellular trap (NET) formation. Using a multiomic approach (plasma proteomics, nasal transcriptomics, phosphoproteomics, and in vitro mechanistic experiments), the study demonstrates that the neutrophil/NET axis — rather than direct SARS-CoV-2 viral cytopathic effect — is the likely driver of pulmonary fibrogenesis, and that at 12 months post-infection, a substantial subset of individuals has not yet achieved full radiological and functional normalization, instantiating the PAIS frame of failed homeostatic recovery.

## Methods

**Study design:** Prospective longitudinal cohort (visit 1 at 3-6 months post-discharge, visit 2 at ~12 months post-discharge) at Royal Brompton and Harefield NHS Foundation Trust and associated NHS centers, UK.

**Cohorts:**
- 46 individuals with severe COVID-19 (hospitalized), sampled at 3-6 months post-discharge (mean 129 days). Clinical phenotyping, chest CT, lung function testing, blood and nasal sampling at visit 1.
- 18 individuals with mild (non-hospitalized) COVID-19 and 17 healthy uninfected controls for comparison.
- Within the severe group: 26/46 (56.2%) had persistent interstitial lung changes (ILC) on CT; 20/46 had complete radiographic resolution.

**Multi-omic platforms:**
- **Plasma proteomics:** Olink proteomics platform (proximity extension assay), 184 unique proteins, all 46 severe + 18 mild + 17 healthy controls.
- **Nasal transcriptomics:** NanoString nCounter Multiplex (>850 immune response genes; table S3); 16 ILC and 10 resolved individuals with sufficient RNA quality.
- **PBMC phosphoproteomics:** 5,934 phosphopeptides; subgroup of 9 ILC and 8 resolved individuals.
- **Blood counts and ELISAs:** Total neutrophil counts, myeloperoxidase (MPO), neutrophil elastase; H3R8 citrullinated nucleosomes (NET marker), H3.1 total nucleosomes.
- **Lung function:** % predicted FVC and TLCO (carbon monoxide diffusion capacity).
- **Radiology:** CT interstitial changes quantified as % radiographic disease extent.

**In vitro:** Primary alveolar epithelial cells (AECs) differentiated at air-liquid interface infected with SARS-CoV-2 (alpha variant, MOI 0.1); separately, A549 epithelial cells treated with purified NETs or medium control.

**Statistics:** Differential protein/gene expression via linear mixed models with Benjamini-Hochberg correction (5% FDR); Spearman rank correlation for continuous associations; Mann-Whitney U test for group comparisons; KSEA (kinase-substrate enrichment analysis) for phosphoproteomics; String-DB for pathway enrichment.

## Key Findings

**Systemic immune activation persists after severe COVID-19 (all severe vs. mild/healthy):**
- 63 proteins significantly altered in severe vs. mild/healthy at 3-6 months (5% FDR); 59 up-regulated, 4 down-regulated.
- Top up-regulated proteins in severe COVID-19: CXCL5, hexamethylene bisacetamide-inducible protein, oncostatin M, eukaryotic translation initiation factor 4E-binding protein 1.
- Pathway enrichment: "immune system process," "immune response," "cytokine-mediated signaling pathway."

**Neutrophil-associated proinflammatory signature distinguishes post-COVID ILC from resolution:**
- 30 proteins significantly different between ILC and resolved groups (5% FDR); 26 up-regulated in ILC.
- Top up-regulated proteins: IL-17C, EN-RAGE, CCL20, CCL25, TNF.
- Pathway enrichment by GO: "neutrophil chemotaxis" was the top pathway (highest −log₁₀ FDR).
- IL-17C was the only plasma protein independently associated with ILC in multivariable analysis: odds ratio 3.72 (95% CI 1.20–16.84; P = 0.0403), adjusting for age, BMI, disease severity, and ventilator requirement.
- CXCL1 and CXCL8 negatively correlated with % FVC (r = −0.33, P = 0.048; r = −0.41, P = 0.04 respectively); CXCL9 negatively correlated with % TLCO.
- CXCL8 and IL-18R1 positively correlated with radiographic disease extent (r = 0.41, P = 0.038; r = 0.54, P = 0.0042 respectively).

**Neutrophilia, protease release, and NET markers are elevated in ILC individuals:**
- Total blood neutrophil counts significantly higher in ILC vs. resolved (p < 0.05).
- Plasma myeloperoxidase (MPO) significantly elevated in ILC; positively correlated with radiographic disease extent (r = 0.53, P = 0.0048) and negatively with % TLCO (r = −0.40, P = 0.04).
- H3R8 citrullinated nucleosomes (NET marker) significantly elevated in ILC vs. resolved (p < 0.05). Total H3.1 nucleosomes not significantly different, indicating specificity to citrullination.

**Nasal transcriptomic signature confirms mucosal neutrophilic and antiviral inflammation:**
- 53 genes up-regulated in ILC vs. resolved nasal samples (5% FDR).
- Top up-regulated genes: antiviral defense (GBP5, IFIT2, OASL) and neutrophilic/inflammasome pathways (CXCL8, CXCR2, IL1R2, NLRP3).
- Pathway enrichment: "cytokine-mediated signaling," "cellular response to type I interferon," "type I interferon signaling," "neutrophil chemotaxis."
- Cellular deconvolution revealed significant enrichment of neutrophils (but not other cell types) in ILC nasal samples.
- Nasal IL17D expression correlated positively with radiographic disease extent (r = 0.62, P = 0.010) and negatively with % TLCO (r = −0.65, P = 0.02).

**Phosphoproteomic kinase network reveals proliferative/proinflammatory kinases in ILC PBMCs:**
- 30 phosphopeptides enriched in ILC (log OR > 4.6, 99% probability); 16 enriched in resolved.
- Key kinases enriched in ILC network: CDK2, PRKCI, IRAK1, MEK1, JNK2 (downstream of type I IFN and TNF receptors; roles in neutrophil migration, inflammasome, TLR signaling, and proinflammatory cytokine responses).
- Resolved individuals' kinase network enriched for diverse homeostatic/metabolic kinases (phosphorylase B kinase gamma; liver/testis isoform), consistent with return to steady state.

**NET administration (not direct SARS-CoV-2 infection) drives fibrogenic gene expression in vitro:**
- Primary AECs infected with SARS-CoV-2 for 7 days: induced IFNα/2/3 and antiviral response, but did NOT induce fibrogenic markers COL1A1 or FN1; ACTA2 was suppressed.
- A549 cells treated with purified NETs: up-regulated FN1 and VEGF mRNA at 24 h; induced ACTA2 and EMT markers (reduced CDH1/e-cadherin) at 24-48 h.
- Conclusion: host neutrophilic inflammatory response (NETs), not direct viral cytopathic effect, is the likely proximate driver of post-COVID-19 interstitial fibrogenesis.

**Longitudinal follow-up at ~12 months shows partial but incomplete normalization:**
- Visit 2 available for 19-20 ILC individuals and 13 resolved individuals (median ~180 days between visits).
- Overall improvement in % TLCO: median IQR at visit 1: 48.0 (44.0–61.0)% → visit 2: 58.0 (52.5–68.4)% (significant, p < 0.0001).
- Overall improvement in % FVC: visit 1 median IQR 80 (71–87.5)% → visit 2: 89.5 (82.1–93.9)% (significant, p < 0.001).
- Despite group-level improvement: 17/19 still had TLCO < 75% at visit 2; 15/16 still had CT radiographic disease extent ≥ 20%.
- Symptom scores (SGRQ) and radiographic disease extent did not show statistically significant improvement.
- Plasma proinflammatory cytokines (TNF, IL-17C, CXCL8/IL-8), myeloperoxidase, and H3R8 citrullinated nucleosomes showed significant reduction between visits but remained higher in ILC vs. resolved group.

## Relevance

This paper is directly relevant to the project research question (research-question:post-acute-infection-syndromes) across multiple dimensions of the PAIS frame.

**Failed homeostatic recovery:** The 12-month follow-up data provide direct evidence that a subset of post-COVID-19 individuals fail to achieve full radiological and functional recovery — 15/16 still had radiographic disease extent ≥ 20% and 17/19 still had TLCO < 75% at ~12 months, despite some improvement. This is a textbook instantiation of the PAIS frame of incomplete homeostatic normalization after acute insult.

**Persistent immune activation as the mechanistic driver:** The neutrophil-associated inflammatory signature persisting at 3-6 months (and partially at 12 months) is a concrete example of the "persistent immune activation" mechanism central to the PAIS framework. The signature is detectable both systemically (plasma proteomics) and mucosally (nasal transcriptomics), suggesting organ-local and systemic entrenchment.

**NET-mediated tissue damage as effector mechanism:** The finding that NETs (not direct viral cytopathology) drive fibrogenic mediator expression in alveolar epithelial cells provides a mechanistic link between immune hyperactivation and tissue remodeling — a specific instance of the general PAIS mechanism of immune-mediated secondary organ damage.

**Type I IFN co-activation:** The concomitant nasal type I IFN signature alongside neutrophilic inflammation suggests a dual innate immune perturbation — antiviral defense pathways that outlast the acute infection co-existing with proinflammatory neutrophilic activation. This pattern resonates with immune dysregulation seen in other PAIS such as ME/CFS and post-treatment Lyme, where IFN signatures and innate immune activation persist without cleared pathogen.

**Therapeutic rationale:** The identification of neutrophil elastase inhibitors (NCT04817332) and kinase targets (CDK2, IRAK1, JNK2) as candidate interventions connects directly to the project's therapeutic-target synthesis strand.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Post-COVID-19 interstitial lung changes (ILC) | PAIS organ-specific sequela (pulmonary) | Subset of PASC with persistent structural lung damage |
| Persistent neutrophil-associated plasma immune signature | Persistent immune activation (PAIS mechanism) | Detectable at 3-6 months post-discharge; partially resolves by 12 months |
| Neutrophil extracellular traps (NETs) | Immune effector → tissue damage pathway | H3R8 citrullinated nucleosomes as NET biomarker; NETs drive fibrogenesis in vitro |
| Myeloperoxidase (MPO) elevation | Neutrophil activation / oxidative stress biomarker | Correlates with both radiographic extent and lung function impairment |
| Type I IFN nasal signature | Antiviral innate immune persistence | Co-occurs with neutrophilic inflammation; nasal IL17D correlates with radiographic severity |
| IL-17C (independently associated with ILC, OR 3.72) | Neutrophil-regulatory cytokine / candidate biomarker | Potentially useful as prognostic marker for post-COVID pulmonary complications |
| PBMC kinase network enrichment (CDK2, IRAK1, JNK2) | Signaling dysregulation / therapeutic target identification | Downstream of type I IFN and TNF receptors; druggable nodes |
| Incomplete normalization at 12 months | Failed homeostatic recovery timeline | Functional and radiographic improvements are partial; true recovery horizon unknown |
| NET-driven fibrogenic gene expression (AEC model) | Immune-to-tissue-damage effector mechanism | NETs induce FN1, VEGF, ACTA2, reduce CDH1 (EMT markers); SARS-CoV-2 alone does not |

## Limitations

1. **Immune sampling not from primary site:** Blood and nasal mucosa were used as pragmatic proxies; the true pathological site is the lower respiratory tract (bronchoalveolar lavage or biopsy would be definitive). Nasal-lower airway immune correlations exist but are imperfect.
2. **No premorbid baseline:** Lung function, radiographic, and immune data before COVID-19 were unavailable; some individuals may have had pre-existing subclinical abnormalities (older cohort, many severe enough to be hospitalized).
3. **Neutrophil subtype resolution limited:** PBMC isolation depletes neutrophils; flow cytometric analysis of neutrophil subpopulations (e.g., low-density granulocytes, aged neutrophils) was not performed on fresh whole blood. Neutrophil debris in PBMCs cannot be excluded.
4. **In vitro model limitations:** AEC NET model cannot fully recapitulate in vivo NET dynamics, which involve complex interactions with ECM, macrophages, and epithelium. In vivo validation in mouse or organoid models is needed.
5. **Cohort size for phosphoproteomics:** Only 9 ILC and 8 resolved individuals contributed PBMC phosphoproteomics; kinase network findings require replication in larger cohorts.
6. **Confounding:** ILC and resolved groups differed in age, BMI, and initial disease severity; multivariable analysis was performed for the plasma proteome but not for all modalities.
7. **Unclear long-term trajectory:** Whether individuals who still had ILC at 12 months eventually achieve full resolution (e.g., at 18 or 24 months) is unknown; ongoing large-scale cohort data are needed.
8. **No genetic data:** HLA or genetic risk factors for pulmonary fibrosis (e.g., MUC5B promoter variant) were not evaluated.

## Model / Tool Availability

No computational models or software tools released. Raw data: plasma proteomics (Olink) and nasal transcriptomic data were generated in-house; supplementary tables (S1-S3) report protein lists and gene lists but raw data availability per GEO or equivalent is not stated in the paper body.

## Follow-up

- **Paper:Cruz2025** — dedicated review of immune mechanisms of pulmonary sequelae in long COVID; directly extends the neutrophil/NET findings from this paper.
- **Paper:Vreeman2025** — mechanisms and therapeutic targets for post-COVID pulmonary fibrosis; builds on the NET-fibrogenesis mechanistic link.
- **Paper:Ryan2022** — complementary peripheral immune perturbation study (lymphocyte-focused) for cross-comparison of immune axes.
- **NCT04817332** — elastase inhibitor trial for post-COVID-19 ILC; directly motivated by this paper's findings.
- Whether the neutrophil/NET/IL-17C signature is specific to pulmonary PASC or is shared across other PAIS organ manifestations (e.g., post-COVID fatigue, cardiac sequelae) is an open question for cross-paper synthesis.
- Whether analogous NET signatures characterize pulmonary sequelae in other PAIS (post-Q-fever, post-influenza) would strongly support the cross-pathogen PAIS mechanism framework.
