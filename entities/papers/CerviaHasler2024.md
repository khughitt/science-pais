---
id: paper:CerviaHasler2024
type: paper
title: Persistent complement dysregulation with signs of thromboinflammation in active
  Long Covid
status: active
ontology_terms:
  - complement system dysregulation
  - terminal complement complex (TCC)
  - thromboinflammation
  - long COVID / PASC biomarkers
  - monocyte-platelet aggregates
  - herpesvirus reactivation
  - coagulation dysregulation
  - serum proteomics (SomaScan)
dataset_usage: []
datasets: []
source_refs:
- cite:CerviaHasler2024
related:
- paper:Adler2024
- paper:Peluso2024
created: '2026-06-11'
updated: '2026-06-11'
---
# Persistent complement dysregulation with signs of thromboinflammation in active Long Covid

- **Authors:** Carlo Cervia-Hasler, Sarah C. Brüningk, Tobias Hoch, Bowen Fan, Giulia Muzio, Ryan C. Thompson, Laura Ceglarek, Roman Meledin, Patrick Westermann, Marc Emmenegger, Patrick Taeschler, Yves Zurbuchen, Michele Pons, Dominik Menges, Tala Ballouz, Sara Cervia-Hasler, Sarah Adamo, Miriam Merad, Alexander W. Charney, Milo Puhan, Petter Brodin, Jakob Nilsson, Adriano Aguzzi, Miro E. Raeber, Christoph B. Messner, Noam D. Beckmann, Karsten Borgwardt, Onur Boyman
- **Year:** 2024
- **Journal:** Science, vol. 383, no. 6680, eadg7942
- **DOI:** 10.1126/science.adg7942
- **BibTeX key:** CerviaHasler2024
- **Source:** PDF

## Key Contribution

This landmark prospective multicenter serum proteomics study (Zurich + Mount Sinai cohorts; 113 COVID-19 patients + 39 healthy controls; 268 longitudinal blood samples; >6,500 proteins measured by SomaScan aptamer platform) establishes persistent complement system dysregulation — specifically terminal complement complex (TCC) imbalance — as the dominant blood-protein signature of active Long Covid at 6 months post-infection. Critically, the authors identify an inversion: decreased soluble C7-containing TCC complexes (C5b-7, C5b-8, C5b-9) combined with elevated C5bC6 complexes, indicating increased membrane insertion of TCCs into cell surfaces — a shift from clearance toward cell lysis and tissue damage. This complement pathology is accompanied by a thromboinflammatory signature (elevated vWF, reduced ADAMTS13, antithrombin III cleavage, monocyte-platelet aggregates), classical pathway activation associated with elevated anti-CMV and anti-EBV IgG antibodies, and machine-learning confirmation of C5bC6/C7 ratio and vWF/ADAMTS13 ratio as the top two protein biomarkers of Long Covid.

## Methods

**Study design:** Prospective longitudinal multicenter cohort study. Primary cohort: 39 healthy adults + 113 RT-qPCR-confirmed COVID-19 patients enrolled April 2020 – April 2021 at four Zurich hospitals (University Hospital Zurich n=77, City Hospital Triemli n=18, Limmattal Hospital n=13, Uster Hospital n=5). Follow-up visits at 6 and 12 months post-acute COVID-19. Independent validation cohort: Mount Sinai COVID-19 Biobank (198 hospitalized patients; 145 [73.2%] developed 6-month Long Covid; subset of n=21 with additional 3-month proteomics; n=85 for mass spectrometry).

**Long Covid case definition (WHO):** New or persisting COVID-19-related symptoms at 6-month follow-up, lasting ≥2 months with no other explanation. Patients with isolated smell/taste changes were excluded from the systemic proteomics analysis.

**Cohort breakdown:** 76 mild/37 severe acute COVID-19; 56 Long Covid at 1 month; 40 Long Covid at 6 months ("6M-Long Covid"); 22 of those 40 still Long Covid at 12 months.

**Proteomics platform:** SomaScan (version 4.0), measuring 7,335 modified single-stranded aptamers specific to 6,596 unique human proteins + 46 internal controls (7,289 aptamers in total). 39 healthy serum + 113 paired COVID-19 serum samples at acute and 6-month time points.

