---
id: paper:Neuhouser2024
kind: paper
title: Risk factors for long COVID syndrome in postmenopausal women with previously reported diagnosis of COVID-19
status: active
ontology_terms:
  - long COVID
  - post-acute sequelae of SARS-CoV-2
  - postmenopausal women
  - Women's Health Initiative
  - risk factors
  - machine learning
  - hormone therapy
dataset_usage: []
datasets: []
source_refs:
  - cite:Neuhouser2024
related:
  - task:t045
  - interpretation:0020-t045-neuhouser2024-whi-hrt-gap-triage
  - interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test
  - interpretation:0003-t018-subphenotype-sex-reproductive-stage
  - proposition:0006-hormone-therapy-effects-on-pais-are-context-dependent
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - topic:menopause-sex-hormones-and-pais-risk
created: '2026-06-25'
updated: '2026-06-25'
---
# Risk factors for long COVID syndrome in postmenopausal women with previously reported diagnosis of COVID-19

- **Authors:** Marian L. Neuhouser, Hamza Islam Butt, Chengcheng Hu, Aladdin H. Shadyab, Lorena Garcia, Shawna Follis, Charles Mouton, Holly R. Harris, Jean Wactawski-Wende, Emily W. Gower, Mara Vitolins, Diane Von Ah, Rami Nassir, Shama Karanth, Ted Ng, Electra Paskett, JoAnn E. Manson, Zhao Chen
- **Year:** 2024
- **Journal:** Annals of Epidemiology, 98, 36-43
- **DOI:** 10.1016/j.annepidem.2024.08.003
- **PMID:** 39142425
- **PMCID:** PMC11405002
- **BibTeX key:** Neuhouser2024
- **Source:** PMC manuscript full text; supplementary docx access attempted but blocked by reCAPTCHA

## Key Contribution

This WHI analysis uses decades of pre-COVID demographic, health, psychosocial, functional, and lifestyle data to screen risk factors for long COVID among postmenopausal women with self-reported positive COVID tests. It is valuable for PAIS work because it is a longitudinal cohort with deep pre-infection history in an older female population, not a post-COVID clinic sample.

For `task:t045`, the key triage result is negative-for-reporting rather than null-for-effect: menopausal hormone therapy is not named in the article text, not among the reported top-20 machine-learning predictors, and no HRT/MHT effect estimate is reported. Because the Supplementary Table S1 full candidate-feature list was not accessible during this pass, the paper cannot be coded as an examined MHT null.

## Methods

- **Design:** WHI cohort risk-factor analysis using gradient boosted classification trees to select candidate predictors, followed by logistic regression.
- **Population:** 37,280 WHI COVID survey respondents; 1,237 postmenopausal women reported a positive COVID-19 test; 425 met the study's long-COVID definition.
- **Outcome:** binary long COVID using new symptoms after COVID diagnosis lasting 8 weeks or longer.
- **Candidate feature pool:** 447 variables spanning sociodemographic characteristics, lifestyle, psychosocial/quality-of-life variables, functional status, and self-reported/adjudicated health outcomes collected from WHI enrollment through 2020.
- **Reported model path:** machine learning selected the top 20 variables; logistic regression then evaluated those selected variables.

## Key Findings

- Long-COVID cases reported common persistent symptoms including fatigue, malaise, memory problems, and brain fog.
- The reported top predictors were dominated by recent weight loss, mobility/physical-function limitations, sleep disturbance, rheumatoid arthritis, heart-valve procedures, and related health/function variables.
- Menopausal hormone therapy is absent from the reported top-20 predictors and from the article text.

## Relevance

This paper does **not** close the HRT evidence gap identified by `interpretation:0008`: it supplies a WHI long-COVID risk-factor screen, not a route/dose/timing/indication-resolved HRT exposure model. It corrects the prior overstatement that WHI had not analyzed long COVID in postmenopausal women, but it leaves the causal HRT-to-PAIS question untested in the graph.

## Limitations

- COVID diagnosis and long-COVID symptoms were self-reported.
- Only survey respondents are included; response selection may affect prevalence and associations.
- Long COVID was defined as symptoms lasting at least 8 weeks, not the full WHO 3-month threshold.
- The machine-learning design reports only the top selected variables; an unselected variable is not equivalent to a modeled null.
- Supplementary Table S1 was needed to determine whether MHT was among the 447 candidates, but the PMC supplement download was blocked by reCAPTCHA during this pass.
