---
id: interpretation:0040-t107-hspc-epigenomics-feasibility-banked-pbmc
kind: interpretation
title: "t107/q0055: opportunistic retrospective HSPC-epigenomics is feasible from banked PAIS PBMC only after a target pivot — GO on monocyte-progeny ATAC-seq, circulating-CD34 ATAC marginal + compartment-mismatched, true-HSPC test needs LIINC banked marrow"
status: active
source_refs:
- cite:Cheong2023
- cite:Corces2017
- cite:Desoutter2019
- cite:Horwitz2023
- cite:Lacerda2018
related:
- task:t107
- question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- topic:innate-immune-memory-trained-immunity-in-pais
- hypothesis:0001-shared-dysregulated-attractor
- interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk
created: '2026-07-10'
updated: '2026-07-10'
input: "Cell-number + specimen-access feasibility triage of q0055's direct test (does HSPC epigenomic imprinting depth predict PAIS persistence?) as an *opportunistic retrospective* study on already-banked PAIS-cohort blood — no new trial. Two grounded literature sweeps: (1) circulating-CD34+ HSPC frequency, ATAC-seq input floors across platforms, and cryopreserved-PBMC recovery/integrity; (2) what biospecimens the major PAIS cohorts (RECOVER, LIINC, UK ME/CFS Biobank, PHOSP-COVID, Cornell/Hanson, MY-LC, NIH intramural) actually bank and their realistic access model. Anchored to Cheong2023 (the imprint being tested, and its transmission to monocyte progeny), Corces2017 (frozen-optimized low-input Omni-ATAC), Desoutter2019 (CD34 preferential thaw apoptosis + granulocyte debris), Horwitz2023 (RECOVER protocol), Lacerda2018 (UK ME/CFS Biobank). No participant data; no assay run. Conceptual/feasibility-grade."
prior_interpretations:
- interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk
relations: []
---
<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE (t107, deliverable for q0055). Cell-number + specimen-access
go/no-go only; no participant-level data, no assay run, no cohort specimen in hand. No evidence-lines or
belief updates on any proposition are minted — this assesses whether the *direct* HSPC-imprint test q0055
names is *buildable opportunistically*, not what it would find. Sibling to interpretation:0039, which
refuted the serum-IL-6 *proxy* shortcut and pointed here (the direct-epigenomic route). -->

# Interpretation: t107/q0055 — opportunistic HSPC-epigenomics feasibility from banked PAIS PBMC

## Verdict

