<!--
core/decisions.md — load-bearing decisions and the reasoning behind them.
Loaded at session start via AGENTS.md.

Length cap: ~150 lines. When the file outgrows that, move older entries
to doc/decisions/ and keep only the still-load-bearing ones here.

This file is APPEND-ONLY for individual decisions. Do not rewrite a
decision when it is later superseded — add a new entry that references and
supersedes the old one, and update the "Status" line on the original.

Each entry follows the format below. Number entries sequentially.
-->

# Decisions

## D-001: Split post-acute infection syndromes out as their own process project

- **Date:** 2026-06-10
- **Status:** active
- **Decision:** Post-acute infection syndromes (long COVID, ME/CFS, PTLDS, post-dengue/Q-fever, post-SARS, PICS) are modeled as a dedicated `process` project under `~/d/health/processes/post-acute-infection`, separate from `health-immunity`.

**Why:**
A literature batch on post-acute infection syndromes revealed a large, coherent clinical-syndrome cluster (~60 papers) that is distinct from immunity's mechanism-level autoimmunity/tolerance focus. PAIS spans immune, autonomic, vascular, and metabolic systems and is organized around clinical syndromes and their post-infectious pathophysiology, not around immune mechanism per se. Keeping it in immunity would have ballooned that project's scope and mixed clinical-syndrome work with immune-mechanism work.

**Alternatives considered and rejected:**
- Fold PAIS into `health-immunity` as a subtopic — rejected because it conflates two distinct units of inquiry (immune mechanism vs. post-infectious clinical syndromes) and overloads immunity's scope.
- House PAIS under `health/conditions/` as disease labels — rejected because the unifying object is a *process* (failed recovery after acute infection), not a fixed set of disease labels; framing it as a process matches the `~/d/health/processes/` family and the homeostasis frame.
- Two projects (PAIS + autoimmunity) leaving immunity for pure homeostasis — rejected as premature scaffolding overhead; immunity already owns autoimmunity adequately.

**Implications:**
- Clinical post-infectious syndrome summaries, topics, hypotheses, and tasks belong in this repo.
- General immune-mechanism/autoimmunity/tolerance papers belong in `health-immunity`; bridging papers are summarized once and shared via `science commons promote`.
- Cross-project conclusions that change the general homeostasis frame escalate to `health-meta`; disease-label-vs-biology questions go to `pan-disease`.

**Revisit if:**
- The project fails to develop a distinct cross-syndrome inquiry and reduces to a per-disease literature dump better handled elsewhere.

## D-002: Adopt pacing as the default activity-management frame; treat incremental GET as contraindicated where PEM is present

- **Date:** 2026-06-20
- **Status:** active
- **Decision:** For PAIS phenotypes that exhibit post-exertional malaise (PEM), this project adopts **pacing / energy-management** (symptom-titrated activity within an energy envelope) as the default activity-management frame, and treats **graded exercise therapy (GET)** — specifically fixed-increment / deconditioning-model exercise prescriptions that escalate regardless of symptom response — as **contraindicated**. Any therapy, trial, or endpoint that relies on incremental GET in a PEM-positive population is flagged as methodologically contested when appraised in `topic:therapeutics-and-clinical-trials` and in any analysis plan with an exercise-based outcome.

**Why:**
PEM is a delayed, disproportionate worsening of symptoms after physical or cognitive exertion (`question:0011`), and provoked-exertion physiology gives it a mechanistic basis: muscle OXPHOS is reduced at baseline and falls *further* after exertion with a selective post-exertional drop in succinate-dehydrogenase activity (Appelman2024), invasive CPET shows impaired peripheral O₂ extraction (Joseph2023), and two-day CPET shows a loss of reproducibility on day 2 (Keller2014). Forcing fixed-increment exertion through that deficit is expected to harm rather than recondition. This aligns with the post-2021 NICE ME/CFS guideline (NG206), which withdrew GET as a recommended treatment and emphasizes staying within energy limits, and with the documented reanalysis challenges to the PACE trial's recovery/improvement claims (outcome-switching; overlapping trial-entry and "recovery" thresholds). The contraindication is **specific to PEM** — it is not a claim that exercise is harmful in post-infectious fatigue without PEM, where graded reconditioning may still be appropriate.