**Additional assays:** SomaScan on Mount Sinai cohort samples; mass spectrometry on 6-month follow-up serum (DIA mode on EASY-nLC/Thermo Orbitrap Eclipse); ELISAs for total C7, factor Ba, sC5b-9 (neoepitope), vWF (WHO-calibrated), antithrombin III; CH50 complement activity assay; indirect immunofluorescence for antinuclear antibodies (ANA; HEp-2 cells); VirScan phage immunoprecipitation for 87,890 viral epitopes (57 COVID-19 patients + 22 Long Covid + 18 healthy controls); spectral flow cytometry + single-cell RNA sequencing of sorted PBMCs (n=19,247 monocytes sequenced).

**Statistical approach:** Univariate logistic regression (adjusting for age, sex, hospitalization status) for individual aptamer–Long Covid associations; Reactome pathway enrichment (fgsea); linear mixed-effects models; random forest classifier (sklearn RandomForestClassifier, 5-fold nested cross-validation stratified by age group and COVID severity) with SHAP interpretability; Bonferroni and BH multiple testing correction.

## Key Findings

**Complement as the top dysregulated pathway:**
- Pathway enrichment of proteins associated with 6M-Long Covid during acute COVID-19 identified "Complement cascade," "Regulation of Complement cascade," and "Immune system" as the top three Reactome pathways (BH-adjusted p = 0.014, 0.03, 0.03 respectively).
- At 6-month follow-up, TCC components were the most differentially expressed proteins, with C7 complexes (measured by aptamer seq.2888.49) being significantly decreased — confirmed in both the Zurich and Mount Sinai cohorts.
- C7 complexes were reduced in both mild and severe COVID-19 patients who developed Long Covid. The reduction was independent of COVID-19 vaccination status and patient age.

**TCC imbalance — membrane insertion model:**
- Soluble TCC components (C5b-7, C5b-8, C5b-9) were reduced in active Long Covid.
- C5bC6 complexes were elevated — a key bifurcation point: C7 normally scavenges C5bC6 to form soluble complexes, but when C7 is sequestered in membrane TCCs, C5bC6 remains elevated and drives further membrane attack complex (MAC) assembly.
- C5bC6/C7 complex ratio was elevated in Long Covid patients both during acute COVID-19 and 6 months later, strongly correlated with complement activity (CH50, Spearman rho = 0.41, p < 0.001).
- Complement activity (sC5b-9 formation upon in vitro activation, CH50 assay): elevated in Long Covid patients at 6-month follow-up vs. recovered patients and controls.
- Linear mixed-effects model: C5bC6 and total C7 positively associated with complement activity; C7 complexes and sC5b-9 negatively associated — confirming the inversion model.

**Classical and alternative pathway activation:**
- Factor B (alternative pathway central component) was increased in Long Covid patients during acute COVID-19 and at 6-month follow-up.
- C2 (classical/lectin pathway) was elevated in Long Covid patients during acute COVID-19 and at 6-month follow-up; AUC of C2 or factor B for prediction of 12-month Long Covid = 0.806 and 0.81 respectively (mass spectrometry).
- C4-binding protein beta (C4BPB) was increased in 6M-Long Covid, consistent with classical pathway upregulation.
- Complement C3d (final degradation product of C3) was elevated in 6M-Long Covid patients at 6-month follow-up vs. controls (confirmed in Mount Sinai cohort: n=21, p < 0.01 at 3-month follow-up).
- MBL (mannose-binding lectin, lectin pathway): unchanged in Long Covid vs. recovered patients at 6-month follow-up.

**Antithrombin III and coagulation dysregulation:**
- Antithrombin III (encoded by SERPINC1) was persistently low in Long Covid patients both during acute COVID-19 and at 6-month follow-up (confirmed in Mount Sinai cohort: n=21, p < 0.01).
- Antithrombin III cleavage at the thrombin-reactive site was increased in 6M-Long Covid patients (ratio of peptide intensities before/after cleavage site elevated; mass spectrometry).
- Heparan sulfate proteoglycan 2 (HSPG2) — a binding partner of antithrombin III — was decreased in 6M-Long Covid, consistent with disrupted antithrombin III anchoring at endothelial surfaces.
- Coagulation factor XI, fibrinogen beta, protein C, and heparin cofactor II were all increased in 6M-Long Covid patients (mass spectrometry).

