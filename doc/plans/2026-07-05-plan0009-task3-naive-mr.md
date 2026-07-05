# plan:0009 Task 3 — Naive MR comparator (IVW / MR-Egger / weighted-median)

> **For agentic workers:** implementation companion to `plan:0009` Task 3. One
> commit for the increment. Steps use `- [ ]` checkboxes. Recommended executor:
> `superpowers:subagent-driven-development`.

**Goal:** For each of the six **eligible** hormone instruments built in Task 2,
harmonise against the long-COVID outcome (`GCST90454541`) and run the **naive
IVW / MR-Egger / weighted-median** comparator (log-OR long-COVID per 1-SD
hormone), on the **1000G-EUR-clumped** instrument set. Emit one per-stratum
result record + one aggregate manifest, every estimate carrying the
**ancestry-flag / non-primary (KD1)** and **bounded-sex (KD3)** labels. **No
overlap correction in this increment** — MRlap is Task 4.

**Design of record:** `entities/plans/0009-wave1-mr-hormone-pilot.md` (Task 3 +
Decision criteria). **Estimand:** `doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`.
**Predecessor increment:** `doc/plans/2026-07-04-plan0009-task2-hormone-instruments.md`.

**Architecture:** Extend the *isolated* `code/workflows/wave1-mr-hormone/`
Snakemake workflow — **not** the frozen `plan:0007` `wave1-mr/` run-of-record.
The naive-MR mechanics are a near-verbatim reuse of the `plan:0007`
`harmonize_estimate.R` (stream-extract the instrument SNPs from the multi-GB
outcome by rsID; `harmonise_data(action = 2)`; IVW/Egger/weighted-median with a
seeded WM bootstrap). Three load-bearing adaptations vs the SLE pilot: (1) the
Task-2 instrument TSV uses `EA`/`OA` column names (not `effect_allele`/
`other_allele`) — the exposure `format_data` mapping changes accordingly; (2)
the exposure is a **continuous SD-scaled hormone**, not a log-OR liability, so
the **estimand string, OR interpretation, and labels** change (KD1 ancestry-flag
+ KD3 bounded-sex, not the plan:0007 SLE label); (3) the pipeline is a **six-way
fan-out with a per-stratum eligibility guard** — a quarantined stratum
(`eligible_for_mr: false` in its Task-2 sidecar) is **loudly skipped, not run**,
and a stratum that drops below the 3-instrument floor *after* harmonisation is
recorded as informative, not fatal (weak is informative, not a pipeline
failure — `plan:0009` Decision criteria).

**Tech stack:** Snakemake `--use-conda`; R 4.5 (`data.table`, `TwoSampleMR`
v0.7.9 — the same `r-mr` env + setup sentinel Task 2 produced); Python 3.12
(`pyyaml`) for the aggregator (`stage.yaml` env).

## Global constraints (from plan:0009, binding)

- **Interpretation ceiling, always.** Every estimate is **ancestry-flagged and
  non-primary** (KD1: outcome is the European-dominant ~85–90% multi-ancestry HGI
  broad/population meta `GCST90454541`; no EUR-only sibling) and any male-vs-female
  read is a **bounded exposure-architecture** probe (KD3), **not** a genotype×sex
  effect-modification test. No result is reported as primary evidence for
  `hypothesis:0005` / `question:0007` / `question:0013`, nor as a sex-modification
  claim.
- **Two exposure-side caveats carried into interpretation:** SHBG and total
  testosterone are **not independent** (shared Ruth instrument loci; steroid-axis
  horizontal pleiotropy plausible — Egger + weighted-median only *partially* bound
  it, a "clean" IVW is not pleiotropy-free); and the **female-testosterone stratum
  is the weakest-instrumented yet most decision-relevant** — a wide or weak female
  estimate is itself informative, not a failure.
- **Weak is informative, not fatal.** Quarantined strata are skipped loudly (never
  silently); a post-harmonisation drop below 3 instruments is recorded, not
  crashed. Technical faults (missing column, unreadable outcome, non-finite
  estimate) still hard-stop.