**Alternatives considered and rejected:**
- Treat GET and pacing as interchangeable exercise interventions — rejected; it conflates a PEM-contraindicated escalation protocol with symptom-bounded energy management, and would let GET-based trial results be read as if they tested pacing.
- Stay agnostic / take no project stance — rejected; therapeutic and endpoint appraisal needs one consistent rule for reading exercise-based trials, otherwise each appraisal silently re-litigates the GET question.
- Blanket "no exercise / no exertional testing" — rejected as overbroad; symptom-titrated activity, pacing, and *provoked-exertion diagnostics* (2-day CPET, iCPET) are endorsed precisely because the signal lives in the provoked state — they must simply be run under PEM-safety bounds (informed consent re: crash risk), not abandoned.

**Implications:**
- `topic:therapeutics-and-clinical-trials` and any analysis plan with an exercise endpoint flag incremental-GET designs in PEM-positive cohorts as contested, and prefer pacing as the behavioral comparator.
- Provoked-exertion testing (2-day CPET — Keller2014; invasive CPET — Joseph2023; post-exercise metabolomic recovery — Germain2022) remains endorsed as diagnostic/endpoint tooling, bounded by PEM-crash-risk consent.
- Distinguish, in every appraisal, PEM-positive from PEM-absent post-infectious fatigue before applying this stance.

**Revisit if:**
- A high-quality, PEM-stratified RCT establishes a safe incremental-exercise protocol for PEM-positive patients, or NICE / IOM / international consensus guidance materially changes the GET recommendation.

## D-003: Post-infectious trigger is the in-scope rule; PACVS and GWS/fibromyalgia are boundary-monitor / read-across, not primary scope

- **Date:** 2026-06-21
- **Status:** active
- **Decision:** The `hypothesis:0001` shared dysregulated attractor is held as **post-infection-specific for primary scope**. The headline inclusion rule is **trigger-type: a syndrome is in primary scope only if its trigger is an acute infection.** Two adjacent syndrome classes that fail this rule are ruled **boundary-monitor / read-across** — retained as mechanism evidence to stress-test cross-trigger claims, but **not** counted as in-scope PAIS cases: (a) **post-COVID-vaccination syndrome (PACVS)**, and (b) **non-infectious fatigue syndromes — Gulf War Syndrome (GWS) and fibromyalgia (FM)**. Recorded in `specs/scope-boundaries.md` (new "Boundary-Monitor / Read-Across" section). Trigger: a 2026-06 ingest of five papers (Halma2026, Bellavite2026, Lesgards2025 for PACVS; Davis2025 for GWS/FM) that each independently forced the question, three of them explicitly requesting this adjudication.

**Why:**
- **Trigger-type, not mechanism-overlap, is the discriminating criterion.** Three candidate criteria were tested against the boundary cases: *infection-trigger-required* (excludes PACVS, GWS, FM by one rule; matches the project name), *mechanism-overlap* (admits all three but is over-permissive — it would admit essentially any oxidative/mitochondrial/dysautonomic condition and collapse the boundary), and *PEM-presence* (admits GWS/FM, excludes PACVS). Infection-trigger is the only rule that cleanly bounds primary scope; mechanism-overlap is therefore explicitly rejected as an *admission* criterion (it remains the basis for read-across *retention*).
- **PACVS is excluded by the rule AND sits at the lowest evidence tier.** Its entire PACVS-specific empirical base reduces to one uncontrolled n≈17 ELISA case series reused across three author-overlapping (Bellavite/Di Fede/Halma), COI-disclosed or advocacy-funded narrative reviews; every cross-condition equivalence claim is self-flagged as speculation. The shared-spike-effector idea (same antigen via infection vs. vaccine) is a genuine same-antigen/different-route discriminator and worth monitoring, but is untested by controlled comparison. Admitting it as primary would let the volume of three non-independent papers be mistaken for corroboration.
- **GWS/FM are excluded by the rule but carry mainstream-tier evidence and are the best non-infectious stress-test of `hypothesis:0001`.** Davis2025 documents a shared metabolic/mitochondrial/oxidative lesion plus the PEM metabolic signature (two-CPET) across ME/CFS, GWS, and FM despite non-infectious triggers. GWS — a toxic-chemical trigger reaching the same downstream signature — is the single best external probe of the attractor's trigger-agnostic claim, so it earns read-across retention rather than hard exclusion (which would discard that probe). PEM-presence is the secondary criterion that discriminates GWS/FM (retain) from PACVS (hold at arm's length) within the read-across set.

