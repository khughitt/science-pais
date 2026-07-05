---
id: proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
kind: proposition
title: Degradation-resistant pathogen fragments persist in tissue after clearance
  and are biologically active
status: active
claim_layer: empirical_regularity
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0002-tissue-reservoir-antigen-fragment
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- topic:antigen-pathogen-persistence
- proposition:0020-antigen-clearance-rescues-established-pais
- task:t052
source_refs:
- paper:McClune2025
- paper:Peluso2024
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: Degradation-resistant pathogen fragments persist in tissue after clearance and are biologically active

## Claim

After the live pathogen is cleared, **degradation-resistant pathogen-derived fragments** — Borrelia
polymeric peptidoglycan (pPG^Bb), circulating SARS-CoV-2 spike/S1/N — **remain detectable in tissue or
plasma for months and retain biological activity** on host cells. Subject = non-viable, degradation-
resistant pathogen fragments; predicate = *persist past pathogen clearance and remain bioactive*; object =
host tissue and immune cells (altered proteome, dysregulated innate signalling, suppressed cellular energy
metabolism). This is the **existence-and-bioactivity** claim — the empirical foundation of
`hypothesis:0002` (a persisting tissue-fragment reservoir is a pathogen-agnostic *initiator* of PAIS). It
is **one core pillar** of h0002's bundle — the directly-evidenced one — **not the whole hypothesis**: the
bundle also conjoins the still-untested cross-pathogen generalization (`proposition:0023`) and the
risk-determinant claim (`proposition:0024`), so a well-supported persistence pillar does **not** by itself
make the initiator hypothesis well-supported. This proposition is also logically upstream of — and distinct
from — the *interventional* corollaries: that clearing the fragment **rescues established disease**
(`proposition:0020`) or that reducing fragment burden **at onset lowers incidence** (`proposition:0021`).
Those test reversibility/causation; this one tests only that the fragment persists and is not inert.

## Evidence Summary

`literature_evidence`. Both coded lines **support**; neither disputes. The base is real but thin and
leans on a single rigorous animal model plus a human detection study with no symptom linkage:

- **Support — moderate (animal model + cross-syndrome molecular bridge):** `evidence-line:0058`
  (`paper:McClune2025`) — in mice, *Borrelia* polymeric peptidoglycan accumulates in the liver
  (Kupffer cells + hepatocytes) and persists for weeks to months after clearance, while PG from other
  bacteria clears within 48 h; persistent pPG^Bb drives liver-proteome shifts, sustained AST/ALT
  elevation, and PBMC energy-metabolism (TCA/electron-transport) downregulation, and its liver-proteome
  signature significantly overlaps the Long COVID protein signature (p = 0.00038). Polymeric pPG^Bb was
  also present in 27/30 human Lyme-arthritis synovial-fluid samples *after* antibiotics — moving the
  persistence claim from mouse into human tissue.
- **Support — weak (human detection only, no symptom or bioactivity link):** `evidence-line:0059`
  (`paper:Peluso2024`) — Simoa detected SARS-CoV-2 spike/S1/N in plasma of ~25% of RNA-confirmed
  survivors out to 10–14 months (excess prevalence vs. 250 pre-pandemic controls significant at every
  window; severity-graded). Establishes *persistence* of a viral fragment in a second pathogen class, but
  measures **plasma only** (not a tissue reservoir), demonstrates **no bioactivity**, and the authors
  explicitly decline the symptom-linkage test.

Net: fragment persistence is established across two pathogen classes; **bioactivity** is demonstrated
*only* for Borrelia and *only* in a mouse model. This is a genuine, directly-evidenced support base that
grades **this proposition** `well_supported` — but it supports **only the persistence pillar**. It does
**not** lift `hypothesis:0002`, which remains `speculative`: the hypothesis is a conjunction that also
requires the still-untested cross-pathogen generalization (`proposition:0023`) and risk-determinant
(`proposition:0024`) conjuncts. This line is the mechanism's *existence*, not its *causal sufficiency for
symptoms* and not the *initiator hypothesis* as a whole.

## Caveats

The two lines have complementary gaps, and neither closes the load-bearing one (fragment burden → PAIS
symptoms):

- **McClune2025 (0058)** is a **mouse** model with no validated PTLDS phenotype, uses immortalized
  Kupffer/hepatocyte lines for the retention kinetics, and the PBMC energy-metabolism data come from
  *healthy*-donor cells stimulated ex vivo, not from PAIS patients. Bioactivity is demonstrated; a
  causal link to *human* chronic-illness symptoms is not.
- **Peluso2024 (0059)** is **detection only**: plasma (not tissue) antigen, no demonstrated bioactivity,
  no symptom correlation, and immunoassay specificity (98%) leaves individual-level positives uncertain.
- The hypothesis's **discriminating** predictions — that *non-Borrelia* PAIS pathogens deposit
  degradation-resistant fragments in tissue-resident macrophages, and that prospectively-measured
  fragment retention predicts chronicity better than initial pathogen load — remain **untested**
  (`hypothesis:0002` Predictions; `question:0002`). This proposition deliberately claims only persistence
  + bioactivity, **not** that the fragment is the proximal cause of symptoms; that reversibility/causation
  content lives in `proposition:0020` (disputed-but-uninterpretable) and the prediction set of h0002.
