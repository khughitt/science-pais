---
id: "paper:Russell2023"
kind: "paper"
title: "Comorbidities, multimorbidity and COVID-19"
status: "active"
paper_kind: "review"
ontology_terms:
  - comorbidity
  - multimorbidity
  - COVID-19
  - PASC
  - long COVID
  - Mendelian randomization
  - adipositis
  - inflammaging
  - frailty
  - syndemic
dataset_usage: []
source_refs:
  - cite:Russell2023
related:
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
  - hypothesis:0020-host-immune-baseline-reserve-gate
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
  - question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
  - question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
  - question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais
created: "2026-07-10"
updated: "2026-07-10"
---

# Comorbidities, multimorbidity and COVID-19

<!--
- **Authors:** Clark D. Russell, Nazir I. Lone, J. Kenneth Baillie
- **Year:** 2023
- **Journal:** Nature Medicine 29: 334–343
- **DOI:** https://doi.org/10.1038/s41591-022-02156-9
- **BibTeX key:** Russell2023
- **Source:** PDF
-->

## Key Contribution

This review introduces a three-phase mechanistic framework for COVID-19 (acute viral illness → inflammatory lung injury → post-acute sequelae) and argues that comorbidities modify each phase through distinct, phase-specific mechanisms rather than through a single generic immunosuppression pathway. The central empirical claim is that **total multimorbidity burden** — not any single comorbidity — is the dominant predictor of severe COVID-19, consistent with the ISARIC4C 4C mortality score using only comorbidity count. The review also synthesizes Mendelian randomization evidence distinguishing causal from confounded comorbidity associations (obesity: causal for inflammatory pneumonitis; type 2 diabetes: not independently causal) and frames the COVID-19/NCD co-epidemic as a 'syndemic' that amplifies harm through socioeconomic inequality, with implications for pandemic preparedness and baseline population health.

## Methods

Narrative review. Synthesizes evidence from:
- **Epidemiological cohort studies:** ISARIC4C (UK-wide hospitalized patients), OpenSAFELY (40% of English primary-care population), UK Biobank, US Veterans Affairs database, Swedish national diabetes registry.
- **Host genetics / Mendelian randomization:** GenOMICC (whole-genome sequencing in critically ill patients), COVID-19 HGI, several published MR studies for obesity, T2D, and other traits.
- **Clinical trial data:** RECOVERY trial for dexamethasone (proof of phase-specific effect), RECOVERY baricitinib.
- **Biological mechanism studies:** tissue proteomics, macrophage biology, cytokine profiling.

Key methodological contribution: uses Mendelian randomization as causal inference in the face of severe confounding, and explicitly addresses collider bias in hospitalized-patient cohort designs.

## Key Findings

### Three-phase mechanistic framework

COVID-19 has three biologically distinct phases with divergent therapeutic and comorbidity profiles:
1. **Acute viral illness (week 1):** viral replication; control requires type I IFN and adaptive (B- and T-cell) responses.
2. **Inflammatory lung injury (weeks 2–4):** innate immune (monocyte/macrophage)-mediated; responsive to anti-inflammatory therapy (dexamethasone, IL-6 receptor blockers, JAK inhibitors).
3. **Post-acute sequelae / PASC (weeks 4+):** mechanistically heterogeneous; involves non-resolving inflammation, but also non-specific critical-illness effects and direct viral damage.

Evidence: the dexamethasone RECOVERY subgroup analysis showed net benefit in patients requiring oxygen/ventilation but a trend to harm in patients not requiring oxygen — the clearest empirical demonstration that clinical and comorbidity effects differ between phases.

### Resistance vs tolerance framework

The review draws a conceptual distinction with direct relevance to the project's hypothesis space:
- **Resistance:** ability to control pathogen replication. Impaired by specific immune defects (B-cell depletion via rituximab; HIV-associated CD4 T-cell depletion <350/μL; CMV latent seropositivity — mechanism unknown but T-cell-independent).
- **Tolerance:** ability to withstand organ injury given a level of pathogen-/immune-mediated damage. Reduced by chronic organ-function impairment (COPD, CKD, pulmonary fibrosis) and frailty/multimorbidity.

