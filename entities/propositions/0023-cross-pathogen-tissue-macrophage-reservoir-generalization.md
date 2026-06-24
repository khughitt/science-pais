---
id: proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization
type: proposition
title: A structurally analogous degradation-resistant tissue/macrophage fragment reservoir
  operates across pathogen classes (Borrelia, SARS-CoV-2, Coxiella-like triggers)
status: active
claim_layer: mechanistic_narrative
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- hypothesis:0002-tissue-reservoir-antigen-fragment
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- topic:antigen-pathogen-persistence
- proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
- task:t052
source_refs:
- paper:McClune2025
- paper:Peluso2024
- paper:Morroy2016
created: '2026-06-24'
updated: '2026-06-24'
---
# Proposition: A structurally analogous degradation-resistant tissue/macrophage fragment reservoir operates across pathogen classes (Borrelia, SARS-CoV-2, Coxiella-like triggers)

## Claim

The fragment-reservoir mechanism is **pathogen-agnostic**: across structurally diverse triggers — the
spirochaete *Borrelia*, the virus SARS-CoV-2, the intracellular bacterium *Coxiella* — the *same* generic
mechanism operates, namely a degradation-resistant, non-viable pathogen fragment evading clearance and
**accumulating in a tissue-resident macrophage sink** (e.g. Kupffer cells), there driving an overlapping
host-tissue dysregulation signature. Subject = the residual-fragment/tissue-macrophage-reservoir
mechanism; predicate = *recurs structurally across*; object = multiple unrelated pathogen classes. This is
the **generalization conjunct** of `hypothesis:0002` — the claim that lifts a Borrelia observation into a
*shared PAIS failure mode*. It is a distinct truth condition from mere persistence (`proposition:0022`):
0022 says fragments persist and are bioactive; **0023 says the *tissue-macrophage-reservoir architecture
itself* is what generalizes**, not just that some fragment lingers in each disease.

## Evidence Summary

**No supporting evidence is coded, because the generalization is not yet established — this is a
discriminating *prediction* of `hypothesis:0002`, held at `speculative`.** What exists is suggestive but
falls short of the claim:
- McClune2025 demonstrates the mechanism *only in Borrelia* (mouse liver) and reports a molecular-signature
  *overlap* with Long COVID (liver proteome vs. LC protein signature, p = 0.00038) — a cross-pathogen
  *correlation*, not a demonstration that SARS-CoV-2 deposits fragments in the *same* macrophage sink.
- Peluso2024 shows SARS-CoV-2 antigen persists in *plasma*, but does not localize a tissue-macrophage
  reservoir.
- Morroy2016's Q-fever immunomodulatory-complex hypothesis is inferential (non-viable Coxiella
  DNA/antigen impairing macrophage clearance), not a tissue-reservoir demonstration.

The mechanism has therefore been *observed in one pathogen* and *predicted* for the others. Per
`hypothesis:0002`'s own Predictions and Falsifiability sections, the discriminating test is direct tissue
sampling in a non-Borrelia PAIS showing fragment retention in tissue-resident macrophages with an
overlapping host signature.

## Caveats

This conjunct is **deliberately coded with no supporting evidence-line** so the hypothesis bundle grades
it `speculative` and the conjunctive roll-up of `hypothesis:0002` reflects that its *distinctive*
(cross-pathogen) claim is untested — rather than letting the well-supported persistence pillar
(`proposition:0022`) stand in for the whole hypothesis. It is a `mechanistic_narrative` generalization;
the molecular-overlap correlation (McClune2025) is consistent with it but is also consistent with
*convergent downstream* signatures arising from *different* upstream mechanisms — so the overlap must not
be coded as direct support without a tissue-localization result. Promotion path: a positive non-Borrelia
tissue-reservoir study would be minted as a supporting evidence-line here, lifting both this conjunct and,
via the conjunction, `hypothesis:0002`.
