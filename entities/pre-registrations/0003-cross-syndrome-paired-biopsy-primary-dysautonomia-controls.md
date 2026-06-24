---
id: "pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls"
type: "pre-registration"
title: "Pre-registration: standardized cross-syndrome paired-site (proximal+distal) skin-biopsy + autonomic protocol with a primary-dysautonomia control arm — the q0004 discriminating test of h0007 (NLD-autoimmune-SFN substrate)"
status: "committed"
committed: "2026-06-24"
mode: data-gated
spec: ""
related:
  - hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
  - proposition:0014-pais-small-fiber-structural-lesion-ienfd
  - proposition:0015-pais-sfn-non-length-dependent-pattern
  - proposition:0016-pais-sfn-autoimmune-causation
  - proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
  - question:0004-convergent-small-fiber-neuropathy-substrate
  - question:0009-functional-autoantibodies-drive-dysautonomia
  - topic:measurement-ascertainment-artifacts-in-pais
  - topic:post-infectious-dysautonomia-and-autoimmunity
  - task:t006
  - task:t049
  - task:t050
  - paper:Oaklander2022
  - paper:Joseph2021
  - paper:Limongelli2026
  - paper:Adler2024
  - paper:deSa2026
  - paper:Walitt2024
commits_to:
  - hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
  - proposition:0014-pais-small-fiber-structural-lesion-ienfd
  - proposition:0015-pais-sfn-non-length-dependent-pattern
  - question:0004-convergent-small-fiber-neuropathy-substrate
created: "2026-06-24"
updated: "2026-06-24"
---

# Pre-registration: standardized cross-syndrome paired-site skin-biopsy + autonomic protocol with a primary-dysautonomia control arm (q0004 discriminating test of h0007)

> **Mode: data-gated.** No admissible vehicle exists in the corpus. This pre-registration commits the
> *interpretation rule* now and defers execution until a study/dataset clears the Vehicle-Admissibility
> Gate (G1–G5 below). Until then the standing verdict is **`[?]` inconclusive-for-coverage** — it
> produces **no `bears_on` belief update** on any commitment target. This is *not* a null result (a null
> is evidence); it is the absence of qualifying evidence. The deferred analysis is tracked by an
> `active` task (t050) whose blocker is the admissibility gate, so it activates when a qualifying vehicle
> arrives. This pre-reg is the operationalization of **h0007 promotion criterion #1**.

## Hypotheses Under Test

This pre-registration is the single most discriminating test named in
`hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` ("Evidence Needed To Shift Belief")
and operationalizes its **promotion criterion #1**. It commits how the first admissible cross-syndrome
standardized paired-site biopsy + autonomic study (with primary-dysautonomia controls) will update the
following epistemic targets. The class of each is marked because epistemic targets and the operational
protocol are interpreted differently (§ Decision Criteria).

