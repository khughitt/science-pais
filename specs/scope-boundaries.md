---
id: "spec:scope-boundaries"
type: "spec"
title: "Scope boundaries for health-post-acute-infection"
status: "active"
source_refs:
  - cite:Nitz2025
  - cite:Bellavite2026
created: "2026-06-10"
updated: "2026-07-19"
---

# Scope Boundaries

## In Scope

- Post-acute infection syndromes as clinical entities and their pathophysiology: long COVID / post-acute sequelae of SARS-CoV-2 (PASC), ME/CFS, post-treatment Lyme disease syndrome (PTLDS), post-dengue and post-Q-fever fatigue, post-SARS syndrome, "long flu", and post-sepsis persistent inflammation/immunosuppression/catabolism syndrome (PICS).
- Candidate mechanisms of failed post-infectious recovery: persistent immune activation and T-cell exhaustion; antigen or pathogen-fragment persistence; autoimmunity and autoantibodies arising after infection; latent-virus reactivation (e.g. EBV); thromboinflammation, microclots, and endothelial dysfunction; dysautonomia and small-fiber neuropathy; mast-cell activation; gut-microbiome dysbiosis; and metabolic/mitochondrial dysfunction.
- Epidemiology, natural history, risk factors, subphenotyping, and long-term outcomes of these syndromes, including comparisons across triggering pathogens and against non-infectious controls (e.g. COVID vs influenza outcomes).
- Cross-syndrome synthesis: the shared "post-acute infection syndrome" failure mode and what distinguishes the syndromes, connecting to the immune-homeostasis frame in `health-immunity` and the multiscale-homeostasis frame in `health-meta`.
- Diagnostic biomarkers and therapeutic strategies evaluated specifically in the post-infectious context.

## Out of Scope

- General immune-mechanism, autoimmunity, tolerance, and immune-homeostasis biology that is **not specific to the post-infectious context** — these belong in `health-immunity` and are cross-linked/commons-shared rather than housed here.
- Acute infectious-disease biology and acute-phase pathogen mechanisms, except where they set up or predict post-acute sequelae.
- Cancer-related fatigue and cancer immunology (belong in the `~/d/cancer/` family; cross-link only).
- Primary chronobiology of fatigue/sleep (belongs in `health-cycles`; cross-reference only when circadian timing is central to a specific PAIS claim).
- Primary computational pipelines and large-scale data analyses until the project is past seed stage; early work is literature synthesis.

## Boundary-Monitor / Read-Across (not primary scope)

Some adjacent fatigue/dysautonomia syndromes share candidate mechanisms with PAIS but **fail the post-infectious-trigger requirement** that defines this project. They are **not** primary subjects of synthesis, but their mechanistic findings are retained as **read-across evidence** — usable to stress-test cross-trigger claims (notably `hypothesis:0001`, the shared dysregulated attractor) without being counted as in-scope PAIS cases. See `D-003` in `core/decisions.md` for the full ruling and criteria.

- **Inclusion criterion (headline rule):** a syndrome is *in primary scope* only if its trigger is an **acute infection**. This excludes the cases below by one consistent rule and matches the project name. *Mechanism-overlap alone is explicitly rejected as an admission criterion* — it is too permissive (it would admit essentially any oxidative/mitochondrial/dysautonomic condition) and would collapse the project boundary. **PEM/post-exertional-symptom presence** is the secondary discriminator used *within* this read-across set (see below).

- **Post-COVID-vaccination syndrome (PACVS):** **boundary-monitor / read-across only.** Non-infectious trigger (vaccination), and the PACVS-specific evidence base is currently the weakest in the corpus (one uncontrolled n≈17 ELISA case series reused across author-overlapping, COI-disclosed/heterodox reviews — Halma2026, Bellavite2026, Lesgards2025). The shared-spike-effector hypothesis (same antigen, infection vs. vaccine) is a *legitimate same-antigen/different-route discriminator* but is **untested by controlled comparison** and must be represented as hypothesis-to-test, not established parallel. **Revisit for admission only if** a controlled PACVS-vs-PASC biomarker comparison appears. See the *trigger × persistence test* below (`D-009`) for how acute vaccine adverse-event papers (e.g. `paper:Nitz2025`) sit relative to persistent PACVS.

- **Non-infectious fatigue syndromes — Gulf War Syndrome (GWS) and fibromyalgia (FM):** **boundary-monitor / read-across only**, and the *preferred* non-infectious stress-test for `hypothesis:0001`. Davis2025 (mainstream-tier review) shows GWS/FM share the metabolic/mitochondrial/oxidative lesion **and** the PEM metabolic signature with ME/CFS despite non-infectious triggers (organophosphate/toxic-chemical for GWS; idiopathic/multifactorial for FM). Because GWS is a non-infectious trigger that reportedly reaches the same downstream signature, it is the single best external test of the attractor's trigger-agnostic claim. Carry GWS/FM findings as read-across, flag unresolved metabolite-direction conflicts (e.g. sphingomyelin/tryptophan sign flips across conditions), and do **not** treat them as PAIS cases.

