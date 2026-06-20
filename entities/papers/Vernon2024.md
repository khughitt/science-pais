---
id: paper:Vernon2024
type: paper
title: "Incidence and Prevalence of Post-COVID-19 Myalgic Encephalomyelitis: A Report from the Observational RECOVER-Adult Study"
status: active
ontology_terms:
  - myalgic encephalomyelitis/chronic fatigue syndrome
  - post-acute sequelae of SARS-CoV-2
  - post-exertional malaise
  - orthostatic intolerance
  - long COVID
  - incidence rate
  - case definition
  - cohort study
  - post-infectious fatigue syndrome
dataset_usage: []
datasets: []
source_refs:
  - cite:Vernon2024
related:
  - topic:mecfs-long-covid-convergence
  - topic:pais-case-definition-heterogeneity
  - topic:shared-failure-mode-across-pais
  - question:0015-does-pem-requirement-improve-cross-study-comparability
  - question:0014-which-pais-case-definition-is-most-biologically-coherent
  - hypothesis:0001-shared-dysregulated-attractor
  - paper:Bateman2023
created: '2026-06-20'
updated: '2026-06-20'
---

# Incidence and Prevalence of Post-COVID-19 Myalgic Encephalomyelitis: A Report from the Observational RECOVER-Adult Study

- **Authors:** Suzanne D. Vernon, Tianyu Zheng, Hyungrok Do, Vincent C. Marconi, Leonard A. Jason, Nora G. Singer, Benjamin H. Natelson, Zaki A. Sherif, Hector Fabio Bonilla, Emily Taylor, Janet M. Mullington, Hassan Ashktorab, Adeyinka O. Laiyemo, Hassan Brim, Thomas F. Patterson, Teresa T. Akintonwa, Anisha Sekar, Michael J. Peluso, Nikita Maniar, Lucinda Bateman, Leora I. Horwitz, Rachel Hess, and the NIH RECOVER Consortium
- **Year:** 2024 (published online January 2025)
- **Journal:** Journal of General Internal Medicine, 40(5):1085–1094
- **DOI/URL:** https://doi.org/10.1007/s11606-024-09290-9
- **BibTeX key:** Vernon2024
- **Source:** Full-text PDF (papers/pdfs/2024_Vernon_incidence-prevalence-postcovid-me-recover-adult.pdf), read 2026-06-20.

## Key Contribution

This paper provides the first large-scale, prospectively followed estimate of how frequently SARS-CoV-2 infection leads to ME/CFS using the 2015 Institute of Medicine (IOM) clinical diagnostic criteria. In the RECOVER-Adult cohort of 11,785 infected adults (enrolled across 83 U.S. sites), 4.5% met full IOM ME/CFS criteria at a visit at least 6 months post-infection — a rate approximately 7.5× that seen in matched uninfected controls (0.6%). The hazard ratio for developing ME/CFS after acute SARS-CoV-2 infection versus matched non-infection was 4.93 (95% CI 3.62–6.71), establishing ME/CFS as a quantifiable, diagnosable sequela of COVID-19 and directly linking the long-COVID and ME/CFS clinical constructs.

## Methods

**Study design:** Longitudinal observational cohort (RECOVER-Adult), NCT05172024, with data from October 2021 to September 2024 (data lock September 2024). Participants were enrolled at 83 sites across 33 U.S. states plus Puerto Rico and Washington, D.C.

**Participants:** 15,181 adults total; after exclusions (hospitalized for COVID, n=294; no symptom data, n=640; no qualifying ≥6-month visit after infection, n=773; pre-existing ME/CFS, n=220), the analysis included:
- 11,785 infected participants (acute enrolled <30 days n=4,515; post-acute enrolled >30 days n=7,270)
- 1,439 uninfected controls

Infection was defined by WHO suspected/probable/confirmed criteria. Uninfected participants had a documented negative SARS-CoV-2 nucleic acid and nucleocapsid antibody test at enrollment. Hospitalized participants were excluded.

**ME/CFS case definition:** 2015 Institute of Medicine (IOM) criteria — operationalized via self-report questionnaires at 3-month-interval study visits:
- Fatigue: PROMIS Global Health 10 item (moderate to very severe over past 7 days)
- Physical impairment: PROMIS Global Health 10 item (moderate to complete interference with daily physical activities)
- Post-exertional malaise (PEM): single binary question ("post-exertional malaise — symptoms worse after even minor physical or mental effort"; positive if "Yes, I have it NOW" or "Yes, and I STILL HAVE IT")
- Unrefreshing sleep: PROMIS Sleep Disturbance item ("My sleep was refreshing"; positive if "Not at all" or "A little bit")
- Cognitive impairment: Neuro-QoL cognition T-score ≤40 (1 SD below national mean) or raw Neuro-QoL score <24
- Orthostatic intolerance (OI): single binary question about feeling faint/dizzy/difficulty thinking after standing (same positive-response criteria as PEM)

