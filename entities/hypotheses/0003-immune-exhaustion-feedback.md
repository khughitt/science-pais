---
id: hypothesis:0003-immune-exhaustion-feedback
type: hypothesis
title: Post-acute chronicity is sustained by a self-reinforcing loop of unresolved
  antigenic stimulation and T-cell exhaustion that fails to terminate inflammation
status: proposed
phase: active
source_refs:
- cite:Aid2025
- cite:Ryan2022
related:
- topic:long-covid-immune-dysregulation
- topic:shared-failure-mode-across-pais
- question:0006-jak-stat-il6-driver-vs-marker
- hypothesis:0002-tissue-reservoir-antigen-fragment
- immunity:research-question:immune-homeostasis-and-dysregulation
created: '2026-06-11'
updated: '2026-06-11'
---
# Hypothesis: Post-acute chronicity is sustained by a self-reinforcing loop of unresolved antigenic stimulation and T-cell exhaustion that fails to terminate inflammation

## Organizing Conjecture

Post-acute chronicity is *maintained* by a positive-feedback loop between unresolved antigenic stimulation and adaptive immune exhaustion. Persisting antigen (or a sterile self-sustaining stimulus) drives continued innate inflammation; the chronic stimulation pushes CD8+ T cells into an exhausted state; exhausted T cells fail to clear the stimulus and fail to deliver the regulatory signals that normally terminate the acute-phase response; so inflammation continues — closing the loop. The result is the paradoxical co-occurrence of *persistent proinflammatory activation* (JAK-STAT/IL-6/IFN/complement) and *immune exhaustion* observed in long COVID, with no replicating virus. This loop is the maintenance engine that, once engaged, keeps the system in the shared attractor of hypothesis 0001 even if the original seed (hypothesis 0002) is partly cleared.

## Proposition Bundle

### Core Propositions

- Long COVID exhibits persistent activation of JAK-STAT, IL-6, IFN, and complement pathways beyond 180 days with no detectable circulating virus (Aid2025).
- This persistent activation co-occurs with CD8+ T-cell exhaustion in the same patients (Aid2025).
- The two are causally coupled in a self-reinforcing cycle: unresolved antigenic/inflammatory stimulation drives exhaustion, and exhaustion perpetuates failure to terminate inflammation — a loop absent in full recovery (Aid2025).

### Supporting Or Auxiliary Propositions

- A distinct arm of the same failure shows blunted/exhausted type-I-IFN transcription (MX1, OAS3, OASL) at 6 months specifically in long-COVID referrals, consistent with a transition from active response to tolerized/exhausted innate sensing (Ryan2022).
- The relevant divergence happens late: all convalescents are broadly perturbed to ~3-4 months, then most normalize while a subset fails at ~5-6 months — implying the maintenance loop, not the acute response, is the intervention target (Ryan2022).

## Current Uncertainty

- Causal direction (exhaustion → persistent inflammation vs the reverse) is asserted from cross-sectional/observational multi-omics, not demonstrated by perturbation (Aid2025).
- The cell source sustaining the IL-6/JAK-STAT signal is unresolved (bulk assays; Aid2025) — see `question:0006`.
- There is an apparent tension between "persistent IFN activation" (Aid2025) and "IFN-I suppression" (Ryan2022); reconciling these by timing/compartment/endotype is unproven.
- Whether the loop is sustained by genuine antigen (hypothesis 0002) or has become antigen-independent (sterile) is unknown and therapeutically pivotal.

## Predictions

**Strong / discriminating:**

- JAK1 inhibition (NCT06597396) will reduce both the inflammatory signature *and* symptoms in patients with the activation+exhaustion signature, and will do so more in this endotype than in non-inflammatory PASC.
- Single-cell profiling will localize the persistent IL-6/JAK-STAT signal to a specific innate population and show exhaustion markers (PD-1, TOX, TIM-3) on CD8+ T cells co-varying with inflammatory pathway activity.
- The activation+exhaustion loop signature will co-segregate with antigen positivity (Peluso2024) in patients where the loop is still antigen-driven, and not in those where it has gone sterile.

**Weaker / corollaries:**

- The same coupled activation+exhaustion pattern will be detectable in at least one non-COVID PAIS (e.g. PTLDS, post-Q-fever) if the loop is a shared maintenance mechanism.

## Falsifiability

Confidence would be materially reduced if:

- JAK/IL-6 inhibition durably suppresses the inflammatory signature but does *not* improve symptoms (marker, not driver — a key result for `question:0006`).
- High-resolution profiling shows activation and exhaustion occur in non-overlapping patient subsets rather than coupled within individuals.
- Longitudinal data show inflammation resolves while exhaustion persists (or vice versa) independently, contradicting a mutually reinforcing loop.

## Supporting Evidence

- **Aid2025 (empirical-data, two cohorts):** persistent JAK-STAT/IL-6/IFN/complement activation + CD8+ exhaustion >180 days, no circulating virus; explicit self-reinforcing-cycle interpretation; motivated a JAK1-inhibitor trial.
- **Ryan2022 (empirical-data):** late (5-6 month) bifurcation; blunted IFN-I transcription as a long-COVID-referral-specific signal — consistent with exhausted/tolerized innate sensing.
- Ganesh2022 (persistent IL-6) and Talla2023 (persistent inflammatory endotypes) are consistent with durable non-terminating inflammation.

## Disputing Evidence

- **Ryan2022 vs Aid2025 tension:** IFN-I *suppression* vs persistent IFN *activation* — if irreconcilable, the loop's inflammatory arm is mischaracterized.
- Broad single-agent therapeutic trials show mostly weak/null effects (Seo2025), which a simple single-loop model would not predict if the loop were the dominant, easily interruptible driver — favoring the multi-loop view of hypothesis 0001 over a single exhaustion loop.

## Evidence Needed To Shift Belief

- **Most efficient upward:** a positive JAK1-inhibitor RCT (symptom + pathway co-endpoints) plus single-cell evidence of coupled activation+exhaustion within individuals.
- **Most efficient downward:** a clean marker-not-driver result from the inhibitor trial, or decoupling of activation and exhaustion across patients/time.
- **Also useful:** antigen-positivity co-segregation test (links to hypothesis 0002); cross-PAIS replication of the coupled signature.

## Related Work

- `topic:long-covid-immune-dysregulation` — the signature evidence base.
- `question:0006-jak-stat-il6-driver-vs-marker` — the driver-vs-marker test.
- `hypothesis:0002-tissue-reservoir-antigen-fragment` — candidate antigen source feeding this loop; `hypothesis:0001-shared-dysregulated-attractor` — this loop as a maintenance engine of the attractor.
- `immunity:research-question:immune-homeostasis-and-dysregulation` — non-resolving-inflammation biology.
