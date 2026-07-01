---
id: patch-definition:immune-state-shift-causal-landscape
type: patch-definition
title: Immune-state-displacement causal landscape (PAIS)
status: active
created: "2026-06-30"
updated: "2026-06-30"
project: post-acute-infection
ontology_terms: []
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0022-immune-state-displacement-mediator-vs-co-traveler
- question:0008-formalize-vicious-cycle-attractor-model
- question:0016-oxidative-stress-upstream-driver-of-bioenergetic
- question:0006-jak-stat-il6-driver-vs-marker
- question:0009-functional-autoantibodies-drive-dysautonomia
- hypothesis:0002-tissue-reservoir-antigen-fragment
- hypothesis:0004-acute-severity-threshold
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- topic:gut-microbiome-barrier-axis
source_refs: []
content_preview: Sketch-level causal landscape around a persistent post-infectious immune-state displacement — an edged core spine (antigen → immune-state → SFN/vascular → O2/autonomic → symptom burden) with feedback-maintenance loops carried as DAG-inexpressible Unknowns, plus named upstream/parallel candidate systems held in prose (not yet edged) with plausibility × data-resolution priority tags.
file_path: entities/patches/immune-state-shift-causal-landscape.md
focal: hypothesis:0001-shared-dysregulated-attractor
scope_set:
- scope: local
neighborhood_policy:
  name: local-closure-v1
  version: local-closure-v1
  max_depth: 2
