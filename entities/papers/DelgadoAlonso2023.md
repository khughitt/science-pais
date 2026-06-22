---
id: paper:DelgadoAlonso2023
type: paper
title: "Unraveling brain fog in post-COVID syndrome: Relationship between subjective
  cognitive complaints and cognitive function, fatigue, and neuropsychiatric symptoms"
status: active
ontology_terms:
  - brain fog
  - post-COVID syndrome
  - subjective cognitive complaints
  - neuropsychological assessment
  - fatigue
  - mediation analysis
  - sex differences
  - long COVID
dataset_usage: []
datasets: []
source_refs:
  - cite:DelgadoAlonso2023
related:
  - question:0007-mechanism-of-female-predominance-in-pais
created: '2026-06-22'
updated: '2026-06-22'
---
# Unraveling brain fog in post-COVID syndrome: Relationship between subjective cognitive complaints and cognitive function, fatigue, and neuropsychiatric symptoms

- **Authors:** Cristina Delgado-Alonso, Maria Diez-Cirarda, Josue Pagan, Carlos Perez-Izquierdo, Silvia Oliver-Mas, Lucia Fernandez-Romero, Alvaro Martinez-Petit, Maria Valles-Salgado, Maria Jose Gil-Moreno, Miguel Yus, Jorge Matias-Guiu, Jose Luis Ayala, Jordi A. Matias-Guiu
- **Year:** 2023
- **Journal:** European Journal of Neurology, vol. 32, art. e16084 (published online Oct 2023; collection Jan 2025)
- **DOI:** 10.1111/ene.16084
- **PMID:** 37797297 | **PMCID:** PMC11618112
- **BibTeX key:** DelgadoAlonso2023
- **Source:** XML full text via Europe PMC (OA)
- **Case definition:** WHO post-COVID syndrome criteria (symptoms ≥2 months, onset ≥3 months post-acute infection, no alternative cause); PCR-confirmed SARS-CoV-2

## Key Contribution

This cross-sectional neuropsychological study (n = 170, 73% women) is the most methodologically complete single-site study of "brain fog" in post-COVID syndrome to establish the *causal order* among objective cognitive function, fatigue, depression, anxiety, and subjective cognitive complaints (measured by the FLEI scale). The load-bearing finding: **fatigue is the primary mediator** between objective cognitive performance and subjective cognitive self-report (standardized indirect β = −0.317, accounting for the majority of the total indirect effect of −0.394); depression's effect on brain fog is indirect and operates *through* fatigue rather than independently. Women report significantly more subjective memory complaints than men (FLEI-memory 26.65 ± 6.54 vs. 23.04 ± 8.41, p = 0.004) but show no sex difference on any objective neuropsychological test score — directly demonstrating that the female excess in self-reported cognitive dysfunction sits in the fatigue-mediated subjective channel, not in objectively measurable deficit.

## Methods

- **Design:** Cross-sectional, single-center (Hospital Clinico San Carlos, Madrid, Spain)
- **N:** 170 post-COVID syndrome patients (73.1% women; mean age 49.4 ± 11.0 years; mean time since acute infection 14.5 ± 6.9 months)
- **Inclusion:** PCR-confirmed SARS-CoV-2; WHO PCS criteria (≥2 months post-onset, ≥3 months since acute infection); cognitive complaints present; no prior cognitive complaints; no neurological/psychiatric history
- **Subjective cognition (primary outcome):** FLEI questionnaire — 35 self-report items across attention (0–40), memory (0–40), and executive function (0–40) domains; total "mental ability" score 0–120 (higher = worse subjective ability). Cutoff for significant complaints: >46
- **Objective neuropsychological battery:**
  - Attention/processing speed: Digit Span Forward/Backward, SDMT, Stroop (A/B/C), Corsi block-tapping
  - Visuospatial/constructional: Rey-Osterrieth Complex Figure (ROCF; copy + recall), Judgment Line Orientation, VOSP
  - Memory (verbal): Free and Cued Selective Reminding Test (FCSRT; free recall, total recall, delayed recall)
  - Language: Boston Naming Test, verbal fluency (semantic/phonemic)
- **Fatigue:** Modified Fatigue Impact Scale (MFIS; cutoff ≥38)
- **Neuropsychiatric:** Beck Depression Inventory-II (BDI-II; cutoff ≥19), State-Trait Anxiety Inventory (STAI-S/T; cutoff ≥40), Pittsburgh Sleep Quality Index (PSQI; cutoff >5)
- **Statistical approach:**
  1. Pearson partial correlations (controlling age, education) between FLEI and all scales/tests
  2. Machine-learning regression (linear, ridge, Lasso, ElasticNet, random forest; 80/20 train/test split) to predict FLEI score
  3. Structural equation model mediation analysis: six models (four simple, one parallel, one serial depression→anxiety→fatigue→sleep quality) using lavaan (MLM estimator, 5000 bootstraps, bias-corrected 95% CIs); goodness-of-fit assessed by χ²/df, RMSEA, SRMR, CFI