**Tissue injury markers:**
- Eight protein measurements associated with 6M-Long Covid across 84 measurements of 49 serum biomarkers: decreased hemopexin (×3), decreased ICAM-1 and S100-A8/A9, increased thrombospondin-1 (TSP-1; ×2), elevated vWF.
- Hemopexin (heme scavenger) persistently low in Long Covid, accompanied by normal hemoglobin/myoglobin — indicating chronic low-level hemolysis without acute hemorrhage.
- Heme levels: colorimetric assay confirmed increased free heme in 6M-Long Covid serum at 6-month follow-up (linear model: female sex and 6M-Long Covid both positively associated with heme).
- vWF: elevated in 6M-Long Covid both during acute COVID-19 and at 6-month follow-up (measured by SomaScan, mass spectrometry, and WHO-calibrated ELISA). vWF elevated in active Long Covid but not recovered patients.
- ADAMTS13 (vWF-cleaving protease): decreased in 6M-Long Covid patients.
- vWF/ADAMTS13 ratio: elevated in 6M-Long Covid both during acute COVID-19 and at 6-month follow-up — positively correlated with complement activity.
- Notably, vWF levels were lower in patients who received remdesivir during acute COVID-19.
- ApoB/ApoA1 ratio: increased in Long Covid — an established cardiovascular risk marker.
- Coagulation factor VIII: elevated in 6M-Long Covid (partially explained by vWF as FVIII carrier).

**Monocyte-platelet aggregates (cellular level):**
- Spectral flow cytometry of PBMCs from 7 healthy controls, 5 no-6M-Long Covid, and 10 6M-Long Covid patients (6 progressing to 12M-Long Covid).
- CD41 (platelet marker) surface abundance on classical monocytes was lowest in healthy controls and highest in Long Covid patients.
- CD41-subclustering identified CD41high (29.6%), CD41dim (61.3%), CD41neg (9.2%) classical monocyte subpopulations.
- CD41high monocytes were highest in 12M-Long Covid patients; represent monocyte-platelet aggregates confirmed by in vivo platelet-to-monocyte ratio.
- scRNA-seq of 19,247 monocytes: Long Covid monocytes showed decreased NR4A1 and IL1B, increased IFTIM3 (interferon-induced transmembrane protein). NR4A1-dependent monocyte subsets are associated with endothelial homeostasis in mice.
- No increased markers of NETosis or neutrophil activation at 6-month follow-up.

**Herpesvirus reactivation and classical pathway:**
- VirScan profiling of 87,890 viral epitopes: no overall increase in reactivity to viral epitopes in Long Covid.
- Specific finding: increased IgG against CMV large structural phosphoprotein (LSP) and increased anti-EBV IgG in 6M-Long Covid patients at 6-month follow-up.
- Anti-CMV IgG and anti-EBV IgG titers associated with Long Covid persistence (6M and 12M).
- C2 levels in the statistical model were associated with anti-CMV IgG titers and Long Covid persistence.
- No SARS-CoV-2 or herpesviral RNA transcripts detected in monocytes by scRNA-seq.
- Interpretation: viral antigen-antibody complexes (immune complexes) involving herpesviruses may be driving classical complement pathway activation in Long Covid.

**Machine learning diagnostic model:**
- Random forest classifier (5-fold nested cross-validation; input: ≤61 uncorrelated protein measurements + 2 protein ratios + 14 clinical variables at acute COVID-19 or 6-month follow-up).
- Performance: AUROC ≥ 0.74 ± 0.10 for 6M-Long Covid prediction on unseen test sets.
- Top 4 features for 6M-Long Covid prediction (6-month follow-up): C5bC6/C7 complex ratio, vWF/ADAMTS13 ratio, age, body mass index (BMI).
- Addition of C5bC6/C7 and vWF/ADAMTS13 ratios to age + BMI improved model performance in all cross-validation scenarios.

## Relevance

This paper is directly relevant to the project research question (**research-question:post-acute-infection-syndromes**) and provides one of the most mechanistically detailed accounts of the PAIS failure mode — failed homeostatic recovery of the innate immune and coagulation systems — available in the Long Covid literature.

**Complement as a PAIS homeostasis system:** The complement system is explicitly framed in the paper as "part of the innate immune system and contributes to immunity and homeostasis by targeting pathogens and damaged cells." Its persistent dysregulation in active Long Covid — 6 months after acute infection — directly instantiates the project's core hypothesis that PAIS represents a failure of homeostatic recovery. The TCC imbalance (membrane insertion rather than soluble clearance) is precisely the kind of locked-in, self-amplifying pathological state the PAIS framework predicts.

