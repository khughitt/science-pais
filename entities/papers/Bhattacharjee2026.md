---
id: paper:Bhattacharjee2026
kind: paper
title: 'Exploratory analyses of Immunologic Features in a Randomized, Placebo-Controlled
  Trial of Nirmatrelvir/Ritonavir for Long COVID'
status: active
ontology_terms:
  - nirmatrelvir/ritonavir
  - long COVID
  - randomized controlled trial
  - RANTES/CCL5
  - SARS-CoV-2 spike protein persistence
  - antigen persistence
  - cytokine profiling
  - immunophenotyping
  - antiviral treatment
dataset_usage: []
datasets: []
source_refs:
- cite:Bhattacharjee2026
related:
- topic:antigen-pathogen-persistence
- topic:biomarkers-and-objective-endpoints
- topic:long-covid-immune-dysregulation
- topic:therapeutics-and-clinical-trials
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- question:0012-prevention-vaccination-antiviral-reduces-pais
created: '2026-06-20'
updated: '2026-06-20'
---
# Exploratory analyses of Immunologic Features in a Randomized, Placebo-Controlled Trial of Nirmatrelvir/Ritonavir for Long COVID

- **Authors:** Bornali Bhattacharjee, Mitsuaki Sawano, William B. Hooper, Kexin Wang, Alexandra Tabachnikova, Valter Silva Monteiro, Peiwen Lu, Pavlina Baevova, Gisele C. Rodrigues, Victoria L. Fisher, César Caraballo, Rohan Khera, Shu-Xia Li, Jeph Herrin, Dany Christian, Andreas Coppi, Frederick Warner, Julie Holub, Yashira Henriquez, Maria A. Johnson, Theresa B. Goddard, Erica Rocco, Amy C. Hummel, Mohammad AL Mouslmani, Kevin D. Carr, Lawrence Charnas, Magdia De Jesus, Dale Nepert, Paula Abreu, Frank W. Ziegler III, John A. Spertus, Leying Guan, Harlan M Krumholz, Akiko Iwasaki
- **Year:** 2026
- **Journal:** medRxiv (preprint)
- **DOI:** 10.64898/2026.02.24.26347001
- **BibTeX key:** Bhattacharjee2026
- **Source:** Full-text PDF (papers/pdfs/2026_Bhattacharjee_immunologic-features-nmvr-rct-long-covid.pdf), read 2026-06-20.

## Key Contribution

This is the immunologic substudy of the PAX LC trial (NCT05668091), a Phase 2 randomised double-blind placebo-controlled trial of a 15-day course of nirmatrelvir/ritonavir (NMV/r, Paxlovid) vs. placebo/ritonavir (PBO/r) in long COVID. The substudy's key finding is that NMV/r produced no detectable virological or immunological change over the treatment course: circulating SARS-CoV-2 Spike protein levels, SARS-CoV-2-specific antibody responses, and peripheral blood immune cell subsets were all unchanged in both arms. Critically, both treatment arms showed similar reductions in more than 30 circulating cytokines, and decreases in the inflammatory chemokine RANTES (CCL5) — independent of treatment allocation — were the strongest immunological correlate of self-reported symptom improvement. The results mechanistically contextualise the null clinical primary endpoint of the PAX LC trial by demonstrating that 15-day NMV/r neither clears circulating viral antigen nor resets immune activation in this cohort.

## Methods

**Trial context.** PAX LC (NCT05668091) was a Phase 2, 1:1 randomised, double-blind superiority trial conducted fully decentralised (participants enrolled from 28 US states, March–August 2024). The primary outcome was change in PROMIS-29 Physical Health Summary Score at day 28; that endpoint was null (reported separately by Krumholz et al., 2024/2025). This immunologic substudy was a pre-specified exploratory objective of PAX LC.