patch_type: inquiry
inquiry:
  profile: investigation
  status: specified
  boundary_roles:
  - ref: concept:persistent-antigen-fragment-burden
    role: BoundaryIn
  - ref: concept:pais-outcome
    role: BoundaryOut
  flow_edges:
  # forcing input
  - subject: concept:persistent-antigen-fragment-burden
    predicate: feedsInto
    object: concept:persistent-immune-state-displacement
    claim_refs: []
  # central state -> effectors
  - subject: concept:persistent-immune-state-displacement
    predicate: feedsInto
    object: concept:small-fiber-neuropathy-dysautonomia
    claim_refs:
      - "proposition:0040-vascular-metabolic-sfn-axes-plausible-effectors"
  - subject: concept:persistent-immune-state-displacement
    predicate: feedsInto
    object: concept:thromboinflammation-and-endothelial-dysfunction
    claim_refs:
      - "proposition:0040-vascular-metabolic-sfn-axes-plausible-effectors"
  - subject: concept:persistent-immune-state-displacement
    predicate: feedsInto
    object: concept:metabolic-mitochondrial-dysfunction
    claim_refs:
      - "proposition:0040-vascular-metabolic-sfn-axes-plausible-effectors"
  # the central HUB/mediator candidate (the contested claim; q0022)
  - subject: concept:persistent-immune-state-displacement
    predicate: feedsInto
    object: concept:pais-outcome
    claim_refs:
      - "proposition:0039-immune-state-displacement-mediates-vs-marks-pais-symptoms"
  # vascular / O2 limb (Joseph2023)
  - subject: concept:thromboinflammation-and-endothelial-dysfunction
    predicate: feedsInto
    object: concept:impaired-o2-delivery-extraction
    claim_refs: []
  - subject: concept:impaired-o2-delivery-extraction
    predicate: feedsInto
    object: concept:pais-outcome
    claim_refs: []
  # neuropathy / autonomic limb (h0007)
  - subject: concept:small-fiber-neuropathy-dysautonomia
    predicate: feedsInto
    object: concept:autonomic-dysfunction
    claim_refs: []
  - subject: concept:autonomic-dysfunction
    predicate: feedsInto
    object: concept:pais-outcome
    claim_refs: []
  # metabolic limb
  - subject: concept:metabolic-mitochondrial-dysfunction
    predicate: feedsInto
    object: concept:pais-outcome
    claim_refs: []
  assumptions:
  - ref: sketch-not-identified-dag
    derived_from: hypothesis:0001-shared-dysregulated-attractor
    statement: 'This is a SKETCH (status: sketch), not an identified causal DAG. Edges are candidate directional relations (sci:feedsInto), not estimated effects; no estimand is committed and no adjustment set is claimed. Promotion of any edge to a causal claim with an estimand belongs in a later causal-profile inquiry targeting a specific question (e.g. q0022 for the hub edge).'
  - ref: descriptive-vs-hub-split
    derived_from: question:0022-immune-state-displacement-mediator-vs-co-traveler
    statement: 'Two claims are kept strictly separate. (i) DESCRIPTIVE: PAIS often involve a persistent immune-state displacement (relatively well-aligned with evidence). (ii) CAUSAL-HUB: immune state is the central mediator through which most symptoms arise (much less settled). The single edge persistent_immune_state_displacement -> pais-outcome encodes claim (ii) and must not inherit support from claim (i); it is the focal estimand of question:0022 and the live test is the abrocitinib JAK1 readout (h0003 / pre-registration:0004).'
  - ref: degenerate-realization-evidence-bar
    derived_from: proposition:0037-shared-analyte-signature-not-required-for-immune-state-displacement
    statement: 'The shared object is a persistent STATE displacement that may be DEGENERATELY realized — many molecular configurations producing one persistent macro-state. Consequently shared-ANALYTE nulls (Galbraith2011, Patterson2024, Chowdhury2026, the t035 pathway-overlap null) weaken "shared molecular signature", NOT automatically "shared persistent state displacement". The strong shared-pathway prediction (q0001) remains the most discriminating POSITIVE test but is not a precondition for the displacement frame.'
  - ref: feedback-loops-not-dag-expressible
    derived_from: proposition:0041-feedback-maintenance-requires-dynamical-treatment-outside-dag
    statement: 'The immune<->autonomic and immune<->metabolic MAINTENANCE loops are genuine cycles and are NOT expressible in an acyclic flow/DAG. They are carried as sci:Unknown nodes (immune_autonomic_feedback_loop, immune_metabolic_feedback_loop), not faked with arrows. Static DAGs can represent candidate directional relations and intervention/confounding questions; they cannot represent attractor maintenance, hysteresis, or feedback stability. Those are deferred to a time-indexed / dynamical-systems treatment (question:0008; cf. peer project ~/d/health/processes/cycles).'
  - ref: candidates-in-prose-not-edged
    derived_from: hypothesis:0001-shared-dysregulated-attractor
    statement: 'Upstream/parallel candidate systems with thin PAIS-specific evidence (HPA/cortisol rhythm, circadian clock, gonadal hormones, mast-cell/connective-tissue, CNS/glial/neuroinflammatory, microbiome/gut-barrier, autoimmune diathesis) are deliberately held in PROSE (see "Candidate upstream/parallel systems not yet edged"), NOT added as edged graph variables. This prevents laundering speculation into graph structure and keeps thin candidates from looking equivalent to the evidenced spine. Promote a candidate to an edged node only when evidence or a specific testable question warrants it.'
  transformations: []
  unknowns:
  - concept:immune-autonomic-feedback-loop
  - concept:immune-metabolic-feedback-loop
---

# Inquiry: Immune-state-displacement causal landscape (PAIS)

## Summary

A **sketch-level** causal landscape situating the immune system within PAIS, built to
operationalize a reframed `hypothesis:0001`. The reframe stops asserting *a single
stable dysregulated attractor* (which implies every subtype should share one analyte /
gene module / cytokine hub / molecular lesion) and instead posits a **persistent
post-infectious immune-state displacement, potentially realized through heterogeneous
molecular configurations and maintained by immune-autonomic-metabolic feedback.** The
useful attractor idea (self-sustaining basin, multi-loop maintenance, resistance to
single-target therapy) is preserved; the over-strong shared-molecule implication is
dropped.

