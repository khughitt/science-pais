---
id: paper:Kwissa2025
type: paper
title: Persistent Immune Dysregulation during Post-Acute Sequelae of COVID-19 is Manifested in Antibodies Targeting Envelope and Nucleocapsid Proteins
status: active
ontology_terms:
  - post-acute sequelae of SARS-CoV-2 infection
  - antibody response
  - antigen persistence
  - immune dysregulation
  - MAIT cells
  - circulating T follicular helper cells
  - autoantibodies
  - cytokine signature
  - longitudinal immunoprofiling
dataset_usage: []
datasets: []
source_refs:
  - cite:Kwissa2025
related:
  - topic:antigen-pathogen-persistence
  - topic:long-covid-immune-dysregulation
  - topic:biomarkers-and-objective-endpoints
  - question:0002-antigen-clearance-rescues-symptoms
  - hypothesis:0002-tissue-reservoir-antigen-fragment
  - hypothesis:0003-immune-exhaustion-feedback
created: '2026-06-20'
updated: '2026-06-20'
---
# Persistent Immune Dysregulation during Post-Acute Sequelae of COVID-19 is Manifested in Antibodies Targeting Envelope and Nucleocapsid Proteins

- **Authors:** Marcin Kwissa, Manikannan Mathayan, Satyajeet S. Salunkhe, Velavan Bakthavachalam, Zijing Ye, Mark A. Sanborn, Samantha Condo, Aditi Upadhye, Athulith Nemakal, Justin M. Richner, Sanjib Basu, Richard M. Novak, Jeffrey R. Jacobson, Balaji B Ganesh, Martha Cerda, Paul J. Utz, Jerry A. Krishnan, Bellur S. Prabhakar, Jalees Rehman
- **Year:** 2025
- **Journal:** bioRxiv (preprint)
- **DOI:** 10.1101/2025.08.18.670908
- **BibTeX key:** Kwissa2025
- **Source:** Full-text PDF (papers/pdfs/2025_Kwissa_persistent-immune-dysregulation-pasc-antibodies-envelope-nucleocapsid.pdf), read 2026-06-20.

## Key Contribution

This preprint from the Illinois Research Network (ILLInet) RECOVER Hub reports a multi-modal longitudinal immunoprofiling study demonstrating that PASC participants exhibit persistently elevated serum IgG responses specifically to SARS-CoV-2 Envelope (E) and Nucleocapsid (N) proteins — but not Spike — relative to fully convalescent controls over a period of at least 5–7 months post-infection. The authors interpret sustained anti-E and anti-N IgG as indirect evidence of ongoing viral antigen exposure, potentially from tissue reservoirs. This humoral skewing co-occurs with elevated circulating T follicular helper (cTFH) and MAIT cell frequencies, a pro-inflammatory cytokine signature, and increased autoantibody reactivity, constituting a broad picture of unresolved immune activation in PASC.

## Methods