**Population.** 82 participants with Long COVID provided blood samples at baseline (Day 0) and post-treatment (Day 28): 45 in the PBO/r arm and 37 in the NMV/r arm. Groups were matched for median age (~42 vs. 43 years), sex (64.4% vs. 73% female), vaccination history (median 4 doses), and duration of Long COVID symptoms (72–1392 days). Variant exposure was characterised using GISAID data and WHO wave classification; the PBO/r arm had a slightly higher proportion of early-wave infections (40% vs. 13.5%) but this did not reach significance.

**Assays.** A multi-orthogonal approach was used:
- *SARS-CoV-2 antigen:* Ultra-sensitive Successive Proximity Extension Amplification Reaction (SPEAR) immunoassays for circulating S1 and full-length Spike (S) protein (functional limit of detection: 7.04 fM for S1; 2.3 fM for S). Measured at Day 0 and Day 28.
- *Antibody responses:* Multiplex Luminex assay for total IgM, IgG subclasses (IgG1–4), and IgA; in-house ELISAs for anti-Spike (S), anti-RBD, and anti-Nucleocapsid (N) IgG; sensitive Elecsys COBAS immunoassay for anti-N IgG; Protein-Based Immunome Wide Association Studies (PIWAS) for linear epitope profiling of anti-S and anti-N responses.
- *Immune cells:* Flow cytometry on peripheral blood mononuclear cells (PBMCs) at Day 0 and Day 28. Panels included exhausted T cells (PD-1+TIM3+), memory T cell subsets, non-conventional monocytes, conventional dendritic cells (cDC1), and activated and double-negative B cell subsets.
- *Cytokines/hormones:* 105-plex multiplexed Luminex assay.
- *Infection history:* Serum Epitope Repertoire Analysis (SERA) for seropositivity against 30 pathogens (6 bacterial, 8 parasitic, 15 viral, 1 fungal).

**Symptom improvement classification.** Participants were classified as "improved" if they showed improvement in at least 4 of 5 instruments: PROMIS-29 v2.1 Physical Health Summary Score (PHSS), PROMIS-29 v2.1 Mental Health Summary Score (MHSS), Modified General Symptom Questionnaire (GSQ)-30, EuroQol EQ-5D-5L Visual Analogue Scale (EQ-VAS), and total symptom burden.

**Statistical approach.** Wilcoxon matched-pairs signed-rank test for within-arm pre/post comparisons; Mann-Whitney U and Chi-Square tests for between-arm comparisons; Spearman correlation for antigen-antibody relationships; multiple logistic regression adjusting for age, sex, and vaccination status to assess immunological predictors of symptom improvement; unsupervised hierarchical clustering on the top 10 cytokines distinguishing improvers from non-improvers, validated by permutation test (100 shuffles); PCA for overall immune profile structure.

## Key Findings

**Circulating SARS-CoV-2 Spike protein: unchanged by treatment.**
- Using the ultra-sensitive SPEAR assay, 55.6% of PBO/r and 43.2% of NMV/r participants had detectable S1 at baseline (difference not statistically significant; p = 0.2672).
- S1 levels were unchanged from baseline to Day 28 in both the PBO/r arm (p = 0.1468) and the NMV/r arm (p = 0.9580).
- Full-length Spike and S1 levels were strongly correlated (Spearman ρ = 0.87 at baseline; ρ = 0.79 at Day 28), validating that S1 reflects full-length Spike ectodomain.
- Conclusion: 15-day NMV/r did not reduce circulating viral antigen.

**SARS-CoV-2-specific antibody responses: unchanged by treatment.**
- No significant differences in anti-Spike IgG levels in either arm.
- Modest but significant declines in RBD-specific IgG were observed by Day 28 in both arms (p_adj PBO/r = 0.024; p_adj NMV/r = 0.0275), with small decreases of <0.5 log10 in median titres — interpreted as time-related waning rather than a treatment effect.
- PIWAS epitope profiling showed no shifts in dominant anti-S or anti-N IgG epitopes within or between cohorts upon NMV/r treatment.
- Anti-N IgG showed a slight increase in the PBO/r arm (p_adj = 0.0026) but no change in the NMV/r arm, with inconsistent direction and very small magnitude.

