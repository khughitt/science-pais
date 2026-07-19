---
id: patch-definition:compound-boundary-conditions-interaction-dag
kind: patch-definition
title: Compound boundary conditions — co-occurring effect-modifier interaction DAG (t111)
status: active
created: "2026-07-18"
updated: "2026-07-18"
project: post-acute-infection
ontology_terms: []
related:
- question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais
- question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
- question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a
- question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory
- hypothesis:0020-host-immune-baseline-reserve-gate
- hypothesis:0004-acute-severity-threshold
- topic:population-boundary-conditions-and-effect-modifiers-in-pais
- task:t111
source_refs:
- cite:Vinson2024
- cite:Hammel2023
- cite:Bruno2024
- cite:Chavatza2025
- cite:Peluso2022a
- cite:Wolff2023
- cite:Augustin2025
content_preview: Causal-sketch DAG for the JOINT/interaction effect of co-occurring PAIS host-modifiers. Drawn on the frailty x chronic-immunosuppression pair (shared reserve-bottleneck archetype) with the pregnancy-state x MCAS pair (distinct/opposite-signed-route, phenotype-redirection archetype) in the same graph. Encodes the shared-bottleneck vs distinct-route structure, the interaction-specific confounding and compound-selection-collider threats, and the scale-dependence of superadditivity — while being explicit that a DAG fixes which terms/confounders the estimand needs but NOT the interaction sign.
file_path: entities/patches/compound-boundary-conditions-interaction-dag.md
focal: question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais
scope_set:
- scope: local
neighborhood_policy:
  name: local-closure-v1
  version: local-closure-v1
  max_depth: 2
