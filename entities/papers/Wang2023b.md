---
id: paper:Wang2023b
type: paper
title: "Sequential multi-omics analysis identifies clinical phenotypes and predictive biomarkers for long COVID"
status: active
ontology_terms:
- post-acute sequelae of COVID-19
- long COVID
- multi-omics
- proteomics
- metabolomics
- cytokine profiling
- unsupervised clustering
- predictive biomarkers
- platelet degranulation
- T cell exhaustion
dataset_usage: []
datasets: []
source_refs:
- cite:Wang2023b
related:
- topic:long-covid-immune-dysregulation
- topic:biomarkers-and-objective-endpoints
- topic:thromboinflammation-and-endothelial-dysfunction
- topic:shared-failure-mode-across-pais
- question:0001-shared-molecular-signature-across-triggers
- question:0010-vascular-microclot-subphenotype
- hypothesis:0001-shared-dysregulated-attractor
- paper:Klein2023
- paper:Talla2023
created: '2026-06-20'
updated: '2026-06-20'
---
# Sequential multi-omics analysis identifies clinical phenotypes and predictive biomarkers for long COVID

<!--
- **Authors:** Kaiming Wang, Mobin Khoramjoo, Karthik Srinivasan, Paul M.K. Gordon, Rupasri Mandal, Dana Jackson, Wendy Sligl, Maria B. Grant, Josef M. Penninger, Christoph H. Borchers, David S. Wishart, Vinay Prasad, Gavin Y. Oudit
- **Year:** 2023
- **Journal:** Cell Reports Medicine, Vol 4, Article 101254
- **DOI/URL:** https://doi.org/10.1016/j.xcrm.2023.101254
- **BibTeX key:** Wang2023b
- **Source:** Full-text PDF (papers/pdfs/2023_Wang_sequential-multiomics-long-covid-phenotypes-biomarkers.pdf), read 2026-06-20.
-->

## Key Contribution

This study performs sequential multi-omics profiling — cytokine multiplex, targeted plasma proteomics, and targeted plasma metabolomics — on 117 hospitalized COVID-19 patients at acute infection and again at a 6-month convalescence follow-up, compared to 28 healthy controls. It demonstrates that convalescence is not a return to baseline: sustained inflammatory activation, persistent platelet degranulation and coagulation abnormalities, and global metabolic dysregulation (particularly arginine biosynthesis, methionine/taurine metabolism, and the TCA cycle) characterize PASC even in individuals who report symptomatic recovery. By applying unsupervised clustering (autoencoder + k-means) to the longitudinal omics changes, the study identifies three molecularly distinct long-COVID phenotypes. A minimal predictive panel of 7 cytokines + 13 metabolites achieves AUC 0.96 and 83% accuracy for predicting adverse clinical outcomes (all-cause mortality or re-hospitalization) at a median of 17.4 months post-discharge, substantially outperforming individual omics layers and pointing to IL-27 signaling and energy-metabolic dysregulation as the dominant predictive axes.

## Methods

**Study design:** Prospective longitudinal cohort; repeat blood sampling (plasma) during acute COVID-19 hospitalization and at 6-month follow-up. Enrolled at COVID-19 wards and ICUs at a University of Alberta–affiliated hospital (October 2020 – June 2021); dominant circulating strains were wild-type and B.1.1.7. Not population-based; all participants were hospitalized for acute COVID-19 (pre-mass-vaccination era; only 6/117 [5.1%] vaccinated at enrollment).

**Participants:**
- COVID-19 patients: n = 117 (median age 62, 56.4% male; comorbidities: diabetes 41.9%, hypertension 53.0%)
- Healthy controls: n = 28 (age- and gender-matched)
- PASC severity classification at 6-month follow-up: Recovered (no PASC symptoms, n = 30), Mild (≤3 symptoms, n = 32), Severe (>3 symptoms, n = 55)
- Adverse outcome (composite of all-cause mortality or re-hospitalization) reached by 36/117 (30.8%) at median 17.4 months

**Omics platforms:**
- Cytokine profiling: multiplex immunoassay, 47 cytokines measured
- Proteomics: targeted plasma proteomics by LC-MS; 274 proteins measured
- Metabolomics: targeted plasma metabolomics by LC-MS; 635 metabolites measured
- Total DEMs between convalescence and healthy controls: 219 (9 cytokines, 31 proteins, 169 metabolites)

