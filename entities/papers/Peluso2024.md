---
id: paper:Peluso2024
type: paper
title: Plasma-based antigen persistence in the post-acute phase of COVID-19
status: active
ontology_terms:
  - SARS-CoV-2 antigen persistence
  - long COVID
  - Simoa single-molecule array
  - viral reservoir
  - spike protein
  - nucleocapsid protein
  - post-acute sequelae of COVID-19 (PASC)
  - antigen-driven immune activation
dataset_usage: []
datasets: []
source_refs:
  - cite:Peluso2024
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# Plasma-based antigen persistence in the post-acute phase of COVID-19

<!--
- **Authors:** Michael J Peluso, Zoe N Swank, Sarah A Goldberg, Scott Lu, Thomas Dalhuisen, Ella Borberg, Yasmeen Senussi, et al.
- **Year:** 2024
- **Journal:** The Lancet Infectious Diseases, Vol 24, June 2024, e345–e347
- **DOI:** 10.1016/S1473-3099(24)00211-1
- **BibTeX key:** Peluso2024
- **Source:** PDF
-->

## Key Contribution

Using the Simoa ultrasensitive single-molecule array platform, this correspondence provides controlled longitudinal evidence that SARS-CoV-2 antigens (spike, S1, nucleocapsid) persist in blood plasma in a significant fraction of individuals for up to 14 months after RNA-confirmed acute infection. By comparing 171 pandemic-era participants against 250 pre-pandemic negative controls, the study demonstrates that antigen detection is significantly above assay background at each of three post-acute timepoints (3–6 months, 6–10 months, 10–14 months), firmly establishing viral antigen persistence — not just prolonged antibody titres — as a detectable feature of the post-acute phase.

## Methods

**Design:** Prospective cohort study (LIINC — Long-term Impact of Infection with Novel Coronavirus, UCSF) with a pre-pandemic negative-control arm.

**Participants:**
- 171 pandemic-era adults with RNA-confirmed SARS-CoV-2 infection; plasma collected at multiple timepoints across 14 months post-onset. Most specimens were collected before vaccination or reinfection (i.e. before Delta/Omicron emergence), limiting confounding from those events.
- 250 pre-pandemic era adults (plasma collected before 2020) serving as true-negative controls to characterise assay false-positive rate.

**Measurement platform:** Simoa (Quanterix) single-molecule array digital ELISA for three antigens:
- SARS-CoV-2 spike (full-length)
- SARS-CoV-2 S1 subunit
- SARS-CoV-2 nucleocapsid (N)

**Specimens:** 660 pandemic-era plasma specimens in total (once-thawed); matched against pre-pandemic specimens at three nominal post-acute timepoints.

**Statistics:** Fisher's two-sided exact tests for prevalence comparisons; absolute prevalence differences with 95% CIs; prevalence ratios for hospitalised vs. non-hospitalised subgroups.

**Specificity:** 98% documented for the Simoa assay against the pre-pandemic cohort (i.e. ~2% background false-positive rate).

## Key Findings

**Overall antigen prevalence:**
- 61/660 (9.2%) pandemic-era specimens had one or more detectable SARS-CoV-2 antigens.
- 42/171 participants (25%) had at least one antigen-positive specimen at some post-acute timepoint.
- Most commonly detected antigen: spike (n=33, 5.0%), followed by S1 (n=15, 2.3%) and nucleocapsid (n=15, 2.3%).

**Time-course comparisons vs. pre-pandemic controls (2% background):**

| Timepoint | Absolute excess prevalence (95% CI) | p-value (any antigen) |
|---|---|---|
| 3.0–6.0 months post-onset | +10.6% (+5.0 to +16.2) | <0.001 |
| 6.1–10.0 months post-onset | +8.7% (+3.1 to +14.3) | <0.001 |
| 10.1–14.1 months post-onset | +5.4% (+0.42 to +10.3) | 0.017 |

Signal for spike antigen specifically was significant at 3–6 months (p=0.012) and 6–10 months (p=0.036) but not 10–14 months (p=0.12). Nucleocapsid reached significance only at 3–6 months (p=0.03). S1 did not reach significance at any individual timepoint (p=0.43, 0.24, 0.40), but contributes to the overall "any antigen" composite signal.

**Hospitalisation effect:**
- Participants hospitalised for acute COVID-19 were nearly twice as likely to have post-acute antigen detected: prevalence ratio 1.97 (95% CI 1.11–3.48), absolute difference +18.4% (+0.3 to +36.5).
- Among non-hospitalised participants, worse self-reported health during acute illness correlated with greater post-acute antigen detection.

