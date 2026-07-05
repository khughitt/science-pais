---
id: "meta:0001-next-steps-2026-07-01"
kind: "meta"
title: "Next Steps — 2026-07-01"
status: "active"
created: "2026-07-01"
updated: "2026-07-01"
related:
  - "patch-definition:immune-state-shift-causal-landscape"
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "question:0022-immune-state-displacement-mediator-vs-co-traveler"
  - "question:0008-formalize-vicious-cycle-attractor-model"
  - "question:0005-latent-to-overt-autoimmunity-conversion"
---

# Next Steps — 2026-07-01

Scope: does recent work cover the gaps/questions from the project-framing discussion
(the h0001 reframe) and discussion:0002? What slipped? What new entities are worth creating?

## Recent Progress

- **h0001 reframed from "single shared attractor" to "persistent immune-state displacement,
  degenerately realized"** — landed as a durable structure: `patch:immune-state-shift-causal-landscape`
  (edged spine + prose candidate layer), five proposition families (`prop:0037`–`0041`), `q0022`
  (mediator-vs-marker), 8 concept nodes, and the h0001 rewrite.
- **The A/B split the discussion demanded is encoded and enforced** — descriptive persistence
  (`prop:0038`, empirical_regularity) is held strictly separate from the causal-hub claim
  (`prop:0039`, causal_effect, contested); the single `immune-state → pais-outcome` edge carries the
  hub claim and is explicitly forbidden from inheriting the descriptive claim's support.
- **Evidence-bar reframe (degeneracy)** — `prop:0037` makes shared-analyte nulls (Galbraith2011,
  Patterson2024, Chowdhury2026, t035) weaken "shared *molecule*" without touching "shared *state*."
- **Feedback loops handled honestly** — immune⇄autonomic / immune⇄metabolic maintenance carried as
  `sci:Unknown` nodes (not faked arrows), deferred to `q0008` + the `~/d/health/processes/cycles` peer.
- **Autoimmune-diathesis fast-follow is the most-invested thread** — plans 0005/0006, search 0009,
  and t079 (BC-1..BC-7 all resolved this session: N3C primary + OpenSAFELY replication vehicle
  decision, PASC definition lock, severity dateability, individual utilisation). Design-complete,
  execution data-gated on N3C.
- **Two candidate hypotheses from emergent-threads: one promoted, one not** — the measurement-channel
  candidate became `h0008`; the *longitudinal latent→overt autoimmune conversion* candidate (to house
  the `q0005` orphan) was **not** created.

## Current State

- **P2 active/blocked:** t079 (autoimmune-diathesis feasibility, in-progress, design-complete →
  data-gated on N3C synthetic prototype); t028 (UKB menopause, blocked on data); t050 (SFN biopsy
  vehicle, blocked on G2 control arm); t054 (abrocitinib readout, blocked on trial — ACTIVE_NOT_
  RECRUITING, primary completion 2026-03-27, no results yet).
- **8 hypotheses / 22+ questions**, all hypotheses `proposed`. h0001 reframed; h0008 (measurement)
  newest.
- **No `results/` run bundles** tied to this thread yet — the landscape is a specified *sketch*, and
  every decisive test downstream is data-gated (abrocitinib, UKB, N3C) or parked-in-prose.
- **`science health`:** clean except one TODO — `prop:0039` "mechanistic proposition lacks linked
  lower-layer support" (expected: as the contested hub claim it should stay marked provisional/
  unidentified rather than borrow `prop:0038`'s support).
- **Cross-project sync is 3 days stale** — relevant here because the circadian thread's natural home
  is the `health-cycles` peer.

## Coverage Gaps

### Coverage Map (discussion point → artifact)