**Analytical pipeline:**
- PCA across all three omics layers for global separation
- Volcano plots and Benjamini-Hochberg-corrected differential expression for pairwise comparisons (acute vs. control; convalescence vs. control; convalescence vs. acute)
- Integrated canonical pathway analysis (Ingenuity Pathway Analysis, IPA) and metabolite set enrichment (MetaboAnalyst)
- Logistic regression of DEMs against self-reported PASC symptoms and SF-12 / EQ-VAS quality-of-life scores (adjusted for age, sex, diabetes, dexamethasone, antibiotics, tocilizumab, remdesivir, WHO Ordinal Scale, vaccination)
- Unsupervised clustering: PCA dimensionality reduction followed by autoencoder (non-linear) + k-means; silhouette coefficient used for cluster number selection
- Machine learning for outcome prediction: linear classifiers on multiplexed cytokines, proteins, and metabolites; 5-fold cross-validation; 90/10 train-validation split; sequential feature selection for minimal panel

**Case definition note:** PASC severity defined by symptom count at 6-month follow-up (0 = recovered, ≤3 = mild, >3 = severe); no WHO or CDC long-COVID operational definition applied. This is a symptom-count threshold, not a standardized case definition.

## Key Findings

**Molecular signature of convalescence vs. acute infection:**
- 157 DEMs distinguish convalescence from acute infection: 8 cytokines, 34 proteins, 115 metabolites
- Convalescence retains a sustained inflammatory state (IL-1β, IL-6, TNF, CXCL1, IL-7, IL-8, IL-18 upregulated; broadly consistent with innate and adaptive immune activation)
- Platelet degranulation and coagulation pathway proteins remain persistently elevated at convalescence (P-selectin, thrombospondin-1, fibronectin, coagulation factor XIII; serotonin and sCD40L continue to rise from acute to convalescence)
- Thrombospondin-1 (mediator of wound healing, angiogenesis, and tissue fibrosis) progressively increased from control → acute → convalescence
- Microthrombi signature: increased clotting cascade proteins and resistance to fibrinolysis at convalescence; functional stimulation of COVID-19 survivor platelets confirmed hyperreactive state and increased granule secretion
- Metabolic dysregulation: TCA cycle metabolites (pyruvate, malate, cis-aconitate, 2-oxoglutaric acid) further elevated at convalescence; glutamine persistently depressed (metabolic signature of COVID-19 disease severity); arginine biosynthesis, methionine/taurine metabolism, and TCA cycle the top dysregulated pathways
- Even the 30 individuals classified as recovered (no symptoms) showed persistently altered molecular signatures, suggesting subclinical pathological processes despite apparent recovery

**Molecular correlates of PASC symptoms and quality of life:**
- Triglycerides negatively associated with nausea and fatigue but positively with tachycardia
- Cystatin C (renal marker) and neutrophil gelatinase-associated lipocalin (NGAL) positively associated with SOB, fatigue, nausea, adverse outcomes — potential kidney involvement in PASC
- Valeric acid (gut-derived short-chain fatty acid) inversely associated with nausea, fatigue, muscle aches, SOB
- Taurine and serotonin levels positively correlated with SF-12 and EQ-VAS quality-of-life scores
- 4-Hydroxyproline and 2-hydroxyisobutyric acid negatively correlated with SF-12 and EQ-VAS
- Downregulation of glycerophospholipids, sphingolipids, phosphatidylcholines, and fatty acids during severe acute COVID-19 — partial recovery in lipids during convalescence associated with lower PASC burden

**Three molecularly distinct PASC phenotype clusters (from unsupervised clustering of acute→convalescence changes):**
- **Cluster A (n = 57, 48.7%):** Minimal molecular deviation; lowest established PASC risk factors; most molecularly "quiet." Individuals spread across all three symptom-severity groups.
- **Cluster B (n = 33):** Predominantly elevated triglyceride and organic acid signature (>65% deviation markers: multiple TG species, indole-3-propionic acid, 4-hydroxyphenylacetic acid, 2-hydroxyisobutyric acid); higher rates of fatigue, insomnia, intubation, palpitations
- **Cluster C (n = 27):** More heterogeneous cytokine/protein/metabolite composition; higher proportion of women; more frequently reported insomnia, palpitations, SOB, general weakness, fatigue; top network enriched in HIF-1α pathway (hypoxia and metabolic adaptation; sex differences in activation); elevated TMAO and phenylacetylglutamine (gut microbiota-derived metabolites associated with cardiovascular disease)
- Cluster membership did not align with symptom-severity classification — individuals from all three severity groups were distributed across clusters, confirming that molecular phenotype is orthogonal to symptom count alone

