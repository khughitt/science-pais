---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:ceba-post-im-adolescent-cohort
kind: dataset
title: CEBA — Chronic fatigue following acute EBV infection in adolescents (NCT02335437),
  author-request only
status: candidate
provided_capabilities:
  - modality: immunophenotype
    assay: olink
    trigger: ebv
    cohort_design: prospective-longitudinal
    stratification: im-history
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: pointer
source_class: observational
tier: track
license: unknown
access:
  level: controlled
  availability: available
  verified: false
  source_url: https://clinicaltrials.gov/study/NCT02335437
  verification_method: ''
  exception:
    mode: scope-reduced
    decision_date: '2026-07-17'
    rationale: 'No repository deposit exists. Data-availability statement is author-request
      (''available by the authors, without undue reservation'') under Norwegian REK/consent
      terms; not third-party retrievable, so below the D-004 bar. Held as the best-matched
      IM->fatigue vehicle for question:0051: 200 IM adolescents + 70 controls, prospective
      to 6-month chronic-fatigue outcome, with PBMC stimulation panels, plasma cytokines,
      hair cortisol. Author-request availability is DEAD/MISSING data, not a lighter
      gate: no defined procedure, no enforcement, no appeal, and unfalsifiable (it
      cannot be shown to be closed). It fails third-party reproducibility on the same
      ground as an enclave -- arguably harder, since an enclave at least publishes a
      followable procedure with a decidable outcome. Must NOT be ranked above
      credential-gated/enclave sources on tractability, must not satisfy coverage for
      question:0051, and must not justify deferring the search for a deposited
      alternative. Scientific value is real; availability is not.'
    followup_task: task:t110
accessions: []
ontology_terms:
- infectious-mononucleosis
- ebv
- post-infectious-fatigue
- adolescent
- gated-access
related:
- question:0051-prior-symptomatic-ebv-mononucleosis-as-pais-risk-amplifier
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# CEBA — Chronic fatigue following acute EBV infection in adolescents (NCT02335437), author-request only

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

CEBA — "Chronic fatigue following acute EBV infection in Adolescents" (NCT02335437; Wyller,
Akershus/Oslo). **200 adolescents with IM + 70 controls**, prospective to a 6-month chronic-fatigue
outcome, with PBMC stimulation panels, plasma cytokines, and hair cortisol.

## Why it fits

The **best-matched IM → fatigue design in existence** for `question:0051`: it has the acute-IM
index event, a prospective post-infectious fatigue outcome, and mechanistic immune readouts in the
same subjects.

## Access / caveats

**Gated — below the D-004 bar. Held under a `scope-reduced` exception pending an explicit
decision.**

Barrier: **no repository deposit exists.** The data-availability statement is author-request
("available by the authors, without undue reservation") under Norwegian REK/consent terms.

**Treat this as dead / missing data, not as a lighter gate.** "Available from the authors on
reasonable request" is a publication formality, not an access path: it has no defined procedure, no
enforcement, no SLA, and no appeal, and it empirically resolves to data almost never (non-response,
departed authors, lost media, refusal without stated cause, indefinite delay). It therefore fails
third-party reproducibility on the **same** ground as an enclave — and arguably harder, since an
enclave at least publishes a followable procedure with a decidable outcome. Author-request
availability is *unfalsifiable*: it cannot be shown to be closed, so it lingers as a false option
and inflates apparent coverage.

Accordingly CEBA must **not** be ranked above credential-gated or enclave sources on tractability,
must not satisfy any coverage requirement for `question:0051`, and must not justify deferring the
search for a genuinely deposited alternative. Its scientific value is real; its availability is not.

## Access verification log

- 2026-07-17 (agent (verify-access)): scope-reduced — No repository deposit exists. Data-availability statement is author-request ('available by the authors, without undue reservation') under Norwegian REK/consent terms; not third-party retrievable, so below the D-004 bar. Held as the best-matched IM->fatigue vehicle for question:0051: 200 IM adolescents + 70 controls, prospective to 6-month chronic-fatigue outcome, with PBMC stimulation panels, plasma cytokines, hair cortisol. Barrier is an author request rather than an enclave.

- 2026-07-17 (curator correction, per user): the preceding line's ladder reasoning is WRONG and is retracted. Author-request availability does not sit above an enclave on tractability -- it is DEAD/MISSING data. "Available from the authors on reasonable request" is a publication formality with no defined procedure, no enforcement, no SLA and no appeal, and it empirically resolves to data almost never. It is unfalsifiable availability: it cannot be shown to be closed, so it lingers as a false option and inflates apparent coverage. Correct disposition is scope-reduced (held, not pursued) or substituted -- never expanded-to-acquire. See feedback fb-2026-07-17-010.
