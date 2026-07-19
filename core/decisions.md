<!--
core/decisions.md — load-bearing decisions and the reasoning behind them.
Loaded at session start via AGENTS.md.

Length cap: ~150 lines. When the file outgrows that, move older entries
to doc/decisions/ and keep only the still-load-bearing ones here.

This file is APPEND-ONLY for individual decisions. Do not rewrite a
decision when it is later superseded — add a new entry that references and
supersedes the old one, and update the "Status" line on the original.

Each entry follows the format below. Number entries sequentially.
-->

# Decisions

## D-001: Split post-acute infection syndromes out as their own process project

- **Date:** 2026-06-10 · **Status:** active · **Full reasoning:** `doc/decisions/D-001.md`
- **Decision:** PAIS (long COVID, ME/CFS, PTLDS, post-dengue/Q-fever, post-SARS, PICS) are modeled as a dedicated `process` project under `~/d/health/processes/post-acute-infection`, separate from `health-immunity`. Clinical post-infectious-syndrome work lives here; general immune-mechanism / autoimmunity / tolerance → `health-immunity`; frame-changing cross-project conclusions → `health-meta`; disease-label-vs-biology → `pan-disease`; bridging papers are summarized once and shared via `science commons promote`.

## D-002: Adopt pacing as the default activity-management frame; treat incremental GET as contraindicated where PEM is present

- **Date:** 2026-06-20 · **Status:** active · **Full reasoning:** `doc/decisions/D-002.md`
- **Decision:** For PEM-positive PAIS phenotypes, adopt **pacing / energy-management** (symptom-titrated activity within an energy envelope) as the default activity frame, and treat fixed-increment / deconditioning-model **GET** as **contraindicated**; flag any therapy/trial/endpoint relying on incremental GET in a PEM-positive population as methodologically contested. Provoked-exertion diagnostics (2-day CPET, iCPET) remain endorsed under PEM-crash-risk consent. The stance is **PEM-specific** — always stratify PEM-positive vs PEM-absent before applying.

## D-003: Post-infectious trigger is the in-scope rule; PACVS and GWS/fibromyalgia are boundary-monitor / read-across, not primary scope

- **Date:** 2026-06-21 · **Status:** active · **Full reasoning:** `doc/decisions/D-003.md`
- **Decision:** `hypothesis:0001`'s shared attractor is **post-infection-specific for primary scope**; the inclusion rule is **trigger-type — a syndrome is in primary scope only if its trigger is an acute infection.** Two classes that fail it are **boundary-monitor / read-across** (mechanism evidence to stress-test cross-trigger claims, never counted as PAIS cases or as independent cross-trigger support for `hypothesis:0001`): (a) **PACVS** (lowest evidence tier; monitor the same-antigen/different-route discriminator) and (b) **non-infectious GWS / FM** (mainstream-tier; the best non-infectious stress-test — any GWS/FM-leaning convergence claim must be labelled a *non-infectious* read-across). Recorded in `specs/scope-boundaries.md`.

## D-004: Shelve the autoimmune × sex × PASC vehicle-based estimand as infeasible-under-transparency-standards

- **Date:** 2026-07-01 · **Status:** active · **Full reasoning:** `doc/decisions/D-004.md`
- **Supersedes:** the operative "N3C primary" verdict in `interpretation:0031` (marked SUPERSEDED).
- **Decision:** The `task:t078`/`t079` autoimmune × sex × PASC effect-modifier estimand is **shelved, not executed** — it needs population-scale individual-level patient EHR, a **categorically access-gated, non-downloadable data class** (N3C enclave-only even at the synthetic tier; OpenSAFELY insider-only aggregate-output). No admissible vehicle makes it **third-party-reproducible** (the D-004 transparency bar; the problem is the data class, not the vehicle). The **design residue is banked** — two-estimand contrast, DAGs, adjustment/negative-control/bracketing design, and the `hypothesis:0008` measurement/ascertainment synthesis remain reusable.

## D-005: Authorize only the Wave-1 open GWAS/MR pilot as the first post-seed computational analysis