The landscape models immune state as a **central latent node** with upstream forcing,
downstream effectors, and bidirectional maintenance loops — *not* as a simple
"treatment". Its primary job is to **keep the alternative upstream/parallel drivers
visible while preventing h0001 from being judged by the wrong evidence bar**:
shared-analyte nulls should weaken "shared molecular signature", not automatically
"shared persistent state displacement".

## The two claims (kept separate)

- **Descriptive** — PAIS often involve a persistent immune-state shift. Plausible,
  relatively well-aligned with evidence.
- **Causal-hub** — immune state is the central *mediator* through which most symptoms
  arise. Much less settled; spun out as `question:0022` and tested separately. The one
  edge `immune-state-displacement → pais-outcome` carries this claim; the live test is
  the abrocitinib JAK1 readout (`hypothesis:0003`, `pre-registration:0004`).

## Proposition families (formalized)

The five families are now durable proposition entities — evidence buckets designed so
future evidence lands in the right one and descriptive immune involvement is never
re-blurred with causal-hub status. None are adjudicated; each is held at its honest layer.

1. **Degeneracy / evidence-bar** [`structural_claim`] — `proposition:0037`: a shared
   analyte signature is **not required** for h0001; shared-analyte nulls weaken "shared
   molecular signature", not "shared state displacement".
2. **Persistence (descriptive)** [`empirical_regularity`] — `proposition:0038`: a
   persistent immune-state displacement *occurs* in PAIS. Proxy-measured; asserts the
   shift exists, **not** that it drives symptoms.
3. **Mediation vs marker (hub)** [`causal_effect`, contested] — `proposition:0039`: the
   displaced state *mediates* symptoms rather than *marking* another process. Focal
   estimand of `question:0022`; wired to the hub edge; must not inherit (2)'s support.
4. **Effectors** [`mechanistic_narrative`] — `proposition:0040`: vascular, metabolic,
   and SFN axes are plausible *downstream effectors*. Wired to the three
   immune-state→effector edges.
5. **Feedback maintenance is dynamical** [`structural_claim`] — `proposition:0041`:
   the immune⇄autonomic / immune⇄metabolic maintenance loops need dynamical-systems
   treatment (`question:0008`), not DAG arrows; carried as the two `unknowns`.

## Core spine (edged now)

Graph nodes with tentative directional (`feedsInto`) edges:

- `persistent antigen fragment burden` **→** `immune-state displacement` *(forcing input; h0002)*
- `immune-state displacement` **→** `small-fiber neuropathy / dysautonomia` *(h0007)*
- `immune-state displacement` **→** `endothelial / vascular dysfunction` *(h0004)*
- `immune-state displacement` **→** `metabolic / mitochondrial dysfunction`
- `immune-state displacement` **→** `PAIS symptom burden` *(the hub/mediator candidate — q0022)*
- `endothelial / vascular dysfunction` **→** `impaired O₂ delivery/extraction` **→** `PAIS symptom burden` *(Joseph2023 limb)*
- `small-fiber neuropathy / dysautonomia` **→** `autonomic dysfunction` **→** `PAIS symptom burden`
- `metabolic / mitochondrial dysfunction` **→** `PAIS symptom burden`

Vascular and metabolic are placed **in the spine** (not as candidates): they are the
best-evidenced parallel actors (the male vascular hard-endpoint signal under h0004;
Joseph2023 preload-failure + impaired peripheral O₂ extraction; Appelman2024 muscle
OXPHOS), and burying them as candidates would hide exactly the alternatives the sketch
exists to keep in view.

### Feedback loops — carried as Unknowns, not arrows

`immune ⇄ autonomic` and `immune ⇄ metabolic` maintenance are genuine **cycles** and
sit in the inquiry's `unknowns` (as `sci:Unknown` nodes), because an acyclic flow/DAG
**cannot** express them. This is the structurally honest encoding of the "DAG view is
unsuitable" concern — see the next section.

