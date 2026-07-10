---
id: evidence-line:0095-mak2025-oas-serology-supports-imprinting-gate
kind: evidence-line
title: Mak2025 original-antigenic-sin serology supports the seasonal-coronavirus imprinting
  gate
status: active
stance: supports
target: proposition:0045-scov-imprinting-attractor-entry-gate
source: paper:Mak2025
strength: moderate
independence: independent
independence_group: mak2025-lc-humoral-serology
evidence_role: proxy_support
related:
- hypothesis:0001-shared-dysregulated-attractor
source_refs:
- paper:Mak2025
created: '2026-07-10'
updated: '2026-07-10'
evidence_type: literature_evidence
---
# Evidence Line: Mak2025 original-antigenic-sin serology supports the seasonal-coronavirus imprinting gate

## What this line shows

`paper:Mak2025` (47 long-COVID vs. 41 healthy controls) is the direct PAIS instance of original antigenic sin supporting `proposition:0045`: LC patients have *reduced* SARS-CoV-2 S1-specific IgG/IgA but *elevated* IgG against the homologous seasonal betacoronaviruses HKU1/OC43, plus an elevated IgM/IgG ratio (impaired class switching) — a humoral response deflected toward conserved, suboptimal epitopes [@Mak2025]. This is the serological signature the imprinting-gate mechanism predicts, giving `proxy_support`.

## Why it is independent

This line is a cross-sectional serological case-control study of the humoral compartment, independent of `evidence-line:0096` (Crotty2026), which contributes only an analogical durability premise from vaccine immunology. Mak2025 supplies the PAIS-specific antibody pattern; Crotty2026 supplies the "priming sets durable set points" background — different evidence types, no shared source.

## Caveats / scope

`proxy_support`, moderate. The central confound is a blood-draw timing mismatch (LC sampled at median 280 days vs. HC at 596 days), across which variant exposure and antibody waning differ. The signal is inferential (antibody ELISAs, no B-cell clonotyping) and cross-sectional, so it **cannot establish that imprinting preceded LC** rather than being shaped by it — the direction of the entry-gate arrow is unproven. Cohort is small (n=47/41).

## Measurement Model

"Imprinting" is a latent B-cell-repertoire property; Mak2025 operationalizes it *indirectly* via serum antibody ELISAs (S1-specific vs. HKU1/OC43-cross-reactive IgG/IgA and the IgM/IgG ratio), not via clonotyping/affinity mapping that would show recall of seasonal-coronavirus clones against SARS-CoV-2 antigen. Cross-sectional post-infection titers conflate pre-existing imprint, waning, and post-infection boosting, so elevated HKU1/OC43 IgG in LC is consistent with, but not diagnostic of, an entry-gating imprint; the directional test requires pre-infection seasonal-coronavirus serology linked to prospective PAIS outcome.
