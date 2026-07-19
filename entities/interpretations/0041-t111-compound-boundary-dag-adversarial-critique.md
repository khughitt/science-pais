---
id: interpretation:0041-t111-compound-boundary-dag-adversarial-critique
kind: interpretation
title: 't111: adversarial critique of the compound-boundary interaction DAG — unfalsifiable-on-admissible-data, and a mediation-test collider contradiction'
status: active
source_refs: &id001
- patch-definition:compound-boundary-conditions-interaction-dag
related:
- patch-definition:compound-boundary-conditions-interaction-dag
- question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais
- hypothesis:0020-host-immune-baseline-reserve-gate
- topic:population-boundary-conditions-and-effect-modifiers-in-pais
- task:t111
created: '2026-07-19'
updated: '2026-07-19'
input: *id001
prior_interpretations: []
relations: []
---

# Causal DAG Critique: Compound boundary conditions — co-occurring effect-modifier interaction DAG (t111)

**Product of** `/science:critique-approach` (discussant role). The framework command specifies
`entities/inquiries/<slug>-critique.md`, but this project reserves `entities/inquiries/` for numbered
`inquiry` entities, so the critique is filed here as an `interpretation` (the project's analysis-verdict
kind), linked to `patch-definition:compound-boundary-conditions-interaction-dag`.

**Inquiry:** `compound-boundary-conditions-interaction-dag` (`patch-definition`, `inquiry.profile: causal`, `inquiry.status: sketch`)
**Treatment (structured field):** `concept:biological-frailty`
**Outcome:** `concept:pais-outcome`
**Reviewed:** 2026-07-19 · discussant role
**Reviewed-status:** critiqued — records that adversarial review *ran*, not that the sketch passed.

> **Framing.** The artifact already carries 14 self-caveats and honestly labels itself an
> *unidentified causal sketch*. A rubber-stamp of those caveats is not the job. This critique targets
> what the correction pass **still gets wrong or leaves undefended** — an internal contradiction
> between two of its own caveats, an unfalsifiability/observational-equivalence limit that guts its
> stated testable value, an undrawn inter-modifier edge that breaks the symmetric-modifier frame, and
> a structured-vs-prose contradiction that will mislead any tool-driven consumer. It closes with the
> honest marginal-value question: after this much caveating, what is the graph *for*?

---

## Structural Validation

`science inquiry validate` (v0.4.1) — 7 pass, 2 skip:

| check | status | note |
|---|---|---|
| boundary_reachability, no_cycles, unknown_resolution, target_exists, orphaned_interior, causal_acyclicity | **pass** | resolution + acyclicity only |
| confounders_declared | **pass** — *"No common causes found"* | **false-clean:** age, comorbidity, and U are all drawn as common causes; the check reads `graph/causal`, where these edges do not live |
| identifiability, adjustment_sets | **skip** | `pgmpy not installed` |

**Two independent reasons no formal identification ran** (both confirmed live this session, not inherited):
1. `export-pgmpy` emits `DiscreteBayesianNetwork([])` — an **empty** model — because the exporter reads the `graph/causal` named graph while the 52 edges live in `inquiry/<slug>`. The generated script would then compute back-door sets over *zero* edges.
2. `pgmpy` is not installed in the project env, so the `identifiability` and `adjustment_sets` checks **skip** regardless.

Consequence: **Step 2 of `/science:critique-approach` (pgmpy graph-theoretic analysis) cannot be executed here.** Every identifiability statement below — like every one in the sketch — is **hand-derived d-separation on the drawn edges**, not a tool result. The `formal-checks-are-vacuous` caveat correctly discloses (1); it does **not** mention (2), and it should, because installing `pgmpy` alone will *not* fix the empty export — a reader who runs `uv add pgmpy` will get green identifiability checks computed over an empty graph, which is *worse* than a skip.

---

## Identifiability & Testability Assessment (hand-derived)

