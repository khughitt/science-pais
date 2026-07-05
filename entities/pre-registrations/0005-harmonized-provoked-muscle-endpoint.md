---
id: pre-registration:0005-harmonized-provoked-muscle-endpoint
kind: pre-registration
title: "Harmonized LC+ME/CFS provoked muscle-endpoint study for h0006 vs h0008-M3"
status: committed
committed: '2026-06-26'
mode: data-gated
spec: ''
related:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- question:0011-mitochondrial-basis-of-pem
- question:0016-oxidative-stress-upstream-driver-of-bioenergetic
- proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
- proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle
- proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
- proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury
- proposition:0035-pem-muscle-lesion-is-self-perpetuating
- proposition:0030-mecfs-exercise-provoked-skeletal-muscle-bioenergetic-abnormality
- discussion:0004-pem-shared-muscle-lesion-vs-endpoint-contingency
- interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion
- task:t056
- task:t057
- task:t058
- paper:Appelman2024
- paper:Joseph2023
- paper:Jones2012
- paper:Wong1992
- paper:Brown2015
- paper:Bizjak2024
- paper:Scheibenbogen2024
- paper:Walitt2024
commits_to:
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- question:0011-mitochondrial-basis-of-pem
- question:0016-oxidative-stress-upstream-driver-of-bioenergetic
- proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
- proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle
- proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
- proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury
- proposition:0035-pem-muscle-lesion-is-self-perpetuating
created: '2026-06-26'
updated: '2026-06-26'
---
# Pre-registration: harmonized LC+ME/CFS provoked muscle-endpoint study for h0006 vs h0008-M3

> **Mode: data-gated.** No admissible vehicle exists in the corpus. This pre-registration commits the
> interpretation rule for the first harmonized long-COVID + ME/CFS provoked muscle-endpoint study and
> defers execution until a study clears the Vehicle-Admissibility Gate below. Until then the standing
> verdict is **`[?]` inconclusive-for-coverage** and there is no belief update on the commitment targets.

## Hypotheses Under Test

This is the decisive adjudicator named by `discussion:0004`, narrowed by `interpretation:0019`, and
operationalized after `task:t057` specified the redox-direction hinge. It asks whether PEM has the same
provoked skeletal-muscle lesion across long COVID and ME/CFS under one endpoint-harmonized protocol, or
whether apparent convergence/divergence is an endpoint-contingent measurement artifact.

| Target | Role | Test | Class |
|---|---|---|---|
| `hypothesis:0006` | candidate skeletal-muscle ischemic-mitochondrial PEM model | joint result across P1-P4 and cross-trigger sharing | confirmatory |
| `proposition:0032` (P1) | muscle localization | provoked muscle injury/OXPHOS signal vs controls | confirmatory |
| `proposition:0033` (P2) | perfusion/extraction upstream leg | perfusion/extraction ordering before muscle injury | confirmatory |
| `proposition:0034` (P3) | Na/Ca mediator leg | ion shift ordering between perfusion stress and mitochondrial injury | confirmatory |
| `proposition:0035` (P4) | self-perpetuating lesion | delayed 24-48 h worsening/recovery trajectory and redox directionality | confirmatory |
| `question:0011` | shared bioenergetic PEM lesion | same endpoint across LC and ME/CFS | confirmatory |
| `question:0016` | redox driver vs marker | redox temporal precedence or target-engagement pattern | confirmatory |
| `proposition:0029` (h0008-M3) | endpoint/trigger contingency | whether harmonization removes or confirms endpoint-specificity | confirmatory adversary |

`hypothesis:0008` is in `related:` but not `commits_to:`. This study directly adjudicates M3
(`proposition:0029`), not the full h0008 bundle (M1/M2 are not tested here).

## Expected Outcomes

Prior is mixed. `paper:Appelman2024` gives the long-COVID reference lesion: baseline muscle OXPHOS
impairment that worsens after PEM, with a selective post-exertional SDH/Complex-II decline and myopathic
injury. `task:t056` found real ME/CFS muscle bioenergetic abnormalities (`proposition:0030`) but not an
Appelman-equivalent ME/CFS pre/post-PEM biopsy time-course. Therefore the expected result is **partial
convergence**: both triggers show a provoked muscle abnormality, but the exact Appelman-style lesion,
timing, or upstream ordering may differ.

That expectation is intentionally weak. A clean same-lesion result would materially strengthen h0006 and
weaken h0008-M3 for PEM; a clean trigger- or endpoint-specific result would strengthen h0008-M3 and cap
h0006 at "muscle-localization plausible, shared ischemic-ionic cascade unproven."

## Vehicle-Admissibility Gate

The interpretation rule activates only if the vehicle satisfies all floor gates:

- **G1 - trigger arms:** long COVID and ME/CFS PEM-positive arms, plus recovered-infection and/or healthy
  controls, enrolled under the same protocol. Diagnostic criteria and PEM instrument must be reported.
- **G2 - harmonized exertion:** the same standardized exertional provocation, effort criteria, and
  sampling schedule across arms.
- **G3 - serial muscle endpoint:** skeletal-muscle readouts at minimum pre-exertion, immediate
  post-exertion, and 24-48 h post-exertion; a recovery/resolution time point is preferred.
- **G4 - endpoint breadth:** OXPHOS/SDH or Complex-II activity, fiber-type composition, myopathic injury,
  perfusion/extraction, Na/Ca or ion-handling markers, ROS/redox markers, and immune infiltrate or
  inflammation markers. Missing one marker family downgrades the affected leg but does not invalidate the
  whole vehicle if P1 and cross-trigger endpoint harmonization remain interpretable.