- **Date:** 2026-07-04
- **Status:** active
- **Extended by:** D-006 (2026-07-04) — clarifies that reportable-grade promotion of this vehicle (`plan:0008`) is in-scope "direct maintenance", and holds FinnGen as a distinct vehicle.
- **Decision:** The project may cross the `specs/scope-boundaries.md` seed-stage boundary for the **specific Wave-1 GWAS/MR pilot** described in `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`: two-sample MR over the three cataloged public GWAS summary-statistic vehicles (`dataset:covid19-hgi-longcovid-gwas`, `dataset:bentham-2015-sle-gwas`, and `dataset:ruth-2020-shbg-testosterone-gwas`), with IVW primary and the pre-committed sensitivity/bridge-assumption checklist in that handoff.
This decision authorizes planning and implementation of that open, third-party-reproducible pilot only.
It does **not** authorize gated-data analysis, patient-level EHR analysis, N3C/OpenSAFELY execution, or a general transition to unrestricted computational pipeline work.

**Why:**
The scope boundary was written to prevent premature large-scale analysis while the project was still establishing its literature and hypothesis frame.
The Wave-1 data-catalog arc now supplies a narrow, auditable, third-party-reproducible vehicle: public summary statistics with resolvable accessions, explicit dataset entities, declared capabilities, and a handoff contract that separates cataloging from execution.
That vehicle clears the transparency objection behind D-004 because arbitrary third parties can retrieve the same public summary-statistic inputs and rerun the intended analysis.
The scientific estimand is also narrower than the shelved autoimmune x sex x PASC EHR line: it is a germline-liability instrumental-variable effect under MR assumptions, not an individual-level diagnosis/treatment/ascertainment-structured effect and not a reconstruction of the D-004 estimand.

**Alternatives considered and rejected:**
- Keep the project fully at seed-stage literature synthesis — rejected because it would treat a fully open, deliberately constrained empirical pilot the same as gated EHR execution, losing a useful reproducible test without reducing a real transparency risk.
- Declare the project generally "past seed stage" for computational work — rejected as too broad.
The current authorization is intentionally vehicle-specific; future computational lines need their own scope decision unless they are direct maintenance of this pilot.
- Reopen the N3C/OpenSAFELY EHR path under the same ruling — rejected.
D-004 still governs gated, non-downloadable EHR vehicles and remains unchanged.

**Implications:**
- `task:t088` is resolved for the Wave-1 MR vehicle.
- `task:t089` may move to the `/science:plan-pipeline` handoff for this pilot.
- Pipeline planning must preserve the handoff's constraints: public retrievable inputs, recorded hashes/datapackages for staged files, ancestry/case-definition/sample-overlap/HLA sensitivity checks, and interpretation only as germline-liability IV evidence.
- Any additional computational analysis line beyond this Wave-1 vehicle requires a separate scope decision unless a future decision explicitly broadens this ruling.

**Revisit if:**
- A planned step needs non-public, credentialed, enclave-only, or non-downloadable data; the MR estimand is expanded toward the D-004-shelved EHR estimand; or the pilot design drops below the project's third-party-reproducible bar.

## D-006: Wave-1 MR reportable-grade promotion (plan:0008) is direct maintenance of the D-005 pilot; FinnGen held as a distinct vehicle

- **Date:** 2026-07-04
- **Status:** active
- **Extends:** D-005 (does not supersede). Discharges `plan:0008` WP0 (the authorisation scope gate).
- **Decision:** The reportable-grade Wave-1 MR design (`plan:0008`) is **direct maintenance of the D-005-authorised pilot vehicle**, not a new computational line, and needs no separate scope authorisation for its primary path. Classifying each input `plan:0008` adds beyond the three D-005 vehicles:
  - **(a) EUR-matched long-COVID outcome — in-scope (same vehicle).** Sourcing a European-ancestry long-COVID **outcome** from the **Long COVID HGI** distribution — the DF4 freeze via LocusZoom (`my.locuszoom.org/gwas/793752/`, "Long COVID HGI – DF4 N1", GRCh38, publicly downloadable without registration), the `covid19hg.org/results` portal, or a GWAS Catalog EUR stratum — is the **same measured-phenotype vehicle** as the D-005-authorised `dataset:covid19-hgi-longcovid-gwas`, in a different freeze/channel. Whether a genuinely EUR-specific stratum exists within that vehicle is a **WP1 factual question**, not presumed here; if none does, `plan:0008` KD1's demotion-to-mechanics-only applies.
  - **(b) LD-score + HapMap3 references — in-scope (infrastructure).** The `eur_w_ld_chr` EUR LD-score reference and the HapMap3 SNP list that the MRlap overlap correction requires are **analysis infrastructure**, the same class as the LD reference panel (`dataset:1000g-eur-ld-panel`) the D-005 pilot already used for clumping — not measured-phenotype vehicles.
  - **(c) FinnGen long-COVID — held (distinct vehicle).** FinnGen (`plan:0008` KD1 rung 3) is a **distinct measured-phenotype vehicle**, not the HGI vehicle. It may **not** be used until (i) a separate decision broadens scope to it **and** (ii) its results-access path is confirmed to clear the third-party-reproducible bar (the `finngen.fi` form/email-mediated access is unverified against that bar). Because (a)/(b) are expected to satisfy the EUR-outcome need, FinnGen stays a contingency and is **not** authorised here.