**Immune cell populations: no treatment effect.**
- No changes in circulating immune cell subsets were detected following NMV/r or PBO/r.
- Specifically, no differences in: non-conventional monocytes (CD14lowCD16high), cDC1, activated B cells (CD86highHLA-DRhigh), double-negative B cells (IgD-CD27-CD24-CD38-), effector or central memory T cells, or exhausted T cells (PD-1+TIM3+ CD4+ or CD8+) in either arm.
- A borderline increase in CXCR3-expressing CD4+ T cells was observed in the NMV/r arm (p_adj = 0.067) but not in PBO/r (p_adj = 0.9277); this did not reach significance after adjustment.

**Hematologic changes: modest, NMV/r-specific, within physiological range.**
- The NMV/r arm showed statistically significant but modest within-arm shifts: reduced median red blood cell counts, platelet counts, and haemoglobin; increased red cell distribution width and mean corpuscular volume (p_adj 0.0027–0.0350). All values remained within normal physiological range. No such changes in PBO/r arm.

**Cytokines: parallel shifts in both arms; RANTES as a symptom correlate.**
- 105 circulating cytokines and hormones were measured. No significant concentration differences between arms at baseline or at Day 28.
- More than 30 cytokines were significantly changed from baseline to Day 28 in both the PBO/r and NMV/r arms, with substantial overlap in the specific cytokines affected. This parallel pattern implicates a time-related or ritonavir-common effect rather than nirmatrelvir-specific immunomodulation.
- RANTES (CCL5) was decreased in both arms and this was validated by ELISA (PBO/r p = 0.0066; NMV/r p = 0.0490).
- NMV/r-arm participants who reported dysgeusia (16/37, vs. 3/45 in PBO/r) had significantly higher cortisol levels (p_adj = 0.0414).

**RANTES and IL-5 correlate with symptom improvement (treatment-independent).**
- Among participants classified as "improved" (regardless of treatment arm), both IL-5 (p_adj = 0.0301) and RANTES (p_adj = 0.0319) were significantly reduced.
- After adjustment for age, sex, and vaccination status in logistic regression, only RANTES remained independently associated with symptom improvement (p_adj = 0.0086); IL-5's association was attenuated (p_adj = 0.291), potentially confounded by age.
- Unsupervised clustering on the top 10 cytokines discriminating improvers from non-improvers identified two clusters: Cluster 2 (66.7% improvers) vs. Cluster 1 (15% improvers), with a significant association between cluster membership and symptom status (Chi-square p = 2.0 × 10-2; permutation test p = 0.0297).
- PCA of these cytokines: PC1 (29.6% variance) was driven by LIF, MIP-3β, IL-5, IFNω, and BAFF; PC2 (20.4% variance) was driven by RANTES, ENA-78, BAFF, IFNω, and LIF.

**Infection history: comparable between arms.**
- SERA seropositivity against 30 pathogens showed no significant differences between PBO/r and NMV/r at baseline.

## Relevance

**To `question:0002-antigen-clearance-rescues-symptoms`.**
This study provides the most directly relevant RCT-embedded data yet available. The null result for Spike protein clearance under NMV/r, combined with the null clinical primary endpoint, is consistent with two non-exclusive interpretations: (a) persistent Spike antigen in this cohort is not virally-replicating and is therefore not targetable by an Mpro inhibitor; (b) the 15-day treatment course and/or systemic drug delivery are insufficient to clear tissue reservoirs, which may generate antigen in the absence of active replication. The failure of NMV/r to move antigen levels does not disprove the antigen-persistence hypothesis — it constrains the mechanism: if antigen drives symptoms, the source cannot be efficiently inhibited by NMV/r at 15 days.

