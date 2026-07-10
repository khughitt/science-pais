---
id: evidence-line:0091-sudre2024-baseline-symptom-continuity-supports-care-seeking-confounder
kind: evidence-line
title: Sudre2024 pre-morbid symptom continuity supports care-seeking confounding
status: active
stance: supports
target: proposition:0042-care-seeking-shared-confounder-test-negative-designs
source: paper:Sudre2024
strength: moderate
independence: independent
independence_group: sudre2024-baseline-symptom-cohort
evidence_role: proxy_support
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
source_refs:
- paper:Sudre2024
created: '2026-07-10'
updated: '2026-07-10'
evidence_type: literature_evidence
---
# Evidence Line: Sudre2024 pre-morbid symptom continuity supports care-seeking confounding

## What this line shows

`paper:Sudre2024` localizes a shared-vulnerability channel to the individual: 32.6% of long-illness cases were already symptomatic pre-COVID (OR 2.14 for any baseline symptom), and baseline symptom burden predicts post-COVID burden (+5.6% per symptom) [@Sudre2024]. A pre-morbid symptom / reporting-continuity propensity that co-determines both testing/care-seeking and reported post-acute outcomes is exactly the confounding structure `proposition:0042` asserts, giving `proxy_support` from a self-report cohort.

## Why it is independent

This line is a community self-report cohort with within-person pre-COVID baselines — a different measurement channel and subject pool from the population claims analysis in `evidence-line:0090` (Nilforoshan2026). Its individual-level baseline-symptom mechanism is not derivable from claims data, so it independently corroborates the confounder rather than restating the same analysis.

## Caveats / scope

`proxy_support`, moderate. The baseline-symptom channel is a *proxy* for care-seeking/reporting propensity, not a direct measure of it, and the data are entirely self-report (subject to reporting continuity and recall). Critically, Sudre2024 also finds 67.4% of long-illness cases were pre-COVID *asymptomatic* — so this channel explains part, not all, of long illness, and this line must not be read as showing long-COVID is mostly artifact.