| Target | Role in h0007 | Test leg | Confirmatory / conditional |
|---|---|---|---|
| `hypothesis:0007` | the candidate frame; promotion gate | overall pattern across P1+P2 | **confirmatory** (promotion criterion #1) |
| `proposition:0014` (P1, structural lesion) | existence claim P2/P3 depend on | site-specific lesion-positive rate vs healthy controls | **confirmatory** |
| `proposition:0015` (P2, non-length-dependent pattern) | **the discriminating leg** | NLD-fraction PAIS vs primary-dysautonomia | **confirmatory — headline** |
| `proposition:0016` (P3, immune-mediation) | weakest causal leg | serology↔lesion co-localization | conditional (only if vehicle carries serology) |
| `proposition:0018` (anti-GPCR pathogenicity) | thinnest auxiliary leg | titer↔autonomic-severity correlation | exploratory (serology-arm-dependent) |
| `question:0004` (convergent NLD substrate) | the primary open question | whole design | **confirmatory** |
| `question:0009` (functional GPCR autoantibodies) | the serology thread | serology arm | conditional/exploratory |

**Commitment scope (`commits_to`).** `bears_on` edges are derived only to the four entities in
`commits_to:` — `hypothesis:0007`, `proposition:0014`, `proposition:0015`, `question:0004` — because
these are the targets the **admissibility floor (G1–G4) guarantees** the vehicle can move. P3
(`0016`), the anti-GPCR route (`0018`), and `question:0009` are addressed **only if** the admissible
vehicle also carries functional-autoantibody serology (an *optional* arm, G5, not part of the floor);
they are therefore handled as conditional/exploratory legs here and remain primarily owned by `task:t006`
and a future serology-specific pre-registration (h0007 promotion criterion #2). Keeping them out of
`commits_to:` prevents over-deriving a belief edge that the floor does not underwrite — they still appear
in `related:` for discoverability.

## Expected Outcomes

Grounded in the t049 evidence base (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`):

1. **P1 — lesion present (expected: yes, moderate confidence).** PAIS autonomic-symptom patients show a
   higher site-specific lesion-positive rate than healthy controls. Priors: long COVID 63% distal /
   ~50% proximal abnormal (`paper:Oaklander2022`), ME/CFS 31% lower-leg SFN (`paper:Joseph2021`),
   post-vaccine PASC ~90% reduced density (`paper:Limongelli2026`), PTLDS 10/10 (`paper:Adler2024`).
   **Tempered by one rigorous null:** the NIH PI-ME/CFS deep-phenotyping cohort found *no*
   small-fiber-density difference (`paper:Walitt2024`, `evidence-line:0040`), so we expect the lesion in
   *a substantial subset*, not universally, and expect prevalence to be protocol- and case-definition-
   sensitive.

2. **P2 — non-length-dependent pattern discriminates (expected: yes, but this is the thinnest leg).**
   Among lesion-positive subjects, the **PAIS NLD fraction exceeds the primary-dysautonomia NLD
   fraction**. This is the *headline discriminating prediction*. Prior: the only clean paired-site NLD
   fraction in the corpus is `paper:Limongelli2026` (33% NLD on paired calf+thigh, **but post-vaccine**,
   `evidence-line:0041`); `paper:Oaklander2022` adds weak distal≈proximal near-parity without per-patient
   NLD classification (`evidence-line:0042`). P2 is currently "asserted more than measured" — this study
   is what would move it from asserted to measured.

3. **P3 / serology (conditional, low confidence).** If serology is present (G5), functional anti-GPCR
   titer correlates with autonomic small-fiber severity within PAIS. Prior is weak and **mixed**:
   `paper:deSa2026` shows long-COVID IgG passive transfer reduces nerve fibers (causal, but its
   autoantigens were **non-GPCR** MED20/USP5 and it spared the autonomic axis); `paper:Stein2025` shows
   β2-AR-selected immunoadsorption helps autonomic symptoms but β2-AR reduction did *not* predict
   response. We do **not** expect a clean anti-GPCR titer↔lesion correlation; this leg is exploratory.

## Decision Criteria

The protocol portion (the biopsy/autonomic/serology procedure) is an **operational** commitment: at
interpretation time `science:interpret-results` confirms the admissible vehicle ran the committed
protocol (or that any deviation has an `amendments:` record). It is not a `bears_on` sink. The belief
updates below are **epistemic**: a null is *evidence weighted by commitment*, not a verdict that kills
h0007.

All confirmatory legs are evaluated **only among subjects who clear the confounder-exclusion screen**
(no diabetes, B12/folate deficiency, significant alcohol, chemotherapy, hereditary neuropathy, or other
length-dependent-SFN cause) — otherwise length-dependent confounders contaminate the NLD-vs-LD contrast,
which is the whole point.

**Three-band significance convention (applies to both confirmatory legs).** Because confirmatory tests
are held at the Bonferroni-corrected α = 0.025 while the weakening criteria reference the nominal
α = 0.05, the intermediate interval is defined explicitly to remove a degree of freedom at
interpretation time:
- **p < 0.025** → **confirmatory support** (corrected threshold; counts toward criterion #1).
- **0.025 ≤ p < 0.05** → **nominal/supportive but NOT confirmatory** — a weak positive that neither
  discharges the criterion nor weakens the proposition; it is recorded as suggestive evidence and, for a
  result of real interest, motivates a replication or a larger vehicle rather than a verdict.
- **p ≥ 0.05** → **weakening** (subject to the G4 well-powered-null floor, below — a high-p result at
  n = 40/side is *inconclusive*, not weakening).

### Confirmatory leg 1 — P1 (`proposition:0014`): is there a lesion?

- **Metric.** Per-subject *lesion-positive* = IENFD **or** SGNFD below the site-specific normative cutoff
  (≤5th percentile / z ≤ −1.645 against site-, age-, sex-, race-adjusted norms) at **any** sampled site.
- **Supports P1:** lesion-positive rate(PAIS-autonomic) > rate(healthy controls), two-proportion test
  **p < 0.025** (Bonferroni across the 2 confirmatory tests), and the effect survives confounder
  exclusion.
- **Weakens P1:** rate(PAIS) not distinguishable from healthy controls (p ≥ 0.05) **or** the excess is
  abolished after confounder exclusion → shifts belief toward the deflationary/functional account
  (`question:0017`). Magnitude of the shift scales with the vehicle's power (G4).
- **Shifts belief strongly away:** a well-powered (per-arm n well above floor) null with tight CIs
  excluding a clinically meaningful difference → P1 fails and the structural-lesion frame collapses into
  a functional account, materially weakening h0007.

### Confirmatory leg 2 — P2 (`proposition:0015`): the headline discriminator

- **NLD classification (per lesion-positive subject).** Convert each site's IENFD/SGNFD to a
  **site-specific z-score**. Classify **non-length-dependent** iff *proximal z-deficit ≥ distal z-deficit*
  **or** *proximal-abnormal-but-distal-normal*. **A raw proximal:distal density ratio is explicitly not
  used** — absolute IENFD differs by site and a raw ratio conflates normal anatomy with pathology
  (locked from `proposition:0015` Measurement Model). Classification is computed only among lesion-
  positive subjects (P2 is conditional on P1).
- **Headline metric.** Δ = NLD-fraction(pooled PAIS-autonomic, lesion-positive) −
  NLD-fraction(primary-dysautonomia, lesion-positive).
- **Supports P2 (the discriminating leg of promotion criterion #1, which also requires P1):** Δ ≥ **20
  percentage points** with two-proportion test **p < 0.025**. This is the discriminating result — PAIS SFN is preferentially
  non-length-dependent *relative to* primary dysautonomia, implicating a ganglionopathy / immune-mediated
  mechanism rather than a length-dependent metabolic gradient.
- **Weakens P2 (only at the well-powered-null floor):** a **null at ≥80 lesion-positive/side** (or a CI
  excluding Δ ≥ 20 pts) — especially where the PAIS lesion is predominantly **length-dependent and
  indistinguishable in pattern** from the primary-dysautonomia / metabolic gradient → P2 fails, the
  "distinct ganglionopathy" reading is lost, and h0007 loses its discriminating leg (downgraded, not
  promoted). A study **between the two G4 floors** (≥40 but <80/side) that fails to reach significance
  **does not weaken P2** — it is *inconclusive* (underpowered to disconfirm), and routes to replication /
  a larger vehicle rather than a verdict.
- **Reverse/diagnostic surprise:** if primary-dysautonomia controls *also* show a high NLD fraction
  (Δ ≈ 0 because **both** arms are NLD), the substrate is real but **not specific to PAIS** — q0004's
  "distinguishes from primary dysautonomia" clause fails even though P2's pattern claim holds. This is a
  distinct outcome from "no NLD anywhere" and is recorded separately (see Null-Result Plan).

### Promotion rule for `hypothesis:0007`

h0007's promotion (candidate → active) requires **both** of its stated criteria: #1 (the standardized
paired-site biopsy + autonomic study with primary-dysautonomia controls) **and** #2 (an independent line
linking the functional-autoantibody thread to the structural lesion). This pre-reg discharges them as
follows:

- **This study discharges criterion #1** iff **both** confirmatory legs support (P1 supported **and** P2
  headline Δ ≥ 20 pts at p < 0.025) in an admissible vehicle. P1-supported but P2-null does **not**
  discharge it (the lesion exists but is not discriminating — h0007's distinctive claim is the *pattern*,
  not mere SFN presence, which `hypothesis:0001` already covers).
- **Promotion still requires criterion #2** (the `question:0009` serology↔lesion link). This pre-reg can
  discharge criterion #2 **only** via the optional conditional serology leg below (and only if the
  admissible vehicle carries G5), or it must already be satisfied elsewhere (owned by `task:t006`).
- **Therefore:** P1+P2 support on a **G1–G4-only** vehicle promotes h0007 **only if criterion #2 is
  independently met**; on a **G1–G5** vehicle whose serology leg also supports, this single study can
  discharge both criteria and promote on its own. Absent criterion #2, a clean criterion-#1 result
  advances h0007 substantially but leaves it **candidate** pending the autoantibody/immune link.

### Conditional leg 3 — P3 / serology (`proposition:0016`, `0018`, `question:0009`) — only if G5 met

- **Supports (weak→moderate):** within PAIS, functional anti-GPCR (β1/β2-adrenergic, M3/M4-muscarinic,
  receptor-*activation* assay, not binding-only) titer correlates with autonomic small-fiber severity
  (Spearman ρ, p < 0.05, **exploratory — uncorrected, labeled**) **or** seropositivity is enriched in
  lesion-positive vs lesion-negative PAIS. Either discharges h0007 promotion criterion #2's correlational
  arm and weakly supports `0016`/`0018`.
- **Disputes:** no titer↔severity association and no seropositivity enrichment → weakens the anti-GPCR
  route (`0018`) specifically, **without** falsifying bare immune-mediation (`0016`), which a non-antibody
  immune mechanism could still satisfy (per `0016` failure-mode scoping).

## Null Result Plan

Because the commitment targets are **epistemic**, every result class below is *evidence*, weighted by the
admissible vehicle's power (G4) and design quality — not a kill-switch.

| Result | Belief update | h0007 disposition |
|---|---|---|
| P1 + P2 both support | criterion #1 met; h0007 advances | candidate → **active** only if criterion #2 (q0009 serology↔lesion) is also met — else **stays candidate** pending the autoantibody/immune link |
| P1 supports, P2 null (Δ not sig.) | lesion real but non-discriminating; P2 downgraded | **stays candidate**; redirect to subtype/mechanism work |
| P1 + P2 support but primary-dysautonomia *also* NLD (Δ≈0) | substrate real, **not PAIS-specific**; q0004 "distinguishes" clause fails | stays candidate; reframe as shared-with-primary |
| P1 null, well-powered | structural-lesion frame collapses to functional account | h0007 **materially weakened** |
| P1 null, underpowered | inconclusive | no update; vehicle did not clear G4 → not admissible |

**Power & adequacy (the comparator NLD rate is the load-bearing assumption).** A null only updates
belief if the vehicle clears the **G4 well-powered-null floor**, and what that floor *is* depends
heavily on the (unknown) primary-dysautonomia NLD rate:
- If the comparator rate is **very low** (~5%, optimistic length-dependent prior): 33% vs 5% reaches
  ~80% power at **n ≈ 40 lesion-positive/side**, α = 0.025 two-sided. This is the *minimum-admissibility*
  floor.
- At **plausible mid-range** comparator rates (~10–13%): 33% vs 13% or 30% vs 10% reach only ~45–50%
  power at n = 40/side. Detecting Δ ≈ 20 pts there needs **n ≈ 80 lesion-positive/side** for ~80% power.
Therefore a **null at n = 40/side is *inconclusive*, not disconfirming** — only a null at the
**≥ 80/side well-powered floor** (or a CI excluding Δ ≥ 20 pts) weakens P2. An underpowered study (below
the minimum floor) returns *inconclusive*, fails admissibility, and does not move belief. Because the
comparator NLD rate is the softest number in this design, the vehicle should report it explicitly and the
required n should be re-derived from the *observed* comparator rate, not the assumed one.

**If ambiguous:** the most common ambiguity is heterogeneous lesion prevalence across PAIS triggers
(e.g. long COVID positive, ME/CFS null à la Walitt2024). That outcome supports **trigger-specificity**
(pressuring P4/`proposition:0017`, an exploratory leg here) rather than the shared substrate, and would
route to a per-trigger stratified re-analysis rather than a pooled verdict.

## Suspicious/Unexpected Result Plan

The discriminating contrast is exactly the kind a subtly broken design can manufacture. Before accepting
any **strongly positive** headline result (e.g. Δ > 50 pts, or PAIS NLD ≈ 100% with primary-dysautonomia
NLD ≈ 0%), require:

- **Reader blinding.** IENFD/SGNFD must be read blind to arm. Unblinded reading + a pattern endpoint is a
  classic inflator. Reject (treat as inconclusive) if blinding is absent or compromised.
- **Site/lab symmetry.** Both arms biopsied at the **same proximal and distal sites**, processed in the
  **same lab** against the **same site-specific norms**. A proximal-site or lab asymmetry between arms
  fabricates an apparent NLD difference. Reject on asymmetry.
- **Confounder-exclusion symmetry.** The length-dependent-SFN exclusion screen applied **identically**
  across arms. Differential exclusion (stricter in controls) inflates Δ.
- **"Primary" label integrity.** If the primary-dysautonomia arm shows an *unexpectedly high* NLD
  fraction, suspect **occult autoimmune SFN misassigned as primary** — audit that arm's inclusion
  (antecedent-infection screen, autoantibody status) before treating it as a clean comparator. A
  contaminated control arm destroys the discriminating contrast in *either* direction.

## Known Limitations

Even a flawless admissible vehicle cannot establish:

- **Lesion→symptom causation.** A cross-sectional pattern study is `identification_strength:
  observational`. It shows the lesion is *present and patterned*, not that it *causes* the dysautonomia.
  Joseph2021's own finding that SFN severity did not correlate with iCPET measures is the cautionary
  prior.
- **Ganglionopathy vs proximal axonopathy.** A non-length-dependent skin-biopsy pattern is *consistent
  with* dorsal-root/autonomic-ganglion cell-body targeting but does not directly image the ganglion; the
  mechanistic inference remains indirect.
- **Autoimmune causation (P3).** Even with the serology arm, an association is correlational. The
  decisive causal test is passive-transfer / depletion (deSa2026 / immunoadsorption designs), owned by
  `task:t006` — not this protocol.
- **Generalizability.** Referral-cohort selection (the Oaklander2022/Joseph2021 pattern) likely enriches
  severity; the lesion-positive *rate* may not generalize even if the *pattern contrast* is valid.

## Metric Selection Rationale

- **Site-specific z-scores, not raw proximal:distal ratio.** Locked from `proposition:0015`'s Measurement
  Model and from review feedback on the specify-model pass: absolute IENFD differs by body site, so a raw
  ratio conflates normal site anatomy with pathology. Norm-referencing each site independently is the
  only way the NLD classification means "proximal abnormality *disproportionate to* distal" rather than
  "proximal density lower than distal density (which is normal)."
- **NLD *fraction among lesion-positive*, not mean z-difference.** P2 is conditional on P1 (a lesion must
  exist before its distribution is meaningful), and a per-subject NLD/LD classification is what the
  clinical literature (Limongelli's 33%) reports, enabling direct comparison.
- **Difference-vs-primary-dysautonomia, not difference-vs-healthy.** The discriminating claim is
  *specificity* against primary dysautonomia, the comparator the entire corpus lacks. Healthy controls
  anchor P1 (lesion existence); primary-dysautonomia controls anchor P2 (pattern specificity). Both arms
  are required.
- **Known limitation of the metric:** the NLD/LD dichotomy is threshold-sensitive at the proximal site
  (where normative data are sparser than distal); the z ≤ −1.645 cutoff and the "proximal ≥ distal
  z-deficit" rule are pre-committed precisely to remove that degree of freedom at interpretation time.

## Exploratory vs. Confirmatory

| Analysis | Status | α |
|---|---|---|
| P1 lesion-positive rate: PAIS vs healthy | **confirmatory** | 0.025 (Bonferroni /2) |
| P2 NLD-fraction Δ: PAIS vs primary-dysautonomia | **confirmatory (headline)** | 0.025 (Bonferroni /2) |
| P4 cross-trigger convergence (per-trigger NLD ≥2 triggers) | exploratory | uncorrected, labeled |
| Serology titer↔autonomic-severity (P3/0018, q0009) | exploratory/conditional | uncorrected, labeled |
| Seropositivity enrichment lesion+ vs lesion− | exploratory/conditional | uncorrected, labeled |
| Immune-profile↔NLD correlation (Limongelli-style) | exploratory | uncorrected, labeled |

## Total Comparison Count

| Category | Count | Correction |
|---|---|---|
| Confirmatory tests | 2 (P1, P2-headline) | Bonferroni (α = 0.025 each) |
| Exploratory tests | ~4 (P4 convergence, 2× serology, immune-profile) | none (exploratory, labeled) |
| **Total** | **~6** | confirmatory family corrected; exploratory uncorrected |

## Vehicle-Admissibility Gate (data-gated mode)

**Standing verdict while gated: `[?] inconclusive-for-coverage` — no `bears_on` update on any commitment
target.** A candidate study/dataset activates this pre-reg's confirmatory analysis **only if it satisfies
G1–G4** (the floor). G5 additionally unlocks the conditional serology legs. Spent vehicles that fail any
of G1–G4 do **not** qualify (Oaklander2022, Joseph2021, Limongelli2026 each fail ≥1 gate — see below).

- **G1 — Paired-site biopsy with site-specific norms.** Proximal (thigh/trunk) **and** distal (lower-leg)
  IENFD on **every** subject, each scored against site-, age-, sex-, race-adjusted normative
  distributions (z/percentile). Distal-only designs fail (→ excludes `paper:Joseph2021`).
- **G2 — Primary-dysautonomia control arm.** An idiopathic-POTS and/or familial/primary autonomic-
  disorder comparator **with no antecedent-infection trigger**, *plus* a healthy-control arm. The arm the
  entire corpus lacks (→ excludes `paper:Oaklander2022`, which had no controls, and `paper:Limongelli2026`,
  post-vaccine without a primary-dysautonomia comparator).
- **G3 — ≥2 distinct PAIS triggers under one protocol.** Minimum: long COVID **plus** one of PTLDS or
  infection-associated ME/CFS, biopsied/scored identically (for the P4 convergence leg and to avoid
  manufacturing convergence from heterogeneous methods, per
  `topic:measurement-ascertainment-artifacts-in-pais`).
- **G4 — Power floor (two-tier).** Two distinct floors, because admissibility and well-powered-null are
  not the same bar:
  - **Confirmatory-support / minimum-admissibility floor:** ≥ **40 lesion-positive subjects per side** of
    the headline P2 contrast (pooled PAIS-autonomic vs primary-dysautonomia). This is enough to *detect*
    a positive Δ ≥ 20 pts when the comparator NLD rate is very low (e.g. 33% vs 5%, ~80% power at
    α = 0.025), but it is **not** a well-powered-null floor at plausible mid-range comparator rates.
  - **Well-powered-null floor:** ≥ **80 lesion-positive subjects per side** for Δ ≈ 20 pts. At α = 0.025
    two-sided, n = 40/side gives only ~45–50% power against realistic contrasts (33% vs 13%, 30% vs 10%),
    so a *null at n = 40* is **inconclusive, not disconfirming**; only a null at the ≥ 80/side floor (or
    a tight CI excluding Δ ≥ 20) updates belief against P2. A study between the two floors can *support*
    P2 (if Δ is significant) but cannot *weaken* it.
  - Each individual trigger sub-arm ≥ 15 (for the exploratory convergence leg). Below the minimum floor →
    study returns *inconclusive*, not *null*; does not move belief.
- **G5 (optional, unlocks conditional legs) — Parallel functional-autoantibody serology.** Functional
  (receptor-activation) anti-GPCR assay (β1/β2-adrenergic, M3/M4-muscarinic) on the same subjects.
  Absence does **not** block G1–G4 admissibility; it only leaves P3/`0018`/`question:0009` un-updated by
  this vehicle.

**Case definitions (must be stated by the vehicle; flagged because PAIS prevalence/mechanism estimates
are definition-sensitive):** long COVID = WHO 2021 post-COVID-19 condition, lab-confirmed acute
SARS-CoV-2; PTLDS = documented prior treated *Borrelia* infection (IDSA-consistent); infection-associated
ME/CFS = NAM 2015 (or CCC) **with documented infectious onset**; primary dysautonomia = idiopathic POTS
(tilt Δ ≥ 30 bpm, no SFN-causing comorbidity) or familial dysautonomia, **no antecedent infection**;
healthy controls = asymptomatic, no neuropathy risk factors. **Q-fever and post-dengue fatigue** are
candidate additional trigger arms to fold in once cohorts exist (per `proposition:0017`); not required
for admissibility.

## Screened Vehicles (vehicle-hunt log)

A vehicle hunt (`task:t050`) is run periodically against the literature; screened candidates and the
gate each fails are logged here so the search is not repeated and so the standing `[?]` verdict is
auditable. **Spent vehicles failing any of G1–G4 do not qualify** and produce no `bears_on` update.

**Hunt 2026-06-24 — no admissible vehicle; G2 is the universal blocker.** The decisive missing element
across the entire corpus remains a **clean primary-dysautonomia control arm** (idiopathic POTS / familial
dysautonomia, *no SFN-causing comorbidity*, no antecedent infection) biopsied under the **same** paired-site
protocol as the PAIS arms. Screened this hunt:

| Candidate | G1 paired-site | G2 primary-dysautonomia arm | G3 ≥2 PAIS triggers | G4 power | Verdict |
|---|---|---|---|---|---|
| **van Campen/Visser/Rowe 2025** ("Shared autonomic phenotype of long COVID and ME/CFS", PMC12829881) | ✓ proximal thigh + distal calf, PGP9.5 | ✗ comparators are **healthy (n=73)** and **hEDS (n=290)** — no idiopathic-POTS/familial arm; hEDS is **explicitly excluded by G2's "no SFN-causing comorbidity" clause** (hEDS itself carries SFN → contaminated control, cf. Suspicious-Results "primary-label integrity") | ✓ **long COVID (n=143) + ME/CFS (n=170)** | ✓ SFN ~80–90% → lesion-positive ≫ 80/side | **INADMISSIBLE (fails G2 only)** — closest vehicle to date |
| **Larsen et al. 2025** ("Long-COVID POTS: a deep phenotyping study", medRxiv 2025.04.28.25326587) | ✓ proximal + distal IENFD + P-Syn | ✗ comparator is **healthy controls only** | ✗ **long COVID only** | n/a (P1 came out inverted: 22% LC-POTS vs 38% HC reduced IENFD) | **INADMISSIBLE (fails G2, G3)** |
| **Gibbons et al. 2013** (neuropathic POTS, PMC3874039) and related POTS-biopsy series | partial | n/a — *is* the primary/neuropathic-POTS arm, but **not run alongside any PAIS arm** | ✗ | 38–45% reduced IENFD in POTS | not a vehicle; **supplies the comparator NLD/lesion prior** (the pre-reg's "softest number" — see Power & Adequacy) |

**Actionable intelligence.** The van Campen/Visser/Rowe group already runs the **exact G1 paired-site
protocol (proximal thigh + distal calf) at scale across two PAIS triggers (G3) with power far above the G4
floor** — it fails *only* on G2. An admissible vehicle is therefore realistically **one protocol amendment
away**: add an idiopathic-POTS or familial-dysautonomia arm (or partition a clean primary-POTS comparator
with the SFN-comorbidity exclusion applied) under the same protocol. This is the highest-yield place to
watch for, or solicit, the discriminating vehicle. Separately, Gibbons-type neuropathic-POTS series let the
**comparator NLD/lesion rate be pre-constrained** from existing data, tightening the G4 power re-derivation
before a head-to-head exists.

**Standing verdict unchanged: `[?]` inconclusive-for-coverage — no `bears_on` update.**
