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
      hair cortisol. Barrier is an author request rather than an enclave, so it sits
      ABOVE N3C/OpenSAFELY on the transparency ladder -- an authorization/contact
      decision is plausible rather than foreclosed.'
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
("available by the authors, without undue reservation") under Norwegian REK/consent terms, so it is
not third-party retrievable as it stands.

**Ladder position matters here:** the barrier is an **author request, not an enclave**. Unlike
N3C/OpenSAFELY — where the gating is structural and export-reviewed by design — a contact/
authorization decision here is **plausible rather than foreclosed**. That makes CEBA the most
tractable gated asset in this sweep, and the one most worth an actual decision.

## Access verification log

- 2026-07-17 (agent (verify-access)): scope-reduced — No repository deposit exists. Data-availability statement is author-request ('available by the authors, without undue reservation') under Norwegian REK/consent terms; not third-party retrievable, so below the D-004 bar. Held as the best-matched IM->fatigue vehicle for question:0051: 200 IM adolescents + 70 controls, prospective to 6-month chronic-fatigue outcome, with PBMC stimulation panels, plasma cytokines, hair cortisol. Barrier is an author request rather than an enclave, so it sits ABOVE N3C/OpenSAFELY on the transparency ladder -- an authorization/contact decision is plausible rather than foreclosed.
