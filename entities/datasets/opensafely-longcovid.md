---
id: dataset:opensafely-longcovid
type: dataset
title: "OpenSAFELY — English primary-care EHR (COVID / long COVID)"
status: candidate
origin: external
dataset_class: pointer
source_class: observational
tier: evaluate-next
license: proprietary
update_cadence: rolling
access:
  level: controlled
  availability: available
  verified: true
  verification_method: landing-confirmed
  last_reviewed: "2026-07-01"
  source_url: "https://www.opensafely.org/"
accessions: []
ontology_terms: [long-covid, sars-cov-2, ehr, primary-care, population-based, computable-phenotype, sex-differences, autoimmune, ascertainment-bias]
related:
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - question:0007-mechanism-of-female-predominance-in-pais
  - dataset:n3c-recover-longcovid
source_refs:
  - cite:Williamson2020
  - cite:Andrews2022
  - cite:WalkerLongCOVID2021
created: "2026-07-01"
updated: "2026-07-01"
---

# OpenSAFELY — English primary-care EHR (COVID / long COVID)

## Summary

Federated analytics platform running **in situ** inside the secure data centres of England's
two largest GP EHR vendors (TPP/SystmOne + EMIS Web), reaching pseudonymised primary-care
records for **~58M** registered patients (~24M TPP + ~33M EMIS), linked at individual level
to SARS-CoV-2 testing, hospital, ICU, and death data. Because GP registration in England is
near-universal and free at point of care, the sampling frame is effectively
**population-based** rather than healthcare-seeking — the decisive contrast with US
commercial-EHR/claims cohorts, and the reason it is the pre-committed **population-based
replication vehicle** for the h0008 ascertainment concern in
`plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan` (candidate for `task:t079`).

**Load-bearing caveat (affects power NOW):** the **EMIS research backend is temporarily
paused** pending NHS England ↔ Optum/EMIS contracting, so a study launching now is
realistically **TPP-only (~24M)** until EMIS reopens.

## Why it fits (and where it doesn't) for the autoimmune × sex × PASC estimand

Per `plan:0005`'s admissibility gates:

| Gate | OpenSAFELY | Note |
|---|---|---|
| Population-based sampling (h0008) | **strong** | GP registration ≈ whole-population England — the platform's headline advantage |
| Dated pre-index autoimmune diagnosis (BC-3) | **strong** | OpenCodelists SNOMED lists with real primary-care event dates (not billing proxies) |
| Autoimmune stratum granularity (BC-3) | **good, partly unverified** | RA/SLE, IBD, MS codelists confirmed; Sjögren/vasculitis/myositis/autoimmune-thyroid [UNVERIFIED] |
| Dated infection index + acute severity (BC-6) | **strong** | SGSS test dates; SUS/HES + ECDS + ICNARC dated admissions/ICU |
| Individual-level utilisation (BC-7) | **strong** | per-patient GP-consultation counts via ehrQL `clinical_events` / consultations |
| Computable PASC outcome (BC-5) | **weak — the binding limitation** | SNOMED long-COVID codes exist but are **severely under-recorded and differentially so** |
| Rare-stratum × sex power (BC-4) | **constrained** | EMIS pause (TPP-only) + SDC suppression force stratum pooling |

## The outcome problem (why this is replication, not primary)

Coded long COVID is **severely under-recorded**: Walker et al. 2021 found long-COVID codes for
only **23,273 people across 58M records**, with **26.7% of practices never using the codes** —
roughly one-to-two orders of magnitude below ONS survey self-report. Crucially the
under-coding is **differential by consultation frequency**: higher-utilisation patients
(which includes autoimmune-disease patients) are more likely to be coded, so a **coded-only
PASC outcome carries h0008 ascertainment bias on the outcome side** — the very bias this
study exists to defeat. A coded-only outcome is therefore inadmissible as the primary
endpoint here; any OpenSAFELY analysis needs a **broader symptom/functional phenotype** plus
utilisation adjustment and negative-control/quantitative-bias analysis.

## Access / caveats

- **Approved-project, federated, code-first TRE model.** NHS England is the data controller;
  researchers must be named on an approved project. Analysis code is written away from the
  data, version-controlled, and **public on GitHub**; it executes against patient data inside
  the vendor's secure environment. **No row-level extraction** — only disclosure-controlled
  aggregate outputs, released after two-checker manual output review.
- **Statistical disclosure control:** redact any statistic describing **≤7 patients**, then
  **round counts to the nearest 5**. This binds directly on rare autoimmune-stratum × sex ×
  PASC cells (e.g. myositis or vasculitis × male) → pre-specify stratum pooling and a power
  floor.
- **England-only** generalisability; NHS coding/care patterns are country-specific.
- Vaccination records are linked; **variant era is only proxied by calendar time**.

## Access verification log

- 2026-07-01 (agent): landing-confirmed via OpenSAFELY docs (data-sources, data-access-policy,
  SDC), reports.opensafely.org TPP schema, and OpenCodelists. EMIS backend noted paused for
  research. No participant-level data retrieved (federated model — none is extractable).

## Connections to Project

- Questions/hypotheses it can inform: `hypothesis:0008` (ascertainment), `question:0007`
  (female predominance), the t078 autoimmune-diathesis effect-modifier line.
- Variables likely available: dated SARS-CoV-2 index (SGSS), dated hospitalisation/ICU
  (SUS/HES/ICNARC), pre-index autoimmune strata (OpenCodelists SNOMED), per-patient GP
  consultation counts, vaccination status, ONS death.
- Planned usage: **population-based replication** of the N3C-primary estimate under
  `plan:0005` — arbiter for the clinic- vs population-based ascertainment contrast, subject to
  building a non-coded-only PASC phenotype.

## Related

- Article notes: `paper:Hill2022` (the N3C substrate this replicates), `dataset:n3c-recover-longcovid`.
- Open items: verify Sjögren / vasculitis / myositis / autoimmune-thyroid codelists on
  opencodelists.org; confirm EMIS reopening timeline.