**Self-perpetuating pathological loop:** The authors note that tissue injury activates complement, and complement activation drives further tissue injury — a positive feedback loop consistent with the PAIS failure-to-recover model. The finding that complement markers normalize in patients who recover before 6 months, but persist in those with ongoing Long Covid, supports a state-transition view: some patients escape the dysregulated attractor state and some do not.

**Coagulation-complement crosstalk:** Thrombin (produced by the coagulation cascade) can directly activate C5 via a complement-independent pathway. The low antithrombin III levels and evidence of increased thrombin-mediated cleavage in Long Covid place coagulation dysfunction not merely as a consequence but as a potential driver of ongoing complement activation — mechanistic detail critical for the project's multi-system homeostasis frame.

**Herpesvirus reactivation as upstream trigger:** The association between elevated anti-CMV/EBV IgG and classical complement pathway activation suggests that chronic herpesvirus immune complex formation may maintain complement dysregulation. This connects directly to herpesvirus reactivation as a proposed PAIS driver and provides a mechanism linking the immune persistence hypothesis to coagulation and complement pathology.

**Cross-PAIS applicability:** The discussion explicitly notes that complement-modulating therapeutics "could offer new treatment strategies for Long Covid and possibly other postinfection syndromes," directly supporting the project's cross-PAIS generalization hypothesis. The ME/CFS literature already implicates similar complement and coagulation abnormalities.

**Biomarker utility:** The C5bC6/C7 ratio and vWF/ADAMTS13 ratio as top machine-learning features (AUROC ≥ 0.74) represent the most quantitatively validated serum biomarker pair for Long Covid in the project's literature set, and their measurement 6 months post-infection independent of initial disease severity strengthens their translational relevance.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Persistent complement dysregulation at 6M | PAIS immune failure mode: innate immune non-recovery | Complement normalizes in recovered patients → failure to normalize defines the PAIS state |
| TCC imbalance (↑C5bC6, ↓C7 complexes, ↑membrane insertion) | Locked-in post-infectious state / self-amplifying pathology | MAC-driven tissue injury feeds back to activate complement further |
| Low antithrombin III + thrombin-mediated C5 activation | Coagulation-complement crosstalk as PAIS mechanism | Coagulation not merely a consequence — active driver of complement dysregulation |
| Elevated vWF + reduced ADAMTS13 + monocyte-platelet aggregates | Endothelial dysfunction / thromboinflammation as PAIS sequela | Endothelial damage as a shared PAIS feature connecting Long Covid, ME/CFS |
| Anti-CMV/EBV IgG elevations → C2 elevation | Herpesvirus reactivation as PAIS trigger/driver | Immune-complex-mediated classical pathway activation; connects to herpesvirus reactivation hypothesis |
| Hemolysis markers (↓hemopexin, ↑heme) | Red blood cell dysfunction as PAIS feature | Consistent with RBC stiffness and microclot literature in Long Covid |
| Complement normalization in recovered patients | Restoration of homeostasis as the recovery phenotype | Recovery = return of C7 complexes and C5bC6/C7 ratio to healthy-control range |
| Machine learning: C5bC6/C7 + vWF/ADAMTS13 as top biomarkers | PAIS biomarker development | Most validated serum biomarker pair for Long Covid in project's current literature |
| CD41high monocyte-platelet aggregates (highest in 12M-Long Covid) | Cellular correlate of PAIS persistence | Progressive monocyte-platelet aggregation with Long Covid duration |
| scRNA-seq: ↓NR4A1, ↑IFTIM3 in monocytes | Monocyte reprogramming as PAIS immune feature | NR4A1 loss linked to endothelial homeostasis disruption; IFTIM3 links to type-I interferon |

## Limitations

1. **Modest cohort size for deep phenotyping:** Primary Zurich cohort has 40 patients with 6M-Long Covid; cellular analyses (flow cytometry, scRNA-seq) include only 10 Long Covid patients. Effect sizes are likely to be reproducible given validation in the Mount Sinai cohort (n=145 Long Covid), but the granular subgroup analyses (12M-Long Covid, mild vs. severe) have very small n.

2. **Predominantly Caucasian cohort, single-geographic region:** The Zurich study population is mostly Caucasian and ethnicity was not systematically assessed. The Mount Sinai validation partially addresses generalizability, but both cohorts are European or US-based; complement allele frequencies and herpesvirus seroprevalence differ across populations.

