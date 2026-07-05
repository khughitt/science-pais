---
id: interpretation:0016-t054-abrocitinib-trial-status-snapshot
kind: interpretation
title: "t054 - NCT06597396/CLEAR-LC abrocitinib registry-status snapshot: primary completion passed, no posted results, pre-registration:0004 remains data-gated"
status: active
source_refs: []
related:
- hypothesis:0003-immune-exhaustion-feedback
- question:0006-jak-stat-il6-driver-vs-marker
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- pre-registration:0004-jak1-inhibitor-driver-vs-marker
- topic:long-covid-immune-dysregulation
- topic:therapeutics-and-clinical-trials
- task:t054
created: '2026-06-25'
updated: '2026-06-25'
input: []
prior_interpretations:
- interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration
relations:
- predicate: "sci:amends"
  target: "interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration"
---
# Interpretation: t054 - NCT06597396/CLEAR-LC abrocitinib registry-status snapshot

## Verdict

**Verdict:** `[?]` still inconclusive-for-coverage. As of the ClinicalTrials.gov API snapshot accessed
2026-06-25, NCT06597396/CLEAR-LC has **no posted results** (`hasResults: false`). The trial is
`ACTIVE_NOT_RECRUITING`; primary completion is listed as **2026-03-27 (actual)** and study completion as
**2026-09-30 (estimated)**. Therefore `pre-registration:0004` does **not** activate: no supporting or
disputing evidence-line should be added to `proposition:0026`, `question:0006`, or `hypothesis:0003`.

Primary source checked: ClinicalTrials.gov API v2 record for NCT06597396
(`https://clinicaltrials.gov/api/v2/studies/NCT06597396`; public study page
`https://clinicaltrials.gov/study/NCT06597396`).

## Registry Facts

The registry record describes CLEAR-LC as a phase 2a randomized, dose-ranging, triple-masked,
parallel-group, placebo-controlled trial of oral abrocitinib in non-hospitalized adults with severe
fatigue from post-COVID condition/long COVID. Key fields:

| Field | Registry value |
|---|---|
| Overall status | `ACTIVE_NOT_RECRUITING` |
| Enrollment | 46 actual |
| Start date | 2024-12-27 actual |
| Primary completion | 2026-03-27 actual |
| Study completion | 2026-09-30 estimated |
| Last update posted | 2026-04-20 |
| Arms | abrocitinib 50 mg daily, abrocitinib 100 mg daily, placebo |
| Treatment duration | 12 weeks / 84 days |
| Primary endpoint | FACIT-Fatigue change from baseline to Day 84 |
| Secondary symptom/health endpoints | EQ-5D-5L, PASC Symptom PRO, safety/labs |
| Posted inflammatory biomarker endpoint | high-sensitivity C-reactive protein (hsCRP), baseline to Day 84 |
| Results | none posted (`hasResults: false`) |

## Gate Audit

Against `pre-registration:0004`'s Vehicle-Admissibility Gate:

- **G1 symptom co-primary:** likely satisfied by the FACIT-Fatigue primary endpoint and PASC Symptom PRO
  secondary endpoint.
- **G2 target engagement:** **not yet satisfied from the registry alone.** The posted biomarker endpoint is
  hsCRP, which is a nonspecific inflammatory marker. The pre-registration's load-bearing target-engagement
  criterion asks for IL-6R / JAK-STAT pathway score / downstream ISG suppression. A future paper or
  supplement may report those assays, but the registry endpoint list does not guarantee them.
- **G3 controlled design:** satisfied by randomized placebo-controlled triple-masked design.
- **G4 endotype resolution:** not visible in the registry fields; no inflammatory-signature enrichment or
  stratification is specified in the public endpoint list.
- **G5 adequacy:** not yet judgeable. Enrollment is 46 actual across three arms; adequacy depends on the
  analysis plan/effect size and whether biomarker-positive subgroups are reported.

Net: the trial remains a plausible vehicle, but the current public registry record is not an admissible
readout and may not, by itself, discharge the target-engagement/endotype parts of the pre-registration.

## Consequence

`proposition:0026` stays `speculative`; `hypothesis:0003` stays capped by its untested causal-loop
conjunct. `task:t054` should remain open/blocked until a posted ClinicalTrials.gov results table, paper,
preprint, or sponsor/investigator readout reports symptom outcomes and enough pathway-engagement detail to
apply the locked decision criteria.