| Discussion point | Coverage | Direction | Key gap |
|---|---|---|---|
| Reframe: state-displacement, not shared gene | **Strong** | new | — |
| Degeneracy / evidence-bar relocation | **Strong** | new | — |
| A/B descriptive-vs-hub split (don't let B ride on A) | **Strong** | new | — |
| Hub (B) tested by abrocitinib | **Strong** | new | wiring explicit in q0022/prop0039/patch |
| Causal layer-cake (upstream/parallel/downstream) | **Strong** | new | vascular/metabolic/SFN spine edged; rest prose |
| Feedback loops as DAG-inexpressible | **Strong** | new | carried as `sci:Unknown` |
| Autoimmune diathesis as sex-conditioned effect-modifier | **Strong** | new | t079 design-complete, data-gated |
| Cycles-project collaboration (circadian) | **Partial** | new | named 3× but no task/shared-question/sync — *no motion* |
| HPA / cortisol axis | **Partial** | new | parked as "thin-evidence"; likely undersold; no question |
| Dynamical signatures as concrete tests | **Partial** | stable | hysteresis/bistability/critical-slowing captured; **bimodality + transient-kick absent** |
| q0005 latent→overt autoimmune conversion | **Missing** | stable | still orphan; candidate hypothesis never created |

### High-Impact Gaps (what actually slipped)

The reframe itself is *well* covered — arguably more complete than the discussion (the patch also
added CNS/glial and microbiome candidates the discussion didn't list, and imposed a "don't launder
speculation into graph structure" discipline). The gaps are all about **forward motion on parked
items**, not missing structure:

1. **`q0005` is still structurally an orphan.** Its `related:` holds only a topic; the h0001 link is a
   one-directional prose mention, not reciprocated. The autoimmune-diathesis thread (t079) covers the
   *reverse* arrow (pre-existing diathesis → PAIS risk); `q0005` is the *forward* arrow (PAIS → later
   overt autoimmunity over 5–10 yr) — genuinely distinct and still unhoused. Emergent-threads even
   drafted the candidate hypothesis. **Decision needed:** promote that hypothesis, or reciprocate the
   h0001 edge and park explicitly.
2. **Circadian/cycles is the discussion's flagged "highest-novelty play" but has zero motion.** Named
   three times, no task, no bridging question, no cross-project scan — and sync is 3 days stale. This
   is the cheapest uniquely-additive step in the whole map: a bridging question + a scan of what
   `health-cycles` already holds on immune–circadian coupling.
3. **Two dynamical signatures are missing from the falsifier set: bimodal outcome distribution and
   kick-out-able / transient-intervention.** hysteresis, bistability, and critical slowing are all in
   `prop:0041`/`q0008`/h0001; the other two aren't. **Bimodality is the cheapest near-term empirical
   check in the project** — testable in *existing* longitudinal recovery-trajectory data (latent-
   transition modeling / Gusinow2026 is already named in q0008 as substrate), no new data required. It
   turns the "resonance/feedback" intuition into a runnable test instead of a wholesale deferral.
4. **HPA/cortisol may be undersold as "thin-PAIS-evidence."** Hypocortisolism in ME/CFS is a
   decades-old replicated finding; a light literature calibration would decide whether HPA promotes
   from prose to an edged node. Lower priority than #1–#3.

## Status Transitions

No prior next-steps analysis exists (`entities/meta/` was empty — this is the first). No delta.

## Task Tracking Gaps

The patch's own "Status & next steps" names three follow-ups (`/science:specify-model`,
`/science:critique-approach` on the q0022 hub estimand, promote-candidate-on-evidence) — none are
tracked as tasks. The q0022 hub estimand in particular is the natural next causal-profile inquiry and
should be a trackable task before it drifts.

## Strategic Decision Point

**Push parked candidates into motion, or hold the sketch and wait on the data-gated tests?**

- The landscape is *specified* but every edged/decisive test downstream is data-gated (abrocitinib
  readout, UKB menopause, N3C autoimmune prototype) or parked-in-prose (HPA, circadian, MCAS/hEDS,
  CNS/glial, microbiome).
- **Recommendation:** do exactly the two *cheap, uniquely-additive* motions and hold the rest parked —
  (a) the circadian↔cycles bridge (near-zero cost, high novelty, the one collaboration the discussion
  singled out), and (b) the bimodality empirical check (runnable on existing data, converts the
  dynamical claim from vibe to test). Everything else (HPA promotion, MCAS/hEDS edging) stays in prose
  until evidence or a specific question warrants it — which is exactly the patch's stated discipline.
  This keeps forward motion without over-investing in speculation while the gated tests mature.

## Recommended Next Actions

| Priority | Action | Rationale | Command |
|---|---|---|---|
| P2 | Resolve the `q0005` orphan: create the longitudinal latent→overt autoimmune-conversion hypothesis (or reciprocate h0001 edge + park) | Only genuinely *unhoused* discussion thread; distinct from the t079 reverse-arrow work | `/science:add-hypothesis` or `science tasks add` |
| P2 | Add bridging question: does circadian/HPA rhythm *hold* the displaced immune state? + scan `health-cycles` for existing immune–circadian coupling | Discussion's flagged highest-novelty play; currently zero motion; cheapest additive step | `science tasks add "circadian/HPA-holds-immune-state bridge to cycles"` then `/science:sync` |
| P2 | Operationalize the **bimodality** dynamical signature on existing longitudinal recovery data; add bimodality + transient-kick to `prop:0041`/h0001 falsifiers | Cheapest near-term empirical test of the attractor claim; two signatures currently missing | `science tasks add` (link `q0008`, `prop:0041`) |
| P3 | Draw the `q0022` hub estimand as its own causal-profile inquiry (adjustment set + collider audit) | Patch names it as next step; untracked; the contested B-claim's formal test | `/science:sketch-model` → `/science:critique-approach` |
| P3 | Light HPA/cortisol literature calibration — decide prose vs edged node | Possibly undersold ("thin-evidence"); hypocortisolism in ME/CFS is well-replicated | `/science:search-literature` |
| P3 | Cross-project sync (3 days stale) | Needed anyway; directly serves the circadian/cycles bridge | `/science:sync` |

## Session Summary

The h0001 reframe was executed cleanly and thoroughly — the discussion's core moves (degeneracy
evidence-bar, A/B descriptive-vs-hub split, abrocitinib-as-live-test, feedback-as-Unknowns, sex-
conditioned autoimmune-diathesis fast-follow) all landed as durable, correctly-layered structure, and
the patch's prose-candidate discipline is a genuine improvement over the discussion's flat lists.
What remains is *motion on parked items*: the `q0005` orphan was left unhoused, and the two cheapest
uniquely-additive threads the discussion emphasized — the circadian↔`cycles` collaboration and a
runnable bimodality test of the attractor — have structure-adjacent homes but no tasks. Those are the
recommended next actions.