patch_type: inquiry
inquiry:
  profile: causal
  status: sketch
  treatment: concept:biological-frailty
  outcome: concept:pais-outcome
  boundary_roles:
  # host-modifiers (the interacting exposures)
  - ref: concept:biological-frailty
    role: BoundaryIn
  - ref: concept:chronic-immunosuppression
    role: BoundaryIn
  - ref: concept:pregnancy-state-immune-milieu
    role: BoundaryIn
  - ref: concept:mast-cell-activation-hyperreactivity
    role: BoundaryIn
  # shared confounders of the modifier-modifier association
  - ref: concept:chronological-age
    role: BoundaryIn
  - ref: concept:baseline-cardiometabolic-comorbidity
    role: BoundaryIn
  # outcome
  - ref: concept:pais-outcome
    role: BoundaryOut
  flow_edges:
  # ===== chronological age: shared common cause (can MANUFACTURE apparent interaction) =====
  - subject: concept:chronological-age
    predicate: causes
    object: concept:biological-frailty
  - subject: concept:chronological-age
    predicate: causes
    object: concept:chronic-immunosuppression
  - subject: concept:chronological-age
    predicate: causes
    object: concept:pregnancy-state-immune-milieu
  - subject: concept:chronological-age
    predicate: causes
    object: concept:baseline-cardiometabolic-comorbidity
  - subject: concept:chronological-age
    predicate: causes
    object: concept:immune-homeostatic-reserve
  - subject: concept:chronological-age
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:chronological-age
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:chronological-age
    predicate: causes
    object: concept:survival-selection
  # ===== baseline comorbidity: shared confounder of frailty & immunosuppression =====
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:biological-frailty
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:chronic-immunosuppression
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:immune-homeostatic-reserve
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:pais-outcome
  # ===== M1: biological frailty (treatment / worked-estimand modifier) =====
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:immune-homeostatic-reserve
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:survival-selection
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:hospital-ascertainment
  # ===== M2: chronic immunosuppression (co-primary modifier) =====
  - subject: concept:chronic-immunosuppression
    predicate: causes
    object: concept:immune-homeostatic-reserve
  - subject: concept:chronic-immunosuppression
    predicate: causes
    object: concept:persistent-antigen-fragment-burden
  - subject: concept:chronic-immunosuppression
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:chronic-immunosuppression
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:chronic-immunosuppression
    predicate: causes
    object: concept:survival-selection
  - subject: concept:chronic-immunosuppression
    predicate: causes
    object: concept:hospital-ascertainment
  # ===== M3: pregnancy-state immune milieu (OPPOSITE-signed routes) =====
  - subject: concept:pregnancy-state-immune-milieu
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:pregnancy-state-immune-milieu
    predicate: causes
    object: concept:th2-mast-cell-axis
  - subject: concept:pregnancy-state-immune-milieu
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:pregnancy-state-immune-milieu
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:pregnancy-state-immune-milieu
    predicate: causes
    object: concept:hospital-ascertainment
  # ===== M4: pre-existing atopy / MCAS (phenotype amplifier) =====
  - subject: concept:mast-cell-activation-hyperreactivity
    predicate: causes
    object: concept:th2-mast-cell-axis
  - subject: concept:mast-cell-activation-hyperreactivity
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:mast-cell-activation-hyperreactivity
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:mast-cell-activation-hyperreactivity
    predicate: causes
    object: concept:hospital-ascertainment
  # ===== shared reserve bottleneck (mediator — do NOT condition for total joint effect) =====
  - subject: concept:immune-homeostatic-reserve
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:immune-homeostatic-reserve
    predicate: causes
    object: concept:persistent-antigen-fragment-burden
  - subject: concept:immune-homeostatic-reserve
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:immune-homeostatic-reserve
    predicate: causes
    object: concept:pais-outcome
  # ===== antigen-persistence route (mediator) =====
  - subject: concept:persistent-antigen-fragment-burden
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:persistent-antigen-fragment-burden
    predicate: causes
    object: concept:pais-outcome
  # ===== immune dysregulation (mediator) =====
  - subject: concept:immune-dysregulation
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:immune-dysregulation
    predicate: causes
    object: concept:pais-outcome
  # ===== Th2 / mast-cell axis (phenotype-specific mediator) =====
  - subject: concept:th2-mast-cell-axis
    predicate: causes
    object: concept:pais-outcome
  # ===== acute infection severity (mediator; the Hammel2023-unadjusted path) =====
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:hospital-ascertainment
  # ===== thrombovascular route (mediator) =====
  - subject: concept:thromboinflammation-and-endothelial-dysfunction
    predicate: causes
    object: concept:pais-outcome
  # ===== outcome -> ascertainment (completes the selection collider) =====
  - subject: concept:pais-outcome
    predicate: causes
    object: concept:hospital-ascertainment
  # ===== latent unmeasured shared confounders (open back-door for every modifier) =====
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:biological-frailty
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:chronic-immunosuppression
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:pregnancy-state-immune-milieu
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:mast-cell-activation-hyperreactivity
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:pais-outcome
  unknowns:
  - concept:unmeasured-shared-confounders
  assumptions:
  - ref: estimand-is-interaction-not-total-effect
    statement: 'The object of this DAG is NOT a single-treatment total effect but the JOINT / interaction effect of two co-occurring host-modifiers on PAIS. The tooling requires one treatment/outcome, so the estimand is drawn on the frailty x chronic-immunosuppression pair (treatment = biological-frailty, modifier = chronic-immunosuppression, outcome = PAIS); pregnancy-state x MCAS is carried in the same graph as the contrasting second pair. The quantity of interest is a two-way interaction / effect-measure-modification term, not a marginal effect of either modifier alone.'
  - ref: two-pairs-two-structures
    statement: 'The two focal pairs instantiate the two rival structures of hypothesis:0020 P2 (shared-mechanism vs distinct-pathways). PAIR 1 frailty x immunosuppression = the SHARED-BOTTLENECK archetype: both deplete the same immune-homeostatic-reserve node (and immunosuppression additionally raises antigen burden), so their effects converge on one mediator. PAIR 2 pregnancy-state x MCAS = the DISTINCT / OPPOSITE-SIGNED-ROUTE archetype: they converge on the Th2/mast-cell axis but pregnancy carries a simultaneous Treg/tolerance arm that dampens the Th1/autoimmune route (Bruno2024 lower cognitive/fatigue PASC) while the thrombovascular route is preserved/amplified (Bruno2024 higher cardiac/thromboembolic PASC) — so the compound effect can be antagonistic and phenotype-redirecting rather than risk-compounding.'
  - ref: dag-does-not-fix-interaction-sign
    statement: 'LOAD-BEARING LIMIT. A DAG encodes conditional-independence / identification structure; it does NOT determine the SIGN or magnitude of an interaction. Even the shared-bottleneck pair can be super-additive OR sub-additive: convergence on immune-homeostatic-reserve yields super-additivity near a threshold (convex reserve->lock-in map, consistent with hypothesis:0004) but a CEILING / sub-additivity if one modifier already floors the reserve. The graph tells you WHICH interaction terms and confounders the estimand needs and WHICH structural rivals are in play; it cannot answer superadditive-vs-distinct-route without a parametric outcome model, a scale choice, and the (currently unknown) shape of the reserve->outcome dose-response. Do not read the drawn convergence as evidence of synergy.'
  - ref: superadditivity-is-scale-dependent
    statement: 'q0057 asks whether modifiers compound "superadditively" — this MUST specify a scale. Interaction on the additive (risk-difference) scale and on the multiplicative (odds/hazard-ratio) scale can disagree in sign; a purely multiplicative model can look "no-interaction" while additive excess risk is large. Biological / mechanistic interaction (Rothman sufficient-component-cause: two modifiers in the same causal complex) maps to DEPARTURE FROM ADDITIVITY, so the interaction terms q0057 needs are additive-scale measures — RERI, attributable proportion (AP), synergy index (S) — computed alongside (not instead of) the model-native multiplicative product term. For the topic''s decision ("which compound strata to target"), additivity is the decision-relevant scale.'
  - ref: interaction-confounding-is-stricter
    statement: 'Identifying an interaction requires blocking back-door paths for BOTH modifiers AND controlling common causes of the modifier-modifier association; a confounder of only one modifier-outcome relation is enough to bias the interaction term. The measured shared common causes here are chronological-age (age->frailty, age->immunosuppression-indication, age->reserve) and baseline-cardiometabolic-comorbidity (comorbidity->frailty, comorbidity->transplant/immunosuppression indication). Uncontrolled, they MANUFACTURE apparent frailty x immunosuppression synergy out of confounding. The measured set that blocks the drawn back-doors is {age, baseline-comorbidity}.'
  - ref: non-identifiable-with-U
    statement: 'HEADLINE (as in the menopause DAG). With unmeasured-shared-confounders (U) latent — U -> each modifier and U -> PAIS — no measured adjustment set blocks the U back-door, so the interaction is NOT point-identified by covariate adjustment. Identification rests on a bounding / E-value argument for U plus sensitivity, not on adjustment alone. networkx d-separation only; science inquiry validate reports pgmpy not installed, so the tool''s identifiability check stays a warning.'
  - ref: compound-selection-collider
    statement: 'FIRST-ORDER THREAT specific to compound strata. Every modifier and PAIS itself causes hospital/clinic ascertainment (and frailty/immunosuppression/age cause survival-selection). Compound-boundary patients are differentially surveilled, so a clinic-/hospital-ascertained or prevalent-survivor cohort CONDITIONS on a common descendant of both modifiers — inducing a spurious (typically negative) modifier-modifier association INSIDE the cohort that biases the interaction term even when each main effect is unbiased. This is why observational interaction estimates from convenience/clinic cohorts are untrustworthy. Do NOT condition on hospital-ascertainment or survival-selection; require population-based sampling and model selection explicitly (IPW / bias analysis).'
  - ref: mediators-not-conditioned-for-joint-effect
    statement: 'For the total joint effect, immune-homeostatic-reserve, persistent-antigen-fragment-burden, immune-dysregulation, th2-mast-cell-axis, thromboinflammation, and acute-infection-severity are MEDIATORS and are left UNADJUSTED. Two mechanism sub-questions condition deliberately: (a) conditioning on immune-homeostatic-reserve tests whether the frailty x immunosuppression interaction RUNS THROUGH the shared bottleneck (mediation); (b) a severity-controlled contrast conditions on acute-infection-severity. Caveat from real data: Hammel2023 (frailty aHR 1.41, <=6 mo) did NOT adjust acute severity, so the frailty->acute-severity->PASC path was left open and its estimate is not a clean reserve-vs-severity separation — the same trap will bias any compound estimand that omits severity.'
  - ref: phenotype-redirection-needs-resolved-outcome
    statement: 'For the pregnancy-state x MCAS pair the interaction may redirect PAIS PHENOTYPE rather than change total incidence (hypothesis:0020 P5). A single binary incidence outcome can show "no interaction" while the Th2/mast-cell, thrombovascular, and Th1/neuro-cognitive-fatigue components move in opposite directions (Bruno2024''s within-pregnancy dissociation is exactly this). The outcome must be phenotype-resolved (component-specific endpoints) for the interaction estimand to be meaningful; pais-outcome is drawn as a single node here only for legibility.'
  - ref: cohort-design-requirements
    statement: 'DELIVERABLE for q0057 / future cohort design. A study able to estimate these interactions needs: (1) JOINT pre-infection measurement of both modifiers in the same subjects (not two single-modifier studies); (2) the shared confounders age + baseline-comorbidity (and ideally a reserve proxy); (3) acute-illness severity measured (as a mediator to hold or not, never to be silently omitted); (4) a phenotype-resolved PAIS outcome; (5) POPULATION-BASED sampling to avoid the compound-selection collider, with ascertainment indicators modelled; (6) enough doubly-exposed cells for an interaction term (compound strata are rare -> the binding constraint is usually power on the joint cell, not the main effects). D-004: the EHR sources with the covariate depth for this (N3C, OpenSAFELY, UKB) are gated / below the third-party-reproducibility bar; open summary-statistic or consented-cohort vehicles are the only compliant route, and none currently holds a doubly-exposed cell of usable size — this remains a design aspiration, not a near-term analysis (t111 defers pending the t097 find-datasets pass).'
  - ref: worked-on-frailty-immunosuppression
    statement: 'The flow_edges are drawn as one acyclic joint graph over all four modifiers; the treatment/outcome estimand is set on frailty x immunosuppression because it is the pair with actual project grounding (q0031: Vinson2024 SOT paradox aOR 1.48, mycophenolate aOR 2.04; Peluso2022a HIV ~4x; Chavatza2025 impaired clearance) and the clean shared-bottleneck archetype. Pregnancy-state x MCAS shares the graph (via immune-dysregulation, th2-mast-cell-axis, thromboinflammation) and is analysed as the contrasting pair; drawing both in one DAG also exposes cross-pair back-doors (e.g. age, U) that a per-pair sketch would miss.'
