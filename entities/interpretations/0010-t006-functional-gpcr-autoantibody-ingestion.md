---
id: interpretation:0010-t006-functional-gpcr-autoantibody-ingestion
type: interpretation
title: 't006 functional GPCR-autoantibody literature: criterion-#2 correlational arm
  partially and contestedly met for autonomic function; antibody-to-lesion bridge
  untested'
status: active
source_refs: &id001 []
related:
- proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
- proposition:0016-pais-sfn-autoimmune-causation
- question:0009-functional-autoantibodies-drive-dysautonomia
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls
created: '2026-06-24'
updated: '2026-06-24'
input: *id001
prior_interpretations:
- interpretation:0009-t049-sfn-cross-syndrome-ingestion
relations: []
---

# Interpretation: t006 functional GPCR-autoantibody literature — criterion-#2 correlational arm partially and contestedly met for autonomic function; antibody→lesion bridge untested

## Verdict

**Verdict:** [~] Mixed/contested — one functional assay shows GPCR-autoantibody *activity* tracks
orthostatic-symptom severity (Kharraziha2020, α1-AR, β=0.77, p=0.009), but the binding-ELISA basis is
non-specific (Hall2022, 98% POTS vs 100% controls) [@Kharraziha2020; @Hall2022], the canonical β-adrenergic/muscarinic targets are
only weakly/contestedly supported, and **no study links anti-GPCR antibodies to the small-fiber lesion**.
h0007 promotion criterion #2's *correlational* arm is **partially discharged for autonomic function
only**; the antibody→IENFD/SGNFD-*lesion* bridge it ultimately needs remains entirely untested.

## Findings Summary

Four papers ingested (t006), coded as `evidence-line:0049`–`0052` against
`proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity`:

| Paper | Assay | Finding | Line | Stance / strength |
|---|---|---|---|---|
| Kharraziha2020 (POTS) | **functional** FRET activity | α1-AR activity ↔ OHQ severity, β=0.77 p=0.009, survives ΔHR/ΔSBP | 0049 | supports / **moderate** |
| Loebel2016 (ME/CFS) | binding ELISA | β2/M3/M4 seroprevalence ~29.5% (canonical targets) | 0050 | supports / weak |
| Schmitz2026 (long COVID) | binding-inferred | anti-GPCR ↔ HRV/BP; **but in-vitro hiPSC-CM test null** | 0052 | supports / weak |
| Hall2022 (POTS) | binding ELISA | 98% POTS / 100% HC seropositive; no group difference | 0051 | **disputes** / moderate (mechanism) |

The decisive structural feature: **the Kharraziha functional line and the Hall binding-null line do not cancel** — they
measure different things. Hall2022 removes binding-ELISA seroprevalence (the Loebel line, and the basis of much of
the field) from the ledger; it does **not** touch Kharraziha's functional-activity correlation. So the
surviving support is narrow: *one* functional assay, on the *off-target* α1-AR (not β/M), in *POTS not
PAIS*.

## Evidence Quality

- **Independence:** all four are independent cohorts/platforms (distinct `independence_group`s) — no
  shared-source inflation. The split is real, not an artifact of one dataset.
- **Assay axis is load-bearing:** the field divides on binding-ELISA (cheap, non-specific per Hall2022)
  vs functional/receptor-activation bioassays (Kharraziha FRET; the agonist-antibody bioassay lineage).
  Support concentrates entirely in the functional camp; the disconfirming evidence is entirely about the
  binding camp. This is the central methodological fault line of `question:0009`.
- **All observational/correlational** — no passive-transfer or depletion in this set (the causal designs
  live with deSa2026 `evidence-line:0045` on `proposition:0016`, and Stein2025 immunoadsorption on
  `proposition:0019`). Schmitz2026 *attempted* a functional in-vitro test and got a **null**.
- **`[UNVERIFIED]` load:** Schmitz2026 (cohort n, case definition, time-since-infection, per-receptor
  stats, assay confirmation all unverified — full text inaccessible) and Loebel2016 (case definition,
  control seropositivity) carry real verification gaps — both coded **weak** partly for this reason.

## Data Quality Checks

No data-quality concerns in the project graph. One methodological finding worth flagging as itself a
result: **Hall2022 is a data-quality critique of the entire binding-ELISA literature** — manufacturer
thresholds make ~everyone seropositive, so binding-ELISA "seroprevalence" papers (including Loebel2016,
and CellTrend-platform long-COVID papers) should be read as existence-of-binding only, never as
disease-specific autoimmunity.

## Proposition-Level Updates

