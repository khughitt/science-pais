---
id: interpretation:0021-t026-pc-cos-adoption-policy
kind: interpretation
title: "t026: Adopt PC-COS domains as minimum dimensional reporting, not as case definition or fixed instrument battery"
status: active
source_refs:
  - paper:Munblit2022PCCOS
  - paper:PCCOS2023COMS
related:
  - task:t026
  - paper:Munblit2022PCCOS
  - paper:PCCOS2023COMS
  - topic:pais-case-definition-heterogeneity
  - topic:biomarkers-and-objective-endpoints
  - question:0014-which-pais-case-definition-is-most-biologically-coherent
  - question:0015-does-pem-requirement-improve-cross-study-comparability
  - pre-registration:0001-menopause-pais-total-effect
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
created: "2026-06-25"
updated: "2026-06-25"
input:
  - paper:Munblit2022PCCOS
  - paper:PCCOS2023COMS
prior_interpretations: []
relations: []
---

<!-- Mode: CONCEPTUAL / METHODS. Input is the adult PC-COS domain paper and its follow-on COMS instrument-consensus paper. No evidence-lines or belief updates are minted. -->

# Interpretation: t026 - PC-COS adoption policy

## Verdict

**[+] Adopt with boundaries.** PAIS analyses should use PC-COS as a **minimum
dimensional-reporting frame** whenever adult long-COVID outcomes are being measured or
harmonized. PC-COS should not replace the binary PAIS case variable, should not be treated
as a mechanistic case definition, and should not be imported wholesale to non-COVID PAIS
without trigger-specific justification.

The important correction to the task shorthand is that adult PC-COS is not just fatigue,
breathlessness, cognition, and quality of life. The 2022 COS contains 12 domains:
fatigue/exhaustion, pain, post-exertion symptoms, work/study changes, survival, recovery,
and cardiovascular, respiratory, nervous-system, cognitive, mental, and physical
functioning/symptom/condition domains.

## Adoption Rule

For future PAIS pre-registrations and analyses:

1. **Keep the binary case definition primary when the estimand is incidence/risk.** PC-COS
   domains do not define who has PAIS; they define what should be reported about outcomes.
2. **Add PC-COS dimensional endpoints where the source data support them.** At minimum,
   report fatigue, post-exertion symptoms, cognition, respiratory/breathlessness, physical
   function, recovery, work/study impact, and pain when available.
3. **Separate "domain adopted" from "instrument adopted."** The follow-on COMS reached
   consensus only for survival, recovery, and mMRC dyspnea. For the other nine domains,
   instruments are ranked candidates, not mandatory standards.
4. **Do not let PC-COS flatten the mechanism question.** Mechanistic PAIS tests still need
   validated PEM/PESE measurement, objective autonomic/vascular/muscle/immune endpoints,
   and trigger-specific case-definition discipline.
5. **For cross-pathogen work, map to PC-COS-like domains rather than claiming formal
   PC-COS compliance.** QFS, PTLDS, post-dengue, post-SARS, and ME/CFS do not share an
   adult long-COVID COS.

## Implications

### t001 / cross-trigger work

Use PC-COS domains as the common symptom/impact vocabulary for cross-trigger matrices:
fatigue, post-exertion symptoms, cognition, respiratory symptoms, pain, physical function,
work/study impact, and recovery. This improves comparability without pretending that the
same validated instrument exists across all PAIS triggers.

### t016 / UKB menopause-PAIS analysis

Do not change the confirmatory outcome. The primary outcome remains the pre-registered
WHO >=90-day Route-A long-COVID risk contrast. PC-COS domains should be used as
secondary/descriptive reporting strata where UKB fields permit them: fatigue/PESE proxy,
cognitive symptoms, respiratory symptoms, pain, physical impact, recovery, and work/study
impact. These are not multiplicity-bearing confirmatory endpoints unless separately
pre-registered.

### h0008 measurement-channel critique

PC-COS helps by making outcome domains explicit, but it does not solve instrument
instability. The COMS paper is the key caveat: most domains still lack a consensus
instrument, so h0008's endpoint-contingency critique remains live.

## Non-adoption Boundaries

- **Not a case definition.** PC-COS complements WHO/NASEM/RECOVER definitions; it does
  not classify cases.
- **Not PEM-specific enough for mechanistic ME/CFS-like PAIS.** "Post-exertion symptoms"
  is included, but PC-COS does not require PEM as an entry criterion.
- **Not a full instrument standard.** Candidate instruments such as FAS/FSS/FACIT-F,
  DePaul Symptom Questionnaire, CFQ/MoCA-Blind, SBQ-LC, SF-36, and WHO-DAS should be
  selected based on dataset availability and analysis purpose, with the no-consensus caveat.
- **Not pediatric.** Adult PC-COS does not discharge pediatric long-COVID/MIS-C outcome
  harmonization (`task:t009`).

## Graph Disposition

Add paper anchors for the 2022 COS and 2023 COMS. Update the case-definition topic and
the UKB pre-registration with the bounded adoption rule. No propositions or evidence-lines
are minted because this is a methods policy, not a causal or mechanistic claim.
