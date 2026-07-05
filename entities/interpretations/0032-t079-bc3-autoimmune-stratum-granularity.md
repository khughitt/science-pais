---
id: interpretation:0032-t079-bc3-autoimmune-stratum-granularity
kind: interpretation
title: "t079/BC-3: disease-specific autoimmune strata resolve in BOTH vehicles (fixes Hill's pooled-Charlson gap); autoimmune-thyroid is the convergent weak stratum"
status: active
source_refs:
  - paper:Hill2022
related:
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - dataset:n3c-recover-longcovid
  - dataset:opensafely-longcovid
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - question:0005-latent-to-overt-autoimmunity-conversion
created: "2026-07-01"
updated: "2026-07-01"
input: "BC-3 feasibility verification (2026-07-01): two parallel read-only vocabulary audits — OpenCodelists/NHSD SNOMED refsets for OpenSAFELY, and OMOP/SNOMED standard concepts + OHDSI Phenotype Library for N3C. No participant-level data accessed on either platform; ATHENA public API returned HTTP 403 so specific OMOP concept_ids remain unverified."
prior_interpretations:
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
relations: []
---

<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE (BC-3 of plan:0005 / task:t079). Vocabulary-resolvability
verdict only; no participant-level data, no cell counts (those are BC-4). -->

# Interpretation: t079/BC-3 — autoimmune stratum granularity

## Verdict

**BC-3's core premise holds: both vehicles resolve *disease-specific* autoimmune strata with
dated pre-index onset, so Hill2022's single pooled Charlson "rheumatologic disease" term can
be replaced by eight distinct strata.** This is a **vocabulary-resolvability** clearance, not
a cell-count clearance — whether each stratum × sex × PASC cell survives the power floor is
**BC-4**, still open. Seven of the eight strata are cleanly resolvable in both vehicles. The
one convergent exception is **autoimmune-thyroid disease**, which is hard to isolate from
all-cause thyroid dysfunction in *both* coding systems — a genuine exposure-misclassification
finding that lands directly on `plan:0005`'s Bias-vs-Variance section, not a codelist-existence
gap. Three strata (vasculitis, autoimmune-thyroid, myositis) require **a-priori scoping
decisions** that must be pre-registered before extraction.

## Findings Summary

Per-stratum resolvability across the two admissible vehicles (N3C primary, OpenSAFELY
replication — `interpretation:0031`):

| Stratum | N3C / OMOP concept set | OpenSAFELY / OpenCodelists | Prior status → now |
|---|---|---|---|
| **SLE** | OHDSI Phenotype Library cohort **#119** (chart-validated) | NHSD `slupus_cod` (official SNOMED refset); OpenSAFELY `ra-sle-psoriasis-snomed` | confirmed → **confirmed, library-backed** |
| **RA** | OHDSI Phenotype Library cohort **#196** | NHSD `rarth_cod`; `opensafely/rheumatoid-arthritis` | confirmed → **confirmed, library-backed** |
| **IBD** (Crohn's + UC) | OHDSI cohorts **#198** (Crohn's) + **#201** (UC), disease-specific | `opensafely/inflammatory-bowel-disease-snomed`; separable Crohn's + NHSD UC | confirmed → **confirmed, splittable** |
| **MS** | Standard SNOMED (24700007) → constructible; no library cohort | NHSD `multiple-sclerosis-snomed-ct`; `opensafely/multiple-sclerosis-v2` | confirmed → **confirmed** |
| **Sjögren's** | Standard SNOMED (83901003) → constructible; no library cohort | **NHSD `sjogrens_cod`** (official SNOMED refset) | `[UNVERIFIED]` → **CONFIRMED** |
| **Systemic vasculitis** | SNOMED family (GCA/GPA/MPA/PAN/Takayasu) → **union** of subtype sets | **subtype-union**: `gca_cod`, `wegenervasc_cod`, `polyarteritis_cod`, `takayasuart_cod`, `cryoglobvasc_cod` | `[UNVERIFIED]` → **CONFIRMED as a subtype union** (no umbrella list; a-priori scope needed) |
| **Inflammatory myositis** | SNOMED DM (396230008) / PM (31384009) → constructible | **NHSD `myositis_cod`** (PM+DM together) | `[UNVERIFIED]` → **CONFIRMED** |
| **Autoimmune thyroid** | SNOMED Hashimoto/Graves exist, **but must exclude all-cause hypothyroidism (E03)** | **Graves `gravesdis_cod` clean; NO autoimmune-hypothyroid refset** — only all-cause `thy_cod` | `[UNVERIFIED]` → **PARTIAL** (Graves clean; autoimmune-hypothyroid not isolable) |