**Study design.** Retrospective longitudinal study nested within the NIH RECOVER Adult Cohort Study. Cryopreserved PBMC, plasma, and serum were received from specimens stored at Mayo Clinic Rochester; all assays were performed at the University of Illinois Chicago (UIC). PCR-confirmed SARS-CoV-2 infection enrolled December 2021 – October 2022. IRB: NYU Grossman School of Medicine and UIC (#2021-1287). Participants were enrolled approximately 6 weeks post-infection (baseline T0, mean ~42 days post-infection), with two further blood draws at ~2–3-month intervals (T1 and T2). All participants reported vaccination against COVID-19. PASC case definition: RECOVER cohort criteria (multi-symptom, longitudinal follow-up); symptom endotypes include cardio-pulmonary, fatigue/malaise, neuropsychiatric, dizziness, dysautonomia, and indeterminate PASC.

**Cohort.** N = 30 total: 20 PASC, 10 convalescent without persistent symptoms (CONV). Heterogeneous PASC phenotypes were represented intentionally to mirror real-world PASC diversity. Pre-COVID-19 control sera (n = 3) served as negative controls for all antibody assays.

**Antibody ELISA.** Serum IgG (total and subclasses IgG1–IgG4) and IgA against SARS-CoV-2 Spike (B.1.1.529/Omicron trimer), Envelope (E), Nucleocapsid (N), and Membrane (M) proteins measured by ELISA (OD450). Serum dilutions: 1:3200 for Spike; 1:200 for Envelope and Membrane; 1:2000 for Nucleocapsid. Virus neutralization (IC50) measured with live SARS-CoV-2 Omicron B.1.1.529 on Vero E6 cells.

**Plasma proteomics (mass spectrometry).** Immunoglobulin content and variable region repertoire profiled by LC-MS/MS (Q Exactive HF, Thermo; UniProt search via Mascot Daemon, 1% FDR). Quantified Ig constant-region and variable-region peptides for IgM, IgA1, IgA2, IgG1–4, J-chain.

**CyTOF immunophenotyping.** High-dimensional PBMC immunophenotyping using a 26-antibody (metal-tagged) panel on the Fluidigm CyTOF2; UMAP and t-SNE clustering; gating for major lineages and subsets (CD4+ T cells including TCM, cTFH, Treg; CD8+ T subsets; B cells; NK cells; ILC-2; MAIT cells; gamma-delta T cells; mDC; pDC; monocytes; basophils).

**Cytokine profiling.** 96-plex MILLIPLEX Human Cytokine/Chemokine/Growth Factor Panel (Panels A and B; Millipore Sigma; HCYTA-60K-PXBK48 and HCTB-60K-PXBK48) measured on a Luminex MAGPIX instrument across all three timepoints. Modular clustering performed in R with Cytomod; logistic regression for PASC-associated cytokines.

**Autoantibody profiling.** HuProt microarray (CDI Labs ImmuneProfiler Assay) interrogating >23,000 human proteins for IgG and IgM reactivity. Benjamini-Hochberg FDR correction; threshold: adjusted p < 0.05 and |log fold change| > 0.5.

**Statistics.** GraphPad Prism v10.2; 2-way ANOVA for group-by-time comparisons; Pearson correlations; Tukey post-hoc. R for cytokine modular analysis (Cytomod) and mass spectrometry visualization.

## Key Findings

**Anti-Envelope and anti-Nucleocapsid IgG are persistently elevated in PASC.**
- Anti-Envelope IgG: 1.98-fold higher mean OD450 in PASC vs. CONV across all timepoints (p = 0.0022); consistent across all PASC symptom endotypes.
- Anti-Nucleocapsid IgG: significantly elevated in PASC (p = 0.0419).
- Anti-Spike IgG: significantly *lower* in PASC vs. CONV (p = 0.0025). PASC showed IgG1/IgG3-biased Spike response; CONV showed IgG4 dominance (54.5% of total anti-Spike IgG), consistent with tolerogenic class-switching after repeated mRNA vaccination.
- Neither group showed significant differences in anti-Spike IgA or virus-neutralization titers.
- The selectivity for E and N — both of which are absent from approved COVID-19 vaccines — is interpreted by the authors as evidence of ongoing antigenic stimulation by virus-derived proteins, not a vaccine response artifact.

**Mucosal immunoglobulin signature in PASC plasma proteome.**
- Mass spectrometry revealed significantly elevated IgM (IGHM, p = 0.0009), IgA1 (IGHA1, p = 0.0026), IgA2 (IGHA2, p = 0.004), and J-chain (p = 0.0028) in PASC; total IgG subclasses (IGHG1–4) were not different. Multiple Ig variable-region peptides (IGHV, IGKV, IGLV) were upregulated.
- The selective enrichment of mucosal/early-phase isotypes suggests active or ongoing humoral responses, possibly at mucosal sites (gut, lung), consistent with a tissue reservoir for viral persistence.

**cTFH and MAIT cells are expanded in PASC.**
- cTFH (CD4+CXCR5+): substantially expanded in PASC vs. CONV (p = 0.0352); cTFH frequency correlated strongly with CD4+ TCM proportions (p < 0.0001, r = 0.55 in PASC).
- MAIT cells (CD3+CD4-CD28+CD161hi): 1.73-fold increase in PASC at all timepoints (p = 0.0461); MAIT frequency correlated with anti-Envelope IgG titers (r = 0.3, p < 0.026), suggesting linked mucosal immune activation.
- Total CD4+ TCM (CCR7hiCD45RA-CD45RO+) were significantly expanded in PASC within CD45+ lymphocytes.
- Total CD4+, CD8+ T cells, B cells, monocytes, mDC, pDC, NK cells, ILC-2, and gamma-delta T cells did not differ significantly between PASC and CONV.

**Pro-inflammatory cytokine signature.**
- t-SNE of 96-plex cytokine profiles separated PASC and CONV into distinct clusters with stable between-group differences over time.
- Module 2 cytokines with highest odds ratio for PASC: IL-11, LIF, Eotaxin-3 (CCL26), IL-23, IFN-beta, HMGB-1.
- ENA-78 (CXCL5) was positively associated; IP-10 (CXCL10) was negatively associated with PASC.
- Greatest fold-elevation over CONV: IL-11 and LIF (IL-6 family members); the authors note their consistency with EBV lytic reactivation-induced cytokines.

**Autoantibodies in PASC.**
- 16 proteins showed significantly elevated auto-IgG in PASC vs. CONV (HuProt array, ~23,000 proteins tested).
- Top 20 proteins targeted by auto-IgM also elevated.
- Auto-IgG against 9 of the 16 top autoantigens were strongly correlated (r > 0.7, p < 0.0001) within PASC individuals, indicating a subset with broad polyclonal autoreactivity against multiple self-proteins.
- No single autoantibody was pathognomonic; targets span diverse cellular compartments, consistent with heterogeneous tissue injury patterns across PASC phenotypes.

**Temporal stability.** IgG responses did not significantly correlate with time since infection to blood draw at any of T0, T1, or T2, indicating that the anti-E and anti-N elevation reflects a state difference between groups, not a simple kinetics artifact.

## Relevance

**hypothesis:0002 (tissue reservoir / antigen fragment):** The paper provides the most direct blood-based, longitudinal evidence to date from the RECOVER cohort that PASC participants maintain elevated antibody responses specifically against two non-vaccine antigens (E and N) for up to 6 months post-infection. The authors explicitly frame this as *indirect* evidence of persistent viral antigen exposure — they do not detect antigen directly, but argue that long-lived sustained IgG against E and N requires continued B cell stimulation by viral antigen. This is consistent with, but does not prove, tissue-reservoir antigen persistence. The mucosal Ig isotype signature (elevated IgM, IgA1, IgA2, J-chain; normal IgG subclasses) further suggests de novo immune activation at mucosal sites rather than simple antibody decay from a past response.

**question:0002 (does antigen clearance rescue symptoms?):** The paper does not test antiviral intervention. However, the observation that anti-E/anti-N IgG is elevated across *all* PASC symptom endotypes (not just one phenotypic cluster) implies that sustained antigen exposure may be a common upstream driver rather than a secondary phenomenon in a subset. This strengthens the rationale for a clearance experiment. Symptom-tracking relative to antibody titer dynamics is not reported.

**hypothesis:0003 (immune-exhaustion feedback):** The expanded cTFH and MAIT populations, together with a pro-inflammatory cytokine milieu and autoantibody diversification, are consistent with a self-amplifying dysregulated immune state — but the paper does not assess T cell exhaustion markers directly.

**topic:long-covid-immune-dysregulation / topic:biomarkers-and-objective-endpoints:** The anti-E and anti-N IgG titers, MAIT cell frequency, and cytokine module scores (IL-11, LIF, HMGB-1) are candidate blood-based biomarkers accessible through routine venipuncture.

**Antigen specificity note (important distinction):** E and N are absent from all approved COVID-19 mRNA vaccines; the higher anti-E/anti-N IgG in PASC cannot be a vaccine effect. Anti-Spike IgG is *lower* in PASC than in CONV, with CONV showing IgG4 class-switching consistent with efficient vaccine-induced humoral memory. This antigen-specificity pattern rules out simple immune hyperactivity across all viral targets and instead implies something specific about E/N antigen exposure in PASC.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Anti-Envelope / anti-Nucleocapsid IgG persistence | Indirect antigen persistence signal | Antibody-based proxy; antigen not measured directly |
| Elevated cTFH + CD4+ TCM | Ongoing germinal center / B cell activation | Consistent with sustained antigen-driven B cell help |
| MAIT cell expansion correlating with anti-E IgG | Mucosal immune activation / possible viral reservoir signal | MAIT cells are innate-like, responsive to mucosal pathogens |
| Elevated IgM, IgA1, IgA2, J-chain (proteomics) | De novo mucosal humoral response | Points to gut/lung mucosa as candidate reservoir site |
| IL-11, LIF, HMGB-1 cytokine module | Tissue damage / IL-6-family inflammatory signature | LIF/IL-11 also induced by EBV lytic reactivation |
| Heterogeneous auto-IgG profile | Autoimmunity as secondary immune dysregulation | No single shared autoantigen; tissue-injury-driven |
| IgG4-biased Spike response in CONV | Tolerogenic immune resolution post-vaccination | Contrast with PASC IgG1/IgG3-biased Spike response |

## Limitations

1. **Small cohort (N = 30; 20 PASC, 10 CONV).** The study is substantially underpowered for detecting associations within PASC endotypes or for identifying individual cytokine-symptom correlations. 2-way ANOVA over three timepoints inflates false discovery risk without sufficient per-cell sample sizes; conclusions should be treated as hypothesis-generating.

2. **No direct antigen measurement.** The central claim — that anti-E and anti-N antibody elevation reflects viral antigen persistence — is an inference. The paper does not detect viral RNA, protein, or immune complexes in blood or tissue. This is acknowledged by the authors.

3. **Heterogeneous PASC phenotypes pooled.** The study intentionally enrolled diverse PASC endotypes to maximize generalizability, but this limits phenotype-specific mechanistic conclusions. Anti-E/anti-N elevation was reported across endotypes (Figure S1), but power to test endotype-specific differences is absent.

4. **Blood-only specimens.** The authors acknowledge that tissue-resident immune changes, viral reservoirs, and local inflammation cannot be directly captured from peripheral blood. Peripheral blood immunophenotyping is a proxy for systemic, not tissue-compartment, immune status.

5. **Self-reported infection date.** Time-since-infection normalization relies on self-report, introducing imprecision in kinetic interpretations.

6. **No symptom severity scores tied to individual antibody or cytokine values.** The paper does not correlate within-individual symptom burden trajectories with anti-E/anti-N titers or cytokine levels at matched timepoints. Whether high anti-E IgG tracks symptomatic worsening or improvement is unknown from this data.

7. **Recruitment window (Dec 2021 – Oct 2022) spans Omicron emergence and mixed vaccine histories.** Variant- and vaccine-dose-specific effects on the Spike vs. E/N antibody hierarchy are not fully controlled.

8. **Preprint; not peer reviewed.** Evidence level is preliminary pending peer review.

9. **EBV reactivation confound.** The discussion raises EBV as a possible contributor to the LIF/IL-11 cytokine pattern and mucosal Ig signature, but EBV serology or reactivation markers were not measured, leaving this as [SPECULATION].

## Model / Tool Availability

No computational model or analysis tool is released with this preprint. Raw data are not deposited in a public repository as of the preprint posting date; no accession numbers are reported. Analysis was performed using GraphPad Prism v10.2, R with Cytomod, Orange Datamining v3.3.8, and Scaffold DDA v6.0.1.

## Follow-up

- **Direct antigen measurement studies** are the necessary complement to this paper. See paper:Peluso2024 for plasma antigen (nucleocapsid) persistence data, which would close the inferential gap between elevated antibody and confirmed antigen.
- Test whether anti-E/anti-N IgG titers decline in PASC patients who undergo antiviral treatment (e.g., nirmatrelvir/ritonavir in RECOVER-VITAL trial) and whether titer decline tracks symptom improvement — a direct test of question:0002.
- Characterize exhaustion markers (PD-1, LAG-3, TIM-3) on cTFH and MAIT cells in PASC to evaluate hypothesis:0003.
- Replicate in a larger RECOVER or UK Biobank cohort, stratified by PASC endotype, acute-illness severity, and vaccination history.
- Test whether mucosal biopsy from gut/lung in PASC shows co-localized E/N antigen and activated MAIT cells or germinal center activity.
- Assess EBV reactivation (VCA IgG avidity, EA-IgG, EBV DNA) in parallel with anti-E/anti-N titers to disentangle SARS-CoV-2 antigen persistence from EBV-driven polyclonal activation.
