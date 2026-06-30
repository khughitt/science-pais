---
type: method
title: Open identification questions + staged adjustment-set amendment for the t029
  independent review
status: active
created: '2026-06-19'
updated: '2026-06-19'
id: method:confounder-open-questions-and-staged-amendment
related:
- task:t029
- task:t023
- task:t016
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- pre-registration:0001-menopause-pais-total-effect
- report:0001-bias-audit-menopause-pais-total-effect
- discussion:0001-menopause-timing-pais-rival-models
---

# Open identification questions + staged amendment (for the t029 independent review)

A focused input for the **independent reviewer (t029)**. It packages three
identification questions that surfaced *after* the bias audit and should have been
caught by it — chiefly that **measured strong confounders sit in a sensitivity arm
rather than the primary adjustment set**. These are **reviewer decisions**, staged here
rather than self-applied, precisely because the audit's central finding was that
same-author criterion changes should not be treated as validated. The reviewer
**ratifies, modifies, or rejects** each.

> **Why staged, not self-amended.** Execution is data-gated (no UKB data), so amending
> the adjustment set now is *pre-data* and carries no HARKing cost. But self-applying a
> criterion change reproduces the **author-independence** problem
> (`report:0001-bias-audit-...`). With the reviewer ready, the clean route is to let the
> criterion change acquire **out-of-author provenance**.

> **REVIEWER RESOLUTION — t029 independent review, 2026-06-19 (applied to `pre-registration:0001`).**
> - **Q1 RATIFIED** with coding/wording modification → smoking moved to the **primary
>   measured adjustment set** `{age, smoking}`; pre-data amendment, not a fresh pre-reg;
>   E-value/U-proxy redefined vs the new set.
> - **Q2 default RATIFIED** → BMI stays out of primary, carried as sensitivity, role to DAG v2.
> - **Q3** → autoimmune-POI, frailty, parity **not** added to primary (routed to
>   stratum/selection-model/DAG-v2 respectively).
> - **Q4 RATIFIED** → MR added as **triangulation only**, with a strengthened
>   pleiotropy-/selection-robust guardrail battery.
> - **Two reviewer findings folded in below:** (i) do **not** call `{age, smoking}`
>   "minimal-sufficient" while U is latent — it is the *primary measured* set; (ii) tighten
>   the smoking temporal wording (baseline smoking is pre-infection but **not** always
>   pre-FMP).

---

## Q1 — STAGED AMENDMENT: add **smoking** to the primary adjustment set

**Change (RATIFIED, modified):** primary adjustment set **`{age}` → `{age, smoking}`**,
named the **primary measured adjustment set**. **Smoking coding (reviewer modification):**
**baseline smoking history — never/former/current plus pack-years or duration where
available** (fields `20116` + `20161`/`2887`/etc., confirm at application) — *not* field `20116`
alone. **Temporal note (reviewer):** baseline smoking is pre-infection but **not always
pre-FMP** (women already postmenopausal at UKB baseline), so it enters as a **measured
confounder**, not a clean pre-menopause exposure.

**Rationale.** Smoking is a **measured strong common cause**: smoking → **earlier**
menopause **and** → worse COVID/long-COVID **and** → higher mortality (so it also drives
the M3a left-truncation). Conditioning on age does **not** block this back-door, yet the
committed design relegated smoking to the "U-proxy adjustment arm" sensitivity. For a
measured confounder that is defensibly *the* strongest determinant of age-at-menopause
besides age itself, sensitivity-only placement is too weak; it belongs in the primary
measured set. **Terminology (reviewer finding):** the result is the **primary measured
adjustment set** `{age, smoking}` — **not** "minimal-sufficient." Per the DAG critique
(`doc/inquiries/menopause-pais-causal-dag-critique.md`), **no valid sufficient adjustment
set exists while U is latent**; calling any measured set "minimal-sufficient" overstates
identification.

**Reviewer asks:**
- (a) Ratify, modify, or reject moving smoking into the **primary** set.
- (b) Confirm this is an **amendment** (additive identification fix, pre-data), not a
  fresh pre-registration. (Our read: amendment — route via
  `statistics-prereg-amendment-vs-fresh` only if you disagree.)
