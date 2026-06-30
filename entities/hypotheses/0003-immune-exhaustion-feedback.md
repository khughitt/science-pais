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
- topic:therapeutics-and-clinical-trials
- question:0006-jak-stat-il6-driver-vs-marker
- hypothesis:0002-tissue-reservoir-antigen-fragment
- immunity:research-question:immune-homeostasis-and-dysregulation
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- proposition:0036-non-covid-pais-partially-recapitulate-ifn-cytokine-exhaustion-axis
- pre-registration:0004-jak1-inhibitor-driver-vs-marker
- interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration
- interpretation:0016-t054-abrocitinib-trial-status-snapshot
- interpretation:0029-t060-cross-pais-ifn-jakstat-pathway-map
- task:t047
- task:t054
- task:t060
created: '2026-06-11'
updated: '2026-06-25'
---
# Hypothesis: Post-acute chronicity is sustained by a self-reinforcing loop of unresolved antigenic stimulation and T-cell exhaustion that fails to terminate inflammation

## Organizing Conjecture

Post-acute chronicity is *maintained* by a positive-feedback loop between unresolved antigenic stimulation and adaptive immune exhaustion. Persisting antigen (or a sterile self-sustaining stimulus) drives continued innate inflammation; the chronic stimulation pushes CD8+ T cells into an exhausted state; exhausted T cells fail to clear the stimulus and fail to deliver the regulatory signals that normally terminate the acute-phase response; so inflammation continues — closing the loop. The result is the paradoxical co-occurrence of *persistent proinflammatory activation* (JAK-STAT/IL-6/IFN/complement) and *immune exhaustion* observed in long COVID, with no replicating virus. This loop is the maintenance engine that, once engaged, keeps the system in the shared attractor of `hypothesis:0001` even if the original seed (`hypothesis:0002`) is partly cleared.

## Proposition Bundle

### Core Propositions

Coded as graph propositions (t047, 2026-06-24). The hypothesis is their **conjunction** — the loop
requires *both* that the inflammatory state exists *and* that it is causal — so it grades `speculative`
until the causal pillar is tested:

- **`proposition:0025` — persistent inflammatory activation + dissociated IFN (SUPPORTED).** LC exhibits
  sustained IL-6/JAK-STAT/type-II-IFN/complement tone with a *blunted type-I antiviral-effector arm*,
  alongside CD8 exhaustion, beyond 180d with no circulating virus — `evidence-line:0061` (Aid2025,
  moderate) + `evidence-line:0062` (Ryan2022, weak). This conjunct **folds the persistent-activation and
  exhaustion-co-occurrence observations together** and resolves the former Aid2025-vs-Ryan2022 IFN tension
  (see Current Uncertainty).
- **`proposition:0026` — the loop is a proximal driver (UNTESTED).** The activation+exhaustion coupling
  *causally maintains* chronicity (reversible by inhibition), not merely marks it. No coded evidence —
  the discriminating test is the JAK1-inhibitor trial, committed in `pre-registration:0004` (data-gated,
  NCT06597396). Grades `speculative`.

### Supporting Or Auxiliary Propositions

- A distinct arm of the same failure shows blunted/exhausted type-I-IFN transcription (MX1, OAS3, OASL) at 6 months specifically in long-COVID referrals, consistent with a transition from active response to tolerized/exhausted innate sensing (Ryan2022).
- The relevant divergence happens late: all convalescents are broadly perturbed to ~3-4 months, then most normalize while a subset fails at ~5-6 months — implying the maintenance loop, not the acute response, is the intervention target (Ryan2022).

## Current Uncertainty