**To `question:0012-prevention-vaccination-antiviral-reduces-pais`.**
Together with the null STOP-PASC (Stanford) trial, PAX LC and this substudy close the evidentiary loop: two independent, adequately powered RCTs of 15-day NMV/r for established long COVID found no clinical benefit and (here) no immunological signal of drug action on SARS-CoV-2 persistence. This is the most informative negative result for the antiviral-treatment arm of the therapeutic landscape for long COVID, and directly constrains what shorter-duration Mpro inhibition can achieve once PASC is established.

**To `hypothesis:0002-tissue-reservoir-antigen-fragment`.**
The inability of NMV/r to reduce circulating Spike levels supports a tissue-reservoir model over an active bloodstream replication model: if virus were actively replicating systemically, standard antiviral levels should reduce antigen. The possibility that Spike originates from non-replicating tissue reservoirs (e.g., via slow protein turnover, immune complex release, or non-replicative transcription from integrated sequences) is strengthened. This shifts the diagnostic priority toward tissue-sampling approaches and toward agents with better tissue penetration.

**RANTES/CCL5 as a potential biomarker.**
The independent association of RANTES decrease with symptom improvement — across both treatment arms, and robust to age/sex/vaccine adjustment — is the study's most actionable positive finding. CCL5–CCR5 signalling is a known driver of chronic inflammatory states; two CCR5 antagonist (Maraviroc) trials (NCT06974084, NCT06511063) are ongoing and their results will directly test whether this pathway is causal rather than correlative. This connects to ongoing interest in therapies targeting CCL5 signalling in the PAIS field.

**Immunophenotyping null.**
The absence of changes in T cell exhaustion markers, memory T cell subsets, activated B cells, or non-conventional monocytes upon NMV/r is informative: if antiviral treatment were clearing persistent viral antigen, one would expect relief of antigen-driven immune activation. The null here is further evidence that either antigen was not moved, or these immune parameters are not sensitive enough to detect changes over 28 days at n = 82.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Circulating SARS-CoV-2 S1/Spike protein | Antigen/pathogen persistence | SPEAR assay detects femtomolar levels; ~55% PBO/r, ~43% NMV/r positive at baseline |
| NMV/r fails to clear Spike antigen | tissue-reservoir-antigen-fragment (hypothesis:0002) | Non-replicating or tissue-sequestered antigen cannot be cleared by an Mpro inhibitor |
| RANTES (CCL5) decrease correlates with improvement | Chronic inflammatory chemokine tone as PAIS driver | Treatment-independent; survives multivariate adjustment |
| Null immunophenotyping (T/B cells, monocytes) | Persistent immune exhaustion/dysregulation | 28 days and n=82 may be insufficient to detect small shifts |
| Parallel cytokine changes in both arms | Ritonavir pharmacology vs. nirmatrelvir specificity | PBO/r contains ritonavir; shared cytokine shifts may be ritonavir-driven |
| 15-day course: insufficient for viral reservoir clearance | Treatment duration and tissue penetration as design parameters | Drives hypothesis that longer or different-target treatment is needed |
| PROMIS-29 primary endpoint null (PAX LC) | Clinical endpoint null context | This substudy provides mechanistic explanation for clinical null |

## Limitations

1. **Small sample; underpowered for immunologic subgroup analyses.** n = 82 (45 PBO/r; 37 NMV/r) for the immunophenotyping substudy provides limited power to detect modest treatment-associated immune shifts. The borderline CXCR3+CD4+ T cell increase (p_adj = 0.067) may be a real signal lost to underpowering.

2. **No ritonavir-only control.** The comparator arm is PBO/r (placebo + ritonavir), not placebo + placebo. Ritonavir is a potent CYP3A4, CYP2D6, and P-gp inhibitor that affects endogenous protein and cytokine metabolism. The parallel cytokine shifts in both arms could partly reflect ritonavir pharmacology, making it impossible to determine whether cytokine changes in the NMV/r arm are due to nirmatrelvir, ritonavir, or time.