**TMAO and phenylacetylglutamine as vascular/microbiome subphenotype markers:**
- Both microbiota-derived metabolites (TMAO and phenylacetylglutamine) are significantly elevated in cluster C and in individuals with adverse outcomes vs. event-free survivors
- Phenylacetylglutamine significantly elevated in severe PASC vs. recovered and mild
- Both metabolites are established cardiovascular risk factors, linking gut dysbiosis to thromboinflammatory risk in PASC

**Predictive biomarker panel for adverse outcomes:**
- Minimal panel: 7 cytokines + 13 metabolites (20 molecules total)
- Performance: AUC 0.96, accuracy 0.83 — outperforms all-omics combined (AUC 0.83), cytokine profiling alone (AUC 0.86), proteomics alone (AUC 0.80), and metabolomics alone (AUC 0.78)
- Key panel cytokines (IPA network centered on IL-27 signaling): IL-27 (strongest single predictor), G-CSF, N-Acetyl-Alanine, Taurine, MCP-3 (CCL7); IL-15 and IL-10 inhibited; G-CSF, MCP-3, IL-22 downregulated
- IL-27 drives TIM-3, PD-L1, and IL-10 expression, impairing CD8+ T cell ability to eliminate chronic viral infections — a direct T cell exhaustion axis
- Panel metabolites related to energy metabolism and T cell exhaustion: alpha-aminoadipic acid, taurine, acylcarnitines, spermidine, asymmetric dimethylarginine (ADMA), methylhistidine, palmitoylcarnitine, PDGF-AB/BB, octadecenoylcarnitine, interleukin-10
- Network analysis: downregulation of spermidine and taurine metabolites accompanied by reduction in protective cytokines (IL-22, CSF3) and upregulation of pro-inflammatory cytokines (IL-15) with concomitant increase in IL-10

## Relevance

**question:0001-shared-molecular-signature-across-triggers:** This paper provides one of the most detailed longitudinal multi-omics characterizations of the PASC molecular signature at 6 months. The persistence of inflammatory, platelet/coagulation, and metabolic dysregulation even in symptomatically "recovered" individuals directly supports the hypothesis that a shared molecular attractor state underlies PAIS regardless of symptomatic presentation. The three-cluster phenotyping — orthogonal to symptom severity — suggests that molecular subphenotype, not symptom count, may be the better unit of analysis for cross-PAIS comparisons. The metabolic axes (TCA cycle, arginine-methionine-taurine pathway, mitochondrial bioenergetics) partially overlap with what has been reported in ME/CFS, offering early cross-syndrome resonance.

**topic:biomarkers-and-objective-endpoints:** The minimal 20-molecule panel (AUC 0.96, accuracy 0.83) is one of the highest-performing reported PASC biomarker panels. Its superiority over any single omics layer is a practical demonstration that cross-omics integration is necessary for robust outcome prediction. The panel's centering on IL-27 signaling and energy metabolism (taurine, acylcarnitines, alpha-aminoadipic acid) provides specific molecular targets for validation in independent cohorts. TMAO and phenylacetylglutamine as adverse-outcome markers are independently actionable as gut-microbiome-linked biomarkers.

**topic:thromboinflammation-and-endothelial-dysfunction / question:0010-vascular-microclot-subphenotype:** Persistent platelet degranulation and coagulation protein elevation at 6 months provides mechanistic grounding for the microclot/thromboinflammation hypothesis. P-selectin, thrombospondin-1, fibronectin, and coagulation factor XIII all remain elevated. The functional evidence (hyperreactive platelets, increased granule secretion) strengthens the mechanistic interpretation beyond biomarker association. TMAO and phenylacetylglutamine elevation in cluster C and adverse-outcome individuals further links gut dysbiosis to vascular risk, supporting a gut-thromboinflammation axis in a PASC subpopulation.