---

# Inquiry: Compound boundary conditions — co-occurring effect-modifier interaction DAG (t111)

## Summary

Causal DAG (**sketch**) for **task t111**, formalizing the interaction structure of
`question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais` under
`hypothesis:0020-host-immune-baseline-reserve-gate`.

**Estimand.** Not a single total effect but the **joint / two-way interaction effect** of
co-occurring PAIS host-modifiers on the outcome. The tool needs one treatment/outcome, so the
estimand is drawn on the **frailty × chronic-immunosuppression** pair (treatment
`concept:biological-frailty`, co-modifier `concept:chronic-immunosuppression`, outcome
`concept:pais-outcome`); the **pregnancy-state × MCAS** pair lives in the same graph as the
contrasting second structure. The question q0057 poses — *do co-occurring modifiers compound
**superadditively** or via **distinct mechanism routes** (possibly offsetting)?* — is read off the
graph as **which structural rival holds** plus **which interaction terms and confounders the
estimand needs**, not as a number the DAG can emit.

> **The one thing this DAG deliberately does NOT do.** It does **not** decide superadditive-vs-
> distinct-route. A DAG fixes conditional-independence / identification structure and the rival
> *shapes*; the **sign and magnitude** of an interaction additionally require a parametric outcome
> model, a **scale** (additive vs multiplicative), and the currently-unknown shape of the
> reserve → lock-in dose–response. The drawn convergence of frailty and immunosuppression on the
> shared reserve node is the *structural precondition* for synergy, **not evidence of it** — the
> same node can produce a **ceiling / sub-additivity** if one modifier already floors reserve.