3. **Short follow-up (Day 28) and limited by IgG half-life.** Serum IgG has a ~21-day half-life; meaningful changes in antibody titres from antigen reduction would not be expected by Day 28 even if antigen were cleared. The 15-day treatment regimen and Day 28 readout may structurally preclude detecting antibody-level changes.

4. **15-day treatment may be insufficient for reservoir clearance.** Persistent viral reservoirs in gut, lymphoid tissue, or central nervous system may not be reached by orally administered nirmatrelvir, or may contain virus replicating slowly enough that a 15-day course cannot fully suppress it. Extended Paxlovid treatment risks resistance and toxicity.

5. **RANTES/CCL5 association is correlational only.** The decrease in RANTES associated with symptom improvement is a treatment-independent correlation, not established as causal. Ongoing Maraviroc RCTs (NCT06974084, NCT06511063) are needed to determine whether CCR5 antagonism is actually therapeutic.

6. **Participant inclusion not stratified by antigen status.** Trials did not require baseline Spike antigen positivity for enrolment, meaning ~45–55% of participants had no detectable antigen at baseline. The subgroup with antigen-positive baseline (more plausibly the target of an antiviral approach) is too small for powered subgroup analysis.

7. **Self-reported Long COVID duration and index infection.** Symptom duration (72–1392 days) is self-reported; index infection timing and variant assignment rely on self-report cross-referenced against GISAID, introducing classification uncertainty.

8. **Preprint; not peer-reviewed.** This medRxiv preprint (posted February 26, 2026) has not been peer-reviewed at the time of this summary.

## Model / Tool Availability

No models, tools, or standalone datasets are released with this paper. The SPEAR (Successive Proximity Extension Amplification Reaction) immunoassay used for ultra-sensitive spike protein detection is described in methods and is referenced as a prior publication (ref 13 in the paper). The PIWAS (Protein-Based Immunome Wide Association Studies) method for linear epitope profiling is also a referenced methodology (ref 20). The SERA (Serum Epitope Repertoire Analysis) pathogen seropositivity platform is referenced (refs 13, 16, 22). No accessions for raw data are listed in the preprint text.

## Follow-up

**Immediate questions for PAIS project:**
- Does the RANTES (CCL5) decrease-symptom improvement association hold in other PAIS cohorts (ME/CFS, PTLDS), or is it specific to long COVID? This could be tested against existing cytokine datasets.
- What fraction of participants with baseline Spike antigen positivity showed symptom improvement? The current paper cannot answer this due to sample size, but it is the most direct test of `question:0002`.
- Ongoing Maraviroc RCTs (NCT06974084, NCT06511063) are the critical next experiment for the CCL5-CCR5 hypothesis. Their results should be tracked.

**Follow-up papers to read:**
- The PAX LC primary clinical endpoint paper (Krumholz et al., 2024/2025) — clinical context for this immunologic substudy. See paper:Krumholz2024 if summarised.
- STOP-PASC trial (Geng et al., Stanford) — the other large NMV/r long COVID RCT; comparison of baseline antigen prevalence and immunologic correlates would be informative. See paper:Geng2024 if summarised.
- PREVAIL-LC (ensitrelvir; NCT06161688) — parallel antiviral approach with a different Mpro inhibitor and longer treatment arms; comparison of immune outcomes will be informative.
- Papers characterising RANTES/CCL5 in ME/CFS and PTLDS to assess whether this is a shared PAIS chemokine signature.

**Design implications:**
- Future antiviral trials for established PAIS should: (a) require documented antigen positivity at enrolment as an inclusion criterion; (b) use longer treatment durations or agents with better tissue penetration; (c) power immunologic substudies for antigen-stratified subgroup analyses; (d) include a true double-placebo arm to disentangle ritonavir pharmacology from nirmatrelvir effects.
