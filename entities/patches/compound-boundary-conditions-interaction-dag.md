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
  - ref: status-is-unidentified-sketch
    statement: 'STATUS. This is a CAUSAL SKETCH, not an identified or evidence-bound interaction DAG. What is established: node/edge resolution and acyclicity (52 flow_edges over 16 nodes, verified by science inquiry validate). What is NOT established here: a well-defined estimand, tool-verified adjustment sets, edge-level evidence grounding, or that any drawn structure is the real one. Every "adjust / do-not-condition / non-identifiable" statement below is a HAND-DERIVED d-separation claim by the author, not a tool output (see formal-checks-are-vacuous). Treat the whole artifact as a structured hypothesis about how a compound-modifier analysis would have to be set up — useful for scoping a cohort, not for making causal claims.'
  - ref: formal-checks-are-vacuous
    statement: 'TOOLING LIMIT (do not mistake green checks for causal validation). science inquiry validate here confirms ONLY reachability + acyclicity. Its confounder check reports "No common causes found" despite age/comorbidity/U being drawn as common causes, and science inquiry export-pgmpy emits an EMPTY model — DiscreteBayesianNetwork([]) — because the causal checks/exporter read the graph/causal named graph (and normalize the hyphenated slug to underscores) while these edges live in the inquiry/<slug> graph. So adjustment-set and identifiability checks never ran on this structure. All identification statements are hand-derived and UNVERIFIED by the toolchain. (Filed as science feedback against the inquiry causal exporter.)'
  - ref: estimand-definition
    statement: 'ESTIMAND (Finding 2). The host-modifiers here (frailty, chronic immunosuppression, active-pregnancy state, atopy/MCAS) are baseline HOST CHARACTERISTICS, not manipulable treatments: a do()-intervention on "frailty" or "pregnancy state" is not well-defined, and "immunosuppression" is a heterogeneous bundle (drug class, dose, duration, or a disease-exhaustion baseline) with no single intervention. Therefore the tool''s treatment=biological-frailty field is a TECHNICAL PLACEHOLDER, not an interventionist estimand. The estimand adopted here is DESCRIPTIVE EFFECT-MEASURE HETEROGENEITY: the standardized cumulative incidence of a case-defined PAIS outcome at a FIXED post-infection horizon, conditional on documented acute infection at time zero (the pre-infection baseline window), COMPARED ACROSS JOINT STRATA of the baseline modifiers. It is associational w.r.t. the modifiers and (at most) interventionist only w.r.t. the separately-definable acute exposure (infection / its severity / a specific treatment regimen), with the host states as baseline effect modifiers — the framing the parent topic uses. The reviewer''s other two candidates — a joint 4-way exposure-combination causal contrast, and an intervention-on-one-exposure-modified-by-a-non-intervened-baseline — are STRONGER estimands requiring extra positivity/consistency and well-defined-intervention assumptions that do not currently hold; they are noted as future targets, not what this sketch identifies. Exposure levels (frailty index cutpoints; immunosuppressant class/duration; gestational timing; atopy vs diagnosed MCAS), time zero, the documented-infection conditioning, and the PAIS case definition (WHO vs CDC) must all be fixed before any estimate.'
  - ref: two-pairs-are-hypothesized-structures
    statement: 'HYPOTHESES, NOT RESULTS (Finding 4). The two "archetypes" are candidate structures, not demonstrated ones. Vinson2024 establishes an SOT-PASC association (N3C, aOR 1.48) and Hammel2023 an EARLY (<=6 mo, severity-unadjusted) frailty-PASC association — in SEPARATE populations; NEITHER measures immune reserve, so "frailty and immunosuppression converge on a shared reserve bottleneck" is hypothesis:0020 P2 (the explicitly fragile core), not an observed convergence. Likewise Bruno2024 measured EHR-CODED PASC components (lower cognitive/fatigue aHR 0.35/0.39; higher cardiac/thromboembolic 1.67/1.88) — NOT Tregs, Th1 biology, or mast-cell mediation; "pregnancy''s Treg arm dampens the Th1/neuro route" is one mechanistic reading competing with differential coding/ascertainment and normal pregnancy physiology. PAIR 1 = the shared-bottleneck HYPOTHESIS; PAIR 2 = the distinct/opposite-signed-route HYPOTHESIS. Their value is that they make different, testable structural predictions — not that either is shown.'
  - ref: dag-does-not-fix-interaction-sign
    statement: 'LOAD-BEARING LIMIT. A DAG encodes conditional-independence / identification structure; it does NOT determine the SIGN or magnitude of an interaction. Even IF the shared-bottleneck structure held, the pair could be super-additive OR sub-additive: convergence on immune-homeostatic-reserve yields super-additivity near a threshold (convex reserve->lock-in map, consistent with hypothesis:0004) but a CEILING / sub-additivity if one modifier already floors the reserve. The graph flags WHICH interaction terms and confounders an estimand would need and WHICH structural rivals are in play; it cannot answer superadditive-vs-distinct-route without a parametric outcome model, a scale choice, and the (unknown) shape of the reserve->outcome dose-response. Do not read the drawn convergence as evidence of synergy.'
  - ref: interaction-effect-measures-and-scale
    statement: 'EFFECT MEASURES (Finding 3, revised). "Superadditive" must name a scale, and additive vs multiplicative interaction can disagree in sign. But RERI/AP/synergy-index are NOT the general prescription: they require a single binary exposure contrast on a risk scale, whereas frailty is multi-level, immunosuppression is heterogeneous, pregnancy is time-varying, and atopy is not MCAS — and AP and especially the synergy index become UNSTABLE or uninterpretable under protective / opposite-signed effects (exactly the pregnancy x MCAS case). PRIMARY target should therefore be STANDARDIZED CUMULATIVE-INCIDENCE RISKS and RISK DIFFERENCES at a fixed horizon across defined strata; derive RERI only for specific, justified BINARY contrasts, and do not compute AP/S when component effects are opposite-signed. Soften the mechanism claim: positive additive interaction licenses a sufficient-component-cause ("both in one causal complex") reading only under additional no-unmeasured-confounding AND (often) monotonicity assumptions (VanderWeele, Epidemiol Methods 2014, doi:10.1515/em-2013-0005) — it is suggestive, not a mechanism proof.'
  - ref: interaction-confounding-and-adjustment-set
    statement: 'CONFOUNDING (Finding 6). Identifying an interaction requires blocking back-doors for BOTH modifiers AND common causes of the modifier-modifier association; a confounder of only one modifier-outcome relation biases the interaction term. {age, baseline-comorbidity} — the only shared confounders DRAWN — block ONLY the paths this sketch drew and are NOT a sufficient real-world set. A real analysis additionally needs, at minimum: treatment INDICATION and the underlying disease; transplant status/organ type; immunosuppressant class, dose, duration; sex and reproductive determinants; healthcare-utilization intensity; vaccination / prior-immunity status; calendar/variant era; infection-detection propensity; and acute treatment. Each is a candidate common cause of a modifier and PAIS (or of the modifier-modifier association) and is currently UNDRAWN — the graph is a schematic, not a completed confounder inventory.'
  - ref: non-identifiable-and-interaction-sensitivity
    statement: 'NON-IDENTIFIABILITY + SENSITIVITY (Finding 6). With unmeasured-shared-confounders (U) latent (U -> each modifier, U -> PAIS), the interaction is not point-identified by adjustment even given the full measured set above. A generic U plus an off-the-shelf E-value is NOT an interaction-specific sensitivity analysis: the relevant bias parameters are the strength of an unmeasured common cause of BOTH modifiers (which drives the spurious modifier-modifier association) and of each modifier-outcome relation, propagated to the interaction contrast (RERI / risk-difference-of-risk-differences), not to a single main effect. Interaction-specific E-value/bounding methods are limited and must be stated explicitly; until then the interaction is reported as bounded/uncertain, not estimated.'
  - ref: compound-selection-collider
    statement: 'SELECTION (Finding 6, expanded). Every modifier and PAIS itself causes hospital/clinic ascertainment; frailty/immunosuppression/age cause survival-selection. Conditioning on a clinic-/hospital-ascertained or prevalent-survivor sample conditions on a common descendant of both modifiers, inducing a spurious (typically negative) modifier-modifier association that biases the interaction term even when each main effect is unbiased. CRUCIAL CAVEAT: population-based sampling does NOT by itself remove the other conditioning events every PAIS study makes — conditioning on DOCUMENTED acute infection (detection depends on the modifiers), on ~30-day acute survival, and on study PARTICIPATION/consent. These are additional selection nodes not fully drawn here; each must be modelled (IPW / bias analysis), not assumed away. Do NOT condition on hospital-ascertainment or survival-selection as covariates.'
  - ref: mediators-not-conditioned-for-joint-effect
    statement: 'For a total joint effect, immune-homeostatic-reserve, persistent-antigen-fragment-burden, immune-dysregulation, th2-mast-cell-axis, thromboinflammation, and acute-infection-severity are MEDIATORS and are left UNADJUSTED. Two mechanism sub-questions condition deliberately: conditioning on immune-homeostatic-reserve tests whether a Pair-1 interaction RUNS THROUGH the (hypothesized) shared bottleneck; conditioning on acute-infection-severity gives a severity-controlled contrast. Caveat from real data: Hammel2023 did NOT adjust acute severity, so the frailty->acute-severity->PASC path was left open — the same trap will bias any compound estimand that silently omits severity.'
  - ref: phenotype-redirection-needs-resolved-outcome
    statement: 'For the pregnancy-state x MCAS pair the interaction may redirect PAIS PHENOTYPE rather than change total incidence (hypothesis:0020 P5). A single binary incidence outcome can show "no interaction" while Th2/mast-cell, thrombovascular, and Th1/neuro-cognitive-fatigue components move in opposite directions — the pattern Bruno2024''s coded-component dissociation is CONSISTENT WITH (not proof of). The outcome must be phenotype-resolved (component-specific endpoints); pais-outcome is drawn as a single node only for legibility.'
  - ref: mcas-construct-validity
    statement: 'CONSTRUCT VALIDITY of the MCAS arm (Finding 5). The modifier drawn is a PRE-INFECTION mast-cell/atopy state, but its cited support does not measure that construct: Wolff2023 concerns ASTHMA/RHINITIS/atopic disease (its own GRADE is VERY UNCERTAIN), not diagnosed MCAS — atopy is not MCAS. Augustin (the Cologne gut-immune-axis line; now a full paper — Mucosal Immunology 2026, doi:10.1016/j.mucimm.2026.03.002, PMID 41794369; cross-sectional, N=43, 15-22 mo POST-infection, no pre-infection baseline; the project''s "conference abstract only" note is stale) measures mast-cell activity AFTER infection, so it is CONSEQUENCE-side evidence and cannot ground a pre-infection effect-modifier arrow at all. The mast-cell-activation-hyperreactivity node is thus a HYPOTHESIZED pre-infection modifier whose exposure definition (diagnosed MCAS vs atopy proxy) and pre-infection ascertainment remain unmet; do not treat Augustin/Wolff as validating the upstream arrow.'
  - ref: cohort-design-requirements
    statement: 'DELIVERABLE for q0057 / future cohort design. A study able to estimate these interactions needs: (1) JOINT pre-infection measurement of both modifiers in the same subjects (not two single-modifier studies), with construct-valid definitions (diagnosed MCAS not atopy proxy; immunosuppressant class/duration not a binary); (2) the full confounder inventory in interaction-confounding-and-adjustment-set, not just {age, comorbidity}; (3) acute-illness severity measured; (4) a phenotype-resolved PAIS outcome under a stated case definition; (5) a fixed time zero (pre-infection baseline + documented infection) and horizon; (6) POPULATION-BASED sampling with the documented-infection / survival / participation selection nodes modelled; (7) enough DOUBLY-EXPOSED cells for an interaction term (compound strata are rare -> power on the joint cell is the usual binding constraint). D-004: the EHR sources with this covariate depth (N3C, OpenSAFELY, UKB) are gated / below the third-party-reproducibility bar; no compliant vehicle currently holds a usable doubly-exposed cell -> design aspiration, deferred pending the t097 find-datasets pass.'
  - ref: edges-are-unsourced
    statement: 'EDGE PROVENANCE (Finding 7). None of the 52 causes-edges carries a claim_ref, and the 5 new concepts'' source_refs are being populated only at the node level; the 7 patch-level citations ground the SCENARIO, not individual arrows. Readers must use the Edge-provenance table in the prose, which classifies each edge class as (i) observed association (few), (ii) analogical import from the menopause DAG / general immunology, (iii) structural/definitional, or (iv) purely hypothesized. The majority are (iii)/(iv). Reused nodes (hospital-ascertainment, biological-frailty, unmeasured-shared-confounders) were authored for the menopause DAG; their concept files now carry a compound-DAG usage note so the reuse does not silently redefine them.'