## The two focal pairs are two different structures

| | **Pair 1 — frailty × immunosuppression** | **Pair 2 — pregnancy-state × MCAS** |
|---|---|---|
| Archetype | **Shared bottleneck** | **Distinct / opposite-signed routes** |
| Convergence node | `immune-homeostatic-reserve` (+ antigen burden) | `th2-mast-cell-axis` (+ thrombo, immune-dysregulation) |
| h0020 mapping | P2 shared-mechanism / P1 reserve gate | P5 phenotype shift, not just incidence |
| Same-direction? | Yes — both deplete reserve, both raise PASC (Vinson2024, Hammel2023) | **No** — pregnancy dampens Th1/neuro route yet preserves/amplifies thrombovascular (Bruno2024); MCAS amplifies Th2 route (Wolff2023) |
| Likely interaction | Super-additive near threshold **or** ceiling/sub-additive if reserve floored | **Sign-ambiguous / antagonistic**; redirects phenotype |
| What breaks the naive "compound = more risk" intuition | Ceiling on a shared depleted node | Offsetting arms + phenotype redirection |

This is the substantive answer to q0057's dichotomy: it is a **false binary** — Pair 1 is
"same route" and Pair 2 is "distinct routes", and *neither* structure alone fixes whether risk
compounds. Superadditivity is a **scale-and-dose-response** property layered on top of the
structure, and distinct-route pairs can be **antagonistic**, not merely additive.