**Verdict:** [~] **CONDITIONAL GO — feasible only after a target pivot.** An opportunistic retrospective
epigenomic test of the HSPC-imprinting hypothesis (q0055) *is* buildable on already-banked PAIS blood with
no new trial — but **not** at the target as literally written ("ATAC-seq of circulating HSPCs from archived
PBMCs"). Three substrates, sharply different feasibility:

1. **Circulating CD34⁺ HSPC ATAC-seq from banked PBMC — MARGINAL and a weak proxy.** Circulating CD34⁺ are
   **0.01–0.1 % of PBMC** (central ~0.05 %), so a typical 5–10 × 10⁶-cell banked vial holds only
   ~1,000–10,000 CD34⁺ *before* losses; after CD34-preferential thaw apoptosis [@Desoutter2019] and
   small-scale sort recovery (~50–70 %), realistic net yield is **a few hundred to ~2,000 HSPCs per vial**.
   That supports **bulk low-input / Omni-ATAC from a single vial** [@Corces2017] but **not** droplet
   scATAC or Multiome (which need a few thousand *viable nuclei* loaded) without **pooling multiple vials**.
   And peripheral CD34⁺ are a **compartment-mismatched** stand-in for the **bone-marrow** HSPCs Cheong2023
   actually imprinted [@Cheong2023] — even a clean result is an indirect read on the marrow imprint.

2. **Monocyte-progeny (CD14⁺) ATAC-seq from banked PBMC — FEASIBLE and the recommended first move.**
   Monocytes are **~10–20 % of PBMC** (>10⁶ per vial) — no rarity constraint, every ATAC platform in
   reach (bulk, scATAC, Multiome). Crucially this is **not a consolation target**: Cheong2023's central
   finding is that the HSPC imprint is **transmitted to and read out in the monocyte progeny**
   [@Cheong2023], which is also the **q0026 effector locus** (hyperreactive monocytes sustaining PAIS
   inflammation). The monocyte epigenome is the **causally downstream, functionally decisive** readout —
   one step removed from the HSPC source, but the step that matters for symptoms.

3. **Marrow HSPC ATAC-seq — the definitive test — exists in exactly one PAIS biobank.** Only **LIINC's
   banked bone marrow** provides HSPC-rich, same-compartment material matching Cheong2023; access is
   **consortium/LCRC-mediated**, not open-application.

**Access is not the binding constraint for the top tier.** RECOVER (open Biospecimen-Access-Committee
application, viable PBMC, longitudinal 0/90/180 d + yearly to ~4 y, full acute-severity spectrum
[@Horwitz2023]) and the **UK ME/CFS Biobank** (open cost-reimbursement, ~20 PBMC aliquots/contact, 4–6
timepoints [@Lacerda2018]) are both realistically obtainable by an outside investigator. The binding
constraints are **cell-number/compartment** (above) and **severity selection** (below), not specimen access.

## Findings Summary

Substrate-level feasibility triage. The decisive axis is not access but **how many usable cells the target
compartment yields from a frozen vial, and how faithful that compartment is to the Cheong2023 imprint:**

| Target substrate | Abundance in PBMC | Net usable cells / banked vial | ATAC platform in reach | Fidelity to Cheong2023 imprint | Best cohort / access |
|---|---|---|---|---|---|
| **Circulating CD34⁺ HSPC** (FACS/MACS-sorted) | 0.01–0.1 % (~0.05 %) | ~a few hundred–2,000 (after thaw + sort loss) | bulk low-input / **Omni-ATAC single vial**; scATAC/Multiome only by **pooling vials** | **Partial** — peripheral CD34⁺ ≠ marrow HSPC (compartment mismatch) | RECOVER / UK ME/CFS Biobank (**open**) |
| **Monocyte progeny** (CD14⁺-gated) | ~10–20 % | >10⁶ — abundant | **any** (bulk, scATAC, Multiome) | **High for the *functional* imprint** — Cheong2023 shows transmission to monocytes; = q0026 effector | RECOVER / UK ME/CFS Biobank (**open**) |
| **Marrow HSPC** (banked bone marrow) | HSPC-rich | ample | **any** | **Highest** — same compartment as Cheong2023 | **LIINC only** (consortium/LCRC) |

Axis findings:

- **Cell number, not access, is the binding constraint — and it forces the pivot.** The circulating-HSPC
  route sits at the very floor of what bulk ATAC can do and *below* the floor for single-cell platforms
  from one vial. Omni-ATAC was purpose-built for **frozen input** and is demonstrated down to ~200 cells
  [@Corces2017], which is what keeps single-vial bulk *just* feasible; droplet scATAC/Multiome need a few
  thousand viable nuclei loaded (target ~10 k, kept ≤7,500 to limit multiplets), unreachable from ~0.05 %
  of one vial without pooling. The monocyte route erases this constraint entirely (>10⁶ cells/vial).
- **Cryopreservation is not itself disqualifying — but it biases *against* the HSPC target specifically.**
  Chromatin-accessibility data from frozen cells recapitulates fresh (Omni-ATAC and frozen-Treg
  demonstrations) [@Corces2017]. However CD34⁺ cells are **preferentially apoptotic on thaw** — ~23 %
  caspase⁺ vs ~12 % for CD3⁺ lymphocytes — and **granulocyte lysis drives that damage and adds ambient
  debris/background** [@Desoutter2019]. So the freeze-thaw penalty falls **hardest on the rare population
  we can least afford to lose**, and mandates dead-cell/granulocyte depletion before sorting. Monocytes,
  abundant and hardier, absorb this penalty easily.
- **The compartment the imprint lives in is only banked by LIINC.** Cheong2023 measured **bone-marrow**
  HSPCs and their monocyte output [@Cheong2023]. No PAIS cohort banks *sorted* HSPCs, and peripheral CD34⁺
  are a different compartment from marrow HSPC. The only same-compartment substrate in any PAIS biobank is
  **LIINC's bone-marrow tissue arm** — highest scientific fidelity, highest access friction (LCRC/PolyBio
  collaboration, no open portal).
- **Severity selection is the inherited design trap.** Cheong2023's imprint was shown **only in
  severe/hospitalized COVID**, yet long COVID arises predominantly after **mild** acute disease — the same
  severity-through-line that sank the serum-IL-6 proxy in `interpretation:0039`. An opportunistic study
  must therefore **span the acute-severity spectrum** to separate "imprint tracks PAIS" from "imprint
  tracks acute severity." This **favors RECOVER** (full spectrum) and **disfavors PHOSP-COVID**
  (hospitalized-only ⇒ severity-confounded, and only two timepoints).

## Evidence Quality

Feasibility-grade, grounded in method + cohort primary sources; two literature sweeps, no assay run.

