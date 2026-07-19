---
id: interpretation:0044-t128-ip10-antigen-vs-sterile-discriminating-panel
kind: interpretation
title: t128 — a co-measurement marker panel to split h0019 (sterile cGAS-STING/NLRP3 sensing) from h0002 (retained antigen-fragment) as the driver of persistent IP-10/CXCL10; the panel is a necessary triage + relative-contribution screen, not an identifying design (the decisive test stays interventional)
status: active
source_refs:
- cite:Vacharathit2025
- cite:Domizio2022
- cite:Peluso2024
- cite:McClune2025
related:
- question:0076-ip10-cxcl10-omicron-persistence-antigen-vs-sterile
- hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver
- hypothesis:0002-tissue-reservoir-antigen-fragment
- hypothesis:0001-shared-dysregulated-attractor
- paper:Vacharathit2025
- topic:innate-immune-memory-trained-immunity-in-pais
created: '2026-07-19'
updated: '2026-07-19'
input: entities/questions/0076; entities/hypotheses/0019 (P1-P5, promotion criterion #1); entities/hypotheses/0002 (proposition:0022 persistence pillar); entities/papers/Vacharathit2025; cite:Domizio2022, cite:Peluso2024, cite:McClune2025 (design proposal; no data analyzed)
prior_interpretations: []
relations: []
---

# Interpretation: t128 — discriminating marker panel for persistent IP-10/CXCL10 (sterile-innate vs antigen-fragment)

## Verdict

**Verdict:** [→] **Design delivered.** A **co-measurement panel** that assays, longitudinally and in the *same* subjects, (A) a **sterile cytosolic-sensing** cluster (cGAS-STING + NLRP3 + DAMPs) and (B) an **antigen-persistence** cluster (viral antigen/RNA + antigen-specific IFN-γ), anchored to the shared output **IP-10/CXCL10**, can adjudicate `question:0076` — but only as a **triage + relative-contribution screen**, not as an identifying design. It can (i) **falsify** either driver in this phenotype if that arm's markers are absent in IP-10-high subjects, and (ii) estimate each arm's *contribution* by mediation — but it **cannot deliver clean causal attribution**, because the two mechanisms are not mutually exclusive, share the IP-10 output, and are subject to unmeasured upstream confounding. The **decisive test remains interventional** — sensor-selective inhibition (h0019 P3) or antigen clearance (h0002 `question:0002`) with IP-10 as the pharmacodynamic endpoint. The panel is the necessary *precondition* that says whether either interventional arm is worth running, and it directly operationalizes **h0019 promotion criterion #1** (persistent cGAS-STING/NLRP3 activity *dissociated from replication*).

## Findings Summary — the discriminating logic

Both hypotheses predict the **same downstream reading** — persistent IP-10/CXCL10 and an interferon/ISG signature (Vacharathit2025: 7–10× baseline IP-10 to 6–8 months after mild Omicron breakthrough). They diverge on the **upstream driver**, and that is what the panel must resolve:

- **h0019 (sterile-innate):** IP-10 is sustained by **host-derived** cytosolic-DNA sensing — cGAS → cGAMP → STING → TBK1/IRF3 → **type-I IFN** (P1) — and/or an **NLRP3 → caspase-1 → IL-1β/IL-18 → gasdermin-D** loop (P2), fed by DAMPs (mtDNA, HMGB1; P5), **with no requirement for viral antigen**.
- **h0002 (antigen-fragment):** IP-10 is sustained by **retained pathogen antigen/fragments** (degradation-resistant, non-replicating) that engage innate sensing and sustain **antigen-specific T-cell IFN-γ (type-II IFN)**, which induces IP-10 in bystander cells.

**The single sharpest axis is the interferon class driving IP-10.** CXCL10/IP-10 is inducible by *both* type-I and type-II IFN, so resolving **which IFN axis dominates** is itself discriminating: **IFN-I-dominant (STING route) favors h0019; IFN-γ-dominant (antigen-specific-T-cell route) favors h0002.** The full panel adds the specific upstream markers that confirm the route and exclude the alternative.

### Panel — two arms + the shared anchor

| Cluster | Marker(s) | h0019 predicts | h0002 predicts | Assay / feasibility tier |
|---|---|---|---|---|
| **Anchor (shared output)** | IP-10/CXCL10 (longitudinal) | elevated, persistent | elevated, persistent | Luminex/Simoa — **practical**; same run as cytokines |
| **IFN class** | IFN-α (type-I) vs IFN-γ (type-II); ISG-I signature | **IFN-I / ISG-I dominant** | **IFN-γ dominant** | IFN-α Simoa + ISG qPCR — practical; the load-bearing discriminator |
| **A1 — cGAS-STING** | 2′3′-**cGAMP**; phospho-**TBK1**(S172) / phospho-IRF3(S396) | **elevated** (active sensing) | not required | cGAMP LC-MS/MS or ELISA (low plasma abundance → **aspirational**); phospho-flow on **fresh** PBMC (**demanding**) |
| **A2 — IFN-I readout (robust proxy)** | **SIGLEC-1/CD169** on monocytes; ISG15/IFI27/MX1/IFIT1 | elevated (STING-driven) | may be elevated (IFN-γ can co-induce some ISGs) | Flow (CD169) + qPCR — **practical**; the workhorse ISG readout |
| **A3 — NLRP3 loop** | IL-18, IL-1β, cleaved **gasdermin-D** (GSDMD-N), caspase-1, ASC specks | **elevated** (P2) | not specifically predicted | IL-18/IL-1β Luminex — practical; GSDMD-N immunoblot/ELISA — **demanding** |
| **A4 — DAMPs** | circulating **mtDNA** (qPCR), **HMGB1**, ox-mtDNA | **elevated**, correlate with ISG-I | not specifically predicted | cell-free mtDNA qPCR — **practical** |
| **B1 — viral antigen** | plasma/tissue **spike / S1 / N** (Simoa/Simoa-style) | absent, or IP-10-**uncorrelated** | **present; IP-10 co-varies with burden** | Simoa (Peluso2024 method) — **practical** |
| **B2 — viral RNA** | plasma/stool total RNA; **subgenomic** RNA (replication indicator) | absent | total/antigen may persist; **sgRNA absent** (fragment, not replication) | ddPCR — practical; distinguishes fragment from replication |
| **B3 — antigen-specific adaptive** | SARS-CoV-2-specific **T-cell IFN-γ** (AIM / ICS / ELISpot) | not the driver | **elevated; statistically mediates IP-10** | AIM/ELISpot — moderate |

### Decision rule (probabilistic, not binary)

- **Antigen arm positive** (B1/B2 antigen present, B3 antigen-specific IFN-γ elevated) **AND IP-10 mediated by them** → **h0002 favored** for this phenotype.
- **Sterile arm positive** (A1 cGAMP/pTBK1 and/or A3 inflammasome and A4 DAMPs elevated; IP-10 tracks IFN-I/ISG-I) **AND antigen arm negative** → **h0019 favored**.
- **Both arms positive** → **co-operation** (q0076's parsimonious reading); report each arm's *partial* mediation of IP-10, do not force a winner.
- **Neither**, or IP-10 tracks a **vaccine-primed IL-15–IFN-γ–IP-10 axis** (Bergamaschi-type; more likely near mRNA dosing) → a **third driver / confounder** → stratify by vaccination status and time-since-dose *a priori*.

### What the panel can *falsify* (its highest-value use)

- If **no viral antigen/RNA** is detectable in IP-10-high subjects across the persistence window → **h0002 is falsified as the IP-10 driver** in mild-Omicron persistent IP-10 (it would remain viable for other phenotypes). This is the single most decisive achievable result, because Vacharathit2025 *did not* measure antigen — the arm is currently unexcluded, not excluded.
- If **cGAS-STING and inflammasome markers are absent** despite persistent IP-10 → **h0019 P1/P2 are falsified as the driver here**, collapsing the sterile-sensing frame toward "downstream output, not upstream seed" (its own `Current Uncertainty` already flags this open direction).

## Evidence Quality

- **Source class:** forward-looking **design proposal**, not an evidence interpretation. No data analyzed. It synthesizes q0076's stated data need, h0019's P1–P5 predictions and promotion criterion #1, and h0002's persistence pillar (`proposition:0022`), grounded in Vacharathit2025 (the IP-10 persistence observation), Domizio2022 (SARS-CoV-2 → mtDNA → cGAS-STING, **acute** endothelium — the sterile-sensor precedent), Peluso2024 (Simoa antigen-persistence method), and McClune2025 (fragment-reservoir logic).
- **Belief impact:** **none directly** — proposing a discriminating assay does not move belief on h0019 or h0002; it specifies the measurement that *would*. No proposition update, no evidence-line minted. It sharpens q0076 from "unadjudicable" to "adjudicable-by-this-panel, with these limits."
- **Confirmatory vs exploratory:** exploratory design; this is itself a pre-registerable protocol skeleton, not a pre-registration entity (kept as an interpretation-rollup to avoid over-committing a study the seed-stage project does not run).

## Data Quality Checks

No dataset analyzed. Design-level fitness flags are captured in Limitations (assay maturity, compartment mismatch, timing, non-independence). No data-quality concern applies.

## Hypothesis- and Question-Level Implications

- **`question:0076`:** **Advanced, not answered.** Logged resolution: the antigen-vs-sterile distinction is **adjudicable by this co-measurement panel** (with the interferon-class axis as the sharpest single discriminator), but the panel is correlational — the decisive adjudication is the interventional arm each hypothesis already names. q0076 stays `active`; its "no study has measured cGAMP/pTBK1/GSDMD/antigen simultaneously with IP-10" gap is now specified as an executable (if unfunded) protocol.
- **`hypothesis:0019`:** **No belief change; the panel operationalizes promotion criterion #1** (persistent cGAS-STING/NLRP3 activity — cGAMP/pTBK1/GSDMD/IL-18 — *dissociated from replication markers*). The antigen arm (B1–B3) is the "dissociated-from-replication" control that criterion #1 requires. A positive sterile arm with a negative antigen arm would be suggestive promotion evidence; the panel does **not** itself promote.
- **`hypothesis:0002`:** **No belief change.** The panel is the phenotype-specific antigen test for the persistent-IP-10 reading; a positive antigen arm would extend `proposition:0022` (persistence + bioactivity) to a new readout (IP-10 induction), but only the interventional `question:0002` test speaks to whether clearing it rescues the phenotype.

## New Questions Raised

- None minted. The interventional follow-through is already owned (h0019 P3; h0002 `question:0002`), and the cohort/assay need is q0076's. A candidate sub-question — *does the vaccine-primed IL-15–IFN-γ–IP-10 axis confound persistent-IP-10 attribution?* — is flagged for a future scope decision, not created, to avoid entity proliferation.

## User Questions

None raised during this design.

## Limitations & Residual Uncertainty

- **Correlational, not identifying.** The panel measures association/mediation; mediation ≠ causation, and a shared unmeasured upstream driver could load both arms. Leading with the floor: **the best achievable panel result is "which arm's markers accompany IP-10," not "which arm causes it."** The decisive test is interventional.
- **Not mutually exclusive.** h0019 and h0002 can co-operate (q0076); the panel is built to estimate *relative contribution*, and a two-positive result is a real, expected outcome — not a failure of the design.
- **Assay maturity is the binding constraint.** The most *specific* sterile-sensing markers (cGAMP, phospho-TBK1/IRF3, GSDMD-N) are labile, low-abundance, and demand fresh-PBMC or mass-spec workflows; the *practical* readouts (SIGLEC-1/CD169, IL-18, cell-free mtDNA, IP-10, Simoa antigen, ddPCR sgRNA) carry most of the discriminating weight. A blood-only panel restricted to practical markers can still resolve the **interferon-class axis** and the **antigen-presence** axis — the two load-bearing discriminators — even if the direct cGAS-STING second-messenger readouts are unavailable.
- **Compartment mismatch.** Both the sterile loop and the antigen reservoir may be **tissue-localized** (gut, lymph node, endothelium) and under-represented in blood; a negative blood panel does not exclude a tissue-confined driver. A tissue substudy is ideal but invasive and out of seed-stage reach.
- **Timing.** The h0019 signal is *temporal dissociation* (IP-10 persisting past antigen clearance); a single cross-section cannot show it — longitudinal sampling across the 6–8-month window is required, with antigen measured at each point.
- **Seed-stage / scope.** This is a **banked design**, not an authorized line. It requires a mild-Omicron-breakthrough cohort with stored longitudinal PBMC + plasma (+ optional tissue) and consent for antigen/nucleic-acid assays; it is **not** a `D-005` computational line and mints no analysis. Vacharathit2025's cohort (n≈30, confidential data) is too small and access-restricted to be the vehicle.

## Updated Priorities

- **Close t128** as done, with this interpretation as the design rollup; no reopening.
- **`question:0076` stays open**, now with an executable discriminating protocol and its identifiability ceiling made explicit.
- **No new analysis authorized.** The panel is design residue; its interventional follow-through (h0019 P3 sensor-selective inhibitor; h0002 `question:0002` antigen clearance) remains the decisive — and separately unfunded/seed-gated — test.