---

# Inquiry: Compound boundary conditions — co-occurring effect-modifier interaction DAG (t111)

## Summary

Causal **sketch** DAG for **task t111**, scoping the interaction structure of
`question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais` under
`hypothesis:0020-host-immune-baseline-reserve-gate`.

> **Status (read first).** This is an **unidentified causal sketch**, not an identified or
> evidence-bound interaction DAG. `science inquiry validate` confirms only resolution + acyclicity;
> the tool's causal checks are **non-functional here** (the exporter emits an empty model — see the
> `formal-checks-are-vacuous` assumption), so every adjustment/identification claim below is a
> **hand-derived** d-separation argument, and the drawn structure is a **hypothesis about how a
> compound-modifier analysis would have to be set up**, not a validated causal model.

**Estimand (see `estimand-definition`).** The four host-modifiers are baseline **host
characteristics**, not manipulable treatments — a `do()` on "frailty" or "pregnancy state" is
ill-defined and "immunosuppression" is a heterogeneous bundle — so the tool's
`treatment: concept:biological-frailty` field is a **technical placeholder**, not an interventionist
estimand. The estimand adopted is **descriptive effect-measure heterogeneity**: standardized
cumulative incidence of a case-defined PAIS outcome at a fixed post-infection horizon, conditional on
documented infection at time zero, **compared across joint strata** of the baseline modifiers —
associational w.r.t. the modifiers, the framing the parent topic uses. Stronger estimands (a joint
4-way exposure-combination contrast; an intervention on one exposure modified by a non-intervened
baseline) need extra assumptions that do not hold yet and are noted as future targets. The question
q0057 poses — *superadditive vs distinct routes* — is read off the graph as **which structural rival
is in play** plus **which terms and confounders an estimand would need**, not as a number the DAG can
emit.