**Why:**
D-005 already contemplates "direct maintenance of this pilot" as not needing a fresh scope decision, and names the HGI long-COVID GWAS as an authorised vehicle. Promoting the pilot to reportable grade reuses that same vehicle (a different HGI freeze is the same public data source) plus LD-reference infrastructure of the kind the pilot already used. The only genuinely new vehicle — FinnGen — is the only element that would need fresh authorisation, and it is held rather than used. Every authorised input remains public and third-party-retrievable, so the D-004 transparency bar is intact.

**Alternatives considered and rejected:**
- Treat `plan:0008` as a wholly new computational line needing full re-authorisation — rejected as over-ceremony; it is the same vehicle promoted, which D-005 already covers as maintenance.
- Pre-authorise FinnGen as a drop-in rung — rejected; distinct vehicle, unverified access path, and unnecessary if the HGI vehicle yields a EUR stratum.
- Rewrite D-005 in place — rejected; `decisions.md` is append-only, so this extends D-005 via a new entry.

**Implications:**
- `plan:0008` WP0 is discharged; WP1 (acquire the HGI EUR distribution) and WP2 (stage `eur_w_ld_chr` + HapMap3) may proceed.
- Any use of FinnGen — or any other non-HGI outcome vehicle — requires a new decision plus a reproducibility-class check first.
- If WP1 finds no EUR-specific HGI stratum, the ancestry hard-stop is not lifted and `plan:0008` KD1 demotes the primary to mechanics/robustness-only.

**Revisit if:**
- No EUR outcome can be sourced from the HGI vehicle and FinnGen (or another vehicle) becomes necessary; or any authorised input's access path drops below the third-party-reproducible bar.

## D-007: Authorize the atopy→long-COVID MR *feasibility packet* only (public sumstats); MR execution gated on a follow-up ratification

- **Date:** 2026-07-18
- **Status:** active
- **Extends:** D-005 (does not supersede). Applies the 2026-07-18 ruling that a **new exposure** against the authorised HGI outcome is a new computational line requiring a fresh D-005 decision (not D-006 maintenance).
- **Decision:** The project may run the **feasibility packet** for an atopy→long-COVID two-sample MR — `dataset:gcst005038-allergic-disease-gwas` (exposure) × `dataset:covid19-hgi-longcovid-gwas` (outcome): (1) instrument construction/clumping, (2) empirical **liability-scale** instrument R², (3) UKB↔HGI **sample-overlap** quantification, (4) binary-exposure **scale** definition — all on public summary statistics. This authorises the feasibility/screening work **only**. MR **execution** (IVW-primary + sensitivity checklist) is **not** authorised here and needs a **follow-up ratification (D-007b)** once the packet clears pre-registered thresholds. The outcome's ancestry status is the **same WP1 question** as `plan:0008` KD1 / D-006(a); if no EUR-specific HGI stratum exists, any eventual estimate inherits the **mechanics/robustness-only demotion** — this is not a reportable-primary MR vehicle on the current outcome file.

**Why:**
The 2026-07-18 power screen left atopy as the only surviving MR candidate among the t110 boundary-strata instruments, but a *provisional* survivor with four undischarged, public-data prerequisites. Those prerequisites are the cheap, transparent work that turns "provisional" into a decidable yes/no; authorising them and only them tests feasibility without pre-committing to an execution whose reportable status is already ancestry-capped. Every input is public and third-party-retrievable (D-004 intact), and the estimand is the same germline-liability IV class D-005 authorised.