## Key Findings

### Subjective cognitive complaint profile
- Mean FLEI scores: attention 24.86 ± 7.97; memory 25.71 ± 7.24; executive function 18.36 ± 8.85; mental ability 68.94 ± 22.28
- Dominant complaints: attention and episodic memory; executive function (planning) least reported

### Sex difference — subjective vs. objective dissociation
- **Subjective memory (FLEI-memory):** women 26.65 ± 6.54 vs. men 23.04 ± 8.41, t = −2.948, p = 0.004
- **All other FLEI subscales:** no significant sex difference (mental ability p = 0.064; attention p = 0.072; executive function p = 0.502)
- **Objective neuropsychological scores:** no significant sex difference reported for any test
- Interpretation: women's elevated subjective memory complaints are not accompanied by objectively worse performance — the sex gap is confined to the self-report domain

### Correlations with FLEI (mental ability; partial r, controlling age/education)
- MFIS (fatigue): r = 0.65, p < 0.001 — strongest correlate by far
- BDI-II (depression): r = 0.45, p < 0.001
- STAI-T (trait anxiety): r = 0.43, p < 0.001
- STAI-S (state anxiety): r = 0.30, p < 0.001
- Stroop 1–3: r = −0.31 to −0.33, p < 0.001 (moderate)
- SDMT: r = −0.24, p = 0.001 (low)
- PSQI (sleep quality): r = 0.25, p < 0.001

### Machine-learning prediction of FLEI
- Best model: random forest, R² = 0.409 (10 best features)
- Top predictors: MFIS, BDI-II, and multiple objective cognitive tests (Digit Span Backward, Corsi Backwards, SDMT, ROCF, FCSRT, Stroop A, verbal fluency M/R, VOSP progressive silhouettes)

### Mediation analysis — the causal structure of brain fog
**Simple mediation models** (cognitive function → mediator → FLEI):
| Mediator | Indirect β | p |
|---|---|---|
| Fatigue (MFIS) | −0.340 | < 0.001 |
| Depression (BDI-II) | −0.254 | < 0.01 |
| Anxiety (STAI) | −0.116 | < 0.01 |
| Sleep quality (PSQI) | −0.059 | 0.133 (ns) |

**Parallel model** (all four mediators simultaneously; acceptable fit):
- Total indirect effect: β = −0.394, p < 0.001
- Fatigue indirect path: β = −0.317, p < 0.001 — accounts for ~80% of total indirect effect
- Depression path: not independently significant in this model
- Direct effect of cognitive function on FLEI: β = −0.297, p < 0.05 (partial mediation)

**Serial model** (cognitive function → depression → anxiety → fatigue → sleep → FLEI; good fit: RMSEA = 0.059, CFI = 0.978):
- Total indirect effect: β = −0.42, p < 0.001 (greater than direct effect)
- Dominant indirect path: cognitive function → depression → fatigue → FLEI (β = −0.161, p < 0.001)
- Paths through depression alone (β = −0.069, p = 0.099) and fatigue alone (β = −0.142, p = 0.070) not individually significant in this fuller model
- Conclusion: depression's role in brain fog is mediated through fatigue; the direct depression→FLEI pathway is subordinate

### Other clinical associations with FLEI
- ICU admission: higher mental ability and executive function FLEI scores (more complaints), p = 0.045 / 0.013
- Acute headache: higher attention complaints, p = 0.021
- Olfactory/gustatory symptoms: lower memory complaints (p = 0.047) — slightly counter-intuitive, discussed as possible neuroinflammatory subtype difference

## Relevance

This paper is directly load-bearing for **question:0007** (mechanism of female predominance in PAIS). The subjective-vs-objective sex dissociation observed here — women report more memory complaints but do not perform worse on any objective test — is the clearest neuropsychological evidence in the post-COVID literature that the female cognitive excess is channeled through subjective/affective-fatigue pathways rather than through objectively measurable neuronal deficit. Combined with the mediation finding that fatigue drives brain fog independently of depression, it raises a testable hypothesis: sex differences in PAIS cognitive burden may be explained by sex differences in fatigue burden (and/or fatigue perception), rather than sex differences in underlying neuropathology or objective cognition.

