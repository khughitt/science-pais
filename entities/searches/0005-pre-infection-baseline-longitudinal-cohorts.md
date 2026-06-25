---
type: search
title: "Literature/cohort search: pre-infection-baseline longitudinal PAIS designs (t008)"
status: active
created: "2026-06-25"
updated: "2026-06-25"
id: search:0005-pre-infection-baseline-longitudinal-cohorts
source_refs:
  - cite:Ballering2022
  - cite:Thompson2022
  - cite:Douaud2022
  - cite:AlcaldeHerraiz2025
  - cite:Neuhouser2024
  - cite:Ng2025
  - cite:deGois2026
  - cite:Thaweethai2023
  - cite:Vernon2024
related:
  - task:t008
  - dataset:recover-adult
  - topic:pais-case-definition-heterogeneity
  - topic:biomarkers-and-objective-endpoints
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
---

# Search: pre-infection-baseline longitudinal PAIS cohorts (t008)

## Search Focus

Identify the strongest longitudinal designs for PAIS causal claims when the core
methodological problem is missing pre-infection baseline data. The target was not another
mechanism-specific paper harvest; it was a **design hierarchy**: which cohorts can break
reverse causation, which can measure deep post-acute biology, and where those strengths
fail to coexist.

## Query Set

This pass combined existing project artifacts with targeted primary-source checks:

1. Existing project inventory: UK Biobank/WHI/Lifelines/RECOVER material already surfaced
   by `search:0001`, `report:0004`, `dataset:recover-adult`, and `paper:AlcaldeHerraiz2025`.
2. Targeted pre-baseline long-COVID anchors: Lifelines (`Ballering2022`), UK longitudinal
   studies/OpenSAFELY (`Thompson2022`), UK Biobank repeat MRI (`Douaud2022`), WHI risk
   screen (`Neuhouser2024`), WHI inflammatory baseline (`Ng2025`).
3. Targeted pre-infection biology anchor already in corpus: Brazilian healthcare-worker
   immune baseline (`deGois2026`).
4. RECOVER status/protocol check against the current official observational-cohort page
   and existing RECOVER paper entities (`Thaweethai2023`, `Vernon2024`).

## Headline Finding

The pre-infection-baseline requirement and the deep-PAIS-biology requirement are still
strongly anti-correlated.

- **Best temporal-ordering designs** are general-population cohorts and biobanks. They
  can measure symptoms, risk factors, imaging, broad labs, or EHR outcomes before
  infection, but they usually have weak PAIS mechanism panels.
- **Best post-acute mechanism designs** are RECOVER-style or clinic/acute-infection
  cohorts. They have deep phenotyping and biospecimens, but usually enroll after infection
  or after symptoms are established, so reverse causation remains live.

There is no single definitive dataset. The honest answer is a ranked set of design
archetypes, each fit for a different kind of causal claim.

## Ranked Design Anchors

| Tier | Cohort / paper | What the baseline controls | Best use | Main caveat |
|---|---|---|---|---|
| A1 | **Lifelines / `paper:Ballering2022`** | Pre-infection symptom burden + matched uninfected population symptom dynamics | Attributable persistent-symptom excess after SARS-CoV-2 | Self-report symptom channel; not a deep mechanism study |
| A1 | **UK Biobank repeat imaging / `paper:Douaud2022`** | Within-person pre-infection brain MRI/cognition | Objective incident neurological change | Not a full long-COVID syndrome outcome |
| A2 | **UK Biobank risk-factor analyses / `paper:AlcaldeHerraiz2025`** | Pre-infection sociodemographics, biomarkers, comorbidity | Ordered biomarker/comorbidity risk-factor tests; reusable outcome engineering | Baseline is 10-15 years before infection; LC/PACS phenotypes differ strongly |
| A2 | **WHI / `paper:Neuhouser2024`, `paper:Ng2025`** | Deep pre-pandemic health, lifestyle, function, and selected labs | Older-women risk/severity tests; pre-pandemic inflammatory-state signal | Women-only, older, and baseline can be decades stale |
| A2 | **de Gois HCW cohort / `paper:deGois2026`** | Pre-infection immune mediators | Baseline immune-state prediction of infection, severity, and early symptom persistence | Persistence threshold is >=4 weeks, not WHO long COVID; HCW exposure confounding |
| B | **10 UK longitudinal studies + OpenSAFELY / `paper:Thompson2022`** | Pre-pandemic general/mental health, BMI, asthma, demographics | Broad population risk-factor triangulation across survey and EHR channels | Heterogeneous long-COVID definitions; EHR coding/care-seeking artifacts |
| C | **RECOVER-Adult / `dataset:recover-adult`** | Limited/ambidirectional baseline; strong post-acute phenotype and biospecimen structure | Deep PASC phenotype, PEM-weighted index, biospecimen-mediated mechanism discovery | Mostly post-infection enrollment; no clean within-person pre-infection baseline |
| D | **EHR-only systems (OpenSAFELY/N3C-like)** | Historical diagnoses and utilization | Large-N sensitivity, comorbidity, medication, severe-outcome surveillance | Care-seeking and diagnostic-coding collider; weak symptom and mechanism measurement |

