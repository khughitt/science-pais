---
id: dataset:n3c-recover-longcovid-synthetic
kind: dataset
title: "N3C — synthetic OMOP slice (open tier) for the autoimmune × sex × PASC prototype"
status: candidate
origin: external
dataset_class: pointer
source_class: observational
tier: evaluate-next
license: proprietary
update_cadence: static
parent_dataset: dataset:n3c-recover-longcovid
ontology_terms: [long-covid, sars-cov-2, ehr, omop, synthetic-data, prototype]
local_path: ""
access:
  level: registration
  availability: available
  verified: false
  verification_method: ""
  last_reviewed: "2026-07-01"
  source_url: "https://covid.cd2h.org/dashboard/recover"
  exception:
    mode: scope-reduced
    decision_date: "2026-07-01"
    followup_task: task:t079
    rationale: "plan:0006 (BC-2) consumes ONLY the open synthetic tier of N3C. This granular sibling exists so the prototype's input path resolves to a synthetic-only artifact and cannot reference the parent's De-identified / Limited (enclave) tiers. Synthetic data not yet acquired — WP0 sets local_path + verified:true on acquisition."
  reproducibility:
    obtainability: registration
    execution: trusted-environment
    extractability: unknown
    notes: "N3C synthetic tier is enclave-only / non-downloadable (D-004), so it is NOT locally rerunnable — the 'reproducible-for-pipeline-mechanics' exception (obtain + rerun locally) does NOT apply. The binding known fact is execution=trusted-environment, which alone places it below the third-party-reproducible bar for access-route reasons (not scientific-strength). Synthetic-tier output/export-control rules are unconfirmed, so extractability is left 'unknown' pending direct verification — do not infer through access.level. Revisit if N3C ever offers a genuinely downloadable synthetic slice (D-004 'revisit if')."
consumed_by:
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - task:t079
related:
  - dataset:n3c-recover-longcovid
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - task:t079
created: "2026-07-01"
updated: "2026-07-01"
---

# N3C — synthetic OMOP slice (open tier)

## Summary

The **open synthetic tier** of N3C (`parent_dataset: dataset:n3c-recover-longcovid`) —
statistically-generated OMOP CDM records with **no real exposure–outcome signal**. This entity
exists to satisfy `plan:0006`'s **F2** requirement (pipeline-review finding): the prototype
pipeline's input must resolve to a **synthetic-only, verifiable artifact** so that no config
value can reach the parent's De-identified or Limited (enclave) siblings. Its role is to
**validate pipeline mechanics and portability**, never to produce an interpretable estimate.

## Access verification log

- 2026-07-01 (agent): created as the F2 structural scope-guard for `plan:0006` (t079/BC-2).
  `access.exception: scope-reduced` — synthetic slice only; parent enclave tiers out of scope.
  **Not yet acquired:** `local_path` empty, `verified: false`. WP0 acquires the synthetic OMOP
  package (N3C Enclave account), sets `local_path` + `verified: true` + `verification_method`,
  and confirms the OMOP CDM version.

## Granularity at this access level

Covers **only** the synthetic tier. The De-identified and Limited/enclave tiers — carrying the
real signal, the real cell counts, and the true PASC/utilisation coding — remain in the parent
entity `dataset:n3c-recover-longcovid` and are **out of scope for the prototype**. Any
interpretable estimate requires those tiers and is deferred (rest of BC-2).

## Connections to Project

- Questions/hypotheses it can inform: none directly — it produces **no estimate**; it de-risks
  the pipeline that will later run on the real tier for the t078 estimand.
- Variables likely available: OMOP-shaped `condition_occurrence`, `drug_exposure`,
  `visit_occurrence`, `measurement`, `observation_period`, `person` — schema fidelity vs the
  enclave to be confirmed in WP0.
- Planned usage: WP0–WP9 of `plan:0006` (synthetic mechanics + portability only).

## Related

- Parent: `dataset:n3c-recover-longcovid`. Decision: `interpretation:0031`. Plan: `plan:0006`.