**The autoimmune-thyroid convergence.** The two audits were independent and hit the *same*
wall from opposite sides: OpenSAFELY publishes a clean autoimmune-*hyper*thyroid (Graves)
refset but no autoimmune-specific *hypo*thyroid list (only the all-cause QOF register); N3C's
SNOMED/ICD-10-CM coding likewise separates Graves (E05, autoimmune) cleanly but buries
Hashimoto (E06.3) inside a much larger all-cause-hypothyroidism space (E03) that is
predominantly non-autoimmune. So in *both* vehicles the autoimmune-thyroid stratum is either
Graves-only (specific but low-sensitivity) or Graves + all-cause-hypothyroid (sensitive but
misclassified). This is the stratum most exposed to differential misclassification.

**Correction to a prior expectation.** The `dataset:opensafely-longcovid` note anticipated
vasculitis and myositis as the weak, hospital-only (ICD-10) cases. That was wrong: both are
well-served by SNOMED primary-care refsets with dated diagnosis events. The actual weak point
is autoimmune-hypothyroid granularity.

## Pre-registered pooling hierarchy (assigned)

`plan:0005` reserves an "organ-specific / systemic-rheumatic / genetic-risk-only" pooling
hierarchy as the fallback when a stratum falls below the BC-4 power floor. BC-3 fixes the
assignment:

- **Systemic-rheumatic / connective-tissue tier:** SLE, RA, Sjögren, systemic vasculitis,
  inflammatory myositis. (The pooled node the rarest of these collapse into.)
- **Organ-specific tier:** IBD (gut), MS (CNS), autoimmune-thyroid (thyroid).
- **Genetic-risk-only tier: NOT EHR-concept-set-resolvable — out of scope for BC-3.** A
  genetic-diathesis stratum (HLA / polygenic risk without an overt clinical diagnosis) lives
  in a *different data modality* (genotype), not diagnosis codes, and neither N3C nor
  OpenSAFELY resolves it from the condition tables this check covers. It is the latent→overt
  arm of `question:0005` and must be carried there, not smuggled into the diagnosis-code
  strata. Flagging this boundary explicitly so the third pooling tier is not mistaken for an
  EHR-derivable stratum.

**Three a-priori scoping decisions to pre-register before extraction (WP1 input spec):**
1. **Vasculitis** — define the stratum as *any-systemic-vasculitis* (union of the five+
   subtype refsets / SNOMED family) vs a specific subset; exclude nonspecific "vasculitis,
   unspecified" codes or keep them. Decide once, apply in both vehicles.