Full ME/CFS required: fatigue + physical impairment + PEM + unrefreshing sleep + (cognitive impairment OR OI). Participants meeting at least one criterion but not the full constellation were classified "ME/CFS-like." PEM and OI severity/frequency were not captured — any positive response counted.

The first qualifying visit at ≥6 months from index infection was used as the classification time point for infected participants.

**Incidence analysis:** Restricted to the 4,515 acutely infected participants (enrolled within 30 days), compared to propensity-score-matched uninfected controls. Propensity matching used greedy nearest-neighbor matching with replacement (caliper 0.2 SD of logit propensity score), adjusting for demographic and comorbidity covariates unrelated to SARS-CoV-2 infection but associated with ME/CFS. Post-match SMD = 0.036 (well-balanced). Only 592 of 1,439 uninfected participants matched to an acute-infected counterpart (847 had no match, indicating substantial baseline dissimilarity between groups). Hazard ratio estimated by Cox proportional hazards model. Analyses used SAS Studio, R, and Python 3.11 (scikit-learn, lifelines, pymatch).

**PASC cluster mapping:** Participants meeting ME/CFS or ME/CFS-like criteria were assigned to one of four previously published RECOVER PASC clusters (Thaweethai et al. 2023, JAMA) based on a 44-symptom algorithm.

## Key Findings

**Prevalence (all infected vs. uninfected):**
- Post-COVID-19 ME/CFS: 4.5% (531/11,785) of infected vs. 0.6% (9/1,439) of uninfected
- ME/CFS-like (≥1 symptom, not meeting full criteria): 39.8% (4,692/11,785) infected vs. 16.1% (232/1,439) uninfected
- No ME/CFS symptoms: 55.7% (6,562/11,785) infected vs. 83.3% (1,198/1,439) uninfected

**Incidence (acute enrolled cohort, ≥6-month follow-up):**
- ME/CFS incidence rate in acute infected: 2.66 per 100 person-years (95% CI 2.63–2.70)
- ME/CFS incidence rate in matched uninfected: 0.93 per 100 person-years (95% CI 0.91–0.95)
- Attributable risk: ~1.74 per 100 person-years
- Hazard ratio: 4.93 (95% CI 3.62–6.71; p<0.005)

For comparison, a pre-COVID CDC study estimated ME/CFS incidence at 0.18 per 100 person-years (Reyes et al. 2003).

**Symptom prevalence in infected participants:**
- PEM: most common symptom; 15.9% of acute infected, 29.1% of post-acute infected (overall 24.0% of all 11,785 infected)
- OI: 14.4% acute infected, 25.0% post-acute infected
- Unrefreshing sleep, cognitive impairment, fatigue: each 9–11% in acute-infected; 19–24% in post-acute infected
- All ME/CFS symptoms lower in uninfected

**Demographic features of post-COVID-19 ME/CFS (vs. infected non-ME/CFS):**
- More likely: White non-Hispanic (61.8%), female (79.5%), age 46–65 (51.8%), rural residence (7.2%)
- Less likely: vaccinated at enrollment (86.4% vs. 90.6%), college-educated (54.8% vs. 70.1%)
- Median age: 48 years (IQR 18)

**Comorbidities enriched in post-COVID-19 ME/CFS (vs. never-ME/CFS infected):**
- Chronic pain syndrome or fibromyalgia (7.0% vs. 1.2%)
- Neuromuscular disease (3.0% vs. 1.2%)
- COPD (2.6% vs. 0.9%)
- Dementia or cognitive impairment (1.7% vs. 0.5%)
- POTS, dysautonomia or autonomic dysfunction (1.7% vs. 0.3%)
- Movement disorder (1.1% vs. 0.4%)
- Other mental health disorder (4.0% vs. 2.7%)

**Overlap with RECOVER PASC case definition:**
- 88.7% (471/531) of post-COVID-19 ME/CFS participants also met RECOVER long-COVID (PASC) criteria
- 45.0% were assigned to PASC cluster 4 (highest severity: fatigue, PEM, dizziness, brain fog, GI, palpitations)
- 29.0% cluster 3 (brain fog + PEM + fatigue)
- 10.0% cluster 2 (PEM + fatigue, no brain fog)
- 5.0% cluster 1 (smell/taste loss, lowest burden)
- 11.0% PASC indeterminate
- In contrast, ME/CFS-like participants were predominantly PASC indeterminate (67%) — the full ME/CFS phenotype tracks with the most severe PASC cluster