- **Cheong2023** [@Cheong2023] is load-bearing twice over: it defines the imprint under test *and* supplies
  the pivot's justification (imprint transmitted to monocyte progeny), so the monocyte route is a faithful,
  not a fallback, readout. It is also the source of the severity bound.
- **Corces2017** [@Corces2017] is the decision-critical method anchor: the ~200-cell frozen-optimized
  Omni-ATAC floor is exactly what determines whether a single banked vial's HSPC yield clears the bar
  (marginally, yes for bulk; no for single-cell).
- **Desoutter2019** [@Desoutter2019] carries the single most HSPC-specific hazard — preferential CD34⁺
  thaw apoptosis with a granulocyte-driven mechanism — which is why the freeze-thaw penalty is not
  compartment-neutral.
- **Horwitz2023** [@Horwitz2023] and **Lacerda2018** [@Lacerda2018] anchor the access verdict for the two
  realistically-obtainable cohorts (open BAC application; open cost-reimbursement, documented ~20-PBMC-vial
  allocation).
- **Boundary (honest):** the CD34-recovery and enrichment-yield figures the arithmetic leans on come
  substantially from **clinical apheresis HPC products**, which are far larger and more cryoprotectant-
  optimized than research PBMC vials, and therefore likely **overstate** achievable recovery from small
  biobank aliquots — the yield estimate is deliberately weighted to the conservative end. Precise
  per-aliquot cell counts for RECOVER/LIINC/PHOSP are **[UNVERIFIED]** (not in the reachable public
  protocol text; the RECOVER medRxiv PDF returned HTTP 403) and must be confirmed with each biorepository
  before a yield is committed.

## Data Quality Checks

Not an empirical-results interpretation; no dataset QA was run. The relevant "data-quality" facts are
structural feasibility hazards feeding the design:

- **CD34 rarity sets the input floor** (~0.05 % of PBMC) — the dominant constraint on the literal-HSPC route.
- **CD34-preferential thaw apoptosis** (~23 % vs ~12 %) + **granulocyte-driven debris/ambient background**
  [@Desoutter2019] — lowers effective HSPC recovery *and* biases the survivors toward the hardier subset;
  mandates dead-cell/granulocyte depletion pre-sort.
- **Compartment mismatch:** peripheral circulating CD34⁺ vs marrow HSPC (the Cheong2023 substrate) — a
  fidelity hazard the monocyte route sidesteps (it reads the *transmitted* imprint) and only LIINC marrow
  fully resolves.
- **Per-aliquot cell counts [UNVERIFIED]** — biorepository protocols do not publish vial cell counts;
  confirm with the RECOVER BAC / UK ME/CFS Biobank before finalizing yield.
- **Severity-selection confound:** Cheong2023 severe-only; PAIS mostly post-mild — the study must span the
  severity spectrum or it re-runs the confound that defeated the serum-IL-6 proxy (`interpretation:0039`).

No data-quality concerns of the empirical kind identified (there is no data); these are enumerated as
methodological findings for the design.

## Proposition-Level Updates

None. This is a buildability verdict, not an endpoint result; no `proposition:` gains or loses an
evidence-line, and no belief on `hypothesis:0001` (or on the q0026/trained-immunity circuit) moves. It
establishes only that the direct HSPC-imprint test is opportunistically constructible — and cheapest and
most decisive as a **monocyte-progeny** assay — not what that assay would find. (Same discipline as
interpretation:0036 and interpretation:0039: proxy/feasibility work mints no belief updates.)

## Hypothesis-Level Implications

- **question:0055 — the direct test it names is buildable, with a target pivot; it stays `active`.** q0055
  asks whether HSPC imprinting depth predicts PAIS persistence and flags that "circulating HSPC frequency
  is low … or bone marrow aspirates are required." This triage confirms that worry and resolves it: the
  low-yield literal route is marginal and compartment-mismatched, so the **feasible high-leverage version
  is monocyte-progeny ATAC-seq** (the transmitted imprint / q0026 effector), and the **definitive
  same-compartment version requires LIINC banked marrow**. The empirical question is untouched.
- **hypothesis:0001 — a concrete opportunistic route to test the HSPC-imprint attractor-maintenance
  mechanism now exists**, moving it from "needs a prospective marrow study" to "testable on banked RECOVER/
  UK-ME-CFS PBMC via the monocyte readout." No belief update — the *route to adjudication* is the deliverable.
- **question:0026 — the effector-locus prediction is the one that is cheaply testable.** Because the pivot
  target (monocyte epigenome) *is* the q0026 locus, an opportunistic banked-PBMC assay tests the
  q0026 hyperreactive-monocyte prediction directly, severity-stratified — the direct-epigenomic test
  `interpretation:0039` said the serum-IL-6 proxy could not perform.