## Node roles

| Node | Role w.r.t. the modifier-interaction estimand | Handling |
|---|---|---|
| Biological frailty (M1) | Modifier / treatment | Exposure of interest |
| Chronic immunosuppression (M2) | Co-primary modifier | Exposure of interest (interaction partner) |
| Pregnancy-state immune milieu (M3) | Modifier (Pair 2) | Exposure of interest; opposite-signed routes |
| Atopy / MCAS (M4) | Modifier (Pair 2) | Exposure of interest; phenotype amplifier |
| Chronological age | **Shared common cause of the modifiers** | **Adjust** (blocks modifier–modifier back-door) |
| Baseline cardiometabolic comorbidity | **Shared confounder (frailty & immunosuppression)** | **Adjust** |
| Immune homeostatic reserve | **Shared mediator (bottleneck)** | Do **not** adjust (joint effect); condition only for the mediation sub-test |
| Persistent antigen/fragment burden | Mediator (impaired-clearance route) | Do not adjust (joint effect) |
| Immune dysregulation | Mediator | Do not adjust (joint effect) |
| Th2 / mast-cell axis | **Phenotype-specific mediator (Pair 2)** | Do not adjust; resolve in the outcome |
| Thromboinflammation / endothelial dysfunction | Mediator (thrombovascular route) | Do not adjust (joint effect) |
| Acute infection severity | Mediator | Do not adjust for joint effect; **measure** (Hammel2023 omitted it) |
| PAIS outcome | Outcome | **Phenotype-resolve** for Pair 2 |
| Hospital / clinic ascertainment | **Collider (selection)** | **Do not condition**; population sampling; model selection |
| Survival selection / left-truncation | **Collider (selection)** | **Do not condition**; competing-risk / IPW |
| Unmeasured shared confounders (U) | Latent confounder (open back-door) | Identifiability threat — non-identifiable as drawn |