Most comorbidities act primarily through reduced tolerance (generic frailty/reserve effect) rather than specific resistance mechanisms.

### Multimorbidity as dominant risk modifier

- >75% of ISARIC4C hospitalized patients had ≥1 comorbidity.
- Crude in-hospital mortality with vs without multimorbidity: 37.2% vs 17.3% (UK study, n = hospitalized COVID-19, adjusted for demographics).
- Performance status (ECOG score, positively correlated with comorbidity count) was independently associated with in-patient mortality with effect size exceeding age after adjusting for physiologic variables.
- UK Biobank: CKD + diabetes combination associated with OR 4.93 (95% CI 3.36–7.22) for severe COVID-19; cardiometabolic cluster is highest-risk multimorbidity pattern.
- Largest risk groupings: organ-transplant recipients (HR 6.00; 4.73–7.61) and CKD (HR 3.48; 3.23–3.75) in OpenSAFELY.

### Phase 1: specific immune mechanisms

- **B-cell depletion (rituximab):** increased in-hospital mortality, prolonged upper-respiratory viral shedding, and relapse; mortality associated with receipt within 6 months. General immunosuppressive therapy not associated with mortality, only B-cell depletion specifically.
- **HIV/CD4 T-cell impairment:** CD4 <350 cells/μL independently associated with severe disease; subtle T-cell activation defects persist even with virologic suppression and apparent reconstitution.
- **CMV latent seropositivity:** associated with increased COVID-19 likelihood and severity, independent of age and other comorbidities; effect strongest in those <60 years old; not explained by classical T-cell CMV-seropositivity phenotype, mechanism TBD.
- **ACE2/hypertension hypothesis:** refuted — ACE2 is rare in alveolar pneumocytes and not upregulated by ACE inhibitors in airways; virus arrives in distal lung via macrophage endocytosis without productive replication.

### Phase 2: obesity as causal driver of pneumonitis

- Obesity is the only comorbidity with consistent **Mendelian randomization support** for causal association with critical COVID-19.
- Proposed mechanism: **adipositis** (low-grade systemic innate immune inflammation from adipose tissue) primes the lung for innate-immune injury when viral replication is not rapidly contained; analogous mechanism proposed for influenza.
- T2D itself is NOT causally supported by MR; the association is likely confounded by shared obesity/BMI (BMI was one of the strongest T2D-COVID outcome predictors in Swedish T2D registry). Glycemic control (HbA1c) associated with outcomes in US T2D cohort, possibly mediated by obesity.
- **Inflammaging** in older patients (subclinical systemic inflammation via monocyte/macrophage activation by cell debris) analogous to adipositis, predisposes to innate immune-mediated lung damage.
- Co-infection with influenza (but not RSV or adenoviruses) specifically increases invasive ventilation risk, suggesting shared lung-injury mechanisms.

### Phase 3: PASC and comorbidities

- Pre-existing comorbidities increase PASC prevalence: 2.8–5.5% in those with health conditions vs 1.8% in those without.
- Multimorbidity associated with persisting symptoms at 12 weeks in non-hospitalized individuals; most of 80 evaluated comorbidities were associated with persistence (COPD HR 1.55; anxiety HR 1.35).
- **Post-acute cardiovascular disease:** COVID-19 increased incident CVD risk 1.6-fold, yielding 45 additional CVD cases per 1,000 persons at 12-month follow-up (Veterans Affairs); risk increased with greater acute severity (non-hospitalized < hospitalized < ICU). [UNVERIFIED: whether this VA cohort result generalizes to other populations or post-Omicron]
- Vaccination reduces PASC risk by only ~15% after breakthrough infection (Al-Aly 2022).
- PASC is mechanistically heterogeneous: virus-direct, non-resolving host inflammation, or non-specific critical-illness effects (overlaps with post-intensive-care syndrome for severe cases).
- Post-acute morbidity recognized after Dengue, SARS, and influenza — situating PASC within a broader PAIS framework.