**Mechanistic interpretation (authors'):** Findings are consistent with two non-exclusive models: (1) SARS-CoV-2 seeds distal tissue reservoirs through the bloodstream during acute infection, establishing protected antigen sources; (2) higher viral inoculum at primary infection sites increases the probability of evading immune clearance. Coupled with a 2024 report of replication-competent SARS-CoV-2 in blood during acute infection (Platt et al.), the data are consistent with haematogenous seeding of sequestered reservoirs.

## Relevance

This study directly addresses the antigen-persistence mechanism that sits at the centre of this project's working frame (see `research-question:post-acute-infection-syndromes`). The project frames PAIS as failed homeostatic recovery after acute infection; antigen persistence is one of the leading candidate mechanisms for why the immune system cannot return to baseline — it provides an ongoing stimulus that sustains effector activation, prevents resolution of inflammation, and could drive autoimmune epitope spreading.

Key connections:

1. **Evidence quality upgrade:** This is a well-controlled, prospective longitudinal study (n=171 + n=250 pre-pandemic controls, 14-month follow-up) with a validated ultrasensitive detection platform — stronger evidence than prior case-series or cross-sectional reports. It moves SARS-CoV-2 antigen persistence from "promising but less settled" toward "has controlled longitudinal support" (per the research question's Working Frame).

2. **Persistence duration:** Detectable antigen at 10–14 months establishes a substantially longer persistence window than previously documented in blood, consistent with the project hypothesis that immune activation can remain sustained over the time scale at which PAIS symptoms are reported.

3. **Severity gradient:** The dose–response relationship between acute illness severity and post-acute antigen burden supports the idea that the acute phase "seeds" the post-acute state — the homeostatic failure trajectory may be established early, during acute infection.

4. **Shared mechanism across PAIS conditions:** Antigen/pathogen fragment persistence is also documented for Borrelia burgdorferi peptidoglycan in PTLDS (e.g., McClune et al. 2025 in this project). This paper provides the SARS-CoV-2 analogue, supporting the cross-pathogen generalisation that is central to the project's shared-failure-mode frame.

5. **Causal gap explicitly acknowledged:** The authors explicitly state that the study does not establish causation between antigen persistence and post-acute symptoms; they call this an "urgent research agenda." This is the level at which the claim should be held: strong mechanistic plausibility with controlled epidemiological presence, but not yet proven causal linkage to specific symptoms.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| SARS-CoV-2 antigen in plasma post-acute | Antigen/pathogen-fragment persistence (shared PAIS mechanism) | SARS-CoV-2-specific instance of a cross-pathogen pattern |
| Simoa ultrasensitive detection of spike/S1/N | Biomarker of persistence | Platform enables sub-pg/mL detection; relevant to future assay decisions |
| Hospitalisation severity → antigen burden | Acute-phase severity as predictor of PAIS trajectory | Supports the idea that seeding occurs during acute illness |
| Haematogenous seeding of distal reservoirs | Viral reservoir formation (failed clearance) | Mechanism linking acute viraemia to post-acute antigen sources |
| Post-acute antigen present up to 14 months | Duration of failed homeostatic recovery | Establishes lower bound on persistence window in blood |
| 25% of participants ever antigen-positive | Subset susceptibility / heterogeneity of PAIS | Not all infected individuals show persistence — subset biology important |
| Pre-pandemic true-negative control group | Assay specificity / methodological standard | Sets the bar for interpreting immune-based PAIS biomarker assays |
| Antigen ≠ proven symptom cause | Mechanism vs. causation distinction | Authors explicitly decline to overstate; project should maintain same precision |

## Limitations

1. **Correlation vs. causation:** The study establishes presence of antigen in plasma but does not link antigen positivity to individual-level symptom burden in this correspondence (the authors flag this explicitly as future work).

2. **Immunoreactivity-based detection:** Unlike nucleic acid detection, immunoassay signals cannot be definitively attributed to SARS-CoV-2 antigen alone — cross-reactive antigens from related pathogens or host proteins could theoretically contribute, though the 98% specificity against pre-pandemic samples argues strongly against systematic confounding.

3. **98% specificity is imperfect at the individual level:** At ~2% false-positive rate, individual-level positive results require caution; population-level prevalence differences are well above the noise floor but individual attribution is uncertain.

4. **Pre-vaccination, pre-reinfection cohort:** Findings reflect pandemic-era (Alpha/ancestral strain) biology, largely before Delta/Omicron-era reinfections; generalisability to vaccinated or repeatedly infected populations is not directly addressed.

5. **Plasma only:** Blood plasma reflects circulating antigen; tissue-resident reservoirs (gut, lymph nodes, bone marrow) are not captured. Plasma negativity does not imply absence of tissue persistence.

6. **Single detection modality per timepoint:** Longitudinal tracking within individuals would strengthen inference about persistence dynamics; the correspondence format limits presentation of full within-subject trajectories.

7. **Cohort size for subgroup analyses:** The hospitalised subset is small; the +18.4% prevalence difference carries a wide CI (+0.3 to +36.5), limiting precision for severity-stratified claims.

## Model / Tool Availability

No computational model or software tool is released. The Simoa (Quanterix) single-molecule array platform is a commercial instrument; the specific antibody pair configurations for spike, S1, and nucleocapsid detection are described in the appendix (not reproduced here) and reference Swank et al. 2023 (Clin Infect Dis) and Wu et al. 2015 (Analyst) for method details.

## Follow-up

- **Symptom linkage study (same cohort):** The LIINC cohort (Peluso et al. 2021, Open Forum Infect Dis) separately characterized post-acute symptom burden; a paired analysis correlating antigen positivity with symptom scores in the same individuals would test the causal hypothesis.
- **Swank et al. 2023** (Clin Infect Dis 76:e487–e490): Prior LIINC report linking persistent circulating spike to PASC sequelae — the direct predecessor to this paper; read together.
- **Proal et al. 2023** (Nat Immunol 24:1616–27): Systematic review of SARS-CoV-2 reservoir evidence in PASC; broader mechanistic context.
- **McClune et al. 2025** (in this project): Borrelia peptidoglycan persistence in PTLDS — the structural analogue for another PAIS condition; cross-compare persistence detection methodologies.
- **Tissue reservoir studies:** gut biopsy, lymph node, and bone marrow antigen persistence studies (e.g., Patterson et al., Cheung et al.) needed to establish whether plasma antigen reflects active tissue sources.
- **Antiviral intervention trials:** If antigen persistence drives PAIS, antiviral treatment (e.g., nirmatrelvir/ritonavir in RECOVER-VITAL) should reduce antigen burden and symptom load — trials underway at time of writing.