## Relevance

This paper is directly load-bearing for two central project questions:

**topic:mecfs-long-covid-convergence.** Vernon et al. provide the strongest population-level quantitative evidence to date that long COVID and post-infectious ME/CFS overlap substantially. 88.7% of RECOVER participants who met IOM ME/CFS criteria also met the RECOVER PASC definition, and 74% (clusters 3+4) fell into the most severely symptomatic PASC subgroups. The 4.5% post-COVID ME/CFS prevalence rate — far above the 0.2–1.0% pre-pandemic U.S. population estimate — demonstrates that SARS-CoV-2 is substantially amplifying ME/CFS population burden. This operationalizes the convergence hypothesis: post-COVID ME/CFS is not a distinct new entity but a recognizable variant of the broader ME/CFS phenotype triggered by SARS-CoV-2.

**topic:pais-case-definition-heterogeneity and question:0014/0015.** The study demonstrates that the IOM 2015 ME/CFS criteria can be operationalized at scale with questionnaire-based instruments in a large longitudinal study — and yields a coherent, severe, biologically plausible phenotype (PASC cluster 4 predominant, enriched for dysautonomia/POTS, fibromyalgia). However, the binary PEM/OI items (no severity or frequency threshold) likely inflate true ME/CFS counts slightly, which the authors acknowledge. The ME/CFS-like category (39.8% of infected) remains clinically amorphous. This tension directly informs question:0015 (whether PEM requirement sharpens cross-study comparability) — here, PEM alone was the most prevalent individual criterion (24%), while the full ME/CFS case — requiring PEM plus all other elements — carves out a much smaller but more severe 4.5%.

**topic:shared-failure-mode-across-pais.** The hazard ratio of 4.93 relative to matched uninfected controls confirms SARS-CoV-2 infection as an independent risk factor for ME/CFS, consistent with the shared-failure-mode framework: a trigger-agnostic post-infectious pathophysiology producing ME/CFS regardless of which pathogen initiates it (cf. Hickie 2006: 11% ME/CFS at 6 months after EBV/Q fever/Ross River virus).

**hypothesis:0001-shared-dysregulated-attractor.** The striking enrichment of POTS/dysautonomia (HR ~6× relative to infected non-ME/CFS) and the cluster 4 positioning of most ME/CFS cases (which includes autonomic and cognitive symptoms alongside PEM) is consistent with a shared attractor state of immune-autonomic-metabolic dysregulation. The discussion also explicitly references structural/metabolic/inflammatory brain abnormalities and peripheral neurovascular dysregulation from the ME/CFS literature, supporting the multi-system nature of the attractor.

**paper:Bateman2023** is a close companion paper from Lucinda Bateman (also at Bateman Horne Center, senior co-author here): the Bateman2023 narrative on ME/CFS diagnosis and management is the clinical backdrop against which these epidemiological rates should be interpreted.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| IOM 2015 ME/CFS clinical diagnostic criteria | PAIS case definition (ME/CFS arm) | The operationalized gold-standard definition used in this study; directly relevant to topic:pais-case-definition-heterogeneity |
| Post-COVID-19 ME/CFS (4.5% of RECOVER infected) | post-acute infection syndrome, ME/CFS subtype | Quantifies the overlap between long COVID and ME/CFS syndromes |
| ME/CFS-like (39.8% of infected) | PAIS spectrum / subclinical PAIS | Large intermediate group; boundaries with full ME/CFS are fuzzy by design |
| PASC cluster 4 | Severe multi-system PAIS phenotype | Highest symptom burden cluster; contains 45% of post-COVID ME/CFS cases |
| Post-exertional malaise (PEM) | Canonical ME/CFS symptom; PAIS cardinal feature | Most prevalent individual ME/CFS symptom in RECOVER infected cohort |
| Orthostatic intolerance / POTS | Dysautonomia mechanism | Enriched in ME/CFS subgroup; connects to topic:post-infectious-dysautonomia-and-autoimmunity |
| Hazard ratio 4.93 for ME/CFS after SARS-CoV-2 | Quantitative PAIS risk attributable to index infection | Directly frames the post-infectious attribution problem |

## Limitations

**Study-level limitations acknowledged by authors:**

1. **Self-reported symptoms only.** The ME/CFS case definition was implemented entirely through validated questionnaires, not clinical examination or biomarker confirmation. Symptom waxing and waning could cause misclassification in either direction at the single qualifying visit.

2. **PEM and OI captured as binary without severity/frequency thresholds.** The IOM criteria require PEM to be present, moderate, and persistent — the RECOVER survey asked only yes/no, potentially capturing mild or transient PEM that would not qualify under clinical assessment.