**Alternatives considered and rejected:**
- Authorise the full line (feasibility + execution) now — rejected as premature: reportable status is ancestry-capped, and three of four prerequisites (R², overlap, scale) could still sink the line; execution authorisation should follow the evidence.
- Decline/defer all effort until a EUR-matched outcome exists — rejected: the packet is cheap, fully public, and its outputs (instrument strength, overlap, scale) are reusable whenever a matched outcome appears; deferring discards that at no transparency saving.
- Treat it as D-006-style maintenance needing no decision — rejected: it adds a new exposure vehicle, which the recorded ruling classes as a new line.

**Implications:**
- `task:t135` is resolved (scope decision taken): feasibility-only authorised, execution deferred.
- A feasibility-packet task carries the four deliverables; its outputs are the go/no-go inputs for the D-007b execution ratification.
- Scope of estimand: this vehicle speaks only to **broad allergic-disease liability**, not q0034's stronger atopy/MCAS-subgroup question. No gated data, no execution, no new outcome vehicle authorised.

**Revisit if:**
- The packet clears thresholds (→ raise D-007b for execution); or the R²/overlap/scale work shows the line cannot detect the pre-registered floor (OR≳1.2) (→ shelve atopy too); or a EUR-matched HGI outcome becomes available (→ revisit the ancestry cap).

## D-008: Authorize the frailty signature-projection *feasibility packet* only (public scRNA/bulk-RNA); full projection gated on a follow-up ratification

- **Date:** 2026-07-18
- **Status:** active
- **Extends:** D-005 (does not supersede). A **new-modality** computational line (scRNA/bulk signature learning + cross-platform projection) — distinct from the D-005/D-006 MR vehicle and from D-007's atopy MR — so it takes its own scope decision. Resolves `task:t138`.
- **Decision:** The project may run a **feasibility packet** for the frailty × PAIS signature-projection line: learn a frailty immune signature from `dataset:gse157007-aging-frailty-pbmc-scrna` (scRNA frail-vs-healthy-old baseline) and/or `dataset:gse196793-frailty-influenza-vaccine-pbmc` (bulk RNA, Fried-phenotype × timed vaccine challenge), then project it onto the project's existing **public** long-COVID / ME-CFS transcriptomic deposits — on public GEO data only. This authorises the feasibility/screening work **only**. A **reportable** frailty×PAIS projection result is **not** authorised here; it is gated on a follow-up ratification (**D-008b**) once the packet clears the five pre-registered gates below. This is the **only DUA-free route** to a frailty×PAIS contrast (both frailty vehicles lack an infection arm; the PAIS deposits lack frailty labels), so a learn-here / score-there projection is structurally required — and therefore structurally at risk of cross-platform artifact, which is exactly what the packet must rule out before any result stands.
- **Feasibility-packet gates (all five must pass for a GO → D-008b):**
  1. **Training power + labels** — donor-level N and the frailty ascertainment (Fried 5-item vs source-study definition) are sufficient and stated explicitly; the small frail-n (GSE157007: 5 frail / 17 donors) is a hard power question, not a footnote.
  2. **Feature compatibility** — the signature's cell types / genes are measurable in *both* the training layer (scRNA / bulk) and the target PAIS deposits (bulk); pseudobulk and feature-intersection choices are frozen before projection.
  3. **Cross-cohort validation + batch/platform robustness** — the signature validates across the two frailty vehicles (or across held-out donors) and survives platform transfer (scRNA→bulk, cross-instrument batch); a signature that only reproduces within one platform fails.
  4. **Negative-control projections** — the signature is projected onto matched non-frailty / permuted-label / unrelated-axis controls and must separate frailty from those, or the projection is uninterpretable.
  5. **Explicit non-causal framing** — every output is a cross-sectional signature-overlap association, never a frailty→PAIS causal effect; D-003 additionally bars counting GSE196793's vaccine challenge as a PAIS case.

**Why:**
Frailty is the best biology of the three t110 boundary strata but the largest ask, and — unlike the IM and atopy MR lines — it has no summary-statistic shortcut: the signal only exists by learning on one platform and scoring on another. That transfer is the dominant failure mode (batch/platform confound masquerading as a frailty signal), and it is cheap to interrogate on fully public GEO data before committing to any reportable claim. Authorising the packet and only the packet tests whether a transferable, non-artifactual signature exists without pre-committing to a result; every input is public and third-party-retrievable (D-004 intact), and the five gates are the same "screen, not green-light" discipline that made t137 decidable.