Parsed edge set: **16 nodes, 52 edges, acyclic** (confirms the sketch's authoritative count). In/out degrees computed directly.

### T1 (headline) — The DAG imposes essentially **no refutable constraint on any admissible dataset**

`unmeasured-shared-confounders` (U) → {frailty, immunosuppression, pregnancy, MCAS, pais-outcome}: a single latent common cause of **all four modifiers and the outcome**. `chronological-age` → all four modifiers + outcome. `pais-outcome` has **in-degree 13** — nearly every node points straight at the outcome.

Net effect: over the *measurable* set {age, comorbidity, the four modifiers, severity, outcome}, the graph predicts **"everything is associated with everything"** — no conditional independence involving the outcome survives U, and the four modifiers stay mutually dependent even given {age, comorbidity} because U keeps them tied. A DAG whose every testable implication lives in the **unmeasured layer** (reserve, th2-axis, dysregulation, antigen, thrombo — all conjectural, `source_refs` empty) is, on an admissible cohort, **unfalsifiable**. This is a stronger statement than the sketch's "non-identifiable": non-identification says *you can't get a point estimate*; this says *you can't even test the structure*. It should be stated as such.

### T2 (critical, internal contradiction) — The prescribed **mediation sub-test conditions on a collider the sketch's own rule forbids**

`immune-homeostatic-reserve` has **in-degree 4**: parents = {age, comorbidity, **frailty**, **immunosuppression**}. It is therefore a **common descendant of both Pair-1 modifiers**.

- `compound-selection-collider` (the sketch's own caveat) states: *"Conditioning on a common descendant of both modifiers … induces a spurious modifier–modifier association that biases the interaction term."*
- `mediators-not-conditioned-for-joint-effect` (also the sketch's own caveat) **prescribes** exactly that: *"conditioning on `immune-homeostatic-reserve` tests whether a Pair-1 interaction runs through the shared bottleneck."*

These two caveats are in **direct conflict**. Conditioning on reserve to "test mediation" opens the collider path `frailty → reserve ← immunosuppression`, manufacturing the very frailty–immunosuppression association that biases the RERI/risk-difference interaction contrast. The same defect hits the prescribed **"severity-controlled contrast"**: `acute-infection-severity` is *also* in-degree-4 (parents {age, comorbidity, frailty, reserve}) — a collider **and** a mediator — so conditioning on it both over-adjusts (blocks part of the frailty effect, which the sketch notes) **and** opens collider paths (which it does not note). A clean mediation test here needs the mediator to be free of exposure-induced collider structure or an explicit sensitivity/g-formula treatment of it; simple stratification on reserve or severity is not valid. **This is the sharpest remaining defect** — not a missing caveat but a contradiction between two present ones.

### T3 (critical) — The two "archetypes" are **observationally equivalent on the incidence scale**; their only distinguishing prediction requires data the design admits it cannot get

The sketch's surviving substantive claim is that shared-bottleneck (Pair 1) and distinct-routes (Pair 2) *"make different, testable structural predictions."* But everything that distinguishes them lives in the **unmeasured convergence nodes** (`immune-homeostatic-reserve`, `th2-mast-cell-axis`, `immune-dysregulation`). On any cohort lacking those measurements — which `cohort-design-requirements` concedes is every admissible cohort — the two wirings imply the **same** conditional independencies over measurables and are **Markov-indistinguishable at the incidence level**. The genuine distinguishing signal is the **phenotype-component vector** (Pair 2 predicts opposite-signed components; Pair 1 predicts same-signed amplification), which *is* outcome-observable — but only with a phenotype-resolved outcome **and enough doubly-exposed cells**, the exact resource D-004 blocks. So "they make different testable predictions" is true **only in a data regime that does not exist**. The sketch should scope the claim to the phenotype-vector level and state plainly that the incidence-scale contrast is untestable.

### T4 — Inert selection nodes

`hospital-ascertainment` (in 6, **out 0**) and `survival-selection` (in 3, **out 0**) are pure sinks. As drawn (unconditioned) they do **zero** d-separation work — they are *warnings* about what not to condition on, not operative structure, and `survival-selection` isn't even wired into an observation/ascertainment node, so left-truncation isn't actually represented, only gestured at. Fine as annotation; the prose should not imply they contribute identifying content.

---

## Edge-by-Edge / Missing-Structure Review

### M1 (important, missing edge) — No **inter-modifier** edges; the symmetric-modifier frame is an undefended assumption

The four modifiers connect only via shared causes (age, comorbidity, U). But **chronic immunosuppression plausibly *causes* frailty** — both through the immunosuppressant drugs and through the underlying disease that indicates them (transplant, autoimmune disease, malignancy accelerate a frailty phenotype). If a direct `chronic-immunosuppression → biological-frailty` (or disease-mediated) edge exists, **frailty is partly a mediator of immunosuppression**, not a parallel co-equal modifier — and the entire "interaction between two baseline modifiers" estimand is misspecified (you'd want a mediation decomposition, not a symmetric interaction term). The sketch draws the zero-edge case without defending it. At minimum this belongs in the assumptions as an explicit, load-bearing "no inter-modifier causation" premise with its biological counter-case named.

### M2 — `treatment: biological-frailty` in the **structured** block contradicts the **prose** estimand

`estimand-definition` (prose) disclaims any `do()` on the host states and adopts descriptive stratum heterogeneity. But the machine-readable `inquiry.treatment` field still names `biological-frailty`, and `inquiry.status` is `sketch` — so the moment the exporter bug is fixed and `pgmpy` installed, the toolchain will hand a consumer **back-door adjustment sets for an interventionist frailty→PAIS effect**, precisely the reading the prose rejects. The correction landed in prose the tool never reads. There is no structured field for "descriptive estimand," so the honest fix is either (a) a prominent structured marker (e.g., keep `status: sketch` *and* add a `treatment`-adjacent note/annotation the exporter surfaces) or (b) accept and **flag** that the structured layer encodes a placeholder that will mislead automated readers. Right now the two layers disagree silently.

### M3 — Edges carry no two-axis evidence labels

Per `references/dag-two-axis-evidence-model.md`, edges should carry `edge_status` (replication) × `identification` (causal-identification), defaulting to `unknown`/`none` — explicitly **not** `observational`. The sketch's prose Edge-provenance table (observed / analogical / structural / hypothesized) is a reasonable hand-classification, but it is prose-only and **not machine-checkable**. Adopting even coarse `edge_status`/`identification` on the flow-edges would make the load-bearing claim — "the majority are structural/hypothesized, few observed" — auditable by `science dag audit` rather than asserted, and would prevent a future reader from silently upgrading a hypothesized convergence edge to observational.

---

## Sensitivity Analysis

| Assumption | If violated | Impact | Robustness |
|---|---|---|---|
| Mediation test = condition on `immune-homeostatic-reserve` (T2) | Reserve is a collider of both modifiers → stratifying on it induces spurious frailty–immunosuppression association → biased interaction term | **high** — the prescribed sub-analysis returns a *biased* interaction, and the bias mimics the very synergy being tested | Not robust; needs g-formula / mediation-with-exposure-induced-confounding, not stratification |
| "Two archetypes make different testable predictions" (T3) | On any admissible (mediator-unmeasured) cohort the wirings are Markov-equivalent at the incidence level | **high** — the sketch's stated *raison d'être* holds only for phenotype-vector outcomes on a doubly-exposed cohort that D-004 blocks | Survives only as a phenotype-resolved claim, not an incidence claim |
| No inter-modifier causation (M1) | immunosuppression → frailty makes frailty a mediator | **moderate–high** — reframes interaction as mediation; changes the estimand and the adjustment set | Undefended; biologically contestable |
| Structured `treatment=frailty` is inert (M2) | A tool consumer reads it as an interventionist estimand | **moderate** — wrong estimand propagates to any automated downstream, silently | Depends entirely on human reading the prose the tool ignores |
| U is the only latent confounder | Additional latents (indication, utilization, era…) unmodelled | **high** for any *estimate* | Already conceded non-identifiable; T1 shows also unfalsifiable |
| `{age, comorbidity}` sketch adjustment set | Real set is far larger (indication, drug class/duration, transplant, vaccination, era, detection…) | **high** | Sketch already concedes this — sustained |

**Minimum surviving claim.** Strip every unmeasured/conjectural node and the incidence-scale predictions, and what remains that is *both* defensible and load-bearing is narrow: (i) q0057's "superadditive **vs** distinct routes" is a **false binary** (structure and sign are separable; distinct-route pairs can be antagonistic); (ii) identifying a compound-modifier **interaction** is confounding-stricter than either main effect (needs both modifiers' back-doors **plus** modifier–modifier common causes) and is **selection-dominated** (documented-infection detection, ~30-day survival, participation); (iii) the pregnancy×MCAS arm is **construct-invalid** as cited (atopy≠MCAS; Augustin is post-infection). All three survive. (i) is textbook interaction theory (VanderWeele 2014) *illustrated* by, not *derived* from, this graph.

---

## Overall Assessment

| Dimension | Verdict | Basis |
|---|---|---|
| Completeness | **warn** | Inter-modifier edge (M1) undrawn; confounder inventory admitted-incomplete; selection nodes inert (T4) |
| Identifiability | **fail (as a DAG)** — honestly disclosed | U + age + outcome-saturation ⇒ non-identified **and** unfalsifiable on admissible data (T1) |
| Evidence quality | **warn** | Majority of edges structural/hypothesized; convergence nodes conjectural; prose-only provenance, no two-axis labels (M3) |
| Structural validity | **fail on the prescribed sub-analyses** | Mediation/severity conditioning hits collider bias (T2) — an internal contradiction, the key finding |
| Temporal coherence | **pass** | Pre-infection modifier fixing + no bidirectional edge is coherent (P4 deferred to a longitudinal inquiry) |
| Tool-vs-prose coherence | **warn** | `treatment=frailty` structured field contradicts descriptive-estimand prose (M2) |
| Sensitivity | **warn** | Correctly demands interaction-specific sensitivity, but the demand is unmet and T2's induced bias isn't in the sensitivity frame |

**Bottom line.** As a *scoping* artifact the sketch is honest and its three surviving points are real. As a *causal model* it is not merely unidentified (its own framing) but, on any dataset it could actually be run against, **unfalsifiable** (T1), and its two headline sub-analyses are **structurally invalid as prescribed** (T2). Its central "two testable archetypes" selling point is **observationally empty at the incidence scale** (T3). These are not caveats the sketch already makes.

---

## Recommendations (actionable)

1. **Fix or delete the mediation sub-test (T2, highest priority).** Either remove the "condition on `immune-homeostatic-reserve` / `acute-infection-severity`" prescriptions, or replace them with an explicit exposure-induced-mediator-confounding treatment (g-formula / natural-effects with sensitivity), and add an assumption reconciling this with `compound-selection-collider`. Right now two caveats contradict.
2. **Rescope the archetype-distinguishability claim (T3).** State that the two structures are Markov-equivalent at the incidence scale on any mediator-unmeasured cohort; the distinguishing prediction is the **phenotype-component vector**, contingent on a phenotype-resolved outcome and doubly-exposed cells (D-004-blocked).
3. **Add T1 as an explicit "unfalsifiable-on-admissible-data" limit** distinct from non-identifiability, and note that installing `pgmpy` will produce *green checks over an empty graph* until the exporter's named-graph bug is fixed — a reader trap the current `formal-checks-are-vacuous` caveat does not close.
4. **Draw or explicitly forbid the inter-modifier edge (M1):** add a load-bearing "no immunosuppression→frailty causation" assumption with its biological counter-case, or redraw frailty as a partial mediator and switch the Pair-1 target to a mediation decomposition.
5. **Reconcile the structured `treatment` field with the prose estimand (M2)** so an automated consumer is not silently handed an interventionist reading.
6. **Add two-axis `edge_status`/`identification` labels (M3)** (default `unknown`/`none`) so "majority hypothesized" is machine-auditable, not prose-only.
7. **Toolchain (already filed):** the empty-`export-pgmpy` / wrong-named-graph bug (fb-2026-07-19-001) blocks the command's Step 2; add that `pgmpy` absence independently skips the identifiability checks.

**Disposition.** Retain t111 as a **scoping sketch** exactly as re-framed — but treat T2 (mediation/severity collider) as a correctness bug to fix before any of its sub-analyses are cited, and downgrade the "testable archetypes" language per T3. No re-open of the design-aspiration status (D-004 still binds); this critique sharpens the artifact, it does not unblock execution.
