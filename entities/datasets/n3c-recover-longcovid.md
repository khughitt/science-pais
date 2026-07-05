---
id: dataset:n3c-recover-longcovid
kind: dataset
title: "N3C — National COVID Cohort Collaborative (+ RECOVER-EHR)"
status: candidate
created: "2026-06-21"
updated: "2026-07-01"
origin: external
source_class: observational
tier: evaluate-next
license: proprietary
access:
  level: mixed
  availability: available
  verified: false
  source_url: "https://covid.cd2h.org/dashboard/recover"
  reproducibility:
    obtainability: approved-project
    execution: trusted-environment
    extractability: aggregate-reviewed
    notes: "Describes the De-identified/Limited (enclave) route — the real-signal tier this mixed umbrella now represents (the open synthetic tier is broken out as dataset:n3c-recover-longcovid-synthetic). Access is DUA + institutional + approved-project onboarding; compute is enclave-only (Palantir Foundry); only export-reviewed aggregates leave. Below the third-party-reproducible bar (D-004). Refines D-004's informal 'insider-only' label to the precise lattice class trust-based-output (reviewed aggregates DO leave — not extract:none, not custodian-run)."
accessions: []
ontology_terms: [long-covid, sars-cov-2, ehr, computable-phenotype, sex-differences]
provided_capabilities:
  - modality: clinical-ehr
    assay: ehr-coded
    trigger: sars-cov-2
    cohort_design: prospective-longitudinal
    case_definition: who-lc
    stratification: sex
related:
  - task:t013
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - interpretation:0032-t079-bc3-autoimmune-stratum-granularity
  - interpretation:0033-t079-bc5-pasc-case-definition-lock
  - interpretation:0034-t079-bc6-acute-severity-dateability
  - interpretation:0035-t079-bc7-individual-utilisation
  - paper:Pfaff2022
  - paper:Thaweethai2023
  - dataset:opensafely-longcovid
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
consumed_by:
  - task:t079
siblings:
  - dataset:n3c-recover-longcovid-synthetic
---

# N3C — National COVID Cohort Collaborative (+ RECOVER-EHR)

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — **open synthetic
tier** lets you build the pipeline now; real data is enclave-gated.

## What it is

Multi-site federated EHR (millions of patients) with a computable long-COVID phenotype. Tiered access:
Synthetic (open) → De-identified → Limited (DUA + institutional approval, enclave-only compute).

## Why it fits t013

EHR scale enables **sex-stratified acute-severity-vs-persistence odds ratios** and a built-in
**dissociation proxy**: psychiatric ICD codes vs fatigue codes. Prototype on the synthetic tier, then
apply for real data.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes (hospitalization) | yes (computable phenotype) | yes (ICD) | yes (ICD) | yes |

## Access / caveats

Enclave-only (no extraction). EHR-coded long COVID is **noisy / under-coded** (vendor-dependent);
no patient-reported fatigue severity. Single trigger.

## Access verification log

- 2026-07-01 (agent): consumed by `plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline`
  (t079/BC-2) — **open synthetic slice only**; the de-identified/Limited enclave siblings remain
  out of scope pending DUA. Locked as primary vehicle by `interpretation:0031`.
- 2026-07-01 (agent, BC-5 / `interpretation:0033`): PASC outcome definition locked. **Primary =
  coded U09.9-or-LC-clinic** (Hill-replicable), WHO-aligned ≥90 d ascertainment window. The N3C
  **ML computable phenotype** (`paper:Pfaff2022`, fully EHR-computable, AUROC 0.92 int/0.82 ext) is
  **demoted to a flagged sensitivity endpoint** — outpatient visit rate is its top feature (outcome
  utilisation-gated by construction, the h0008 axis under study), with an untested sex-specific error
  profile on top (75% female training positives, sex excluded → sex-proxy-leakage *risk*, not verified).
  RECOVER survey PASC index (`paper:Thaweethai2023`) not EHR-computable → construct anchor via
  `dataset:recover-adult` only. U09.9 = left-truncated/differential outcome availability (active in US
  ICD-10-CM from 2021-10-01; pre-activation infections codable later only if still observed).
  Every EHR outcome is utilisation-gated → ascertainment handled by design.
- 2026-07-01 (agent, BC-7 / `interpretation:0035`): individual utilisation buildable — OMOP
  `visit_occurrence`/`visit_detail` per-patient encounter counts over a fixed pre-index window
  **replace Hill's county physicians-per-1,000 proxy** (third of Hill's three gaps closed).
  **Two caveats carried into `plan:0005`/`plan:0006`:** (a) utilisation is **dual-role** — the
  ascertainment confounder **and** a consequence of the autoimmune exposure → adjust pre-index
  *outpatient* contact only (inpatient = severity-side, F6 denylist), report adjusted/unadjusted E1
  pair (divergence read by sex), negative control not-autoimmune-specific / not-downstream
  (baseline association checked, not strict independence); (b) **N3C-specific
  differential undercount** — only care at contributing sites is visible, so "low utilisation"
  conflates truly-low-contact with out-of-network care → the ascertainment defence is **bounded**,
  quantified by negative control + E-value. No participant-level data accessed (no access gate).
- 2026-07-01 (agent, BC-6 / `interpretation:0034`): acute-severity **dateability** confirmed —
  Hill2022's dated N3C severity set (hospitalisation, LOS tiers, invasive mechanical ventilation,
  ECMO, vasopressor, AKI, sepsis) dates the mediator relative to the earliest positive-test/dx
  index, so severity is **dateable enough to compute E2/E3 candidates** (CDE *identification*
  stays assumption-dependent — mediator–outcome confounding, positivity across severity strata).
  Two riders carried into `plan:0005`/`plan:0006`:
  (a) moderate/**oxygen rung differentially under-captured** → primary mediator = coarse dated
  hospitalisation-based severity, WHO-ordinal = sensitivity; (b) Hill's **≥45 d survival
  exclusion selects on a downstream consequence of the mediator** (severe acute COVID → acute
  death) → **E1 relabelled survivor-conditional (+ E1 death sensitivity)** and acute death
  modelled as a **competing risk** for E2/E3, not a row-drop. No participant-level data accessed
  (no access gate for this check).
- 2026-07-01 (agent, BC-3 / `interpretation:0032`): autoimmune-stratum granularity confirmed —
  all 8 disease-specific strata constructible as OMOP concept sets (fixes Hill's pooled-Charlson
  gap). SLE/RA/Crohn's/UC have curated **OHDSI Phenotype Library** cohorts (#119/#196/#198/#201);
  MS/Sjögren/vasculitis/myositis/autoimmune-thyroid are author-buildable from standard SNOMED
  disorders (unvalidated → clinical-review pass before a real estimate). Specific OMOP concept_ids
  **[UNVERIFIED]** (ATHENA API 403) — confirm under `task:t081`. A-priori scoping needed for
  vasculitis (family vs subtype), autoimmune-thyroid (exclude all-cause hypothyroidism E03), and
  myositis (exclude drug-induced/paraneoplastic).