## Identifiability (as drawn)

- **U latent (real world):** the interaction is **not point-identified** by covariate adjustment —
  no measured set blocks U → {modifiers} and U → PAIS. Headline matches the menopause DAG.
- **U set aside:** the measured set that blocks the drawn modifier–modifier back-doors is
  **{age, baseline-comorbidity}**. This is *necessary* but delivers the interaction only under the
  additional no-unmeasured-confounding-of-either-modifier assumption; identification still leans on
  an E-value / bounding argument for U plus sensitivity.
- **Never condition** on `hospital-ascertainment` or `survival-selection`: they are common
  descendants of both modifiers, and conditioning induces a spurious modifier–modifier association
  that biases the **interaction term specifically** (the compound-selection collider). This is the
  dominant threat for observational interaction estimates from clinic/convenience cohorts.
- **Mediators** (reserve, antigen burden, dysregulation, Th2/mast-cell, thrombo, severity) are
  excluded from the joint-effect set; conditioning on `immune-homeostatic-reserve` is the *mediation*
  test (does the Pair-1 interaction run through the shared bottleneck?), and conditioning on
  `acute-infection-severity` gives the severity-controlled contrast — the path Hammel2023 left open.
- 17 nodes, acyclic. `pgmpy` not installed → `science inquiry validate` identifiability checks
  remain warnings (networkx d-separation reasoning only).

## What q0057 actually needs (interaction terms + cohort)

- **Terms:** an additive-scale interaction (RERI / AP / synergy index) reported *alongside* the
  model-native multiplicative product term — because mechanistic interaction is departure from
  **additivity** and the "who to target" decision is an additive-scale question.
- **Cohort (deliverable, see the `cohort-design-requirements` assumption):** joint pre-infection
  measurement of both modifiers in the same subjects; {age, comorbidity, reserve-proxy} covariates;
  measured acute severity; a **phenotype-resolved** outcome; **population-based** sampling with
  modelled ascertainment; and enough **doubly-exposed** cells for the interaction term — the usual
  binding constraint, since compound strata are rare.
- **D-004:** the EHR sources deep enough for this (N3C, OpenSAFELY, UKB) are gated / below the
  third-party-reproducibility bar. No compliant vehicle currently holds a usable doubly-exposed
  cell → **design aspiration**, deferred pending the t097 find-datasets pass.

## Reverse causation / bidirectional coupling

`hypothesis:0020` P4 (frailty ↔ PAIS bidirectional coupling) would add a PAIS → frailty edge that
**cycles** this graph. As in the menopause DAG, it is handled by **temporal ordering** — modifiers
fixed at their **pre-infection** value — not a bidirectional edge; the feedback belongs to a separate
longitudinal inquiry.

## Notes

- Built via the inquiry patch-definition layout (layout v3); causal edges are `flow_edges` with
  `predicate: causes`, materialized to the `inquiry/<slug>` named graph by `science graph build`.
- Five new concept nodes were minted for this DAG: `chronic-immunosuppression`,
  `pregnancy-state-immune-milieu`, `mast-cell-activation-hyperreactivity`,
  `immune-homeostatic-reserve` (the shared bottleneck), and `th2-mast-cell-axis` (the phenotype
  route). The rest reuse the menopause-DAG concept library.
- Evidence bindings: Vinson2024 (SOT PASC paradox), Hammel2023 (frailty, severity-unadjusted),
  Bruno2024 (pregnancy phenotype dissociation), Chavatza2025 (rituximab impaired clearance),
  Peluso2022a (HIV exhaustion), Wolff2023 / Augustin2025 (atopy/MCAS). All are already project
  paper/cite entities via `topic:population-boundary-conditions-and-effect-modifiers-in-pais`.
- Next: `/science:critique-approach` on this sketch if an adversarial pass is wanted; otherwise the
  DAG stays a design artifact until a doubly-exposed dataset is admissible (t097).