- Causal direction (exhaustion → persistent inflammation vs the reverse) is asserted from cross-sectional/observational multi-omics, not demonstrated by perturbation (Aid2025). This is the untested `proposition:0026`, gated on `pre-registration:0004`.
- The cell source sustaining the IL-6/JAK-STAT signal is unresolved (bulk assays; Aid2025) — see `question:0006`.
- **IFN tension RESOLVED (t047, `interpretation:0012`).** The apparent conflict between "persistent IFN activation" (Aid2025) and "IFN-I suppression" (Ryan2022) is reconciled as a **dissociated IFN signature**: Aid2025 indexes the *type-II/inflammatory* arm (IFNγ + IL-6/JAK-STAT, PBMC, LC-vs-recovered, >180d) while Ryan2022 indexes the *type-I antiviral-effector* arm (MX1/OAS3/OASL, whole blood, referral-vs-convalescent, 6-mo bifurcation). Persistent inflammatory tone + tolerized type-I effectors is the *predicted* exhausted-innate-sensing signature, so Ryan2022 now **supports** `proposition:0025` rather than disputing it. Residual: the two arms are inferred across studies, not co-measured in the same patients (the discriminating confirmation).
- Whether the loop is sustained by genuine antigen (hypothesis 0002) or has become antigen-independent (sterile) is unknown and therapeutically pivotal.
- **Belief-graph note (t047, 2026-06-24).** h0003's bundle is conjunctive over its core members: `proposition:0025` (descriptive state) is **supported**, but `proposition:0026` (the causal-driver loop) is **untested** and gated on the JAK1 trial — so the conjunction grades h0003 honestly **`speculative`** ("the inflammatory-arm signature is real; the maintenance-engine claim is unproven"). A descriptive state being well-evidenced must not promote the causal loop; that is exactly what `pre-registration:0004` exists to test. (Same honest-conjunction structure as `hypothesis:0002` post-t052.)
- **Registry-status note (t054, 2026-06-25).** NCT06597396/CLEAR-LC is `ACTIVE_NOT_RECRUITING` with primary completion 2026-03-27 actual and `hasResults: false`; study completion is still estimated for 2026-09-30. The public endpoint list includes fatigue/PASC symptom outcomes and hsCRP, but not a specific IL-6R/JAK-STAT/ISG target-engagement readout. The causal-loop conjunct remains untested; no belief update.
- **Cross-PAIS note (t060, 2026-06-26).** `proposition:0036` now records the generalizability map: ME/CFS and QFS partially recapitulate IFN/cytokine/exhaustion-axis abnormalities, with EatonFitch2024 providing the cleanest same-panel LC/ME/CFS support line. This is kept local to q0006 and **not** added to the h0003 core bundle, because h0003's grade should still be controlled by the LC descriptive state (`0025`) plus the untested causal-driver conjunct (`0026`).

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

- **Aid2025 (empirical-data, two cohorts):** persistent JAK-STAT/IL-6/IFN/complement activation + CD8+ exhaustion >180 days, no circulating virus; explicit self-reinforcing-cycle interpretation; motivated a JAK1-inhibitor trial. Now **coded as `evidence-line:0061` (moderate, supports `proposition:0025`)** (t047).
- **Ryan2022 (empirical-data):** late (5-6 month) bifurcation; blunted *type-I* IFN-effector transcription (MX1/OAS3/OASL) as a long-COVID-referral-specific signal — consistent with exhausted/tolerized innate sensing. Now **coded as `evidence-line:0062` (weak, supports `proposition:0025`)** as the dissociated type-I-effector arm (t047) — *no longer a disputing tension* (see Current Uncertainty).
- Ganesh2022 (persistent IL-6) and Talla2023 (persistent inflammatory endotypes) are consistent with durable non-terminating inflammation.
- **EatonFitch2024 (empirical-data, LC+ME/CFS same panel):** NanoString immune-exhaustion PBMC profiling shows overlapping IFN/cytokine/exhaustion pathway themes across ME/CFS and long COVID, now coded as `evidence-line:0089` on local q0006 proposition `0036`. This supports cross-PAIS pathway-family recurrence, not the h0003 causal-driver claim.

## Disputing Evidence

- **(Resolved) Ryan2022 vs Aid2025 IFN tension** — reconciled (t047, `interpretation:0012`) as a dissociated IFN signature (type-II/inflammatory tone up; type-I antiviral effectors down), not a contradiction; both papers now *support* `proposition:0025`. Retained here only as a pointer to the resolution.
- Broad single-agent therapeutic trials show mostly weak/null effects (Seo2025), which a simple single-loop model would not predict if the loop were the dominant, easily interruptible driver — favoring the multi-loop view of hypothesis 0001 over a single exhaustion loop. This is the live caution on `proposition:0026` and is built into `pre-registration:0004`'s null-result plan (an unstratified flat null is weak disconfirmation).

## Evidence Needed To Shift Belief

- **Most efficient upward:** a positive JAK1-inhibitor RCT (symptom + pathway co-endpoints) plus single-cell evidence of coupled activation+exhaustion within individuals.
- **Most efficient downward:** a clean marker-not-driver result from the inhibitor trial, or decoupling of activation and exhaustion across patients/time.
- **Also useful:** antigen-positivity co-segregation test (links to hypothesis 0002); cross-PAIS replication of the coupled signature.

## Related Work

- `topic:long-covid-immune-dysregulation` — the signature evidence base.
- `question:0006-jak-stat-il6-driver-vs-marker` — the driver-vs-marker test.
- `hypothesis:0002-tissue-reservoir-antigen-fragment` — candidate antigen source feeding this loop; `hypothesis:0001-shared-dysregulated-attractor` — this loop as a maintenance engine of the attractor.
- `immunity:research-question:immune-homeostasis-and-dysregulation` — non-resolving-inflammation biology.