- **Naive arm only.** No MRlap, no canonicalization adapter, no LDSC — Task 4.
- Payloads/outputs stay **off Dropbox** under `data/` + `results/` (gitignored,
  symlinked to `/data`); `git status` shows nothing under `data/`.
- Same pinned `r-mr` env + setup sentinel as Task 2; the weighted-median RNG seed
  is recorded for reproducibility.

---

## Inputs (all present on disk from Tasks 1–2)

- **Exposures (instruments)** — the six Task-2 instrument TSVs at
  `data/processed/wave1-mr-hormone/instruments/{stratum}.instrument.tsv`
  (columns: `SNP chr pos EA OA beta se eaf pval F`) + their
  `{stratum}.instrument.json` sidecars (carry `eligible_for_mr` + reasons).
  All six are **eligible** (159–353 instruments, mean F 90–155).
- **Outcome** — `data/raw/gwas/hormone-pilot/covid19-hgi-longcovid-broad-population.GCST90454541.h.tsv.gz`
  (binary long-COVID, `hm_beta` = log-OR; European-dominant multi-ancestry — the
  ancestry flag). Stream-extracted by rsID; never fully loaded.
- **Setup sentinel** — `.setup_twosamplemr.json` (TwoSampleMR 0.7.9 / ieugwasr
  1.1.0, version-assert pass) from Task 2; reused, not rebuilt.
- **Datasets** `covid19-hgi-longcovid-gwas` and `ruth-2020-shbg-testosterone-gwas`
  already carry `plan:0009` in `consumed_by` (Task 1); the data-access gate passed
  at staging. This increment consumes only already-gated inputs — no new dataset.

## File structure

```
code/workflows/wave1-mr-hormone/
├── config.yaml                    MODIFY  + harmonise: + estimate: blocks
├── Snakefile                      MODIFY  + harmonize_estimate (wildcard) + aggregate_mr rules + naive_mr target
└── scripts/
    ├── harmonize_estimate.R       CREATE  copy of plan:0007 harmonize_estimate.R with: EA/OA exposure mapping,
    │                                       KD1/KD3 labels + hormone estimand, per-stratum eligibility guard,
    │                                       graceful <3-harmonised handling (record, don't abort)
    └── aggregate_mr.py            CREATE  join 6 per-stratum results (+ benchmark TSVs, setup sentinel,
                                            instruments_manifest) → naive_mr_results.json + cross-stratum concordance
```

`harmonize_estimate.R` is a deliberate **copy into the isolated workflow**
(plan:0003 KD4 / plan:0007 isolation convention), not a shared import — the frozen
`wave1-mr/` run-of-record is never edited.

## config.yaml additions

```yaml
# ------------------------------------------------------------- harmonise -----
# plan:0009 Task 3. TwoSampleMR harmonise action=2 (infer palindromic strand by
# EAF, drop ambiguous); same as plan:0007. All drops logged (non-silent).
harmonise:
  action: 2

# -------------------------------------------------------------- estimate -----
# plan:0009 Task 3 naive comparator: IVW (primary) / MR-Egger / weighted-median
# on the 1000G-EUR-clumped instruments. Outcome effect is log-OR long-COVID per
# 1-SD hormone. WM SE is bootstrapped → fixed seed (IVW/Egger are closed-form).
estimate:
  methods: ["mr_ivw", "mr_egger_regression", "mr_weighted_median"]
  weighted_median_seed: 20260705
  weighted_median_bootstrap_n: 1000
```

`config["exposures"]` already carries each stratum's `name` / `accession` /
`trait` / `sex`; the script resolves trait+sex by `--stratum`. `config["outcome"]`
already carries the outcome `name` / `accession`.

## harmonize_estimate.R — load-bearing changes vs plan:0007

