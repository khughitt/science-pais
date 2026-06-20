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