### Causal inference challenges

- **Collider bias** in hospitalized-patient cohorts: both comorbidity and outcome predict hospitalization.
- **Non-random testing ascertainment bias:** PCR-defined cases enriched for symptomatic/care-seeking individuals.
- **Exposure bias:** comorbid patients may shield more, altering infection probability.
- **Clinical decision confounding:** comorbidities influence thresholds for hospitalization, ICU admission, and organ support (independently of clinical need), distorting intervention-defined severity outcomes.
- Critically: in a multicenter European ARDS study, patients with comorbidities were *less* likely to receive invasive mechanical ventilation — suggesting clinical decisions can produce protective-appearing comorbidity associations.

### Mendelian randomization and host genetics

- MR supports obesity as causal for critical COVID-19.
- MR does NOT support T2D or hypertension as independently causal.
- TYK2 variants: identified TYK2 expression levels as causal for critical COVID-19 → directly informed RECOVERY baricitinib trial (effective) — the first host-genetic discovery to yield a new drug in infectious disease/critical care medicine.
- Limitations: single-pathway assumption is less plausible for multimorbidity contexts; UK Biobank controls may inflate BMI-associated gene effects.

### Syndemic framing

The paper explicitly frames the interaction of COVID-19, NCDs (obesity, diabetes, cardiovascular disease), and socioeconomic inequality as a **syndemic** — not merely co-occurring epidemics. This implies that addressing PASC and COVID-19 severity requires not only biomedical interventions but also structural efforts to reduce the NCD burden and socioeconomic inequalities that produce it.

## Relevance

This paper is directly relevant to the post-acute-infection project across several axes:

**Acute severity threshold (hypothesis:0004):** The three-phase mechanistic framework operationalizes the "acute insult magnitude" concept. The resistance/tolerance distinction provides a mechanistic vocabulary for why the same acute viral burden produces divergent outcomes by host. The ISARIC4C finding that performance status (correlated with multimorbidity) predicts ICU mortality with effect size exceeding age is strong evidence that host reserve is a major threshold-modulating variable, directly supporting the h0004 reserve-modulation arm.

**Host immune baseline reserve gate (hypothesis:0020):** The review provides the strongest available epidemiological grounding for the reserve-gate concept: multimorbidity count, frailty/performance status, and functional organ reserve are the dominant risk modifiers across all three COVID-19 phases. The cardiometabolic cluster (CKD + diabetes, OR 4.93) exemplifies compound reserve depletion. The transplant-recipient / rituximab findings specify that the relevant reserve dimension in Phase 1 is adaptive immune clearance capacity, distinct from the innate-immune tolerance dimension relevant in Phase 2.

**Shared dysregulated attractor (hypothesis:0001):** The paper's description of PASC as "mechanistically heterogeneous" and overlapping with post-intensive-care syndrome explicitly positions PASC as a convergent endpoint reachable via multiple routes — consistent with h0001's attractor framing. The cross-pathogen precedent (Dengue, SARS, influenza post-acute morbidity) strengthens the trigger-nonspecific character of the attractor.

**Post-infectious immune set-point shift → autoimmune conversion (hypothesis:0009):** The MR finding that obesity (via adipositis) is causally implicated in inflammatory lung injury — rather than the commonly assumed metabolic/glycemic pathway — suggests that chronic innate immune priming can shift the COVID-19 host response enough to drive a qualitatively different inflammatory trajectory. This is mechanistically adjacent to (though not identical to) a post-infectious set-point shift; worth noting as a supporting parallel.

**Cross-PAIS / pan-disease relevance:** The syndemic framing directly bridges this project to the pan-disease comparisons project (~/d/health/comparisons/pan-disease). The observation that the NCD cluster (obesity, T2D, CVD) amplifies COVID-19 severity and PASC risk through shared chronic inflammation provides a mechanistic hook for cross-disease integration.