3. **Lack of pre-infection baseline samples:** No pre-COVID baseline blood samples exist. Whether the complement and coagulation abnormalities represent pre-existing risk factors or are purely infection-induced cannot be determined.

4. **Cannot determine directionality of complement-coagulation-herpesvirus loop:** The cross-sectional snapshots at 6 months cannot resolve whether complement drives coagulation dysfunction, coagulation drives complement, or herpesvirus immune complexes initiate both. Temporally resolved mechanistic studies are needed.

5. **Long Covid case definition excludes chemosensory-only presentations:** The 8 patients with only smell/taste changes were excluded from systemic serum proteomics analysis. This may undercount Long Covid and enriches the analyzed group for patients with systemic symptoms.

6. **High-throughput aptamer platform limitations:** SomaScan aptamers target specific epitopes; the C7 aptamer (seq.2888.49) recognizes an epitope accessible on monomeric C7 but in C5b-8 complexes (not monomeric C7), confirmed by ELISA. Total C7 levels (ELISA) were comparable between groups, emphasizing that the SomaScan finding is specifically about C7 complexes, not total protein.

7. **No functional validation of herpesvirus mechanism:** While the correlation of anti-CMV/EBV IgG with C2 elevation is suggestive of immune-complex-driven classical pathway activation, this is not directly demonstrated (e.g., by immune complex isolation or depletion experiments).

8. **Limited racial and sex diversity in scRNA-seq subset:** Only 5 out of 19 participants in the flow cytometry/scRNA-seq sub-study were Long Covid patients; sex: 1M/4F for Long Covid group; age range 35–54. Inferences about CD41high monocyte biology are preliminary.

## Model / Tool Availability

No computational model or standalone tool is released. Data and code are available:
- All proteomics data deposited on Mendeley Data (10.17632/dvr5yvrg4x.1) and Zenodo (10.5281/zenodo.10022438).
- Mount Sinai COVID-19 Biobank data accessible via Synapse (https://www.synapse.org/#!Synapse:syn38747390) after registration for a free account.
- Replication data from previously published work available from the authors upon request.

## Follow-up

- **Complement modulator trials in Long Covid:** The paper explicitly proposes complement-targeted therapies as a next step. C5 inhibitors (eculizumab, ravulizumab), C3 inhibitors, and factor B inhibitors are in development for complement-mediated conditions. Investigate whether any ongoing Long Covid therapeutic trials target TCC formation.
- **Herpesvirus reactivation mechanistic studies:** The anti-CMV/EBV IgG → C2 → Long Covid axis needs mechanistic dissection. Read recent herpesvirus reactivation papers in Long Covid (e.g., Bhatt et al. 2023 on EBV/HHV-6 reactivation) to determine whether viral antigen persistence vs. immune complex formation is the better model.
- **Cross-PAIS comparison of complement findings:** Are similar C5bC6/C7 imbalances found in ME/CFS, post-treatment Lyme disease, or post-dengue fatigue cohorts? A literature search for complement abnormalities in non-COVID PAIS would test the shared-mechanism hypothesis.
- **vWF/ADAMTS13 ratio as a pan-PAIS biomarker candidate:** Given the strong machine-learning signal and the role of vWF/ADAMTS13 in thromboinflammation broadly, examine whether this ratio is elevated in ME/CFS or post-Lyme disease cohorts.
- **NR4A1 monocyte biology:** The decreased NR4A1 in Long Covid monocytes and its link to endothelial homeostasis in mice (citation 58 in the paper) is an underexplored pathway. NR4A1 nuclear receptor biology in the context of PAIS monocyte reprogramming deserves a focused literature review.
- **Remdesivir effect on vWF:** The observation that vWF levels were lower in patients treated with remdesivir during acute COVID-19 raises the question of whether antiviral treatment during acute phase blunts the downstream thromboinflammatory signature — relevant to the acute-phase intervention window hypothesis the project tracks.
- **Relationship to paper:Adler2024 and paper:Peluso2024:** Both papers examine immune features of Long Covid. Adler2024 likely covers immune cell phenotypes; Peluso2024 covers viral reservoir hypothesis. CerviaHasler2024 adds complement/thromboinflammatory dimension — synthesize these papers for a complete immune-failure picture.
