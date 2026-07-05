---
id: interpretation:0020-t045-neuhouser2024-whi-hrt-gap-triage
kind: interpretation
title: "t045: Neuhouser2024 WHI long-COVID risk screen does not adjudicate the HRT evidence gap"
status: active
source_refs:
  - paper:Neuhouser2024
related:
  - task:t045
  - paper:Neuhouser2024
  - interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test
  - interpretation:0003-t018-subphenotype-sex-reproductive-stage
  - proposition:0006-hormone-therapy-effects-on-pais-are-context-dependent
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - topic:menopause-sex-hormones-and-pais-risk
created: '2026-06-25'
updated: '2026-06-25'
input:
  - paper:Neuhouser2024
prior_interpretations:
  - interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test
  - interpretation:0003-t018-subphenotype-sex-reproductive-stage
relations: []
---

<!-- Mode: CONCEPTUAL / LITERATURE. Input is the Neuhouser2024 WHI long-COVID risk-factor paper and its accessible full text; the supplementary docx was attempted but blocked by PMC reCAPTCHA. -->

# Interpretation: t045 - Neuhouser2024 WHI HRT-gap triage

## Verdict

**[⌀] Non-adjudicating.** Neuhouser2024 corrects the prior wording that "even WHI did not analyze long COVID" because WHI now has a published long-COVID risk-factor analysis in postmenopausal women. But it does **not** become the first WHI-grade HRT-vs-long-COVID evidence-line: menopausal hormone therapy is not in the article text, not among the reported top-20 machine-learning predictors, and no HRT/MHT odds ratio or null estimate is reported.

The residual uncertainty is narrower than before. The inaccessible Supplementary Table S1 prevents confirming whether MHT was in the 447-variable candidate pool and failed selection, or was never included [@Neuhouser2024]. Either way, the published result is not an admissible HRT effect estimate.

## Findings

1. **WHI long-COVID risk screen exists.** Among 37,280 WHI COVID survey respondents, 1,237 postmenopausal women reported a positive COVID-19 test and 425 met the study long-COVID definition of new symptoms lasting at least 8 weeks.

2. **The reported risk-factor signal is health/function, not hormone therapy.** The top selected predictors include recent weight loss, physical/mobility limitations, sleep disturbance, rheumatoid arthritis, heart-valve procedures, and related health/function variables. MHT/HRT is absent from the main text and reported top-20 list.

3. **No HRT evidence-line is warranted.** A top-20 omission from a machine-learning screen is not a modeled null, and without Supplementary Table S1 there is no basis to say MHT was examined. Coding a null would overstate the paper.

## Graph Disposition

- Add `paper:Neuhouser2024` and this interpretation as the durable triage record.
- Update `interpretation:0008`: the t019 gap verdict stands, but the "un-ingested lead" is now resolved as a non-adjudicating WHI risk screen.
- Update `interpretation:0003`'s matrix row: WHI long-COVID risk data exist, but not an HRT effect estimate.
- Leave `proposition:0006` belief unchanged; add Neuhouser2024 to prose context only, not as an evidence-line.

## Implication

The route to a real HRT test remains the same: a WHI/UKB/All-of-Us style design that explicitly models HRT exposure with route, dose, timing, indication, and active-comparator/new-user handling. Neuhouser2024 demonstrates WHI's value as a pre-infection baseline cohort, but its published risk-screen output does not discharge that design.
