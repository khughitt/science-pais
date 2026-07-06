---
id: paper:Gandhi2023
kind: paper
title: Post-viral sequelae of COVID-19 and influenza
status: active
ontology_terms:
- post-acute sequelae
- post-viral syndrome
- long COVID
- post-influenza syndrome
- encephalitis lethargica
- chronic immune activation
- multisystem morbidity
- ICD-10 outcome ascertainment
dataset_usage: []
source_refs:
- cite:Gandhi2023
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# Post-viral sequelae of COVID-19 and influenza

- **Authors:** Monica Gandhi
- **Year:** 2023
- **Journal:** The Lancet Infectious Diseases, vol. 24, no. 3, pp. 218–219
- **DOI:** 10.1016/S1473-3099(23)00762-4
- **BibTeX key:** Gandhi2023
- **Source:** PDF

## Key Contribution

This invited Comment contextualizes the Al-Aly/Xie et al. VA cohort study (Lancet Infect Dis 2023, DOI: 10.1016/S1473-3099(23)00684-9) comparing long-term health outcomes after hospitalization for COVID-19 versus seasonal influenza. Gandhi argues that while COVID-19 carries a higher burden of post-acute sequelae across most organ systems, the high rate of sequelae in both groups is the most clinically important finding — establishing that severe respiratory viral illness per se, not SARS-CoV-2 specifically, is a potent driver of post-viral pathology. The comment situates this within more than a century of recognized post-viral syndromes and calls for cross-pathogen pathophysiology research and treatment development.

## Methods

This is a commissioned Comment piece, not an original study. Gandhi summarizes and critically evaluates the methodology of the underlying Al-Aly/Xie et al. cohort study:

- **Index study design:** Retrospective cohort study using the US Department of Veterans Affairs (VA) healthcare database.
- **COVID-19 cohort:** 81,280 participants hospitalized for COVID-19 between March 1, 2020, and June 30, 2022 (sub-stratified by pre-delta, delta, and omicron variant eras).
- **Influenza cohort:** 10,985 participants hospitalized for seasonal influenza between October 1, 2015 and February 28, 2019.
- **Outcome ascertainment:** 94 pre-specified health outcomes defined by ICD-10 diagnosis codes, grouped across 10 organ systems (cardiovascular, coagulation/haematological, fatigue, gastrointestinal, kidney, mental health, metabolic, musculoskeletal, neurological, pulmonary).
- **Comparison period:** Non-contemporaneous by necessity — influenza rates dropped dramatically during COVID-19 pandemic due to viral interference and public health measures.

## Key Findings

**From the Al-Aly/Xie et al. study as reported in this Comment:**

- Excess death rate in COVID-19 vs. influenza: **8.62 per 100 persons** (95% CI 7.55–9.44).
- COVID-19 cohort had higher risk of hospital readmission vs. seasonal influenza (HR 1.11; 95% CI 1.08–1.13).
- COVID-19 showed increased risk of adverse health outcomes in **9 of 10 organ systems** vs. influenza; most prominent excess in gastrointestinal and musculoskeletal systems.
- Exception: the pulmonary system showed *higher* longer-term burden in the seasonal influenza cohort.
- Cumulative adverse health outcome rate: **615.18 per 100 persons** (95% CI 605.17–624.88) in COVID-19 vs. **536.90 per 100 persons** (95% CI 527.38–544.90) in seasonal influenza.

**Gandhi's critical evaluation and broader synthesis:**

1. **"For vs. with" COVID bias:** During the omicron era (when most patients were vaccinated or previously infected), universal inpatient SARS-CoV-2 screening captured patients hospitalized for other reasons who tested positive — potentially inflating COVID-19 sequelae counts. The Society of Healthcare Epidemiology did not recommend against routine asymptomatic screening until December 2022, six months after the study period ended.
2. **Ascertainment asymmetry:** The influenza cohort was not systematically screened on admission (unlike the COVID-19 cohort), creating differential detection that may undercount influenza admissions.
3. **Reporting bias:** Heightened public awareness of post-viral syndromes after COVID-19 may have increased symptom reporting and diagnostic testing in that cohort, inflating apparent sequelae burden relative to pre-pandemic influenza.
4. **Historical depth of post-viral syndromes:** Gandhi documents that post-viral sequelae are not a COVID-19 novelty — they were first described after the 1918 influenza pandemic ("encephalitis lethargica," a syndrome of marked lethargy with neurological features); subsequent examples include post-EBV, post-CMV, post-HSV, post-measles (all with chronic inflammation and elevated antibody titres), and HIV-related chronic immune activation.
5. **Comparable burden across severe infections:** A large Ontario study (Quinn et al., JAMA Intern Med 2023, n not specified in Comment) found that post-acute medical and mental health burden after COVID-19 hospitalization was comparable to that of other acute infectious illnesses including influenza and sepsis.
6. **Severity dependence:** Hospital admission for SARS-CoV-2 (severe illness) carries much higher long-term risk than mild COVID-19 illness (citing Xie, Bowe, Al-Aly, Nat Commun 2021).

## Relevance

This Comment connects directly to the project research question — *"Why do some people fail to recover after acute infection, and what shared mechanisms link the post-acute infection syndromes?"* — through several threads:

1. **Severity as a homeostatic threshold:** The observation that severe illness (requiring hospitalization) drives substantially worse post-acute sequelae than mild illness directly implicates acute-phase physiological insult magnitude as a determinant of homeostatic recovery failure. The 8.62/100-person excess mortality and ~15% higher cumulative multisystem morbidity in COVID-19 vs. influenza map onto the project's working frame that more severe initial dysregulation raises the probability of failing to return to baseline.