## Evidence vs. Open Questions

- **question:0055 — feasibility gate cleared (conditional GO); empirical question open.** Whether imprint
  depth predicts persistence is unanswered; the vehicle to answer it opportunistically is now specified.
- **question:0026 — direct route specified.** The hyperreactive-monocyte-imprint prediction is testable on
  banked PBMC (monocyte ATAC-seq, severity-matched); no result yet.
- **hypothesis:0001 — unchanged standing**, now with a costed-to-first-approximation opportunistic test.

## New Questions Raised

- **(feasibility/access, P2):** Can a LIINC/LCRC (PolyBio) collaboration be secured to reach the **banked
  bone-marrow** arm — the only same-compartment HSPC substrate — or should the design commit to the
  monocyte-progeny readout as its permanent feasible form? *Not reserved as a standalone `question:`* — it
  is a design fork for q0055, folded into Updated Priorities.
- **(design, P2):** What is the minimum severity-stratified per-arm N (PAIS-persistent vs recovered, both
  infected, spanning mild→severe acute) for a monocyte-ATAC imprint-depth contrast to clear an
  *arbitrating* bar rather than a Monte-Carlo one? Ties to the same power/bias-floor concern raised in
  interpretation:0036 (#4) and interpretation:0037.
- **(operational, P3):** Confirm actual per-aliquot viable-cell counts and number of banked PBMC vials/
  timepoint with the RECOVER BAC and the UK ME/CFS Biobank — the [UNVERIFIED] number that decides whether
  single-cell (vs bulk) monocyte ATAC, and any circulating-CD34 sort, is on the table without pooling.

## Limitations & Residual Uncertainty

- **Per-aliquot cell counts are [UNVERIFIED].** The whole single-vial-vs-pooling boundary rests on an
  assumed ~5–10 × 10⁶-cell vial; biorepositories do not publish this and it must be confirmed.
- **Recovery figures are apheresis-biased (optimistic).** CD34 recovery/enrichment yields are drawn largely
  from clinical HPC products; research vials will likely do worse, so the circulating-HSPC route may be
  *more* marginal than the central estimate.
- **The monocyte readout is one step removed from the HSPC source.** It faithfully reports the *transmitted*
  imprint (Cheong2023) and the q0026 effector state, but cannot by itself localize whether a difference
  originates in the HSPC compartment vs peripheral monocyte reprogramming — only the LIINC marrow arm can.
- **Severity confound is designed-around, not eliminated.** Spanning the severity spectrum is necessary but
  not sufficient; residual confounding by acute severity remains the dominant interpretive threat, exactly
  as in interpretation:0039.
- **This is a feasibility verdict, not a protocol.** No IRB, sort panel, ATAC chemistry, per-arm N, or
  power calculation is committed here; the GO licenses drafting those, not skipping them.

## Updated Priorities

1. **Adopt the target pivot as the operative form of q0055's direct test:** primary readout =
   **monocyte-progeny (CD14⁺) ATAC-seq from banked PBMC** (abundant, all-platform, the transmitted imprint
   and q0026 effector locus). This is the feasible, high-leverage opportunistic analysis the serum-IL-6
   negative (interpretation:0039) pointed to.
2. **Source it from RECOVER first** (open BAC application; viable PBMC; longitudinal 0/90/180 d + yearly;
   **full acute-severity spectrum** — the design-critical property [@Horwitz2023]); **UK ME/CFS Biobank** as
   the ME/CFS-arm parallel (open cost-reimbursement, documented ~20 PBMC vials/contact [@Lacerda2018]).
3. **Design the contrast severity-stratified and within-trigger** (PAIS-persistent vs infected-recovered,
   both spanning mild→severe) so imprint-depth is estimated orthogonal to acute severity — not adjusted
   post hoc.
4. **Pursue a LIINC/LCRC collaboration in parallel for the bone-marrow arm** as the definitive
   same-compartment confirmation, accepting the consortium-access friction; treat it as the Tier-2
   fidelity check on a positive monocyte result.
5. **Confirm per-aliquot viable-cell counts with the biorepositories before committing** to single-cell
   (vs bulk) monocyte ATAC or any circulating-CD34 sort — the [UNVERIFIED] number that sets the platform.
6. **Do not pursue circulating-CD34⁺ ATAC as the primary readout, and do not use PHOSP-COVID as the primary
   cohort** — recorded as explicit non-choices (marginal yield + compartment mismatch; hospitalized-only
   severity confound + two timepoints, respectively) so they are not re-proposed.