> **What this DAG deliberately does NOT do.** It does **not** decide superadditive-vs-distinct-route.
> A DAG fixes conditional-independence / identification structure and the rival *shapes*; the **sign
> and magnitude** of an interaction additionally require a parametric outcome model, a **scale**
> (additive vs multiplicative), and the currently-unknown reserve → lock-in dose–response. The drawn
> convergence of frailty and immunosuppression on the shared reserve node is a *hypothesized*
> structural precondition for synergy, **not evidence of it** — and even if true the same node can
> produce a **ceiling / sub-additivity** if one modifier already floors reserve.

## The two focal pairs are two *hypothesized* structures

These are **candidate structures, not demonstrated ones** (see `two-pairs-are-hypothesized-structures`):
the cited studies are single-population associations that do **not** measure the convergence nodes.

| | **Pair 1 — frailty × immunosuppression** | **Pair 2 — pregnancy-state × MCAS** |
|---|---|---|
| Hypothesized archetype | **Shared bottleneck** (conjecture) | **Distinct / opposite-signed routes** (conjecture) |
| Conjectured convergence node | `immune-homeostatic-reserve` (+ antigen burden) | `th2-mast-cell-axis` (+ thrombo, immune-dysregulation) |
| h0020 mapping | P2 shared-mechanism / P1 reserve gate (**fragile core**) | P5 phenotype shift, not just incidence |
| What the evidence actually is | Vinson2024 SOT-PASC *association*; Hammel2023 early (≤6 mo, severity-unadjusted) frailty-PASC *association* — **separate populations, reserve never measured** | Bruno2024 **coded-component** dissociation (lower cognitive/fatigue, higher cardiac/thrombo) — **not** Tregs/Th1/mast-cell; Wolff2023 = **atopy** (asthma/rhinitis, GRADE *very uncertain*), **not** MCAS |
| Conjectured interaction | Super-additive near threshold **or** ceiling/sub-additive if reserve floored | **Sign-ambiguous / antagonistic**; may redirect phenotype |
| What breaks the naive "compound = more risk" intuition | Ceiling on a shared depleted node | Offsetting arms + phenotype redirection |

