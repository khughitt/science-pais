---
id: interpretation:0026-t043-boneva2015-early-menopause-directionality
type: interpretation
title: "t043: Boneva2015 early-menopause signal is partly antecedent-surgical, not a clean forward or reverse causal test"
status: active
source_refs:
  - paper:Boneva2015
related:
  - task:t043
  - paper:Boneva2015
  - interpretation:0003-t018-subphenotype-sex-reproductive-stage
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold
  - proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing
  - evidence-line:0081-boneva2015-early-surgical-menopause-weakly-supports-stage-threshold
  - evidence-line:0082-boneva2015-surgery-precedes-cfs-disputes-simple-reverse-causation
  - topic:menopause-sex-hormones-and-pais-risk
created: '2026-06-26'
updated: '2026-06-26'
input:
  - paper:Boneva2015
prior_interpretations:
  - interpretation:0003-t018-subphenotype-sex-reproductive-stage
relations:
  - predicate: "sci:amends"
    target: "interpretation:0003-t018-subphenotype-sex-reproductive-stage"
---

<!-- Mode: CONCEPTUAL / LITERATURE. Input is Boneva2015 and the t018 reproductive-stage matrix. -->

# Interpretation: t043 - Boneva2015 early-menopause directionality

## Verdict

**[~] Partly informative, still non-adjudicating.** Boneva2015 should not be left as "purely reverse-causation ambiguous." The dated-surgery subset shows hysterectomy/oophorectomy preceded CFS onset in 71% of women with both dates, which weakly favors an antecedent gynecologic/surgical-menopause component over a blanket "CFS caused early menopause" explanation.

But the result is not a clean predisposition test. The strongest timing handle is surgical, not natural menopause; CFS onset is not infection onset; and gynecologic disease/surgery indications may be shared vulnerability, mediator, confounder, or ascertainment. The right graph disposition is weak proxy support for `proposition:0001` plus weak model criticism against the simplest reverse reading of `proposition:0003`, with no h0005 promotion.

## Findings

1. **The stage signal is real within the study.** CFS cases had earlier menopause than controls and more gynecologic disorders/surgeries. This remains the strongest non-COVID reproductive-stage signal from `interpretation:0003`.

2. **Directionality is asymmetric, not unknowable.** If all early menopause were downstream of CFS, dated hysterectomy/oophorectomy would not commonly precede CFS onset. Boneva reports the opposite for 71% of the dated-surgery subset.

3. **The result mainly localizes the problem to surgical/gynecologic pathways.** The temporal result is not a pre-infection natural-menopause baseline. It may indicate that endometriosis/pelvic pain/bleeding and surgery are upstream risk markers, that surgery/hormone withdrawal contributes to vulnerability, or that a shared underlying process drives both gynecologic morbidity and later CFS.

## Graph Disposition

- Add `paper:Boneva2015`.
- Add `evidence-line:0081` as weak `proxy_support` for `proposition:0001`.
- Add `evidence-line:0082` as weak shared-source `model_criticism` against `proposition:0003`'s simple reverse-causation reading.
- Update `interpretation:0003` to remove t043 as an open question and replace the "reverse-causation plausible" shorthand with the narrower verdict above.
- Leave h0005 at its current belief band; the evidence is too indirect, surgical-pathway-heavy, and non-post-infection-specific to promote.

## Implication

Boneva2015 narrows the t043 ambiguity but does not close the h0005 causal question. The decisive design remains the pre-infection/staged cohort logic already represented by `task:t028`, `task:t039`, and `task:t040`: time-index reproductive stage and hormones before infection, or at least before PAIS onset, then separate natural menopause, surgical menopause, gynecologic indications, hormone therapy, age, and ascertainment.