Same stream-extract, `harmonise_data(action = 2)`, and IVW/Egger/WM estimator
core as the `plan:0007` script (`code/workflows/wave1-mr/scripts/harmonize_estimate.R`),
with these edits:

1. **New args + config-driven stratum resolution.** Accept `--stratum`,
   `--instrument`, `--sidecar`, `--outcome`, `--harmonised-out`, `--results-out`.
   Resolve `spec <- config$exposures[[which(names==stratum)]]` to get
   `trait` / `sex` / `accession` (the pattern `build_instrument.R` uses).

2. **Eligibility guard (loud skip).** Read the stratum's Task-2 sidecar. If
   `eligible_for_mr == false`, write a results JSON with
   `status: "skipped-quarantined"` + `eligibility_reasons`, print a loud
   `cat("SKIP …")`, write an **empty** harmonised TSV (header only, so the
   Snakemake output exists), and `quit(save = "no", status = 0)` — no estimator
   runs. (All six are eligible now; this guard is required by `plan:0009`
   "Task 3/4 skip or loudly flag them.")

3. **Exposure column mapping (`EA`/`OA`).** The Task-2 instrument TSV uses
   `EA`/`OA`, not `effect_allele`/`other_allele`:
   ```r
   exp_dat <- format_data(
     as.data.frame(inst), type = "exposure", snp_col = "SNP", beta_col = "beta",
     se_col = "se", effect_allele_col = "EA", other_allele_col = "OA",
     eaf_col = "eaf", pval_col = "pval")
   exp_dat$exposure <- spec$name
   ```
   The outcome `format_data` and the `pick()` column resolver (`hm_rsid` /
   `hm_beta` / `standard_error` / `hm_effect_allele` / …) are **unchanged** from
   plan:0007 — same outcome file family.