The **surviving substantive point** for q0057 is structural, not empirical: its dichotomy is a
**false binary** — a "same-route" structure and a "distinct-routes" structure are *both* possible, and
*neither* alone fixes whether risk compounds. Superadditivity is a **scale-and-dose-response** property
layered on top of the structure, and distinct-route pairs can be **antagonistic**, not merely additive.
Which structure actually holds is untested.

## Node roles

| Node | Role w.r.t. the modifier-interaction estimand | Handling |
|---|---|---|
| Biological frailty (M1) | Baseline modifier (multi-level; **tool `treatment` placeholder**, not an interventionist target) | Stratifying exposure |
| Chronic immunosuppression (M2) | Baseline modifier (**heterogeneous**: class/dose/duration/disease) | Stratifying exposure (interaction partner) |
| Pregnancy-state immune milieu (M3) | Baseline modifier (**time-varying**; Pair 2) | Stratifying exposure; opposite-signed routes |
| Atopy / MCAS (M4) | Baseline modifier (**atopy ≠ diagnosed MCAS**; Pair 2) | Stratifying exposure; construct-validity caveat |
| Chronological age | **Shared common cause of the modifiers** | **Adjust** — blocks *a* drawn back-door; **not** a sufficient set |
| Baseline cardiometabolic comorbidity | **Shared confounder (frailty & immunosuppression)** | **Adjust** — drawn subset only; see full inventory |
| Immune homeostatic reserve | **Hypothesized** shared mediator (bottleneck) | Do **not** adjust (joint effect); condition only for the mediation sub-test |
| Persistent antigen/fragment burden | Mediator (impaired-clearance route) | Do not adjust (joint effect) |
| Immune dysregulation | Mediator | Do not adjust (joint effect) |
| Th2 / mast-cell axis | **Phenotype-specific mediator (Pair 2)** | Do not adjust; resolve in the outcome |
| Thromboinflammation / endothelial dysfunction | Mediator (thrombovascular route) | Do not adjust (joint effect) |
| Acute infection severity | Mediator | Do not adjust for joint effect; **measure** (Hammel2023 omitted it) |
| PAIS outcome | Outcome | **Phenotype-resolve** for Pair 2 |
| Hospital / clinic ascertainment | **Collider (selection)** | **Do not condition**; population sampling; model selection |
| Survival selection / left-truncation | **Collider (selection)** | **Do not condition**; competing-risk / IPW |
| Unmeasured shared confounders (U) | Latent confounder (open back-door) | Identifiability threat — non-identifiable as drawn |

