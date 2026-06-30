---
id: interpretation:0002-t013-cross-trigger-sex-effect-sizes
type: interpretation
title: 'Cross-trigger sex-stratified effect sizes: female excess concentrates in post-acute
  persistence; domain dissociation unresolved'
status: active
source_refs: &id001
- dataset:sylvester-2022-longcovid-sex
- dataset:dengue-postinfective-fatigue-meta
- dataset:colombo-dengue-study
- dataset:dutch-qfever-qfs-cohort
related:
- question:0007-mechanism-of-female-predominance-in-pais
- task:t013
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
created: '2026-06-21'
updated: '2026-06-22'
input: *id001
prior_interpretations: []
relations: []
---
<!--
Conclusion chains:
- Use `relations:` with `predicate: "sci:amends"` when this interpretation revises,
  narrows, qualifies, or extends an older conclusion.
- Use `relations:` with `predicate: "sci:supersedes"` when this interpretation
  replaces an older conclusion as the current canonical reading.
- Keep `prior_interpretations` only as a narrative breadcrumb. The graph relation
  is the machine-readable source of truth.
-->

# Interpretation: Cross-trigger sex-stratified effect sizes: female excess concentrates in post-acute persistence; domain dissociation unresolved

> **Mode: conceptual.** No new computation. This assembles already-published, sex-stratified
> effect sizes from the `tier: use-now` catalog entities (`task:t013` step 2) into one
> cross-trigger comparison table and reads it against `question:0007`. All findings are
> `literature_evidence`; none are re-analyzable microdata.

## Verdict

**Verdict:** [~] Mixed — the **persistence-concentration** claim (female excess is larger in post-acute persistence than in acute severity) holds across every trigger with usable sex-stratified data; the **domain-dissociation** claim (somatic-fatigue vs neuropsychiatric) does **not** resolve — the two strongest anchors point in *opposite* directions and the dengue depression arm is too underpowered to adjudicate.

## Findings Summary

### The cross-trigger table (use-now published effect sizes)

Female-vs-male effect sizes. "Acute sex bias" is the direction of the acute-phase
risk/severity gradient; "persistence" and "neuropsychiatric" are post-acute female ORs.

| Trigger | Acute-phase sex bias | Post-acute persistence / fatigue (female) | Neuropsychiatric / mood (female) | Source(s) |
|---|---|---|---|---|
| **COVID** | **male**-biased mortality/severity | Overall long COVID **OR 1.22** (1.13–1.32); fatigue domain-specific | **mood OR 1.58** (1.37–1.82); neuro 1.30; ENT 2.28; GI 1.60. Male-skewed: endocrine 0.75, renal 0.74 | Sylvester2022 meta (`dataset:sylvester-2022-longcovid-sex`) |
| **COVID** | (as above) | LC risk higher in females; clearest at **age 40–54**, smaller at ≥55 | not separately stratified | Shah2025 (RECOVER; via `question:0007`) |
| **Dengue** | severe-dengue/DHF risk **not** female-predominant | fatigue **OR 1.65** (1.27–2.14; Hertanti2025, 40 studies, n≈38,406) and **OR 1.69** (1.33–2.14; Conde2026, 9 studies, n≈1,470) | depression **OR 1.05** (0.16–6.79); **2 studies / 169 pts, "very low certainty"** | `dataset:dengue-postinfective-fatigue-meta` (Hertanti2025, Conde2026) |
| **Dengue** | acute dengue (sex-neutral severity) | persistent symptoms **aOR ~1.99**; **~2.24 beyond 90 d**; fatigue **RR ~2.45** | weak arm — baseline depression/anxiety were **exclusion criteria** | Colombo / Seneviratne2021 (`dataset:colombo-dengue-study`) |
| **Q-fever** | **male**-skewed acute exposure (occupational/farming) | QFS persistence **not** male-skewed (sex recorded; no published female OR) | partial; CIS-based | Dutch QFS cohort (`dataset:dutch-qfever-qfs-cohort`; Raijmakers2019) — qualitative natural experiment |

### What the table shows

1. **Persistence-concentration is robust** (`suggestive`, `literature_evidence`, convergent across 3 triggers).
   In COVID and Q-fever the **acute** phase is *male*-biased (COVID mortality; Q-fever occupational
   exposure) while the **post-acute** phase is female-biased; in dengue acute severity is sex-neutral
   yet post-acute fatigue carries female OR ≈1.65–2.0. The female excess therefore *emerges in*
   (or is *amplified by*) the persistence phase rather than being inherited from an acute female-skew.

2. **Domain dissociation does not resolve** (`ambiguous`, `literature_evidence`). The two `use-now`
   anchors disagree on *which* domain carries the excess:
   - **COVID (Sylvester2022):** the *mood* domain (OR 1.58) is **more** female-biased than overall (1.22)
     — i.e. neuropsychiatric **> ** the average, the opposite of a "somatic-fatigue-specific" story.
   - **Dengue (meta):** *fatigue* is clearly female-biased (1.65–1.69) while *depression* is null
     (1.05) — but that null rests on **2 studies / 169 patients** and is "very low certainty," and the
     Colombo cohort **excluded** baseline mood disorders, structurally suppressing its neuropsychiatric arm.

   So the apparent fatigue-vs-depression dissociation that `question:0007` flags as *provisional* is, on
   the assembled cross-trigger evidence, **not merely underpowered but directionally inconsistent**:
   COVID points mood-up, dengue points fatigue-up-with-depression-unmeasurable. No clean universal
   domain boundary is supported.