- **G5 - central/peripheral decomposition:** CPET, invasive CPET, NIRS, MRI, or equivalent readout able to
  separate central/cardiac limitation from peripheral extraction or muscle utilization.
- **G6 - ascertainment control:** matched or modeled age, sex, acute-severity, time-since-infection,
  baseline activity/fitness, medication/supplement exposures relevant to redox or mitochondrial biology,
  and comorbidities affecting muscle, vascular, or mitochondrial endpoints.
- **G7 - power floor:** at least 30 PEM-positive participants per disease arm with analyzable serial
  muscle data, or a precision argument showing CIs narrow enough to classify same-lesion vs
  trigger-specific patterns. Smaller studies can support pilot feasibility but cannot weaken h0006 or
  h0008-M3.

## Decision Criteria

### Primary endpoint: same-lesion cross-trigger muscle convergence

Define the Appelman-style lesion as a post-exertional worsening in skeletal-muscle oxidative metabolism
or injury, anchored by OXPHOS/SDH or Complex-II activity and supported by myopathic injury/fiber-type
shift. The primary contrast is whether LC and ME/CFS show the **same direction and comparable timing** of
this lesion relative to recovered/healthy controls.

- **Supports h0006 P1 and q0011:** both LC and ME/CFS show a provoked muscle bioenergetic lesion under
  the same endpoint.
- **Strongly supports h0006 and weakens h0008-M3:** both triggers show the same lesion family, timing,
  and recovery trajectory, and whole-body endpoint differences are explained by sensitivity rather than
  different biology.
- **Supports h0008-M3 and limits h0006:** one trigger is positive and the other null, or both are positive
  only under different endpoint definitions/timings. This means endpoint choice can manufacture or hide
  the shared-mechanism claim.
- **Weakens h0006 P1:** neither disease arm differs from controls on provoked muscle endpoints in a
  well-powered vehicle.

### Secondary leg P2: perfusion or extraction ordering

- **Supports P2:** impaired muscle perfusion/extraction precedes or predicts later OXPHOS/SDH decline,
  myopathic injury, or PEM duration within subjects.
- **Weakens P2:** intrinsic muscle utilization failure is present in hyperoxic or perfusion-normal
  conditions, or perfusion/extraction abnormalities appear only after mitochondrial injury.
- **Inconclusive:** peripheral extraction abnormalities are present but only cross-sectionally or without
  temporal ordering.

### Secondary leg P3: ionic mediation

- **Supports P3:** intracellular sodium/calcium or ion-pump stress changes temporally bridge
  perfusion/extraction stress and later mitochondrial injury.
- **Weakens P3:** sodium/calcium changes are absent, downstream-only, or unrelated to muscle injury and
  PEM kinetics in a well-powered vehicle.
- **Inconclusive:** only 23Na-MRI sodium or only inferred calcium is measured without paired
  mitochondrial timing.

### Secondary leg P4 and q0016: self-perpetuation and redox directionality

Use the three-model rule in `question:0016`:

- **Driver / loop-closing support:** early muscle redox shift precedes or independently predicts later
  OXPHOS/SDH decline, ion/perfusion stress, and PEM recovery time.
- **Reciprocal-node support:** redox rises with injury and predicts persistence/recovery even if it is not
  the first abnormality.
- **Downstream-marker weakening:** redox changes only after mitochondrial injury, does not predict
  recovery, or can be normalized without improving downstream muscle or PEM endpoints.

P4 requires more than a single immediate post-exercise abnormality. It needs delayed 24-48 h worsening,
slow normalization, recurrence, or intervention-linked reversal consistent with positive feedback.

## Promotion Implications

For h0006, this study can discharge the cross-trigger muscle-endpoint promotion criterion if LC and ME/CFS
share an Appelman-style post-exertional muscle lesion under the same protocol. Promotion still depends on
the full bundle: a same-lesion P1 result with null P2/P3/P4 advances h0006 but leaves the ischemic-ionic
self-perpetuation model candidate.

For h0008-M3, a trigger-specific or endpoint-specific result provides a prospective second-instance style
support for endpoint contingency in PEM. A same-lesion result weakens the PEM instance of M3 but does not
falsify h0008 M1/M2 or the SFN endpoint-contingency thread.

## Null Result Plan

| Result | Belief update |
|---|---|
| LC and ME/CFS same lesion, P2-P4 coherent | strong support for h0006; q0011 shared-muscle answer; M3 weakened for PEM |
| LC and ME/CFS both muscle-positive but different timing/endpoint | supports P1/q0011 broadly; supports h0008-M3; h0006 same-lesion claim remains unproven |
| LC positive, ME/CFS null under same protocol | Appelman-style lesion may be LC-specific; h0008-M3 strengthened; h0006 criterion #3 fails |
| ME/CFS positive, LC null | forces audit of Appelman comparability/cohort; supports endpoint or cohort contingency |
| both null, well-powered | weakens h0006 P1 and the muscle-substrate reading |
| both null, underpowered or missing serial muscle endpoint | inconclusive; no belief update |

## Suspicious/Unexpected Result Plan

Before accepting an unusually clean same-lesion result, check: biopsy-reader blinding, exertion-dose
equivalence, activity pacing before challenge, tissue-processing batch effects, fiber-type composition
imbalance, medication/supplement imbalance, and whether PEM-positive case definitions were equivalent.

Before accepting a clean divergence result, check: unequal timing windows, unequal PEM severity, acute
severity/time-since-infection imbalance, differential deconditioning, and whether one arm had lower effort
or failed effort criteria. A divergence caused by protocol imbalance is inconclusive, not h0008 support.

## Standing Verdict

`[?]` inconclusive-for-coverage until a qualifying vehicle clears G1-G7. Tracked by `task:t058`.