## Identifiability (hand-derived, NOT tool-verified)

> These are the author's d-separation arguments on the drawn edges. The toolchain did **not** check
> them: `export-pgmpy` emits an empty model and the confounder check reports "No common causes found"
> (it reads the wrong named graph — see `formal-checks-are-vacuous`). Read this as reasoning to be
> checked, not as a result.

- **U latent (real world):** the interaction is **not point-identified** by covariate adjustment —
  no measured set blocks U → {modifiers} and U → PAIS. Headline matches the menopause DAG.
- **Even with U set aside, `{age, baseline-comorbidity}` is NOT sufficient** — it blocks only the
  back-doors this schematic drew. A real analysis needs the fuller inventory (treatment indication and
  underlying disease; transplant status/organ; immunosuppressant class/dose/duration; sex/reproductive
  determinants; healthcare utilization; vaccination/prior immunity; variant/era; infection-detection
  propensity; acute treatment — see `interaction-confounding-and-adjustment-set`). Those nodes are
  **undrawn**; the graph is a schematic, not a completed confounder inventory.
- **Never condition** on `hospital-ascertainment` or `survival-selection` (common descendants of both
  modifiers → spurious modifier–modifier association → biased interaction term: the compound-selection
  collider). And note that population sampling does **not** remove the other selection events every PAIS
  study conditions on — **documented-infection detection, ~30-day acute survival, and participation** —
  which are further (largely undrawn) selection nodes to model, not assume away.
- **Mediators** (reserve, antigen burden, dysregulation, Th2/mast-cell, thrombo, severity) are
  excluded from the joint-effect set; conditioning on `immune-homeostatic-reserve` is the *mediation*
  test (does a Pair-1 interaction run through the *hypothesized* bottleneck?), and conditioning on
  `acute-infection-severity` gives the severity-controlled contrast — the path Hammel2023 left open.
- **Sensitivity** for the residual U must be **interaction-specific** — bias parameters for an
  unmeasured common cause of *both* modifiers propagated to the interaction contrast (RERI /
  difference-of-risk-differences), not a single-effect E-value (see `non-identifiable-and-interaction-sensitivity`).
- **16 nodes, 52 edges, acyclic** (`science inquiry validate`: reachability + acyclicity pass).

## What q0057 actually needs (interaction terms + cohort)

- **Terms:** report **standardized cumulative-incidence risks and risk differences at a fixed
  horizon** across defined strata as the primary quantity; derive **RERI only for specific, justified
  binary contrasts**, and do **not** compute AP / synergy-index when component effects are
  opposite-signed (unstable/uninterpretable — the pregnancy × MCAS case). Additive-scale departure is
  the decision-relevant "who-to-target" measure, but positive additive interaction supports a
  sufficient-cause mechanism reading only under extra no-unmeasured-confounding + monotonicity
  assumptions (VanderWeele 2014) — suggestive, not a mechanism proof.