**hypothesis:0001-shared-dysregulated-attractor:** The finding that even "recovered" individuals (n = 30, no PASC symptoms) retain a persistently altered molecular signature is direct evidence for a sub-symptomatic attractor state — the system has not returned to its pre-infection configuration despite apparent clinical resolution. This is consistent with the attractor hypothesis and complicates symptom-based case definitions.

**topic:long-covid-immune-dysregulation:** IL-27 as the dominant predictive cytokine — activating T cell exhaustion (TIM-3, PD-1, PD-L1) and suppressing viral clearance — is a specific mechanistic node connecting immune exhaustion to long-term PASC outcomes. The upregulation of innate/adaptive inflammatory markers (IL-1β, IL-6, TNF, IFN family) alongside the coagulation signature suggests a dual immune-vascular failure mode in convalescence.

**topic:shared-failure-mode-across-pais:** TCA cycle and mitochondrial bioenergetic dysregulation, arginine-nitric-oxide axis perturbation, and methionine/taurine pathway disruption at convalescence parallel metabolic findings in ME/CFS (hypometabolic state, TCA cycle suppression). This suggests metabolic convergence across PAIS triggers, though direct cross-condition comparison awaits dedicated multi-PAIS studies.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Persistent molecular signature in symptomatically "recovered" individuals | Sub-symptomatic pathological attractor state | Directly supports hypothesis:0001; recovery ≠ return to pre-infection baseline |
| Three unsupervised clusters (A/B/C) orthogonal to symptom severity | Molecular subphenotypes of PAIS | Demonstrates that symptom count is an inadequate proxy for biological state |
| Platelet degranulation + coagulation protein persistence at 6 months | Thromboinflammation axis (topic:thromboinflammation-and-endothelial-dysfunction) | Mechanistic grounding for microclot/hyperreactivity hypothesis |
| TMAO + phenylacetylglutamine elevation in cluster C and adverse outcomes | Gut dysbiosis → vascular risk linkage | Links microbiome axis to thromboinflammatory PASC subphenotype |
| IL-27 → T cell exhaustion (TIM-3, PD-L1, IL-10) axis as top predictor | Immune exhaustion as PAIS driver (hypothesis:0003-immune-exhaustion-feedback) | Provides a specific mechanistic pathway, not just an association |
| TCA cycle + methionine/taurine/arginine metabolic dysregulation at convalescence | Mitochondrial/metabolic dysfunction axis | Parallels ME/CFS hypometabolism; supports hypothesis:0011-mitochondrial-basis-of-pem |
| Minimal 20-molecule panel (AUC 0.96) outperforms single-omics layers | Multi-omics integration required for PASC biomarker utility | Practical implication for biomarker strategy (topic:biomarkers-and-objective-endpoints) |
| Cluster C: HIF-1α network, more women, gut metabolites elevated | Sex-stratified molecular subphenotype | Partial resonance with hypothesis:0007-mechanism-of-female-predominance-in-pais |
| Sustained IL-1β, IL-6, TNF, CXCL1, IL-7/8/18 at convalescence | Persistent innate/adaptive immune activation | Consistent with shared immune dysregulation across PAIS |

## Limitations

1. **Hospitalized-only cohort, pre-vaccination era:** All 117 participants required hospitalization for acute COVID-19 (October 2020 – June 2021); only 5.1% vaccinated. Findings may not generalize to the broader long-COVID population, which skews toward non-hospitalized individuals. Post-vaccination PASC pathophysiology may differ.

2. **Symptom-count PASC definition, no standardized case definition:** PASC severity classified by symptom count at 6 months (0 / ≤3 / >3). No WHO, CDC, or clinical long-COVID case definition applied. The "recovered" category (n = 30, 25.6%) is defined by the absence of self-reported symptoms — not by molecular normalization (and indeed the paper shows their molecular profiles are not normal).

3. **Small validation cohort for predictive panel:** The 90/10 train-validation split yields a validation set of roughly 12 individuals; external replication in an independent prospective cohort has not been performed. The AUC 0.96 should be treated as preliminary pending larger validation.

4. **Single-timepoint follow-up at 6 months:** Repeat sampling was performed only at one follow-up timepoint (~6.3 months). Longitudinal resolution of when molecular signatures emerge, peak, and potentially resolve beyond 6 months is not captured. No data on whether cluster membership is stable over time.