2. **Autoimmune-thyroid** — primary definition = **Graves + explicit-Hashimoto/autoimmune-
   thyroiditis codes only** (autoimmune-specific, **low sensitivity**), with an
   **all-cause-hypothyroid-inclusive** version as a pre-registered sensitivity stratum. Never
   silently fold all-cause hypothyroidism into the autoimmune exposure. Implementation detail
   that makes this concrete: "Hashimoto-specific" means an **author-built code set of the
   explicit autoimmune-thyroiditis concepts** — SNOMED *Hashimoto thyroiditis* (21983002) /
   *autoimmune thyroiditis* / *chronic lymphocytic thyroiditis*, i.e. ICD-10-CM **E06.3** — which
   both vehicles can express because the SNOMED concept exists in each. The asymmetry is only
   that OpenSAFELY has **no curated *refset*** bundling these (unlike Graves' `gravesdis_cod`),
   so the Hashimoto side is author-built there; N3C is likewise author-built (no Phenotype
   Library cohort). The stratum is low-sensitivity in both because most autoimmune-hypothyroid
   patients are coded only with a generic hypothyroidism code (all-cause `thy_cod` / E03) that
   the specific definition deliberately excludes. If explicit Hashimoto coding proves too sparse
   in a vehicle, the fallback there is **Graves-only** (still autoimmune-specific), not
   all-cause hypothyroid — the sensitivity variant is reported separately, never as the primary.
3. **Myositis** — exclude drug-induced and paraneoplastic myopathy; OpenSAFELY's `myositis_cod`
   pools PM+DM (acceptable); N3C build should match that grain for cross-vehicle comparability.

## Evidence Quality

Feasibility-grade, sourced. OpenSAFELY side is landing-confirmed (2026-07-01) against
OpenCodelists site-search and individual codelist pages; the confirmed refsets sit in the
curated **NHSD Primary Care Domain** autoimmune refset family (official, versioned, SNOMED CT,
UK-OGL-licensed) — the strongest provenance tier, not single-user contributions. N3C side:
the four OHDSI Phenotype Library cohorts (#119/#196/#198/#201) were verified by direct lookup
of the library's `Cohorts.csv`; the other four strata are grounded in the fact that every one
is a standard SNOMED disorder with ICD-10-CM source codes that N3C maps to SNOMED standard
concepts (constructible, but author-built and unvalidated). Durable source pointers are
listed below so the audit is reproducible.

## Sources (durable pointers)

Checked 2026-07-01. OpenCodelists slugs resolve at `https://www.opencodelists.org/codelist/<slug>/`;
**version tags are intentionally not pinned here** — codelist version-pinning (a specific
release hash per slug) is a `plan:0006` WP1 bundle-build step, not a BC-3 deliverable.

- **OpenSAFELY / OpenCodelists (SNOMED CT unless noted).** NHSD Primary Care Domain refsets:
  SLE `nhsd-primary-care-domain-refsets/slupus_cod`, RA `.../rarth_cod`, UC
  `.../ulcerative-colitis-uc-codes`, Sjögren `.../sjogrens_cod`, myositis (PM+DM) `.../myositis_cod`,
  Graves `.../gravesdis_cod`, all-cause hypothyroidism (sensitivity variant only) `.../thy_cod`;
  vasculitis subtype-union `.../gca_cod`, `.../wegenervasc_cod`, `.../polyarteritis_cod`,
  `.../takayasuart_cod`, `.../cryoglobvasc_cod`. NHSD `nhsd/multiple-sclerosis-snomed-ct`.
  OpenSAFELY-org (CTV3/Read→SNOMED): `opensafely/rheumatoid-arthritis`,
  `opensafely/ra-sle-psoriasis-snomed`, `opensafely/inflammatory-bowel-disease-snomed`,
  `opensafely/crohns-disease`, `opensafely/multiple-sclerosis-v2`, `opensafely/giant-cell-arteritis`.
  *(MPA and EGPA/Churg-Strauss refsets not separately verified — likely in the same NHSD family;
  resolve at WP1.)*
- **N3C / OMOP.** OHDSI Phenotype Library — `https://ohdsi.github.io/PhenotypeLibrary/`,
  cohort list snapshot `https://raw.githubusercontent.com/OHDSI/PhenotypeLibrary/main/inst/Cohorts.csv`:
  cohorts **#119** (SLE), **#196** (RA), **#198** (Crohn's), **#201** (UC). SNOMED standard
  concepts (author-built strata): SLE 55464009, RA 69896004, Crohn's 34000006, UC 64766004,
  MS 24700007, Sjögren 83901003, Hashimoto 21983002, GCA 195350000, DM 396230008, PM 31384009.
  OMOP `concept_id`s for these are **`[UNVERIFIED]`** — the ATHENA public API
  (`https://athena.ohdsi.org`) returned **HTTP 403** (needs an authenticated token); confirm
  interactively under `task:t081`.
- **Supporting validation.** SLE EHR-phenotype chart validation: PLOS ONE 2023,
  `doi:10.1371/journal.pone.0281929`.

## Data Quality Checks

Not an empirical-results interpretation. The relevant structural data-quality facts, carried
forward into `plan:0005`:
- **Autoimmune-thyroid misclassification** (above) — the dominant stratum-level exposure-QA
  hazard; resolved by the conservative Graves+Hashimoto-specific primary definition.
- **OMOP concept_ids `[UNVERIFIED]`** — the ATHENA public API returned HTTP 403, so specific
  concept_ids must be confirmed interactively at athena.ohdsi.org. This is exactly **`task:t081`
  (OMOP Athena vocabulary)** — BC-3 sharpens t081's punch-list rather than duplicating it.
- **EHR under-coding of rarer conditions** (Sjögren, myositis, some vasculitides) reduces
  stratum *sensitivity/sample size* — that is BC-4 (power), distinct from BC-3's
  constructibility clearance.

## Proposition-Level Updates

None. BC-3 is a vocabulary-feasibility verdict; no `proposition:` gains or loses an
evidence-line.

## Hypothesis-Level Implications

- `hypothesis:0008` (ascertainment / measurement-channel meta-finding) is **operationally
  reinforced on the exposure side**: the autoimmune-thyroid convergence shows the *exposure*
  channel — not only the outcome channel — carries a measurement failure mode that is plausibly
  differential (autoimmune-hypothyroid patients who are higher-utilisation are more likely to
  get the specific Hashimoto code rather than a generic hypothyroid code). h0008's claim that
  the measurement channel shapes the apparent signal now has an exposure-side instance, not
  just the outcome-side long-COVID-coding instance from BC-1.
- `question:0005` (latent→overt autoimmunity) gains a concrete boundary: the genetic-risk-only
  diathesis stratum is **not** derivable from these EHR vehicles and must be pursued in a
  genotype-linked modality if it is to be tested at all.
- No update to `hypothesis:0004` / `hypothesis:0005`; BC-3 is infrastructure feasibility.

## Evidence vs. Open Questions

**Settled (BC-3):** disease-specific strata resolve in both vehicles; 7/8 clean, autoimmune-
thyroid partial; pooling hierarchy assigned; three a-priori scoping decisions named; the
codelist-provenance map is the input spec for `plan:0006` WP1 (the versioned concept-set
bundle) — which stays **code-gated**, BC-3 does not build it. **Still open:** BC-4 (does each
stratum × sex × PASC cell clear the power floor — the *counts* BC-3 deliberately did not
touch); BC-5 (PASC phenotype); BC-6 (severity dateability); BC-7 (individual utilisation);
and t081 (confirm the OMOP concept_ids).

## New Questions Raised

- Does restricting autoimmune-thyroid to the specific (Graves + Hashimoto-only) definition
  cost enough sensitivity to drop that stratum below the BC-4 power floor — forcing it into
  the organ-specific pool? This is answerable only with BC-4 counts.
- (No new `question:` entity reserved — this folds into BC-4 on `task:t079`.)

## Limitations & Residual Uncertainty

- **Cell counts untouched.** BC-3 clears *constructibility*, not *estimability*. A confirmed
  refset with 40 patients is still underpowered; that verdict is BC-4's.
- **OMOP concept_ids unverified** (ATHENA 403) — carried to t081.
- **Vasculitis subtype completeness partial** — GCA/GPA/PAN/Takayasu/cryoglobulinaemic
  refsets confirmed; dedicated MPA and EGPA/Churg-Strauss refsets were not separately verified
  (likely present in the same NHSD family). Resolve at bundle-build (WP1).
- **Author-built N3C strata are unvalidated** — the five without a Phenotype Library cohort
  (MS, Sjögren, vasculitis, myositis, autoimmune-thyroid) need a clinical-review pass before
  use for a real estimate; fine for the synthetic prototype.

## Updated Priorities

1. **BC-4 next among the open BCs:** obtain per-stratum × sex × PASC cell counts against the
   power floor — the binding unknown, and the one that decides whether the autoimmune-thyroid
   and rare-vasculitis/myositis strata survive standalone or must pool.
2. **Feed the resolved codelist-provenance map into `plan:0006` WP1** as the concept-set
   bundle's input spec (draft-unreviewed): Sjögren/myositis/vasculitis promoted from
   BC-3-gated stubs to draft-confirmed; autoimmune-thyroid stays flagged (specific-vs-all-cause
   fork); SLE/RA/IBD reuse the OHDSI library cohorts. WP1 itself remains code-gated (t082).
3. **Pre-register the three scoping decisions** (vasculitis union, autoimmune-thyroid specific-
   primary, myositis exclusions) when the plan moves to pre-registration — not before.