4. **Graceful weak-harmonised handling (record, don't abort).** plan:0007 does
   `if (nrow(kept) < 3) stop(...)`. Replace with a **non-fatal record** so one
   thin stratum does not crash the batch:
   ```r
   if (nrow(kept) < 3) {
     cat(sprintf("WEAK: %s — only %d harmonised instruments (<3); recording, not estimating\n",
                 stratum, nrow(kept)))
     write_results(status = "insufficient-harmonised-instruments",
                   n_harmonised = nrow(kept), dropped = dropped, methods = list())
     fwrite(dat, harmonised_out, sep = "\t"); quit(save = "no", status = 0)
   }
   ```
   (Won't trigger for the six built strata — all ≥159 instruments — but the guard
   honours "weak is informative, not a failure".)

5. **Hormone estimand + KD1/KD3 labels.** Replace the SLE estimand/label with:
   ```r
   estimand <- sprintf(paste0("germline-liability IV effect of a 1-SD increase in %s ",
     "(%s; Ruth 2020, European UKB continuous-trait GWAS) on long-COVID liability ",
     "(log-OR), 1000G-EUR-clumped genome-wide-significant instruments."),
     spec$trait, spec$sex)
   labels <- list(
     ancestry_flag = paste0("Outcome GCST90454541 is a European-dominant (~85-90%) ",
       "multi-ancestry HGI broad/population meta; no EUR-only sibling. ANCESTRY-FLAGGED, ",
       "NON-PRIMARY (KD1) — exploratory/robustness only, never primary evidence for ",
       "hypothesis:0005 / question:0007 / question:0013."),
     bounded_sex = paste0("Male-only / female-only strata give a BOUNDED ",
       "exposure-architecture read against a mixed-sex outcome (KD3) — NOT a ",
       "genotype x sex effect-modification test. No sex-modification claim."),
     exposure_side = paste0("SHBG and total testosterone share Ruth instrument loci ",
       "(steroid-axis pleiotropy plausible; Egger+WM only partially bound it). ",
       "Female-testosterone is weakest-instrumented yet most decision-relevant."))
   ```
   `OR = exp(b)` is now **OR of long-COVID per 1-SD hormone** — recorded per method.

6. **Estimators (unchanged core).** `set.seed(cfg$estimate$weighted_median_seed)`;
   `mr(dat, method_list = cfg$estimate$methods)`; `mr_pleiotropy_test(dat)` for the
   Egger intercept; sign-concordance across the three methods; resource capture
   (`extract_secs`, `peak_mb`). Snakemake `benchmark:` additionally records
   `max_rss` + wall-clock for the real-data stream-extract step.

**Per-stratum results JSON** (written by `write_results`, small helper):
```json
{
  "stratum": "ruth-shbg-female", "accession": "GCST90012107",
  "trait": "shbg", "sex": "female",
  "estimand": "...", "exposure": "ruth-shbg-female", "outcome": "covid19-hgi-longcovid-broad-population",
  "status": "estimated",
  "n_instruments_input": <int>, "n_harmonised": <int>,
  "mean_f_instruments": <num>,
  "methods": [ {"method": "Inverse variance weighted", "nsnp": <int>,
                "b": <num>, "se": <num>, "pval": <num>, "or": <num>}, "...Egger, WM..." ],
  "egger_intercept": {"intercept": <num>, "se": <num>, "pval": <num>},
  "concordance": {"all_methods_same_sign": <bool>, "ivw_beta": <num>},
  "dropped_snps": [<rsid...>],
  "harmonise_action": 2, "weighted_median_seed": 20260705,
  "resources": {"outcome_extract_seconds": <num>, "peak_memory_mb": <num>},
  "labels": { "ancestry_flag": "...", "bounded_sex": "...", "exposure_side": "..." }
}
```

## aggregate_mr.py → naive_mr_results.json

Reads the six per-stratum result JSONs + six benchmark TSVs + the setup sentinel +
`instruments_manifest.json` (for the instrument-count cross-ref); **hard-stops** on
any missing/malformed input. Writes under `results/wave1-mr-hormone-pilot/`:

```json
{
  "plan": "plan:0009-wave1-mr-hormone-pilot", "task": "t089",
  "stage": "Task 3 — naive MR comparator (IVW / Egger / weighted-median)",
  "labels": { "ancestry_flag": "...(KD1)...", "bounded_sex": "...(KD3)...",
              "exposure_side": "...SHBG<->testosterone coupling; female-T caveat..." },
  "estimate_params": { "methods": ["mr_ivw","mr_egger_regression","mr_weighted_median"],
                       "weighted_median_seed": 20260705,
                       "weighted_median_bootstrap_n": 1000, "harmonise_action": 2 },
  "strata": [ "...six per-stratum result records..." ],
  "summary": { "n_strata": 6, "n_estimated": <int>, "n_skipped": <int>,
               "skipped": [ {"stratum": "...", "reasons": ["..."]} ] },
  "cross_stratum": {
    "_note": "BOUNDED exposure-architecture descriptor (KD3) — sign concordance of the
              male-only vs female-only IVW estimate for each trait against the common
              mixed-sex outcome. NOT a sex-modification test; no interaction is estimated.",
    "shbg":         {"combined_ivw_sign": <int>, "male_ivw_sign": <int>,
                     "female_ivw_sign": <int>, "male_female_sign_concordant": <bool>},
    "testosterone": {"combined_ivw_sign": <int>, "male_ivw_sign": <int>,
                     "female_ivw_sign": <int>, "male_female_sign_concordant": <bool>}
  },
  "twosamplemr_setup": { "...resolved versions from the sentinel..." },
  "resource": { "per_stratum": [ {"stratum": "...", "wall_clock_s": <num>, "max_rss_mb": <num>} ],
                "peak_rss_mb": <max>, "total_wall_clock_s": <sum> }
}
```

`cross_stratum` is purely **descriptive sign-concordance** — it is the material
Task 5's write-up needs for the bounded male-vs-female read; it estimates **no**
interaction and makes **no** sex-modification claim. `sign` is `sign(ivw_beta)`;
a stratum with `status != "estimated"` contributes `null` and
`male_female_sign_concordant: null`.

## Snakefile additions

```python
# --- resolved naive-MR targets (plan:0009 Task 3) ----------------------------
MR_DIR = f"{PROC}/mr"
NAIVE_MR_MANIFEST = f"{RESULTS}/naive_mr_results.json"


rule naive_mr:                              # Task-3 target
    input:
        NAIVE_MR_MANIFEST,


# --- harmonise one stratum's instruments <-> outcome, run IVW/Egger/WM --------
rule harmonize_estimate:                    # fan-out over the six strata
    input:
        instrument=f"{INS_DIR}/{{stratum}}.instrument.tsv",
        sidecar=f"{INS_DIR}/{{stratum}}.instrument.json",
        outcome=OUTCOME_FILE,
        setup=SETUP_OK,
    output:
        harmonised=f"{MR_DIR}/{{stratum}}.harmonised.tsv",
        results=f"{MR_DIR}/{{stratum}}.mr_results.json",
    benchmark:
        f"{MR_DIR}/{{stratum}}.benchmark.tsv"    # real-data stream-extract: wall-clock + max_rss
    conda:
        "envs/r-mr.yaml"
    params:
        config=CONFIGFILE,
    shell:
        "Rscript {SCRIPTS}/harmonize_estimate.R --config {params.config} "
        "--stratum {wildcards.stratum} --instrument {input.instrument} "
        "--sidecar {input.sidecar} --outcome {input.outcome} "
        "--harmonised-out {output.harmonised} --results-out {output.results}"


# --- aggregate: six per-stratum results + benchmarks -> one naive-MR manifest -
rule aggregate_mr:
    input:
        results=expand(f"{MR_DIR}/{{stratum}}.mr_results.json", stratum=STRATA),
        benchmarks=expand(f"{MR_DIR}/{{stratum}}.benchmark.tsv", stratum=STRATA),
        setup=SETUP_OK,
        instruments=INSTRUMENTS_MANIFEST,
    output:
        manifest=NAIVE_MR_MANIFEST,
    conda:
        "envs/stage.yaml"
    shell:
        "python {SCRIPTS}/aggregate_mr.py --config {CONFIGFILE} "
        "--results {input.results} --benchmarks {input.benchmarks} "
        "--setup {input.setup} --instruments {input.instruments} "
        "--manifest {output.manifest}"
```

`INS_DIR`, `SETUP_OK`, `INSTRUMENTS_MANIFEST`, `STRATA`, `OUTCOME_FILE`, `PROC`,
`RESULTS`, `SCRIPTS`, `CONFIGFILE` all already exist in the Snakefile.

## Tasks

- [ ] **Step 1 — config.** Add the `harmonise:` and `estimate:` blocks to
      `config.yaml` (verbatim above).
- [ ] **Step 2 — estimator script.** Write `scripts/harmonize_estimate.R` by
      copying `code/workflows/wave1-mr/scripts/harmonize_estimate.R` and applying
      the six edits above (new args + `--stratum` resolution, eligibility guard,
      `EA`/`OA` exposure mapping, graceful `<3`-harmonised record, hormone
      estimand + KD1/KD3 labels, `write_results` helper emitting the per-stratum
      JSON). Keep the stream-extract + `harmonise_data(action=2)` + estimator core
      unchanged.
- [ ] **Step 3 — aggregator.** Write `scripts/aggregate_mr.py` (join six results +
      benchmark TSVs + sentinel + instruments manifest → `naive_mr_results.json`
      with `summary`, `cross_stratum` sign-concordance, `resource`; hard-stop on
      missing/malformed input).
- [ ] **Step 4 — Snakefile.** Add `MR_DIR` / `NAIVE_MR_MANIFEST`, the
      `harmonize_estimate` (wildcard + `benchmark:`) and `aggregate_mr` rules, and
      the `naive_mr` target.
- [ ] **Step 5 — run (real data).** `uv run snakemake -s
      code/workflows/wave1-mr-hormone/Snakefile --use-conda -c1 naive_mr`
      (reuses the Task-2 `r-mr` env + setup sentinel; no reinstall). Per-stratum
      wall-clock + `max_rss` captured by `benchmark:`.
- [ ] **Step 6 — inspect.** Read `naive_mr_results.json`: six strata each with
      `n_harmonised`, per-method `b`/`se`/`pval`/`or`, Egger intercept, sign
      concordance; the `cross_stratum` male-vs-female sign block; the labels; and
      `peak_rss_mb`. Confirm IVW/Egger/WM are finite and sane, the Egger intercept
      is computable, and the female-testosterone stratum's estimate is recorded
      (wide/weak = informative, not an error).
- [ ] **Step 7 — validate + note.** `uv run --frozen science validate`; record a
      t089 note summarising per-stratum IVW OR + concordance + peak RSS; commit.

## Final validation / Definition of done

- All six strata produce a `{stratum}.mr_results.json` + `{stratum}.benchmark.tsv`
  and appear in `naive_mr_results.json`; the aggregator hard-stops on any
  missing/malformed input.
- Each **eligible** stratum ran IVW/Egger/weighted-median on `harmonise(action=2)`
  instruments; drop-log present and **non-silent**; WM RNG seed recorded.
- Per-method `b`/`se`/`pval`/`or` finite; Egger intercept present (or explicitly
  `null` with reason); sign-concordance recorded.
- **Eligibility guard demonstrably works** (spot-checked): a stratum flagged
  `eligible_for_mr: false` in its sidecar is skipped loudly with a recorded reason
  and no estimator output; a `<3`-harmonised stratum is recorded, not crashed.
- **Scale/resource on real data:** per-stratum `max_rss_mb` + wall-clock from
  `benchmark:` for the outcome stream-extract in the manifest `resource` block;
  `peak_rss_mb` reported. (The multi-GB outcome is streamed by rsID, never fully
  loaded.)
- **Every output carries the ancestry-flag + non-primary + bounded-sex labels;**
  the `cross_stratum` block is labelled a descriptive exposure-architecture read,
  not a sex-modification test.
- `git status` shows nothing under `data/`; `naive_mr_results.json` lives under
  `results/wave1-mr-hormone-pilot/` (gitignored, regenerable); config pins
  reproduce it.

## Decision criteria (inherited from plan:0009)

- Mechanics-GO for the naive arm: naive IVW/Egger/weighted-median return finite,
  sane estimates with a computable Egger intercept and reported concordance for
  each eligible stratum.
- A weak/wide estimate (esp. female testosterone) is an **informative** scientific
  outcome under the KD1/KD3 ceilings, **not** a pipeline failure.
- NO-GO / fix-first only on a **technical** fault (unresolved outcome column,
  unreadable outcome, non-finite estimate from harmonised instruments) — repair
  before any naive result is quoted even as exploratory.

## Out of scope (this increment)

- **MRlap overlap correction + the hard-stop canonicalization adapter** and the
  `r-mrlap` + `r-genomicsem` env extension (Task 4).
- **The results write-up + go/no-go note** and the full reproducible bundle
  (`datapackage.json` / `qa_report` / `run_metadata`) (Task 5).
- **Any reportable-primary or sex-modification claim** — barred by the KD1/KD3
  ceilings.
- **BMI-adjusted / bioavailable-testosterone / estradiol strata** — later increment.

## Notes on scope

One science-task increment sized like Task 2: run the naive comparator over the
six built instruments and stop, so the uncorrected IVW/Egger/WM estimates and
their concordance exist **before** the MRlap overlap-corrected arm (Task 4) is
built — preserving the naive↔corrected comparison the design turns on. It reuses
the proven `plan:0007` estimator mechanics and the Task-2 `r-mr` env; the only new
mechanism (MRlap/LDSC) is deliberately deferred to Task 4.