## Evidence Quality

- **All literature-derived, mostly unadjusted/partly-adjusted ORs** pooled across heterogeneous case
  definitions — exactly the definitional-heterogeneity caveat AGENTS.md flags. No microdata re-analysis.
- **Non-independence (critical):** Hertanti2025 and Conde2026 **share primary studies** (per Conde2026),
  so their concordant ~1.65/~1.69 is **one evidence line, not two**. They must occupy a single
  `independence_group` (post-dengue-fatigue-meta), not be counted as independent replication.
- **Power asymmetry across domains:** the fatigue arms are well-powered (n in the tens of thousands for
  dengue; large LC meta for COVID); the dengue depression arm is not (n=169). Any "fatigue > depression"
  read is a **power contrast as much as a biology contrast**.
- **Confirmatory vs exploratory:** exploratory synthesis. This is a *navigation* result for `t013`, not a
  pre-registered test.
- **Ascertainment confound** (unquantified): care-seeking/reporting differences could inflate apparent
  female persistence excess uniformly (Zhang2022, per `question:0007`); the table cannot separate this
  from biology.

## Data Quality Checks

No microdata involved, so the standard control-uniqueness / dimensionality checks do not apply. One
structural concern surfaced and is recorded as `methodological`: **the dengue fatigue-vs-depression
contrast conflates effect size with statistical power** (well-powered fatigue arm vs n=169 depression
arm + a cohort that excluded mood disorders by design) [@Conde2026]. Treat the dengue "dissociation" as an artifact
candidate until a powered, mood-inclusive dengue cohort exists.

## Question-Level Implications

**`question:0007` (mechanism of female predominance) — partially addressed, sharpened, no belief flip.**

- *Supports* the question's framing that female excess is a post-acute phenomenon: the persistence-
  concentration pattern is now explicit and cross-trigger, anchored by the two triggers (COVID, Q-fever)
  whose acute phase is *male*-biased. This strengthens the "emerges in persistence" reading over an
  "inherited acute female-skew" reading.
- *Disputes / tempers* the somatic-vs-depression dissociation sub-claim. `question:0007` already called
  this "provisional … may be a power artifact"; this synthesis upgrades that caution: across triggers the
  dissociation is **directionally inconsistent**, not just weak. The question's own text should not be
  read as leaning toward a fatigue-specific subtype.
- Leaves the **mechanism** (estrogen amplification vs immune-setpoint vs X-dosage vs ascertainment)
  entirely open — none of these effect sizes discriminate among them.

**`hypothesis:0005` / `question:0013` (reproductive-stage immune-homeostatic margin) — weak, indirect support.**
The Shah2025 age-banding (excess clearest at 40–54, the perimenopausal window) is consistent with a
reproductive-stage modifier, but age and menopausal transition are confounded and this single cohort
cannot isolate them. No update beyond "consistent-with."

## New Questions Raised

- **Is the COVID-vs-dengue domain inversion real or a measurement artifact?** (priority P2, empirical)
  Most efficient resolution: a dengue or Q-fever cohort that measures depression with a powered,
  *non-excluded* sample — the dengue depression arm is the single weakest cell in the table.
- **Does the persistence-concentration pattern survive ascertainment correction?** (P2, methodological)
  Needs a design with symmetric male/female care-seeking (e.g. a systematically-followed cohort like
  Dubbo) rather than clinic-referred series.

## Limitations & Residual Uncertainty

- Pooled ORs only; no individual-level adjustment for age, severity, time-since-infection, or prior
  immunity — the covariate sensitivities AGENTS.md requires are unaddressed here.
- The strongest *conceptual* test of persistence-concentration (acute male-skew → post-acute female-skew
  within one design) is the Dubbo/Dutch-QFS natural experiment, whose **microdata are private** — so the
  cross-trigger claim rests on between-study comparison, not a within-cohort transition.
- Q-fever and Lyme contribute *direction* but no usable female OR; the quantitative table is effectively
  COVID + dengue.

## Updated Priorities

- **Record the persistence-concentration line** against `question:0007` as `suggestive`,
  `independence_group: cross-trigger-persistence` (COVID + dengue + Q-fever are methodologically distinct
  triggers → genuinely separate lines), and the **dengue fatigue meta as a single shared-source line**
  (Hertanti2025 ⊕ Conde2026, `independence_group: post-dengue-fatigue-meta`) to avoid double-counting.
  **DONE (2026-06-22, t013 step 3):** minted as `proposition:0008-female-excess-concentrates-in-post-acute-persistence`
  + `evidence-line:0016` (COVID, `sylvester2022-lc-sex`, moderate), `evidence-line:0017` (dengue meta,
  `post-dengue-fatigue-meta`, moderate, Colombo folded as same-trigger corroboration), `evidence-line:0018`
  (Q-fever, `dutch-qfs-natural-experiment`, weak/qualitative). `belief.fragile-single-line` does not fire
  on 0008 (3 independent lines); validate PASSED.
- **Do not** promote any "somatic > neuropsychiatric" proposition — the cross-trigger evidence is
  directionally inconsistent.
- t013 step 3 candidate: pursue the **Dubbo within-cohort transition** (acute male-skew → post-acute
  female-skew) as the decisive design, contingent on data access (currently private → deferred).
- Lower-friction alternative: extract Shah2025's age-banded ORs in full to feed `question:0013`.
