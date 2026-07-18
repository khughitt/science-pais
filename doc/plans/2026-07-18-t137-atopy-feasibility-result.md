# t137 — Atopy → long-COVID MR feasibility packet: GO/NO-GO result

- **Date:** 2026-07-18
- **Task:** `task:t137` · **Pre-registration:** `doc/plans/2026-07-18-t137-atopy-feasibility-preregistration.md`
- **Verdict: NO-GO.** Do **not** draft D-007b; the atopy → long-COVID MR execution is **not** requested.

## What was run (public sumstats only, D-007 feasibility scope)

- **Exposure staged + verified:** `29083406-GCST005038-EFO_0003785.h.tsv.gz` (267M, GRCh38
  harmonised), md5 `e861def041c81a74b5df95963d7ca1fa` confirmed against the EBI pin.
- **Instrument (frozen params):** p < 5×10⁻⁸, extended-MHC chr6:25–34 Mb excluded (1,814 GWS SNPs
  dropped), local PLINK clumping r² < 0.001 / 10 Mb against the 1000G-EUR panel.
- **Outcome:** reused in place — `GCST90454541` (HGI long-COVID, European-dominant multi-ancestry,
  ~6,450 broad-definition cases). Mechanics/robustness-only per the settled ancestry cap; freshness
  = same freeze already staged for Wave-1.

## Results

| Quantity | Value |
|---|---|
| GWS non-MHC SNPs (pre-clump) | 7,113 |
| **Independent instruments (post-clump, MHC-excluded)** | **63** |
| Mean F / min F | **62.0 / 30.1** (all ≫ 10) |
| Σ 2p(1−p)β² (log-odds scale) | 0.0656 |
| logit-latent R² = Vg/(Vg+π²/3) | **1.96%** |
| Lee-2011 normal-liability R² across K∈{0.20,0.30,0.40} | **2.14% / 2.39% / 2.53%** |
| naïve Σ2p(1−p)β² as R² | 6.56% *(overstates — treats log-OR as liability-SD; excluded)* |
| Power @ OR 1.20/SD (K = 0.20/0.30/0.40) | **0.57 / 0.62 / 0.64** |
| Minimum detectable OR @ 80% power | **≈ 1.25–1.27** |
| R² required for 80% power @ OR 1.20 | 3.66% |

## Why NO-GO (against the frozen GO/NO-GO rule)

- Criteria **(i) instruments ≥ 5** and **(ii) mean F ≥ 10** *pass* decisively (63 instruments,
  F = 62). The instrument is **strong** — this is not an instrument-quality failure.
- Criterion **(iii) ≥ 80% power at OR 1.20/SD** *fails*: liability-scale R² is ~2–2.5%, giving
  0.57–0.64 power; the pre-registered NO-GO trigger ("power < 80% at OR 1.20 even at the most
  favourable K") is met (best case K = 0.40 → 0.64). The two principled R² estimators (logit-latent
  and Lee-normal) **converge** at ~2–2.5%, and ~2–2.5% for 63 lead SNPs is biologically consistent
  with Ferreira's per-component variance; only the naïve estimator disagrees and it is biased high.
- Criterion **(iv) sample overlap** was **not the binding constraint** and was not quantified —
  power short-circuits the decision. (Overlap could only bias toward the confounded observational
  estimate, which would not rescue a power-limited line.)

## Interpretation

The limit is the **ancestry-capped outcome**, not the exposure. The atopy instrument is excellent,
but ~6,450 multi-ancestry long-COVID cases cannot power a **plausible** atopy effect: published
atopy→disease MR effects run OR 1.1–1.2, *below* the ~1.25 minimum this design can detect. A null
here would be uninformative; a "hit" would require an implausibly large effect.

**Atopy is therefore shelved** — joining IM, but for a cleaner reason (outcome power, not
instrument weakness or pleiotropy). **No boundary-strata MR line survives.** The only remaining
open computational candidate is the non-MR frailty signature-projection line (`task:t138`, still
needing its own D-005 decision).

**Revisit if:** a EUR-matched or substantially larger long-COVID outcome GWAS becomes available
(the instrument is already built and would be reusable), which would raise the case count and could
move OR 1.20 back inside the detectable range.