## Vaccine-adverse-event papers: the trigger × persistence test (`D-009`)

Vaccine-adverse-event papers (e.g. `paper:Nitz2025`, cardiovascular sequelae of COVID-19 vaccines; `paper:Bellavite2026`, PACVS/RAS-autoantibodies) recur in the corpus because they share the SARS-CoV-2 spike antigen with post-infection PAIS. Admissibility is decided by **two independent axes**, and **primary scope requires passing both**:

1. **Trigger axis** (the `D-003` headline rule): in primary scope only if the trigger is an **acute infection**. *Vaccination fails this axis.*
2. **Persistence axis** — the phenotype must persist into the **post-acute window**. There is **no single PAIS duration threshold**: the project's own `topic:pais-case-definition-heterogeneity` documents thresholds ranging from ≥4 weeks (CDC / NICE early long COVID) through ≥3 months (WHO / NASEM) to ≥6 months (ME/CFS, QFS, PTLDS), with ICC-ME and PICS setting none. For the narrow purpose of **routing vaccine papers**, this axis applies a **conservative ≥12-week routing convention** (not a claim about "the" PAIS definition). A phenotype whose long-term trajectory is **unmeasured** is **indeterminate** on this axis — neither a pass nor a fail.

This yields a routing 2×2 (below); the two axes are **not** interchangeable — persistence alone can never promote a vaccine-triggered phenotype to primary scope, because the trigger axis still fails. The 2×2 is a summary, not exhaustive: it omits the 4–12-week interval and the **unknown/censored-persistence** state that `Nitz2025` actually occupies (see below).

| | **Acute-event / onset estimand** | **Post-acute persistence** (routing convention ≥12 wk) |
|---|---|---|
| **Infection trigger** | acute-infection biology — out of scope except where it sets up sequelae | **PAIS — primary scope** |
| **Vaccine trigger** | **acute-event vaccine papers (`Nitz2025`) — comparator-only** | **PACVS (`Bellavite2026`) — boundary-monitor** (per `D-003`) |

- **Acute-event vaccine papers (the `Nitz2025` cell) — comparator-only.** `Nitz2025` characterises **acute-event incidence and onset** of vaccine-induced myocarditis/pericarditis, VITT/anti-PF4 thrombosis, and CVST (onset median ≤14 days, range to 90 days; myocarditis/pericarditis time-to-hospital-**discharge** 6–7 days; follow-up only **21–183 days** for myocarditis/pericarditis, 10–150 for thrombosis; thrombosis resolution not reported). It is comparator-only because of **(i)** the vaccine trigger (fails the trigger axis outright) and **(ii)** its **acute-event estimand** — it measures onset/incidence, not a persistent syndrome. It is **not** classified comparator-only on the ground that the events were *shown* to fail the persistence criterion: the authors explicitly state persistence, recurrence, and delayed-onset complications **cannot be assessed** from this literature, so the acute-vaccine corpus is **indeterminate, not negative, on persistence** (that gap is `question:0073`). On these grounds it is **not a PAIS case, not boundary-monitor-as-a-PAIS-analog, and not independent cross-trigger support for `hypothesis:0001`** (same bar `D-003` sets for PACVS/GWS). It is admitted **only as a mechanistic / epidemiological comparator**, for two specific uses:
  - the **infection-vs-vaccination CV risk asymmetry** (myocarditis vaccination ~2–3.2 vs infection ~15–18.3 — several-fold, ≈5–9× across these **non-meta-analyzed ranges**) as a **qualitative, hypothesis-generating comparator** — see `question:0081`. It is **not** a quantitative antigen-burden anchor and **not** belief-bearing support for antigen-burden dependency: the comparison is of *acute myocarditis* (not PAIS incidence) across heterogeneous observational studies with no common contrast, and does not isolate antigen dose from viral replication, tissue tropism, non-spike proteins, immune priming, or ascertainment. `proposition:0021` already holds vaccination evidence as **context/triangulation only**; and
  - the **acute-vaccine reference point** that bounds the same-antigen/different-route discriminator `D-003` monitors under PACVS.
- **The persistence dimension is unmeasured in this literature.** `Nitz2025`'s ≤183-day follow-up means the acute-vaccine corpus **cannot itself speak to whether any subset persists** — that open gap is `question:0073`, not evidence of resolution or of a chronic syndrome. (Persistent abnormal cardiac-MRI findings around five months are recognised in post-vaccination myocarditis outside this corpus, reinforcing that "acute onset" ≠ "resolved.")
- **Revisit-for-admission (mirrors the `D-003` PACVS clause):** if a **controlled longitudinal** study establishes that a post-vaccination CV phenotype **persists** into the post-acute window, it moves from the acute-event cell into the **PACVS (persistent-vaccine) cell** and is adjudicated there — i.e. it rises to **boundary-monitor / read-across at most, never primary scope**, because the trigger axis still fails. A controlled **PACVS-vs-PASC biomarker comparison** remains the trigger for reconsidering the PACVS cell itself (per `D-003`).