## Interpretation by Causal Question

### Symptom attribution

`paper:Ballering2022` is the benchmark. It addresses the exact problem that most
post-COVID symptom studies leave open: symptoms present before infection and symptoms
changing in the uninfected population during the same pandemic period. For any claim that
SARS-CoV-2 caused persistent symptom excess, this is the cleaner design class than a
post-hoc long-COVID survey.

### Objective incident tissue/organ change

`paper:Douaud2022` is the benchmark. It shows what a true objective pre/post endpoint
looks like: within-person MRI before infection, repeat MRI after infection, and
matched controls. It is not a general PAIS case-definition study, but it is a stronger
causal design than cross-sectional cognitive or imaging reports.

### Baseline vulnerability / risk factors

`paper:Thompson2022`, `paper:AlcaldeHerraiz2025`, `paper:Neuhouser2024`, and
`paper:Ng2025` are the reusable risk-factor anchors. They constrain reverse causation
for broad pre-pandemic predictors, but they do not automatically turn those predictors
into mechanisms. A baseline leukocyte count, SHBG, BMI, asthma, or mental-health signal
is ordered in time; it still needs mechanistic mediation or replication before being
promoted beyond risk stratification.

`paper:deGois2026` is the most biologically granular pre-infection immune example in the
current corpus. Its symptom-persistence threshold is too early for definitive PAIS, but
its design is exactly the kind of prospective immune baseline that would be decisive if
replicated with a >=12-week/WHO or RECOVER-index outcome.

### Deep mechanism discovery

RECOVER remains the strongest current US resource for post-acute phenotyping and
biospecimens, and the official observational-cohort page now notes a next phase beginning
May 4, 2026 with two more years of surveys, health checks, tests, and blood collection.
That improves future longitudinal follow-up, but it does not convert RECOVER into a
true pre-infection-baseline cohort. It is a mechanism-discovery and post-acute trajectory
resource, not the cleanest causal-ordering resource.

## Methodological Rule Carried Forward

Do not collapse these designs into one evidence tier. "Longitudinal" is not enough.
For PAIS causal claims, record which baseline exists:

| Baseline type | What it can rule out | What it cannot rule out |
|---|---|---|
| Pre-infection symptom baseline + controls | Pre-existing symptom burden and background population symptom drift | Molecular mechanism |
| Pre-infection objective endpoint | Baseline organ/tissue differences | Full syndrome attribution unless paired with symptom/functional outcome |
| Pre-pandemic broad risk factors/labs | Reverse causation for those predictors | Whether predictors are causal, confounded, or proxy markers |
| Acute-infection baseline only | Post-acute change from acute state | Pre-existing vulnerability before infection |
| Post-acute enrollment baseline | Subsequent trajectory | Reverse causation by established chronic illness |

## Implications for Current Project Claims

- **`question:0017` reverse-causation alternative:** materially constrained only by tier-A/A2
  designs. Cross-sectional biomarker studies should continue to be scored as ambiguous.
- **`hypothesis:0005`:** UKB and WHI remain the best pre-baseline vehicles for reproductive-stage
  and inflammatory baseline questions, but WHI/Neuhouser still does not adjudicate HRT/MHT.
- **RECOVER-dependent paths:** strong for phenotype and post-acute mediators, weak for
  pre-infection causal ordering unless an external baseline, prior biospecimen, or linked
  pre-COVID cohort arm is added.
- **Cross-pathogen PAIS:** no comparable pre-infection-baseline resource was identified for
  PTLDS, QFS, post-dengue, or post-SARS fatigue. Cross-trigger mechanism claims therefore
  remain especially exposed to reverse-causation and ascertainment artifacts.

## Recommended Next Actions

1. Use this design hierarchy as the default citation whenever a hypothesis claims
   "pre-infection baseline needed" rather than re-litigating cohort options.
2. Treat Lifelines and UKB repeat-imaging as methodological benchmarks in future reviews:
   symptom attribution and objective pre/post change are different gold standards.
3. Track RECOVER's 2026-2028 follow-up for new incident/trajectory papers, but keep the
   "no true pre-infection baseline" caveat unless a linked pre-COVID baseline appears.
4. If a future task needs a runnable positive test, prefer the already developed UKB/WHI
   routes for baseline risk and RECOVER only for post-acute phenotype/mechanism questions.

## Search Verdict

`task:t008` is complete as a design audit. It does not add evidence-lines or change any
belief grade. The result is a methodological constraint on future evidence interpretation:
pre-infection-baseline designs exist and should be privileged for temporal ordering, but
they are sparse, single-trigger, and usually shallow mechanistically.
