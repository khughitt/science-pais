---
id: evidence-line:0057-bramante2026-activ6-metformin-partial-replication-supports-0021
type: evidence-line
title: "Bramante2026 ACTIV-6 — acute metformin partially replicates the long-COVID prevention signal (clinician-diagnosis halved) but misses its primary symptom endpoint"
status: active
stance: supports
target: proposition:0021-acute-antigen-burden-determines-pais-incidence
source: paper:Bramante2026
strength: weak
independence: independent
independence_group: activ6-metformin-prevention
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: interventional
related:
- proposition:0021-acute-antigen-burden-determines-pais-incidence
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0012-prevention-vaccination-antiviral-reduces-pais
source_refs:
- paper:Bramante2026
created: '2026-06-24'
updated: '2026-06-24'
---
# Evidence Line: Bramante2026 (ACTIV-6) — partial replication of metformin prevention

## What this line shows

The ACTIV-6 platform RCT (acute outpatient COVID, mITT n=2983) is an independent test of acute-phase
metformin for PAIS prevention. The **primary 6-month symptom endpoint was not met** (posterior
probability of efficacy 0.83, below the 0.975 threshold), but the **clinician-diagnosed long-COVID
endpoint at day 180 was approximately halved** (RR 0.50, 95% CrI 0.16–0.99; PPE 0.96). The direction
matches COVID-OUT (`0056`), so it supports `proposition:0021` — but weakly, as a *partial* replication [@Bramante2026].

## Why it is independent

`independence: independent` — separate platform, sites, and (largely JN.1-era, highly immune)
population from COVID-OUT; same agent, different trial. Two independent prevention RCTs agreeing in
direction is the basis for treating the prevention signal as real.

## Caveats / scope

**Weak** because of the **mixed endpoint result**: the pre-specified primary symptom outcome did not
cross its efficacy bar, and the benefit was attenuated relative to COVID-OUT — plausibly because the
highly vaccinated/previously-infected population already had low baseline PAIS risk. Same antigen-vs-
metabolic mechanistic ambiguity as `0056` (the protective lever is not demonstrably *antigen* clearance),
and same prevention-not-reversibility scope. Net: corroborates a real but modest acute-phase prevention
effect without resolving whether antigen burden specifically is the operative determinant.
