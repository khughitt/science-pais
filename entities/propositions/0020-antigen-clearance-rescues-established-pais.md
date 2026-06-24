---
id: proposition:0020-antigen-clearance-rescues-established-pais
type: proposition
title: Clearing persistent antigen rescues symptoms in established PAIS
status: active
claim_layer: causal_effect
identification_strength: interventional
proxy_directness: indirect
supports_scope: hypothesis_bundle
discusses:
- frame: hypothesis:0002-tissue-reservoir-antigen-fragment
  role: background
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- proposition:0021-acute-antigen-burden-determines-pais-incidence
- topic:antigen-pathogen-persistence
- discussion:0003-antigen-persistence-treatable-vs-fixed
- interpretation:0011-t046-antigen-clearance-trials-ingestion
source_refs:
- paper:Geng2024
- paper:Bhattacharjee2026
- paper:Peluso2026
- paper:Fallon2008
- paper:Krupp2003
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: Clearing persistent antigen rescues symptoms in established PAIS

## Claim

Therapeutically **removing or neutralizing residual pathogen antigen in patients with already-established
PAIS causally attenuates their symptoms** — i.e. persistent antigen is a *reversible therapeutic target*
in the chronic phase, not merely a fixed risk factor (`proposition:0021`) or a non-operative
epiphenomenon. Subject = antigen-clearing intervention in established disease; predicate = *causally
attenuates*; object = post-acute symptom burden. This is the decisive *interventional* corollary of
`hypothesis:0002` and the direct content of `question:0002`. It is distinct from the claim that antigen
burden *at onset* shapes who develops PAIS (`proposition:0021`), which the same evidence base leaves
intact.

## Evidence Summary

`literature_evidence`, and on the **interventional** axis the claim is **weakly disputed but
mechanistically uninterpretable** (`interpretation:0011-t046-antigen-clearance-trials-ingestion`). Three
RCTs in *established* long COVID are null on the clinical endpoint, but **none demonstrated antigen
target-engagement**, so they cannot distinguish "antigen does not drive symptoms" from "the drug never
cleared antigen":

- **Dispute — weak:** `evidence-line:0053` (`paper:Geng2024`, STOP-PASC) — 15-day nirmatrelvir/ritonavir,
  null on the primary 6-symptom composite and all PROMIS secondaries (stopped early for futility); no
  baseline antigen-positivity enrichment and *no detectable baseline stool SARS-CoV-2 RNA*, so the treated
  population may not have carried the antigen the hypothesis requires.
- **Dispute — weak, and the load-bearing one:** `evidence-line:0054` (`paper:Bhattacharjee2026`, PAX-LC
  immunologic substudy) — NMV/r changed **neither circulating Spike antigen, anti-Spike antibody, nor PBMC
  subsets**; the *only* correlate of improvement (in both arms) was falling RANTES/CCL5. This directly
  demonstrates the **target-engagement failure** that makes the other nulls uninterpretable.
- **Dispute — weak:** `evidence-line:0055` (`paper:Peluso2026`, outSMART-LC) — a single infusion of the
  long-acting anti-RBD monoclonal AER002 was null on the primary PHSS and all secondaries; but **no
  plasma antigen-clearance assay was run** and baseline tissue antigen was scarce (gut-biopsy RNA in only
  1/17). Adds a mechanistically *independent* clearance modality (neutralizing mAb, not an Mpro inhibitor)
  to the same uninterpretable-null pattern.
- **Dispute — weak, PTLDS parallel:** `paper:Fallon2008` (Fallon 2008, Neurology) — 10-week IV
  ceftriaxone vs placebo in patients with Lyme encephalopathy (documented prior Lyme, IgG Western blot
  positive, objective memory impairment). Significant broad cognitive improvement at week 12 (end of
  treatment), but improvement was **not sustained at week 24** after antibiotics stopped. No Borrelia
  antigen or peptidoglycan fragment (pPG^Bb) was measured at any timepoint, so whether treatment altered
  residual antigen burden is unknown. The transient-then-relapse time-course is consistent with either
  an antigen-re-drive mechanism (antigen persists, re-drives pathology once antibiotic pressure lifts) or
  a direct pharmacological suppression of a self-sustaining loop — the design cannot discriminate them.
  Adverse event rate 26% in the ceftriaxone arm (vs 7% placebo), primarily PICC-line events.

There is **no supporting line**: no completed trial both achieved demonstrated antigen clearance and
measured symptom change. The honest net is *not* "antigen clearance fails to rescue" — it is "the
reversible-target reading has not yet been tested by an adequate vehicle."

## Caveats

`proxy_directness: indirect` — administering an antiviral/neutralizing agent is a **proxy for antigen
clearance**, not a measurement of it; the antecedent of this proposition (antigen actually cleared) was
unmet in every trial coded here. The load-bearing confound (per `discussion:0003`): a trial that does not
demonstrate target-engagement cannot test whether clearing antigen helps, so these nulls **must not be
cited as refuting antigen persistence** (`hypothesis:0002`). Each trial carries additional standard
caveats — short course (15 days), tissue-reservoir inaccessibility, no antigen-positive enrichment,
protracted highly-vaccinated cohorts (median >1 yr since infection), and the `proposition:0021`
reconciliation (antigen as a fixed risk factor at onset that becomes non-operative once the chronic state
is self-sustaining, `hypothesis:0001`) that would make late clearance ineffective *without* refuting the
mechanism. The decisive test remains an **antigen-positive-enriched, clearance-demonstrated, symptom-
endpoint** trial.