## DAGs vs dynamical models (don't reject DAGs wholesale)

- **DAGs** are the right tool for *confounding / intervention / mediation* questions
  about individual candidate directional relations (e.g. the menopause→PAIS total
  effect in `menopause-pais-causal-dag`, or the q0022 hub estimand).
- **Time-indexed / dynamical-systems models** are required for *maintenance*: attractor
  stability, bistability, hysteresis (recovery threshold ≠ onset threshold), and
  critical slowing. A static DAG can represent candidate directional relations but
  **not** feedback stability.
- Project stance: a static DAG/flow sketch represents candidate directional relations;
  it does **not** represent attractor maintenance, hysteresis, or feedback stability.
  Those are owned by `question:0008` and the peer project
  `~/d/health/processes/cycles`.

## Candidate upstream/parallel systems not yet edged

Held in prose deliberately (see the `candidates-in-prose-not-edged` assumption), tagged
by **biological plausibility × data resolution**:

- **HPA / cortisol axis** — *high-plausibility / thin-PAIS-evidence*; master immune
  regulator, hypocortisolism reported in ME/CFS. Rhythm-sensitive → needs
  cycles-aware (timestamped) sampling.
- **Circadian clock** — *high-novelty / low-data*; clock gates cytokine and
  glucocorticoid rhythms and could *hold* a displaced state. The natural bridge to the
  `cycles` peer; data resolution is the bottleneck (needs repeated timestamped measures).
- **Gonadal hormones (E2 / testosterone)** — *high-plausibility / partly-covered*;
  already `hypothesis:0005` (homeostatic-margin), with a bounded testosterone-conditioned
  immune exception. UKB-gated for the decisive test.
- **Mast-cell / connective-tissue substrate (incl. hEDS)** — *high-plausibility /
  thin-evidence*; explanatorily load-bearing because hEDS (a non-infectious
  dysautonomia) carries comparable-or-greater SFN — the `hypothesis:0007` specificity
  caveat. A partly non-immune substrate.
- **CNS / glial / neuroinflammatory axis** — *high-plausibility / uncertain-direction*;
  systemic enough to shape fatigue, cognition, sleep, autonomic tone. Counter-signal:
  the TSPO-PET null across ME/CFS and QFS (Raijmakers2021).
- **Microbiome / gut-barrier axis** — *high-plausibility / data-quality-varies*;
  plausible upstream or maintaining input into immune tone. Already carried as a local
  reinforcing node (`proposition:0031`), mature only for long COVID + ME/CFS.
- **Autoimmune diathesis as effect-modifier** — *high-data / uncertain-direction*; see
  fast-follow below.

## Fast-follow: autoimmune diathesis as effect-modifier

The cleanest near-term empirical check. Framing: **pre-existing autoimmune diathesis as
an effect-modifier for post-infectious failed recovery**, conditioned on **sex, age,
acute severity, ascertainment intensity, and healthcare-contact bias** — *not* as a
mechanism claim (that is `hypothesis:0007` territory). Trap: autoimmunity and long COVID
are both female-predominant, so any naive association is **sex-confounded** (the
project's standing measurement-channel meta-finding, `hypothesis:0008`). Neighbors:
`question:0005` (latent→overt autoimmunity conversion; Rojas2022). Tracked as a task for
a sex-conditioned EHR/cohort check.

## Status & next steps

- **Tentative throughout** — every edge is a candidate proposition, not a validated
  relation; the hub edge in particular is contested.
- `/science:specify-model immune-state-shift-causal-landscape` to formalize the five
  proposition families and attach evidence.
- `/science:critique-approach` when the q0022 hub estimand is drawn as its own
  causal-profile inquiry (it will need an explicit adjustment set and collider audit).
- Promote a candidate system to an edged node only when evidence or a specific testable
  question warrants it.