**Question:0057 (compound boundary conditions):** The cardiometabolic cluster analysis (CKD + diabetes OR 4.93 > either alone) provides the clearest empirical demonstration of compound boundary-condition risk in COVID-19, directly motivating the interaction-testing agenda of q0057.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Resistance (pathogen control capacity) | Adaptive immune clearance arm of hypothesis:0002 (tissue reservoir / antigen persistence) | Impaired resistance → longer antigen presence → feeds PAIS attractor entry |
| Tolerance (injury tolerance given immune insult) | Host reserve component of hypothesis:0004 (acute severity threshold) | Lower tolerance → threshold crossed at lower acute severity |
| Multimorbidity count as dominant risk factor | hypothesis:0020 (baseline reserve gate) | Count-based risk prediction ≈ reserve depletion without specifying mechanism |
| Adipositis (obesity-driven innate immune inflammation) | chronic low-grade inflammation as PAIS susceptibility modifier | Mechanistic bridge from cardiometabolic NCD to PAIS risk |
| Inflammaging | chronic innate immune activation axis in frailty | Supports frailty-as-reserve-depletion framing in h0020 |
| Post-acute sequelae / PASC | PAIS (post-acute infection syndrome) | Paper uses PASC and "long COVID" interchangeably |
| Syndemic | multi-level causal model (biology + socioeconomic) | Absent from current project; suggests an unmodeled socioeconomic confounding pathway |
| Collider bias in hospitalized cohorts | methodology concern for project epidemiology | Calibration required when interpreting hospitalized-cohort severity associations |
| MR: T2D not causally supported | Caution on diabetes as PAIS mediator | T2D associations may be obesity/BMI artifacts in project analyses |

## Limitations

- Pre-Omicron evidence base: most cited cohorts are from 2020–2022; post-Omicron comorbidity risk profiles may differ (lower severity baseline).
- Observational association studies dominate; MR is available for only a few traits (obesity, T2D), leaving most comorbidity–COVID associations without causal validation.
- PASC section is thinner than acute phases — reflects the state of evidence in late 2022; mechanistic PASC drivers are underspecified.
- The "three-phase" model is somewhat idealized — phases overlap clinically and the distinct nature of Phase 1 vs Phase 2 is not always separable in observational data.
- Multimorbidity analyzed primarily as burden count; specific comorbidity interactions (interaction terms, DAG structure) are largely absent.
- Does not address sex-stratified effects on comorbidity-PASC interactions, despite evidence from ISARIC4C and VA for sex-modified trajectories.
- Most cohorts are majority-White, UK/US/Swedish populations; LMIC/ancestry diversity is noted as a gap but not addressed.

## Model / Tool Availability

Review paper; no models or tools released. The ISARIC4C 4C mortality score referenced (Knight et al. 2020, BMJ) is publicly available. GenOMICC data accessible via controlled access.

## Follow-up

- **Xie et al. 2022 (Nat Med 28:583–590):** Long-term cardiovascular outcomes of COVID-19, the VA study cited here for the 1.6× CVD risk and 45/1,000 excess burden — if not already in entities/papers/, read next.
- **Al-Aly et al. 2022 (Nat Med 28:1461–1467):** Long COVID after breakthrough infection, the 15% vaccine effectiveness against PASC study — key for question:0012 (vaccination → PAIS prevention).
- **Subramanian et al. 2022 (Nat Med 28:1706–1714):** Symptoms and risk factors for long COVID in non-hospitalized adults — the 12-week multimorbidity/comorbidity persistence study cited here.
- **Nalbandian et al. 2021 (Nat Med 27:601–615):** Post-acute COVID-19 syndrome review — recommended by [@Russell2023] for PASC epidemiology.
- **Pan-disease project link:** The syndemic framing (COVID-19 + NCD + socioeconomic inequality) merits explicit connection to the pan-disease comparisons project.
- **Open question:** Does the adipositis/innate-immune-priming mechanism (obesity → pneumonitis; inflammaging → older-patient lung damage) also operate as a PASC chronicity driver, independently of acute severity? This is not addressed in the paper and maps onto a gap in hypothesis:0020.