Relevant to **task:t018** (compare female and male PAIS cognitive trajectories using causal-diagram methods): the mediation structure here provides a causal template and a set of specific measured variables (MFIS, BDI-II, FLEI, objective battery) for a sex-stratified causal analysis. The finding that the depression→FLEI path is mediated through fatigue rather than direct suggests that sex differences in fatigue, not depression, should be the primary effect modifier to test.

Relevant to **hypothesis:0001** (shared dysregulated attractor) and **hypothesis:0005** (reproductive-stage immune homeostatic margin) via the indirect pathway: if fatigue is the proximate mediator of brain fog and women have more fatigue-mediated complaints, then immune/neuroimmune drivers of fatigue become the upstream causal locus to investigate.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| FLEI (subjective cognitive complaints / "brain fog") | subjective cognitive subphenotype | Project-relevant target variable for sex stratification |
| MFIS (Modified Fatigue Impact Scale) | fatigue subphenotype | Central fatigue; overlaps conceptually with PEM but measures different construct |
| Mediation: cognitive function → fatigue → FLEI | fatigue as proximate mediator of subjective cognition | Mechanistic bridge between objective deficit and patient-reported outcome |
| Sex difference in FLEI-memory only | female excess in subjective cognitive burden | Key evidence node for q0007 |
| Depression indirect via fatigue | fatigue-depression nexus | Consistent with shared neuroimmune substrate hypothesis |
| No sex difference on objective battery | absent objective sex gap | Argues against sex-differentiated neuropathology as explanation for female excess |

## Limitations

1. **Cross-sectional design:** Cannot establish temporal causation or whether the fatigue-cognition relationship precedes or follows subjective complaint emergence. Longitudinal follow-up of the same battery would be needed to confirm the mediation structure over time.
2. **All patients had cognitive complaints (ascertainment bias):** The sample is a clinical referral cohort, not population-based. Patients without complaints were excluded; this truncates the range of FLEI and may distort correlation magnitudes.
3. **MFIS/FLEI item overlap:** Some MFIS items overlap conceptually with FLEI cognitive-fatigue items; the authors acknowledge this may inflate the observed fatigue-complaint correlation and fatigue's mediating role.
4. **Sex difference interpretation limited by no immune/hormonal data:** No estrogen, menopausal status, hormonal contraceptive, or immune-profiling data available; the subjective-vs-objective sex gap is documented but its upstream cause (sex-differentiated fatigue biology, reporting bias, or both) cannot be resolved from this data.
5. **Single center (Madrid), predominantly women (73%):** The male subsample is small (~46 men), reducing statistical power to detect sex differences on objective tests; a true null on objective tests cannot be confidently established with this sample size.
6. **No no-COVID control group:** Cannot assess whether fatigue mediates brain fog specifically in post-COVID or is a general property of cognitive-complaint presentations; limits causal specificity.
7. **Executive function battery incomplete:** No tower test (planning) included, despite executive planning being one of the FLEI domains; visuospatial executive items may be better captured.
8. **Medication confounding:** 29% were on antidepressants and 19% on benzodiazepines at assessment; these could affect both subjective and objective cognitive measures, and the analysis does not stratify or adjust for current psychotropic use.
9. **No sex-stratified mediation analysis conducted:** The reported mediation is in the full pooled sample. Whether the fatigue-mediation path has a larger indirect effect in women vs. men is not tested directly.

## Model / Tool Availability

No model, tool, or dataset is released. Data available from the corresponding author on reasonable request.

## Follow-up

- **Direct next step for q0007 / t018:** Run a sex-stratified mediation analysis (or a moderated mediation with sex as moderator of the cognition→fatigue→FLEI indirect path) in this or a similar dataset to quantify whether the fatigue-mediation indirect effect is larger in women.
- **Immune link:** Pair this design with immune marker data (e.g., IL-6, NK cell exhaustion, cortisol) to test whether fatigue-mediation strength tracks neuroimmune activation markers and whether sex moderates that relationship.
- **Longitudinal replication:** The same group has published related cross-sectional work (Delgado-Alonso 2022, J Psychiatr Res) and neuroimaging data (Diez-Cirarda 2022, Brain). A longitudinal extension tracking FLEI and MFIS changes with symptom recovery would test whether fatigue recovery precedes subjective cognitive recovery (as predicted by the mediation structure).
- **Cross-PAIS generalization:** Test whether the fatigue-as-mediator structure replicates in ME/CFS, post-Lyme, or post-dengue neuropsychological studies, which could support a shared mechanism rather than a COVID-specific one.