- **Cohort (deliverable, see `cohort-design-requirements`):** joint pre-infection measurement of both
  modifiers with **construct-valid definitions** (diagnosed MCAS not an atopy proxy; immunosuppressant
  class/duration not a binary); the **full confounder inventory** (not just {age, comorbidity});
  measured acute severity; a **phenotype-resolved** outcome under a stated case definition; a fixed
  time zero + horizon; **population-based** sampling with the infection-detection / survival /
  participation selection nodes modelled; and enough **doubly-exposed** cells for the interaction term
  — the usual binding constraint, since compound strata are rare.
- **D-004:** the EHR sources deep enough for this (N3C, OpenSAFELY, UKB) are gated / below the
  third-party-reproducibility bar. No compliant vehicle currently holds a usable doubly-exposed
  cell → **design aspiration**, deferred pending the t097 find-datasets pass.

## Reverse causation / bidirectional coupling

`hypothesis:0020` P4 (frailty ↔ PAIS bidirectional coupling) would add a PAIS → frailty edge that
**cycles** this graph. As in the menopause DAG, it is handled by **temporal ordering** — modifiers
fixed at their **pre-infection** value — not a bidirectional edge; the feedback belongs to a separate
longitudinal inquiry.

## Edge provenance (Finding 7 — none of the 52 edges is individually sourced)

No `flow_edge` carries a `claim_ref`; the 7 patch-level citations ground the *scenario*, not any
single arrow. By epistemic class:

| Edge class | Examples | Provenance |
|---|---|---|
| **Observed association** (weakest link to *these* nodes) | immunosuppression → PAIS; frailty → PAIS | Vinson2024 / Hammel2023 — associational, single-population, reserve/mechanism unmeasured |
| **Analogical import** (from the menopause DAG / general immunology) | age/comorbidity → modifiers; severity/thrombo/dysregulation → PAIS; the selection colliders | Structure carried over by analogy; not re-established for compound strata |
| **Structural / definitional** | modifier → its named mediator route; mediator → PAIS chain | Definitional wiring of the hypothesized routes, not empirical claims |
| **Purely hypothesized** (the load-bearing conjectures) | frailty & immunosuppression → `immune-homeostatic-reserve`; pregnancy/MCAS → `th2-mast-cell-axis`; U → modifiers | h0020 P2/P5 conjecture; **no** direct evidence for the convergence nodes |

The **majority are structural/hypothesized**, not observed. Promoting any edge to an evidence-backed
`claim_ref` requires a proposition entity and is deferred.

## Notes

- Built via the inquiry patch-definition layout (layout v3); causal edges are `flow_edges` with
  `predicate: causes`, materialized to the `inquiry/<slug>` named graph by `science graph build`.
  **16 nodes, 52 edges** (authoritative count; an earlier draft mis-stated "17 nodes / 51 edges").
- Five new concept nodes were minted, now each with node-level `source_refs`:
  `chronic-immunosuppression`, `pregnancy-state-immune-milieu`,
  `mast-cell-activation-hyperreactivity`, `immune-homeostatic-reserve` (hypothesized bottleneck),
  `th2-mast-cell-axis` (phenotype route). Reused nodes (`biological-frailty`,
  `hospital-ascertainment`, `unmeasured-shared-confounders`) were authored for the menopause DAG and
  now carry a compound-DAG usage note so the reuse does not silently redefine them.
- Evidence bindings and their **limits**: Vinson2024 (SOT-PASC association), Hammel2023 (early,
  severity-unadjusted frailty association), Bruno2024 (coded-component dissociation — not mechanism),
  Chavatza2025 (rituximab impaired clearance), Peluso2022a (HIV exhaustion), Wolff2023 (atopy, *very
  uncertain*; not MCAS). **Augustin** (Cologne gut-immune-axis line) is now a full paper — Mucosal
  Immunology 2026, doi:10.1016/j.mucimm.2026.03.002, PMID 41794369 (cross-sectional, N=43, 15–22 mo
  post-infection); it is **consequence-side** and cannot ground a pre-infection MCAS arrow. The
  project's `Augustin2025` "conference abstract only" note is stale — spin-off task to reconcile the
  Augustin paper entity + topic maturity line.
- Next: `/science:critique-approach` for a further adversarial pass; the DAG stays a design artifact
  (unidentified sketch) until a construct-valid, doubly-exposed dataset is admissible (t097).