3. **Pre-existing undiagnosed ME/CFS not excluded.** The study excluded participants with a prior formal ME/CFS diagnosis (n=220), but could not identify participants with pre-existing qualifying symptoms who were never formally diagnosed, potentially overestimating new post-COVID ME/CFS.

4. **Selection bias toward long-COVID phenotype.** Participants with PASC may be differentially more likely to enroll and remain in RECOVER, inflating prevalence estimates relative to the general post-COVID population. The post-acute enrolled group (enrolled >30 days post-infection) is particularly susceptible to this bias.

5. **Hospitalized participants excluded.** The most severely ill patients during the acute phase were excluded, creating potential underestimation of ME/CFS in those with severe initial disease, and limiting generalizability to hospitalized COVID.

6. **Predominantly Omicron era and vaccinated cohort.** Most participants were enrolled during the Omicron wave. Earlier, more severe variants may have generated different ME/CFS rates. High vaccination rates (86–91%) may reduce incidence and severity relative to an unvaccinated population.

7. **Uninfected control group was poorly matched at baseline.** 847 of 1,439 uninfected participants (58.9%) had no matched acute-infected counterpart, reflecting fundamental differences in baseline characteristics between who chose to enroll infected vs. uninfected. Propensity matching addressed this partially (post-match SMD 0.036) but the small uninfected ME/CFS cell (n=9) makes comparisons within the uninfected group unreliable.

8. **2015 IOM criteria reflect chronic, severe ME/CFS.** The criteria were designed for established illness of many years' duration and may undercount early or mild post-COVID ME/CFS, or alternatively may overcount transient post-COVID states that would not meet criteria longitudinally.

9. **IOM criteria operationalized across multiple questionnaire instruments.** The mapping from PROMIS, Neuro-QoL, and single-item PEM/OI questions to IOM criteria is reasonable but not identical to the clinical diagnostic process described in the IOM report. Cross-study comparability depends on whether other studies use the same instruments.

**Additional project-specific concerns:**

- The study does not stratify by COVID variant, time since infection, or number of COVID episodes — all covariates that may affect ME/CFS incidence.
- Race/ethnicity differences are noted (White participants over-represented in ME/CFS group) but not adjusted for or explained.
- The "ME/CFS-like" category (39.8%) is clinically heterogeneous and may include early ME/CFS, partial recovery, or unrelated symptom clusters; it should not be aggregated with the ME/CFS group.

## Model / Tool Availability

No computational model or tool is released with this paper. The statistical code used SAS Studio, R, and Python 3.11 with open-source packages (scikit-learn 1.3.1, lifelines 0.29.1, pymatch 0.3.4). Data are stored on the RECOVER analytic platform (Seven Bridges); RECOVER data access is governed by NIH. Supplementary propensity-matching tables are available at https://doi.org/10.1007/s11606-024-09290-9.

## Follow-up

**Directly related papers to read:**
- Thaweethai et al. 2023 (JAMA) — the RECOVER PASC case definition and four-cluster analysis that is cross-referenced throughout this paper (cluster assignments for ME/CFS participants)
- Unger et al. 2024 (JAMA Network Open, INSPIRE study) — parallel ME/CFS-after-COVID prevalence estimate (3–4%) cited for comparison
- Hickie et al. 2006 (BMJ) — the landmark post-infectious ME/CFS prospective cohort (11% ME/CFS at 6 months after EBV/Q fever/Ross River) that provides the historical baseline
- paper:Bateman2023 — ME/CFS diagnosis and management essentials from the same Bateman Horne Center group

**Questions this raises for the project:**
- question:0014 (which PAIS case definition is most biologically coherent) — does the IOM 2015 definition, as operationalized here via questionnaires, track with distinct biological endotypes or just symptom severity?
- question:0015 (does PEM requirement improve cross-study comparability) — Vernon et al.'s PEM-alone prevalence (24.0%) vs. full-ME/CFS prevalence (4.5%) illustrates the ~5× inflation from not requiring the full symptom constellation; how does binary PEM assessment compare to structured PEM scales?
- Are the demographic skews (female, White, age 46–65, rural, lower education) in post-COVID ME/CFS explained by differential exposure, biological susceptibility, or ascertainment bias?
- What proportion of the 4.5% ME/CFS cases recover vs. persist at 12 and 24 months? RECOVER longitudinal data should enable this; it would directly test the shared-failure-mode hypothesis.
- Do participants in PASC cluster 4 who also meet ME/CFS criteria differ from those in cluster 4 who do not on any biomarker or objective measure (e.g., orthostatic challenge, heart rate variability, cognitive testing)?
