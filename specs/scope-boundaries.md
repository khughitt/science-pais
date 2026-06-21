---
id: "spec:scope-boundaries"
type: "spec"
title: "Scope boundaries for health-post-acute-infection"
status: "active"
source_refs: []
created: "2026-06-10"
updated: "2026-06-21"
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

- **Post-COVID-vaccination syndrome (PACVS):** **boundary-monitor / read-across only.** Non-infectious trigger (vaccination), and the PACVS-specific evidence base is currently the weakest in the corpus (one uncontrolled n≈17 ELISA case series reused across author-overlapping, COI-disclosed/heterodox reviews — Halma2026, Bellavite2026, Lesgards2025). The shared-spike-effector hypothesis (same antigen, infection vs. vaccine) is a *legitimate same-antigen/different-route discriminator* but is **untested by controlled comparison** and must be represented as hypothesis-to-test, not established parallel. **Revisit for admission only if** a controlled PACVS-vs-PASC biomarker comparison appears.

- **Non-infectious fatigue syndromes — Gulf War Syndrome (GWS) and fibromyalgia (FM):** **boundary-monitor / read-across only**, and the *preferred* non-infectious stress-test for `hypothesis:0001`. Davis2025 (mainstream-tier review) shows GWS/FM share the metabolic/mitochondrial/oxidative lesion **and** the PEM metabolic signature with ME/CFS despite non-infectious triggers (organophosphate/toxic-chemical for GWS; idiopathic/multifactorial for FM). Because GWS is a non-infectious trigger that reportedly reaches the same downstream signature, it is the single best external test of the attractor's trigger-agnostic claim. Carry GWS/FM findings as read-across, flag unresolved metabolite-direction conflicts (e.g. sphingomyelin/tryptophan sign flips across conditions), and do **not** treat them as PAIS cases.