5. **Canadian single-center cohort, moderate demographic breadth:** Enrolled from a single tertiary hospital; cohort is 56.4% male, predominantly White (69.2%), with high comorbidity burden (diabetes 41.9%, hypertension 53.0%). Findings may not fully generalize across sex, ethnicity, age, or comorbidity strata.

6. **Morning plasma collection protocol may not fully control diurnal variation:** The paper notes metabolomics assays were performed on plasma; despite protocolized morning collection, fasting status confounds are acknowledged in the discussion.

7. **Unsupervised cluster characterization is post-hoc:** Cluster A/B/C labels are data-driven and descriptive; the biological meaning of each cluster requires prospective validation and mechanistic dissection. In particular, cluster A (48.7% of the cohort) is largely defined by the absence of strong molecular deviation — a low-information characterization.

8. **No mechanistic validation of proposed therapeutic targets:** Therapeutic suggestions (anti-IL-6/TNF/IL-1 monoclonal antibodies, anticoagulation, taurine supplementation, antioxidants for TCA/methionine pathway) are speculative; no intervention data are presented.

9. **Multi-omics integration approach is non-harmonized:** Cytokine, proteomics, and metabolomics data are analyzed semi-independently before integration; no joint dimensionality reduction (e.g., MOFA+, DIABLO) is applied. The "combined omics" model (AUC 0.83) underperforms the targeted minimal panel (AUC 0.96), suggesting information redundancy or noise from unintegrated concatenation.

## Model / Tool Availability

No standalone computational model or software tool was released as a companion to this paper. Data and code availability are described in the Supplemental Information (https://doi.org/10.1016/j.xcrm.2023.101254); lead contact for materials: gavin.oudit@ualberta.ca. Proteomics assays performed by MRM Proteomics, Inc. (Montreal, QC); metabolomics by The Metabolomics Innovation Centre (Edmonton, AB). Analysis used Ingenuity Pathway Analysis (IPA, Qiagen), MetaboAnalyst (pathway analysis and dimensionality reduction), and standard R-based machine learning pipelines.

## Follow-up

**Papers for cross-reference:**
- paper:Klein2023 — immune-profiling long COVID (Stanford); compare immune exhaustion signatures and whether IL-27/T-cell-exhaustion axis is corroborated by CyTOF/scRNA data
- paper:Talla2023 — longitudinal multi-omics of convalescent COVID (ISB); compare metabolic and proteomic trajectories and see whether TCA cycle and platelet degranulation signals replicate
- Peluso MJ et al. (multimodal molecular imaging, viral RNA persistence up to 2 years, medRxiv 2023) — mechanistic complement: if viral persistence drives the IL-27/T-exhaustion axis, persistence imaging would corroborate
- Shen B et al. (Cell 2020, proteomic/metabolomic characterization of COVID-19 patient sera) — cited as ref 20; provides acute-phase multi-omics baseline to compare against Wang2023b's convalescence findings
- Pretorius et al. (Cardiovasc Diabetol 2021) — cited re: persistent clotting in PASC; direct mechanistic prior for the platelet/coagulation axis in this paper

**Questions this raises:**
- Does the IL-27 → TIM-3/PD-L1 T cell exhaustion axis appear in non-COVID PAIS (ME/CFS, PTLDS)? If so, it could be a shared molecular driver across triggers (question:0001).
- The three unsupervised clusters do not map onto symptom-severity categories. Is there a clinical or demographic variable that does predict cluster membership, and can cluster assignment at 6 months predict 2–3 year outcomes?
- Given that "recovered" individuals retain a detectable molecular signature, what is the relationship between molecular recovery and clinical recovery? Do recovered-by-symptoms individuals eventually normalize molecularly, or does the attractor persist indefinitely?
- Can the 20-molecule panel (7 cytokines + 13 metabolites) be validated in a non-hospitalized long-COVID cohort, where the base rate of adverse outcomes is lower? The panel was trained on a severe (hospitalized) cohort, and its calibration in mild long COVID is unknown.
- TMAO and phenylacetylglutamine link gut microbiome dysbiosis to cardiovascular risk in cluster C. Does microbial composition at 6 months predict TMAO/phenylacetylglutamine levels, and are these metabolite levels modifiable by diet or probiotic intervention?
