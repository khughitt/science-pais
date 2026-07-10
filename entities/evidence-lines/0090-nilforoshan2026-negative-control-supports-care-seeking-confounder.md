---
id: evidence-line:0090-nilforoshan2026-negative-control-supports-care-seeking-confounder
kind: evidence-line
title: Nilforoshan2026 negative-control designs support care-seeking as a shared confounder
status: active
stance: supports
target: proposition:0042-care-seeking-shared-confounder-test-negative-designs
source: paper:Nilforoshan2026
strength: strong
independence: independent
independence_group: nilforoshan2026-claims-negative-control
evidence_role: direct_test
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
source_refs:
- paper:Nilforoshan2026
created: '2026-07-10'
updated: '2026-07-10'
evidence_type: literature_evidence
---
# Evidence Line: Nilforoshan2026 negative-control designs support care-seeking as a shared confounder

## What this line shows

`paper:Nilforoshan2026` directly demonstrates the shared-confounder structure on 14.4 billion claims from 244.7M US patients. Two negative-control analyses do the work: a negative-control-*outcome* check shows switching from never-tested to PCR-negative controls drops the false-positive rate on biologically implausible outcomes from 53.1% to 4.1%; and a negative-control-*exposure* analysis shows PCR-negative individuals themselves carry elevated long-term risk that correlates (Spearman r=0.48) with the effects conventional designs attribute to COVID [@Nilforoshan2026]. Together these isolate care-seeking / health-utilization propensity — not infection — as a driver of much of the conventional long-COVID signal, a `direct_test` of `proposition:0042`.

## Why it is independent

This line rests on a claims-coded (billing-event) measurement channel at population scale, methodologically distinct from the self-report community-cohort channel of `evidence-line:0091` (Sudre2024). The two channels do not share subjects, ascertainment mechanism, or outcome definition, so their agreement on the confounding direction is genuinely independent corroboration rather than shared-source repetition.

## Caveats / scope

`direct_test`, strong, but bounding rather than eliminating a real infection effect. The population return-to-baseline is a *mean* under a deliberately conservative RR ≥ 1.1 + Bonferroni threshold that by construction misses small (RR 1.0–1.1) effects and does not stratify by severity, vaccination, or subgroup — so it cannot exclude a real, small chronically-affected stratum. Outcomes are claims-coded billing events, not validated phenotypes. This line supports that care-seeking confounding is *large*, not that long-COVID is *entirely* artifact.
