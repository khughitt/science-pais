---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:23andme-multiancestry-longcovid-gwas
kind: dataset
title: 23andMe multi-ancestry long-COVID GWAS (Latinx + African-American arms) — proprietary
status: candidate
provided_capabilities:
- data_product: data-product:gwas-summary-statistics
  qualifiers:
    cohort_design: summary-stats
    stratification: ancestry
    trigger: sars-cov-2
created: "2026-07-17"
updated: "2026-07-17"
origin: external
dataset_class: pointer
source_class: observational
tier: track
license: proprietary
access:
  level: commercial
  availability: available
  verified: false
  source_url: https://www.medrxiv.org/content/10.1101/2024.10.07.24315052v1
  verification_method: ''
  exception:
    mode: scope-reduced
    decision_date: '2026-07-17'
    rationale: 'Gated behind a 23andMe proprietary Data Transfer Agreement; summary statistics are NOT deposited in GWAS Catalog. Below the D-004 third-party-reproducibility bar: a third party cannot re-obtain the data, so no result built on it is independently checkable. Held as the highest-value gated asset for question:0032 -- reportedly the only well-powered non-European long-COVID GWAS (EUR ~42,899 cases; Latinx ~8,631/20,351; African-American ~2,234/5,596). CASE COUNTS UNVERIFIED: taken from search-result text, the medRxiv full text 403''d on fetch; confirm before any use. Requires an explicit authorization decision, not silent inclusion.'
    followup_task: task:t110
accessions: []
ontology_terms:
- long-covid
- multi-ancestry
- gwas-summary-statistics
- gated-access
related:
- question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# 23andMe multi-ancestry long-COVID GWAS (Latinx + African-American arms) — proprietary

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

23andMe multi-ancestry long-COVID GWAS (medRxiv 2024.10.07.24315052). Reported to carry the
only well-powered non-European long-COVID arms: EUR ~42,899 cases, **Latinx ~8,631 / 20,351**, and
**African-American ~2,234 / 5,596**.

## Why it fits

`question:0032` asks about PAIS burden and mechanism outside high-income European-ancestry
cohorts. This is the single highest-value asset for that question and the only located vehicle that
genuinely **stratifies ancestry** — everything else open is orders of magnitude smaller or measures
the wrong phenotype.

## Access / caveats

**Gated — below the D-004 bar. Held under a `scope-reduced` exception; requires an
explicit authorization decision, not silent inclusion.**

Barrier: a **23andMe proprietary Data Transfer Agreement**; summary statistics are **not** deposited
in the GWAS Catalog. A third party cannot re-obtain the data, so no result built on it is
independently checkable — which is exactly what D-004 exists to prevent.

**Reported case counts are [UNVERIFIED]:** they come from search-result text, as the medRxiv full
text returned 403 on fetch. Confirm before relying on them for any power calculation.

**The decision-relevant tension for `question:0032`:** the only well-powered non-European PAIS
genetics asset is gated, and the only *open* non-European vehicle
(`dataset:bbj-jctf-severe-covid-gwas`) measures **acute severity, not PAIS**. That tension is not
resolvable by more searching — it resolves only by authorizing this route or by accepting an
acute-severity proxy with the transferability caveat stated.

## Access verification log

- 2026-07-17 (agent (verify-access)): scope-reduced — Gated behind a 23andMe proprietary Data Transfer Agreement; summary statistics are NOT deposited in GWAS Catalog. Below the D-004 third-party-reproducibility bar: a third party cannot re-obtain the data, so no result built on it is independently checkable. Held as the highest-value gated asset for question:0032 -- reportedly the only well-powered non-European long-COVID GWAS (EUR ~42,899 cases; Latinx ~8,631/20,351; African-American ~2,234/5,596). CASE COUNTS UNVERIFIED: taken from search-result text, the medRxiv full text 403'd on fetch; confirm before any use. Requires an explicit authorization decision, not silent inclusion.
