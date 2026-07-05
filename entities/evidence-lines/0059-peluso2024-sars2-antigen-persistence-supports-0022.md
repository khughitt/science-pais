---
id: evidence-line:0059-peluso2024-sars2-antigen-persistence-supports-0022
kind: evidence-line
title: "Peluso2024 detects persisting SARS-CoV-2 antigen in ~25% of survivors to 14\
  \ months — weak support for fragment persistence (detection only, no symptom\
  \ or bioactivity link)"
status: active
stance: supports
target: proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
source: paper:Peluso2024
strength: weak
independence: independent
independence_group: peluso2024-liinc-plasma-antigen-persistence
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: observational
related:
- proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
source_refs:
- paper:Peluso2024
created: '2026-06-24'
updated: '2026-06-24'
---
# Evidence Line: Peluso2024 detects persisting SARS-CoV-2 antigen in ~25% of survivors to 14 months — weak support for fragment persistence (detection only, no symptom or bioactivity link)

## What this line shows

Peluso2024 (LIINC cohort, *Lancet Infect Dis*) used the Simoa ultrasensitive single-molecule array to
detect SARS-CoV-2 spike, S1, and nucleocapsid antigen in plasma of RNA-confirmed survivors, benchmarked
against 250 pre-pandemic true-negative controls. 42/171 participants (**~25%**) had ≥1 antigen-positive
specimen at some post-acute timepoint, with excess prevalence over controls significant at **every**
window out to **10–14 months** (3–6 mo +10.6%, p<0.001; 6–10 mo +8.7%, p<0.001; 10–14 mo +5.4%, p=0.017),
and antigen burden graded by acute-illness severity (hospitalised prevalence ratio 1.97). This provides
**controlled longitudinal evidence that a degradation-resistant viral fragment persists** well into the
post-acute phase — extending `proposition:0022`'s persistence claim from Borrelia to a **second pathogen
class** (SARS-CoV-2) [@Peluso2024].

## Why it is independent

`independent` under `independence_group: peluso2024-liinc-plasma-antigen-persistence`. Distinct pathogen
(SARS-CoV-2), compartment (plasma), platform (Simoa digital ELISA), and cohort (LIINC) from the Borrelia
liver-reservoir line (`evidence-line:0058`, McClune2025). Their concordance on persistence is genuine
cross-pathogen corroboration rather than shared method or source.

## Caveats / scope

`direct_test`, **weak** — this is a **detection-only** study and supports the persistence half of the
proposition but not the bioactivity half: (1) it measures **plasma** antigen, which is *not* a tissue
reservoir — the paper notes plasma negativity cannot exclude tissue persistence and, conversely, plasma
positivity does not localize a tissue sink (the macrophage-reservoir compartment central to h0002 is
unobserved here); (2) **no bioactivity** is demonstrated — antigen presence is not shown to perturb host
proteome, signalling, or metabolism; (3) the authors **explicitly decline the symptom-linkage test**, so
this says nothing about whether the antigen drives PAIS; (4) immunoassay specificity is 98%, so
individual-level positives carry ~2% false-positive uncertainty (population-level prevalence differences
are well above noise); (5) the cohort is largely pre-vaccination/pre-reinfection (ancestral-strain
biology). It corroborates *persistence* across pathogens but adds **no** weight to bioactivity or
causation — hence weak, and complementary to the moderate, bioactivity-bearing Borrelia line.