- (c) If ratified, the E-value benchmark and the U-proxy arm are re-defined relative to
  the **new** primary set (the arm becomes "what an unmeasured U beyond `{age, smoking}`
  would need"). Confirm.

**Low-regret note.** Smoking is plausibly already partly controlled via the U-proxy arm;
elevating it to primary mainly changes *which* estimate is the headline, not whether
smoking is handled at all. Downside of the change is near-zero; downside of *not*
changing it is a defensible-confounding objection to the primary estimate.

---

## Q2 — OPEN ROLE QUESTION: what is **BMI/adiposity's** correct causal role?

**Not** staged as a primary-set inclusion, because BMI is genuinely ambiguous:

- **Confounder reading:** higher BMI → *later* menopause (peripheral estrogen) **and** →
  worse COVID/LC → belongs with smoking in the primary set.
- **Mediator reading:** menopause → central/visceral adiposity → estrogen/inflammation →
  LC → BMI is **on the M1 path**, and adjusting for it would be **over-adjustment** that
  *biases* the total effect.
- **Timing matters:** baseline BMI (2006–2010) is more confounder-like for women still
  pre-transition; peri/post-menopausal weight change makes later BMI mediator-like.

**Proposed default (pending reviewer + DAG v2):** keep BMI **out** of the primary
total-effect set; carry **baseline** BMI as a sensitivity covariate only; let **t023
(DAG v2)** fix its role with an explicit edge before any promotion.

**Reviewer ask:** adjudicate BMI's role, or endorse deferring it to DAG v2.

---

## Q3 — SUFFICIENCY CHECK: is the primary measured set complete, or do these also belong?

(Reading "sufficient" loosely — strictly, no sufficient set exists while U is latent; the
question is which *measured* confounders belong in the primary set vs the sensitivity arm.)
Other **measured** candidates that the `{age}`-minimal claim may have wrongly folded
into latent U:

- **Autoimmune POI / autoimmune common cause** — autoimmunity → early menopause
  (autoimmune oophoritis, thyroid) **and** → PAIS predisposition. The generic
  autoimmune-dx flag (20002) is a proxy; the **POI subtype is a specific confounding
  structure** (one disease causing both exposure and outcome).
- **Biological frailty / subclinical pre-infection ill-health** — a **non-SES** common
  cause of both earlier menopause and higher LC susceptibility (distinct from M4).
- **Parity** (2734) — currently a *staging input*; but parity → later menopause **and**
  parity → immune/LC effects → potential **dual role** as a confounder of the
  timing→LC edge, not only a staging predictor.

**Reviewer ask:** which (if any) of {autoimmune-POI, frailty, parity} belong in the
**primary** set vs the sensitivity arm vs latent-U/E-value, and which can wait for DAG v2.

---

## Q4 — NEW IDENTIFICATION STRATEGY: Mendelian randomization triangulation arm

**Proposal:** add an **MR of genetically-instrumented age-at-menopause → long-COVID** as
a **pre-registered triangulation arm** (UKB carries the genotyping; age-at-menopause has
strong GWAS instruments).

**Why it is high-value.** A genetic instrument for menopause timing is **exogenous to
SES, smoking, behaviour, and survival-into-2020**, so it attacks **M2 (aging), M4 (SES),
and M3a (survival) simultaneously** — and it is a partial answer to the rival-model
packet's central asymmetry that *UKB can refute but barely confirm M1*. A concordant MR
estimate is the strongest available out-of-design corroboration of a causal reading.

**Load-bearing caveat (pre-stated):** menopause-timing loci **overlap DNA-damage-response
and immune genes**, so **horizontal pleiotropy is a live threat** — the MR's exclusion
restriction is not free. It is a **triangulation arm with orthogonal assumptions**, not a
replacement for the observational estimand; standard MR sensitivity (MR-Egger, weighted
median, pleiotropy-robust methods) must be pre-committed.

**Reviewer ask:** should MR be a **pre-registered triangulation arm** (with the
pleiotropy-robust battery), and does the DNA-repair/immune-gene overlap make it too
pleiotropy-prone to rely on even as triangulation?

---

## Routing of the broader candidate set

The mechanism-level mediators (visceral-fat/metabolic, **estrobolome/microbiome**,
**vasomotor-sleep→autonomic**, iron-status reversal) and the additional structural
alternatives (**shielding→infection-timing/variant-era** confounding,
**testing-into-denominator** selection, **HRT healthy-user/collider** check) do **not**
threaten the total-effect estimand (mediators) or are selection structures best modelled
in the DAG. They are routed to **t023 (DAG v2)** as the comprehensive redraw input, not
to this review. Mediators matter for the *direct-effect/mediation* secondary, not the
primary identification the reviewer is asked to ratify here.

---

## Summary of reviewer actions

| # | Item | Type | Reviewer ruling (t029, 2026-06-19) |
|---|---|---|---|
| Q1 | Smoking → primary set | staged amendment | **RATIFIED (modified coding)** → `{age}`→`{age, smoking}` *primary measured* set; applied to pre-reg |
| Q2 | BMI role | open role question | **default RATIFIED** → out of primary; sensitivity (baseline, timing-split); role to DAG v2 |
| Q3 | autoimmune-POI / frailty / parity | open question | **not promoted** → POI = etiologic stratum/quarantine; frailty = selection model; parity = staging + DAG-v2 |
| Q4 | MR triangulation arm | new strategy | **RATIFIED** → triangulation only, strengthened pleiotropy-/selection-robust guardrails |

**Applied:** Q1 is now an `amendments:` record on `pre-registration:0001`; Q4 is added
under its Exploratory arms. Q2/Q3 route to **DAG v2 (t023)** plus sensitivities. Reviewer
findings on terminology ("primary measured", not "minimal-sufficient") and smoking
temporal coding are folded into Q1 above and the pre-reg.