- **`proposition:0018` (anti-GPCR pathogenicity)** — now **contested**, and the validator flags it
  `belief.fragile-single-line` (the verdict flips on dropping any single line), which is the honest state
  of a thin 4-line base. Net: the *autonomic-function* half of 0018 has weak-to-moderate functional
  support (0049) against a moderate binding-specificity dispute (0051); the **small-fiber-lesion half is
  unsupported by any line** — every paper uses autonomic/HRV/symptom endpoints, none an IENFD/SGNFD or
  skin-biopsy correlate. 0018 remains the weakest leg of h0007, exactly as `interpretation:0009`
  predicted.
- **`proposition:0016` (bare immune-mediation)** — essentially unchanged. These lines target the
  anti-GPCR *route* (0018), not the bare claim; 0016 still rests on deSa2026 (causal, non-GPCR) vs
  Walitt2024 (null in ME/CFS). t006 does not move it.
- **`proposition:0014`/`0015` (the lesion and its pattern)** — untouched. The antibody→lesion bridge is
  the gap, not a new finding.

## Hypothesis-Level Implications

For **`hypothesis:0007`**, this **does not promote** and does not warrant leaving `candidate`. Mapping to
the promotion criteria (now operationalized in `pre-registration:0003`):

- **Criterion #2 (the q0009 serology↔lesion link)** has two readings. Its *correlational-with-autonomic-
  severity* reading is **partially and contestedly met** (Kharraziha α1-AR↔OHQ). Its stricter
  *titer↔IENFD/autonomic-small-fiber-severity* reading — the one h0007 actually states — is **not met**:
  no ingested study correlates any anti-GPCR antibody with the small-fiber lesion. So criterion #2 is
  **not cleanly discharged**.
- **Criterion #1** remains the data-gated `pre-registration:0003` (no admissible vehicle yet).

Therefore h0007 stays **candidate** with *both* criteria still open — but the picture is now sharper:
the autoimmune leg's failure mode is specifically the **antibody→lesion** step, not the existence of
autoantibodies or their loose association with autonomic symptoms.

## Evidence vs. Open Questions

- **`question:0009` (functional GPCR autoantibodies drive dysautonomia)** — materially advanced from
  "asserted, primary literature not ingested" to **ingested and adjudicated as contested**. The causal
  chain (functional antibody → receptor dysregulation → POTS) has one supportive functional-assay
  correlation and a strong binding-assay specificity rebuttal; it is *the most testable bridge but still
  unproven*, now with the bibliographic backing the question previously lacked (was: Stahlberg/Rojas/
  Sharma general autoimmunity; now: Kharraziha/Loebel/Hall/Schmitz primary functional-autoantibody work).
- **`question:0004`** — unchanged by t006 (that is criterion #1 / the biopsy study).

## New Questions Raised

1. **The antibody→lesion bridge (highest value).** No study correlates functional anti-GPCR autoantibody
   activity with IENFD/SGNFD in the *same* PAIS patients. This is the precise missing measurement that
   would connect `question:0009` to `proposition:0014`/`0015` — and it is naturally co-measurable in the
   `pre-registration:0003` G5 serology arm. Candidate new question or a tightening of q0009's "Required
   data."
2. **Functional vs binding assay as an admissibility gate.** Given Hall2022, any future autoantibody
   evidence should be gated on a *functional/receptor-activation* assay; binding-ELISA seroprevalence
   should not count toward criterion #2. Worth encoding as a methodological note on q0009.

## Limitations & Residual Uncertainty

- Only 4 papers (a focused, balanced set, not exhaustive); the agonist-antibody bioassay lineage
  (Wallukat) and the IVIG/plasmapheresis pilots are represented only indirectly (Stein2025 already coded;
  others not ingested). The verdict is robust on the *fault line* (functional vs binding; no lesion link)
  but not a systematic review.
- Schmitz2026 and Loebel2016 carry `[UNVERIFIED]` cohort/statistic fields (full text inaccessible);
  their weak weighting already reflects this.
- The strongest support (Kharraziha) is **α1-AR in POTS** — off the canonical β/M targets and off the
  PAIS cohort — so even the supportive line is an analogical reach for PAIS specifically.

## Updated Priorities

1. **Fold the antibody→lesion correlation into `pre-registration:0003`'s serology arm (G5)** as the
   concrete way to discharge criterion #2's strict reading — measure functional anti-GPCR activity and
   IENFD/SGNFD in the same subjects. (No code change needed now; the pre-reg already scopes serology as
   conditional/exploratory — this interpretation supplies the *why*.)
2. **Gate criterion #2 on functional assays**, not binding ELISA (Hall2022 lesson) — note on q0009.
3. **Keep `proposition:0018` as the explicit weakest leg**; its `belief.fragile-single-line` flag is
   acceptable and accurate. Do not over-read the Kharraziha correlation.
4. t006 is **complete** (literature ingested and adjudicated); the live gap it exposes is now owned by
   the q0004 biopsy study (t050 / pre-reg:0003), not by further autoantibody lit-search.
