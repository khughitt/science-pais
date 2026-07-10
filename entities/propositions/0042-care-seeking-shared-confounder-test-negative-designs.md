---
id: proposition:0042-care-seeking-shared-confounder-test-negative-designs
kind: proposition
title: Care-seeking behavior is a shared confounder inflating apparent post-COVID
  risk in test-negative control designs
status: active
claim_layer: structural_claim
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
source_refs:
- paper:Nilforoshan2026
- paper:Sudre2024
created: '2026-07-10'
updated: '2026-07-10'
---
# Proposition: Care-seeking behavior is a shared confounder inflating apparent post-COVID risk in test-negative control designs

## Claim

Care-seeking / health-utilization propensity is a **shared confounder** of both COVID-testing exposure and post-acute outcomes, so conventional long-COVID designs that compare tested-positive individuals against never-tested or unmatched controls attribute a large share of an ascertainment-driven signal to infection. Switching the comparator to a PCR-*negative* (test-based) control — matched on the act of seeking a test — removes most of the apparent effect. This is the forward reading of `hypothesis:0008` at the confounding-structure level.

## Evidence Summary

`paper:Nilforoshan2026` supplies the direct structural demonstration on 14.4 billion claims / 244.7M patients: replacing never-tested with PCR-negative controls drops the negative-control-outcome false-positive rate from 53.1% to 4.1%, and — decisively — a negative-control-*exposure* analysis shows PCR-negative individuals themselves carry elevated long-term risk that correlates (Spearman r=0.48) with the effects conventional designs attribute to COVID, i.e. shared care-seeking vulnerability, not infection, drives much of the conventional signal. `paper:Sudre2024` localizes the same channel to the individual: 32.6% of long-illness cases were symptomatic pre-COVID (OR 2.14 for any baseline symptom) and baseline symptom burden predicts post-COVID burden (+5.6% per symptom) — a pre-morbid / reporting-continuity vulnerability that co-determines both testing and reported outcomes.

## Caveats

The claim bounds, but does not eliminate, a real infection effect: Nilforoshan2026's population return-to-baseline is a *mean* under a conservative RR ≥ 1.1 + Bonferroni threshold that by construction misses small (RR 1.0–1.1) effects and does not stratify by severity or subgroup, and Sudre2024 finds 67.4% of long-illness cases were pre-COVID *asymptomatic* — so care-seeking confounding cannot explain all long illness. The two supporting papers use non-overlapping measurement channels (claims-coded billing events vs. self-report), which agree on direction but not on residual magnitude. Care-seeking confounding is also entangled with the host-reserve gate (`hypothesis:0020`): EHR reserve proxies are themselves ascertainment-shaped.