**Alternatives considered and rejected:**
- Authorise the full projection now — rejected as premature: cross-platform artifact is the dominant, still-unassessed risk; the result's credibility *is* gates 3–4.
- Decline all effort until a frailty-labelled PAIS deposit exists — rejected: the packet is cheap, fully public, and the learned signature is reusable whenever such a deposit appears; deferring discards that at no transparency saving.
- Treat it as D-006-style maintenance — rejected: it is a new modality and new vehicles, which the recorded ruling classes as a new line.

**Implications:**
- `task:t138` is resolved (scope decision taken): feasibility-only authorised, full/reportable projection deferred to D-008b.
- A feasibility-packet task carries the five gates as deliverables; its outputs are the GO/NO-GO inputs to the D-008b ratification.
- Scope of estimand: a cross-sectional frailty-signature-overlap association in PAIS transcriptomes, not a causal frailty→PAIS effect; no gated data, no reportable claim, no new outcome vehicle authorised.

**Revisit if:**
- The packet clears all five gates (→ raise D-008b for reportable projection); or it fails on power/transfer/negative-control (→ shelve the frailty line too, at which point **no t110 boundary-strata line survives** and the boundary-conditions program closes on public data); or a PAIS deposit with native frailty labels appears (→ learn-there/score-here projection is no longer required).

## D-009: Vaccine-adverse-event papers are adjudicated by a trigger × persistence test; acute vaccine AEs (Nitz2025) are comparator-only, never a PAIS case

- **Date:** 2026-07-19
- **Status:** active
- **Extends:** D-003 (does not supersede) — adds the temporal (acute-vs-persistent) axis and the acute-vaccine cell D-003 never covered. Recorded operationally in `specs/scope-boundaries.md`.
- **Decision:** Admissibility of vaccine-adverse-event papers is decided on **two independent axes**, and **primary scope requires passing both**: (1) **trigger** — infection required (the D-003 rule; vaccination fails it); (2) **persistence** — >~12 weeks required (acute self-resolving events fail it). The two are not interchangeable: **persistence alone can never promote a vaccine-triggered phenotype to primary scope**, because the trigger axis still fails, so vaccine papers are capped at **boundary-monitor / read-across** regardless of persistence.
  - **Acute vaccine adverse events (`paper:Nitz2025` — myocarditis/pericarditis, VITT/anti-PF4, CVST) fail both axes** (onset ≤90 d, median ≤14 d, resolution within weeks; whole-literature follow-up ≤185 d) and are **not a syndrome**. They are **not a PAIS case, not boundary-monitor-as-a-PAIS-analog, and not independent cross-trigger support for `hypothesis:0001`** (same bar D-003 sets for PACVS/GWS). They are admitted **only as mechanistic / epidemiological comparators**: the infection-vs-vaccination CV risk asymmetry (~5–6× myocarditis, RR ~15–18.5 vs ~2–3.2) as a same-antigen antigen-burden anchor (`question:0081`, `proposition:0021`), and the acute-vaccine reference point bounding the same-antigen/different-route discriminator D-003 monitors.
  - **Persistent post-vaccination syndrome (PACVS; `paper:Bellavite2026`) fails only the trigger axis** and stays **boundary-monitor / read-across** per D-003.

**Why:**
D-003 fixed the trigger rule and placed PACVS/GWS as boundary-monitor, but never addressed *acute* vaccine adverse events, which are not a persistent syndrome at all. `paper:Nitz2025` (and `paper:Bellavite2026`) both carry scope notes asking for a single adjudication in `specs/scope-boundaries.md`. Separating the temporal axis from the trigger axis makes the ruling exhaustive (a clean 2×2), keeps the antigen-burden comparator value usable without smuggling vaccine data in as PAIS cases, and preserves D-003's bar on counting non-infectious triggers as `hypothesis:0001` support.

**Revisit if:**
- A **controlled longitudinal** study establishes a **persistent** (>12 wk) post-vaccination CV phenotype — it then moves into the PACVS cell (boundary-monitor at most, never primary scope, trigger axis still fails); or a **controlled PACVS-vs-PASC biomarker comparison** appears (the D-003 trigger to reconsider the PACVS cell itself).