2. **Cross-pathogen generalizability:** Gandhi's historical framing — post-1918-influenza encephalitis lethargica, post-EBV/CMV/HSV/measles syndromes, HIV chronic immune activation — reinforces the project's core claim that failed homeostatic recovery is a *shared failure mode* across diverse pathogens, not a SARS-CoV-2 idiosyncrasy. The convergence of COVID-19 and influenza sequelae at the severe-illness end of the spectrum is particularly relevant: two antigenically unrelated RNA viruses produce overlapping multi-organ sequelae patterns, pointing to host-mediated mechanisms rather than pathogen-specific ones.

3. **Organ-system specificity as a constraint on mechanism:** The divergence between COVID-19 (excess GI + musculoskeletal burden) and influenza (excess pulmonary burden) at the organ-system level suggests that while shared failure modes exist, pathogen-specific tropism or tissue damage patterns modulate *which* homeostatic failure predominates. This nuance is relevant to the project's working frame of "partly convergent, partly trigger-specific" mechanisms.

4. **Methodological flags for VA-database/ICD-10 studies:** The "for vs. with" COVID ascertainment problem and the asymmetric screening issue are directly transferable cautions for any future computational analyses using administrative health data in this project.

5. **Call for treatment research:** Gandhi's closing call for "comprehensive studies into the pathophysiology of post-viral syndromes, along with investigation of non-pharmaceutical and pharmaceutical treatments" resonates with the project's translational orientation.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Post-acute sequelae of COVID-19 / influenza | post-acute infection syndrome (PAIS) | Gandhi uses "post-viral sequelae" and "post-acute sequelae" — aligns with project umbrella term |
| Severe viral illness requiring hospitalization | acute-illness severity as PAIS risk factor | The hospitalization threshold approximates the high-severity end of the acute-insult spectrum |
| Post-1918-influenza encephalitis lethargica | historical post-viral syndrome | Prototype of failed neurological recovery after severe acute infection; neurological PAIS subtype |
| Chronic inflammation + elevated antibody titres (EBV, CMV, HSV, measles) | persistent immune activation | Named mechanism across pathogen classes; maps to project's "immune dysregulation" node |
| HIV chronic immune activation | persistent immune activation | Retroviral model of chronic immune dysregulation; mechanistically related to PAIS immune axis |
| Cumulative multi-organ morbidity (615/100 persons, COVID) | multi-system dysfunction | Quantifies the multisystem burden of failed homeostatic recovery post-hospitalization |
| "For COVID" vs. "with COVID" classification bias | case-definition problem in PAIS research | Methodological challenge relevant to any administrative-data PAIS study |
| Pulmonary-excess in influenza vs. GI/musculoskeletal-excess in COVID | trigger-specific vs. shared failure mode | Organ-tropism differences within a shared post-viral failure framework |
| Comparable burden across COVID, influenza, and sepsis (Ontario study) | PAIS as a cross-trigger shared phenomenon | Strongest evidence that post-acute sequelae are an acute-illness-severity effect, not SARS-CoV-2-specific |

## Limitations

- **Comment format:** This is a 2-page editorial Comment — no primary data, no methods section, no statistical analyses. All quantitative findings are drawn from the Al-Aly/Xie et al. study; the Comment's contribution is framing and critique, not new evidence.
- **Incomplete access to the primary study:** The Comment summarizes selected findings from the Al-Aly/Xie et al. cohort; detailed hazard ratios, covariate adjustment, and variant-era sub-analyses require reading the primary article.
- **VA population caveat (not raised by Gandhi):** The VA database is predominantly male, older, and with high comorbidity burden — limiting generalizability to younger, female, or otherwise healthier populations who may show different PAIS profiles.
- **Non-contemporaneous comparison not fully resolved:** Gandhi acknowledges the temporal mismatch between cohorts but does not quantify the potential confounding introduced by secular trends in hospitalization practices, variant differences in pathogenicity, or changes in standard-of-care over time.
- **ICD-10 outcome limitation:** Gandhi correctly flags that ICD-10 codes may capture conditions not causally related to the index respiratory infection, and that COVID-19 awareness inflated symptom reporting — but no correction or sensitivity analysis is available from this Comment.
- **No mechanistic discussion:** The Comment references chronic immune activation and inflammation as established mechanisms for other post-viral syndromes but does not synthesize mechanistic hypotheses for COVID-19 or influenza sequelae specifically.

## Model / Tool Availability

Not applicable. This is an invited editorial Comment; no dataset, model, or software tool is released.

## Follow-up

- Read the primary Al-Aly/Xie et al. cohort study (DOI: 10.1016/S1473-3099(23)00684-9) for full variant-era stratified results, hazard ratios per organ system, and covariate adjustment details — this Comment provides only a subset of the findings.
- Compare with Quinn et al. 2023 (JAMA Intern Med 183:806–17) on post-hospitalization sequelae across COVID-19, influenza, and sepsis in Ontario — cited by Gandhi as showing comparable burden.
- The historical note on encephalitis lethargica post-1918-influenza warrants follow-up: Hoffman & Vilensky (Brain 2017; 140:2246–51) on mechanisms and parallels to modern PAIS.
- The "for vs. with" COVID classification issue (Kushner et al., Hosp Pediatr 2021) is relevant to any project analyses using hospital administrative data — document as a methodological caution.
- Consider whether the organ-system divergence (influenza-excess pulmonary, COVID-excess GI/musculoskeletal) can be interrogated in available PAIS transcriptomic or proteomics datasets to identify pathogen-specific vs. shared post-viral signatures.