**Alternatives considered and rejected:**
- **Admit either class as in-scope** (via mechanism-overlap, or mechanism+PEM for GWS/FM) — rejected: redefines the project away from "post-acute *infection*," and for PACVS would import the weakest, most-contested evidence tier as primary subject matter.
- **Hard-exclude all three** (not even monitored) — rejected: discards the PACVS same-antigen/different-route discriminator and the GWS non-infectious stress-test, both of which bear directly on whether `hypothesis:0001`'s trigger-agnostic claim holds. Read-across retains their probative value at the correct (non-primary) weight.

**Implications:**
- Scope-boundaries carries the read-across set; PACVS/GWS/FM papers are summarized as read-across mechanism evidence, never tallied as PAIS cases or as independent cross-trigger support for `hypothesis:0001`.
- Any cross-trigger convergence claim that leans on GWS/FM must state it is a *non-infectious* read-across, and flag the unresolved metabolite-direction conflicts (sphingomyelin/tryptophan/taurine sign flips across conditions).
- PACVS shared-spike claims are represented as hypothesis-to-test with their evidence tier (single uncontrolled case series) stated inline.

**Revisit if:**
- A controlled **PACVS-vs-PASC** biomarker comparison appears (would reopen PACVS for possible admission), or a powered design resolves the GWS/FM metabolite-direction conflicts and establishes a shared-attractor signature on causal (not cross-sectional) footing.

## D-004: Shelve the autoimmune × sex × PASC vehicle-based estimand as infeasible-under-transparency-standards

- **Date:** 2026-07-01
- **Status:** active
- **Supersedes:** the operative "N3C primary" verdict in `interpretation:0031` (marked SUPERSEDED).
- **Decision:** The `task:t078`/`task:t079` autoimmune-diathesis × sex × PASC effect-modifier estimand is **shelved, not executed.** It requires population-scale, individual-level patient EHR (rare autoimmune-stratum × sex power — the binding BC-4 gate), which is a **categorically access-gated, non-downloadable data class.** N3C (the locked primary vehicle) was found gated **and** non-downloadable *even at the synthetic tier* (enclave-only compute); OpenSAFELY carries the same real-data gating (insider-only execution, only disclosure-controlled aggregates leave) despite a more transparent code model. No admissible vehicle can produce this estimate as **third-party-reproducible** knowledge, so the line is shelved rather than run. The **design work is banked** — the two-estimand contrast (total vs controlled-direct + mediation), DAGs, adjustment sets, negative-control + bracketing design, and especially the **`hypothesis:0008` measurement/ascertainment synthesis** remain valid and reusable.

**Why:**
Durable scientific knowledge in this ecosystem must be independently re-runnable and verifiable by an arbitrary third party (see [[avoid-gated-nondownloadable-datasets]] in agent memory). Gated + non-downloadable data breaks this even in the best case: an OpenSAFELY-style result is reproducible only by credentialed insiders behind a manual output-review gate, producing a "gray-zone" knowledge patch — *someone with access ran it and got a number; everyone else can only trust them.* The problem is the **data class**, not the vehicle choice: population-scale patient EHR is inherently gated, so no vehicle swap rescues the estimand. The multi-BC feasibility investment was not wasted — it produced the transparent design residue and the first two entries for a forthcoming reproducibility inventory.

**Alternatives considered and rejected:**
- **Promote OpenSAFELY to primary** — rejected: same real-data gating, still insider-only/trust-based, and it reintroduces the coded-long-COVID differential under-recording problem (`interpretation:0033`/BC-5) that had made it replication-not-primary.
- **Accept gated-execution vehicles** ("open code + gated data + aggregate outputs" is good enough) — rejected: it violates the third-party-reproducibility bar and normalises gray-zone patches into the knowledge base.

**Implications:**
- `task:t079` → deferred (shelved); `plan:0005` stays `not-ready` (it never became viable) with a SHELVED banner; `plan:0006` → archived; `interpretation:0031` → superseded; the `doc:` feasibility memo carries a SHELVED banner. `task:t080`/`t081`/`t082` → deferred.
- N3C and OpenSAFELY are to be recorded as `insider-only` in the reproducibility inventory being scoped in `~/d/science` (the change that would have flagged N3C at *plan* time).
- The `hypothesis:0008` synthesis is the durable residue and remains live for other lines.

**Revisit if:**
- A population-scale EHR vehicle offers a genuinely **third-party-reproducible** access path (downloadable de-identified individual-level data, or a truly open/downloadable synthetic tier), **or** the estimand is reformulated so it no longer requires population-scale gated EHR.
