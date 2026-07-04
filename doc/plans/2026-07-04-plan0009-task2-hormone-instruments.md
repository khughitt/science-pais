# plan:0009 Task 2 — Build hormone instruments (implementation plan)

> **For agentic workers:** implementation companion to `plan:0009` Task 2. One
> commit for the increment. Steps use `- [ ]` checkboxes.

**Goal:** Build the six Ruth hormone-exposure instruments (SHBG · total
testosterone × combined/male/female) from the staged harmonised sumstats —
genome-wide-significant SNPs, local 1000G-EUR LD-clumping, per-instrument + mean
F — and emit one aggregate manifest that marks each stratum eligible or
quarantined for downstream MR. **No outcome-facing estimate in this increment.**

**Design of record:** `entities/plans/0009-wave1-mr-hormone-pilot.md` (Task 2 +
Decision criteria). **Estimand:** `doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`.

**Architecture:** Extend the *isolated* `code/workflows/wave1-mr-hormone/`
Snakemake workflow (built in Task 1) — **not** folded into the frozen `plan:0007`
`wave1-mr/` run-of-record. Reuse the proven `plan:0007` instrument mechanics
(`ieugwasr::ld_clump` + local `plink`, F = (β/se)²) and its `r-mr` conda env
spec, adapted for six strata with **MHC exclusion off** (hormones are not
HLA-dominated; the strong *cis*-SHBG signal is a legitimate instrument to keep).
**Reproducibility honesty (F1):** `--use-conda` materializes the env from
`r-mr.yaml` (matching `plan:0007`); `r-mr.conda-lock.yml` is carried as the
**recorded provenance** artifact, *not* the execution source (it is not consumed
by `--use-conda`). The genuine drift risk is the R layer — `TwoSampleMR` from a
GitHub tag + `ieugwasr` from CRAN resolve at install time — so the setup step
**hard-fails on version mismatch** (below), rather than the plan overclaiming a
byte-locked stack it does not actually pin.

**Tech stack:** Snakemake `--use-conda`; R 4.5 (`data.table`, `ieugwasr`,
`TwoSampleMR` v0.7.9 pinned by tag); `plink` (bioconda) for local clumping;
Python 3.12 (`pyyaml`) for the aggregator.

## Global constraints (from plan:0009, binding)

- Clumping is **local** against the staged `1000G-EUR` panel, **by rsID**
  (build-independent; Ruth files are GRCh38-harmonised, panel is GRCh37).
- `p_threshold = 5×10⁻⁸`; `clump_r2 = 0.001`; `clump_kb = 10000` (10 Mb);
  **no MHC exclusion**; `f_min = 10`.
- **Weak is informative, not a failure.** A complete manifest is emitted for all
  six strata. Technical faults hard-stop; weak/underpowered strata are
  quarantined, never silently used.
- Payloads/outputs stay **off Dropbox** under `data/` + `results/` (gitignored,
  symlinked to `/data`); `git status` shows nothing under `data/`.
- Pinned env; resolved `TwoSampleMR`/`ieugwasr` versions recorded to the sentinel
  for the eventual `run_metadata.json`.

---

## Eligibility gate (the Task-2 contract)

Two classes of outcome, per the Task-2 decision:

**Technical failure → hard-stop the stratum's rule (loud):**
- a required column cannot be resolved from the sumstats;
- `plink` not on PATH / clump call fails;
- **zero** instruments survive p-filter + clump from a parseable file;
- any surviving instrument has a **non-finite** F.

**Scientific viability → complete record, no abort:**
- `eligible_for_mr = (mean_F > f_min) AND (n_instruments ≥ min_instruments_mr)`
  (strict `>`, matching `plan:0009` Decision-criteria "mean F > 10" — F4 ruling);
- `min_instruments_mr = 3` (Egger / weighted-median floor) →
  `too_few_instruments` reason if below;
- `mean_F ≤ f_min` → `weak_mean_f` reason;
- `n_instruments < target_instruments` (`= 10`) → `below_target_n` **quality
  flag** (not an eligibility gate);
- quarantined strata (`eligible_for_mr: false`) carry their reason(s) so Task 3/4
  **skip or loudly flag** them.

## File structure

```
code/workflows/wave1-mr-hormone/
├── config.yaml                         MODIFY  + env: (pinned TwoSampleMR) + instrument: blocks
├── Snakefile                           MODIFY  + setup_twosamplemr, build_instrument (wildcard),
│                                                 aggregate_instruments rules + build_instruments target
├── envs/
│   ├── r-mr.yaml                       CREATE  verbatim copy of wave1-mr/envs/r-mr.yaml (execution source)
│   └── r-mr.conda-lock.yml             CREATE  verbatim copy — recorded provenance, NOT consumed by --use-conda
└── scripts/
    ├── setup_twosamplemr.R             CREATE  copy + version-assert: hard-fail unless TwoSampleMR==0.7.9;
    │                                            validate ieugwasr against the plan:0007-recorded version → sentinel
    ├── build_instrument.R              CREATE  hormone-local: MHC-optional + tiered gate + attrition-logged sidecar
    └── aggregate_instruments.py        CREATE  combine 6 sidecars (+ benchmark TSVs) → instruments_manifest.json
```

`build_instrument.R` and `setup_twosamplemr.R` are deliberate **copies into the
isolated workflow** (plan:0003 KD4 / plan:0007 isolation convention), not shared
imports — the frozen `wave1-mr/` run-of-record must not be edited. Changes vs the
`plan:0007` builder: **MHC exclusion is optional** (driven by presence of
`instrument.mhc_exclude`, absent here); the builder **never aborts on
weak/underpowered instruments** (records eligibility); it **logs per-boundary
attrition** (F2). The setup copy adds a **version hard-fail** (F1).

## config.yaml additions

```yaml
# --------------------------------------------------------------- env ----------
# TwoSampleMR is not on conda; setup_twosamplemr installs the pinned tag (with
# ieugwasr for local clumping) into the r-mr env library and records resolved
# versions. Same pin as plan:0007 (v0.7.9). The conda-lock.yml is recorded
# provenance only — --use-conda materializes r-mr.yaml (F1). The R layer is the
# real drift risk, so setup HARD-FAILS unless the resolved versions match:
env:
  twosamplemr_repo: "MRCIEU/TwoSampleMR"
  twosamplemr_ref: "v0.7.9"
  twosamplemr_version_expected: "0.7.9"        # hard-fail if packageVersion != this
  ieugwasr_version_expected: "<from plan:0007 run_metadata/sentinel>"  # resolve at Step 1; hard-fail on mismatch

# ------------------------------------------------------- instrument -----------
# plan:0009 Task 2. Genome-wide-sig → local 1000G-EUR clump → F=(beta/se)^2.
# NO mhc_exclude — hormones are not HLA-dominated; the cis-SHBG signal is a
# legitimate instrument (plan:0009 Approach). Weak strata are quarantined, not
# fatal (eligible_for_mr:false + reason), per the Task-2 gate.
instrument:
  p_threshold: 5.0e-8
  clump_r2: 0.001
  clump_kb: 10000                    # 10 Mb
  f_min: 10                          # mean-F floor for MR eligibility
  min_instruments_mr: 3              # Egger/weighted-median eligibility floor
  target_instruments: 10             # quality flag only (not a gate)
  # mhc_exclude: (intentionally absent — no MHC exclusion for hormones)
```

## setup_twosamplemr.R — version gate (F1)

The hormone copy adds a hard-fail after install, so a fresh run cannot silently
resolve a different R stack than the `plan:0007` run of record:

```r
tsmr <- as.character(packageVersion("TwoSampleMR"))
if (tsmr != cfg$env$twosamplemr_version_expected)
  stop(sprintf("setup: TwoSampleMR %s != expected %s — HALT", tsmr, cfg$env$twosamplemr_version_expected))
ieu <- as.character(packageVersion("ieugwasr"))
if (!is.null(cfg$env$ieugwasr_version_expected) && ieu != cfg$env$ieugwasr_version_expected)
  stop(sprintf("setup: ieugwasr %s != expected %s — HALT", ieu, cfg$env$ieugwasr_version_expected))
```

The sentinel still records the full resolved version set for `run_metadata.json`.
At **Step 1**, read `plan:0007`'s recorded `ieugwasr_version` (its setup sentinel
/ `results/.../run_metadata.json`) and write it into `ieugwasr_version_expected`.
If `plan:0007`'s value cannot be recovered, pin to whatever this run resolves and
record that the pin was established here (still deterministic thereafter).

## build_instrument.R — load-bearing changes vs plan:0007

Same column-resolution, p-filter, and local `ieugwasr::ld_clump` as the
`plan:0007` builder, with four edits:

1. **MHC optional.** `mhc <- ins$mhc_exclude`; apply the drop + the post-clump
   in-window assertion **only if `!is.null(mhc)`**. Record `mhc_excluded` in the
   sidecar (here `false`).
2. **Per-boundary attrition log (F2).** Count rows lost at each stage so a small
   instrument set is diagnosable as biology/power vs an rsID-join/panel-mismatch
   artifact. Capture `ld_clump`'s stdout/stderr to a clump-log file (it reports
   SNPs absent from the reference bfile):
   ```r
   a <- list(
     n_rows         = nrow(raw),                       # rows read from the sumstats
     n_complete     = nrow(std),                       # after rsID/beta/se/pval completeness + se>0
     n_missing_rsid = sum(is.na(raw_rsid) | raw_rsid == ""),
     n_passing_p    = nrow(std[pval < p_thr]),         # genome-wide significant
     n_clump_input  = nrow(gws),                       # fed to ld_clump (post-MHC if any)
     n_clumped      = nrow(inst),                      # independent instruments
     n_absent_in_panel = <parsed from clump log where available>
   )
   ```
3. **Tiered gate, no weak-abort.** After clumping and F:
   ```r
   if (!all(is.finite(inst$F))) stop("build_instrument: non-finite F — HALT (technical)")
   n_inst <- nrow(inst); mean_F <- mean(inst$F)
   reasons <- character(0)
   if (mean_F <= f_min)             reasons <- c(reasons, "weak_mean_f")          # gate: eligible iff mean_F > f_min (F4)
   if (n_inst < min_instruments_mr) reasons <- c(reasons, "too_few_instruments")
   eligible <- length(reasons) == 0
   quality  <- if (n_inst < target_instruments) "below_target_n" else character(0)
   ```
   `stop()` remains for **technical** faults only, and the **zero-instrument**
   message must distinguish the two causes (F2):
   - `n_passing_p == 0` → `stop("… zero genome-wide-significant variants — HALT (technical)")`
   - `n_passing_p > 0 && n_clumped == 0` → `stop("… all GWS variants lost in reference matching/clumping (see clump log) — HALT (technical)")`
4. **Per-stratum JSON sidecar** written next to the instrument TSV:
   ```json
   {
     "stratum": "ruth-shbg-female", "accession": "GCST90012107",
     "trait": "shbg", "sex": "female",
     "attrition": {
       "n_rows": <int>, "n_complete": <int>, "n_missing_rsid": <int>,
       "n_passing_p": <int>, "n_clump_input": <int>, "n_clumped": <int>,
       "n_absent_in_panel": <int|null>
     },
     "n_genomewide_sig": <int>, "n_instruments": <int>,
     "mean_F": <num>, "min_F": <num>, "max_F": <num>,
     "clump": {"r2": 0.001, "kb": 10000, "panel": "1000G-EUR", "by": "rsid",
               "clump_log": "<path>"},
     "mhc_excluded": false,
     "eligible_for_mr": <bool>, "eligibility_reasons": [<...>],
     "quality_flags": [<...>], "instrument_tsv": "<path>"
   }
   ```
   The instrument TSV (SNP, chr, pos, EA, OA, beta, se, eaf, pval, F) is always
   written when ≥1 instrument survives.

New args: `--sidecar <path>`, `--clump-log <path>`, `--stratum <name>` (trait/sex
read from config by `--stratum`). Assert every emitted instrument has `pval <
p_threshold` before writing (drop-log non-silent). **Gate (F4, decided):**
`eligible` uses **`mean_F > f_min`** — the stricter of `plan:0009`'s two phrasings
(Decision-criteria "mean F > 10"), so a stratum at exactly `mean_F == 10.0` is
*quarantined*, not passed. Task-2's "halt if mean F < 10" prose is left as-is;
the two differ only at the measure-zero equality point and the implementation is
the single source of truth for the gate.

## Snakefile additions

```python
STRATA = {e["name"]: e for e in config["exposures"]}          # name -> spec
INS_DIR = f"{config['paths']['processed']}/instruments"
SETUP_OK = f"{INS_DIR}/.setup_twosamplemr.json"
INSTRUMENTS_MANIFEST = f"{RESULTS}/instruments_manifest.json"

rule build_instruments:                    # Task-2 target
    input: INSTRUMENTS_MANIFEST

rule setup_twosamplemr:                     # copy of plan:0007 rule (r-mr env)
    output: sentinel=SETUP_OK
    conda: "envs/r-mr.yaml"
    params: repo=config["env"]["twosamplemr_repo"], ref=config["env"]["twosamplemr_ref"]
    shell: "Rscript {SCRIPTS}/setup_twosamplemr.R --repo {params.repo} --ref {params.ref} --sentinel {output.sentinel}"

rule build_instrument:                      # fan-out over the six strata
    input:
        exposure=lambda w: f"{GWAS_DIR}/{w.stratum}.{STRATA[w.stratum]['accession']}.h.tsv.gz",
        ld_bed=f"{LD_PREFIX}.bed", setup=SETUP_OK,
    output:
        tsv=f"{INS_DIR}/{{stratum}}.instrument.tsv",
        sidecar=f"{INS_DIR}/{{stratum}}.instrument.json",
        clump_log=f"{INS_DIR}/{{stratum}}.clump.log",
    benchmark: f"{INS_DIR}/{{stratum}}.benchmark.tsv"   # F3: wall-clock + max_rss per stratum
    conda: "envs/r-mr.yaml"
    params: config=CONFIGFILE, ld_prefix=LD_PREFIX
    shell:
        "Rscript {SCRIPTS}/build_instrument.R --config {params.config} "
        "--stratum {wildcards.stratum} --exposure {input.exposure} "
        "--ld-prefix {params.ld_prefix} --out {output.tsv} --sidecar {output.sidecar} "
        "--clump-log {output.clump_log}"

rule aggregate_instruments:
    input:
        sidecars=expand(f"{INS_DIR}/{{stratum}}.instrument.json", stratum=STRATA),
        benchmarks=expand(f"{INS_DIR}/{{stratum}}.benchmark.tsv", stratum=STRATA),
        setup=SETUP_OK,
    output: manifest=INSTRUMENTS_MANIFEST
    conda: "envs/stage.yaml"
    shell: "python {SCRIPTS}/aggregate_instruments.py --config {CONFIGFILE} "
           "--sidecars {input.sidecars} --benchmarks {input.benchmarks} "
           "--setup {input.setup} --manifest {output.manifest}"
```

Snakemake's `benchmark:` writes a TSV with `s` (wall-clock) and `max_rss`
(peak resident MB) per rule invocation — the idiomatic peak-memory capture, no
`/usr/bin/time` wrapper needed. The aggregator joins each stratum's benchmark
into the manifest `resource` block.

`LD_PREFIX` and `GWAS_DIR` already exist in the Task-1 Snakefile.

## aggregate_instruments.py → instruments_manifest.json

Reads the six sidecars + the setup sentinel; writes:

```json
{
  "plan": "plan:0009-wave1-mr-hormone-pilot", "task": "t089",
  "stage": "Task 2 — hormone instruments",
  "instrument_params": { "...": "the config instrument block, mhc_exclude: null" },
  "strata": [ "...six sidecar records..." ],
  "summary": {
    "n_strata": 6, "n_eligible": <int>, "n_quarantined": <int>,
    "quarantined": [ {"stratum": "...", "reasons": ["..."]} ]
  },
  "twosamplemr_setup": { "...resolved versions from the sentinel (incl. version-assert pass)..." },
  "resource": {
    "per_stratum": [ {"stratum": "...", "wall_clock_s": <num>, "max_rss_mb": <num>} ],
    "peak_rss_mb": <max over strata>, "total_wall_clock_s": <sum>
  }
}
```

Hard-stop if any sidecar or benchmark TSV is missing or malformed (structural
completeness). `peak_rss_mb` is read from the Snakemake `benchmark:` `max_rss`
column (F3) — the real-data resource figure Task 3/4 planning needs.

## Tasks

- [ ] **Step 1 — env + setup.** Copy `envs/r-mr.yaml` + `r-mr.conda-lock.yml`
      verbatim from `wave1-mr/`; copy `scripts/setup_twosamplemr.R` and add the
      **version-assert** (F1). Add the `env:` block to `config.yaml`; resolve
      `ieugwasr_version_expected` from `plan:0007`'s recorded sentinel/run-metadata.
- [ ] **Step 2 — config.** Add the `instrument:` block (no `mhc_exclude`).
- [ ] **Step 3 — builder.** Write `scripts/build_instrument.R` (hormone-local:
      MHC-optional, **attrition log + clump-log**, tiered gate with
      cause-distinguishing zero-instrument messages, JSON sidecar, `pval <
      p_threshold` assertion).
- [ ] **Step 4 — aggregator.** Write `scripts/aggregate_instruments.py` (joins
      sidecars + **benchmark TSVs** → manifest with summary + resource).
- [ ] **Step 5 — Snakefile.** Add the four rules (`build_instrument` with
      `benchmark:` + `clump_log` output) + `build_instruments` target; wire
      `STRATA`, `INS_DIR`, `SETUP_OK`, `INSTRUMENTS_MANIFEST`.
- [ ] **Step 6 — run (real data).** `uv run snakemake -s
      code/workflows/wave1-mr-hormone/Snakefile --use-conda -c1 build_instruments`.
      (First run builds the r-mr env + installs/asserts TwoSampleMR.) Per-stratum
      wall-clock **and max_rss** captured by `benchmark:`.
- [ ] **Step 7 — inspect.** Read `instruments_manifest.json`: six strata, each
      with attrition counts, `n_instruments`, `mean_F`, `eligible_for_mr` +
      reasons, and `max_rss_mb`. Confirm the expected pattern (SHBG/testosterone
      combined + male well-powered; watch the female-testosterone stratum for
      `weak_mean_f`/`too_few_instruments`) — and that any small set is explained
      by the **attrition trail**, not a silent rsID-join/panel-mismatch.
- [ ] **Step 8 — validate + note.** `uv run --frozen science validate`; record a
      t089 note summarising per-stratum instrument counts / mean-F / eligibility /
      peak RSS; rebuild the graph if any entity changed; commit.

## Validation / Definition of done

- All six strata produce a sidecar + benchmark + appear in
  `instruments_manifest.json`; the aggregator hard-stops on any missing/malformed
  sidecar or benchmark.
- Every emitted instrument SNP has `pval < 5×10⁻⁸` (asserted in the builder);
  clumping was local, by rsID, r²<0.001 / 10 Mb; `mhc_excluded: false` recorded.
- **Per-boundary attrition (F2)** recorded per stratum (`n_rows` → `n_complete`
  → `n_missing_rsid` → `n_passing_p` → `n_clump_input` → `n_clumped`,
  `n_absent_in_panel`) with a clump-log path; any small instrument set is
  explained by the trail, not silent.
- `mean_F` and `n_instruments` reported per stratum; eligibility (`mean_F >
  f_min` **and** `n ≥ min_instruments_mr`) + reasons set by the tiered gate;
  `below_target_n` recorded where `n < 10`.
- Technical faults demonstrably hard-stop (spot-checked): missing column / plink
  failure / non-finite F, and the two **distinct** zero-instrument messages
  (zero GWS variants vs all lost in matching/clumping).
- **Version gate (F1):** setup hard-fails unless `TwoSampleMR == 0.7.9` and
  `ieugwasr` matches the expected pin; resolved versions in the sentinel/manifest.
- **Peak memory (F3):** per-stratum `max_rss_mb` + wall-clock from `benchmark:`
  in the manifest `resource` block; `peak_rss_mb` reported.
- `git status` shows nothing under `data/`; the manifest lives under
  `results/wave1-mr-hormone-pilot/` (gitignored, regenerable); config pins
  reproduce it.

## Decision criteria (inherited from plan:0009)

- Mechanics-GO signal for the instrument stage: each stratum yields a workable
  independent set (**target ≳ 10**) with **mean F > 10** → `eligible_for_mr`.
- A weak/underpowered stratum (esp. female testosterone) → **quarantined**, which
  is an **informative scientific outcome**, not a pipeline failure; Task 3/4 skip
  or loudly flag it.
- NO-GO / fix-first only on a **technical** fault (zero instruments from a valid
  file, unresolved column, clump failure) — repair before proceeding.

## Resolved: gate inequality (F4)

`plan:0009` states the F-floor two ways — Task 2 "halt if mean F < 10" and
Decision-criteria "mean F > 10". **Decision (2026-07-04): keep `mean_F > f_min`**
— the stricter reading, so a borderline stratum is quarantined rather than
silently passed, and the parent plan is not relaxed. The implementation carries
the explicit gate (`eligible = mean_F > f_min AND n_instruments ≥
min_instruments_mr`; `weak_mean_f` when `mean_F ≤ f_min`), which is the single
source of truth; no amendment to `plan:0009` prose is required.

## Out of scope (this increment)

- Any harmonisation against the outcome or MR estimate (Task 3).
- The MRlap canonicalization/overlap stack and its `r-mrlap` + `r-genomicsem`
  env extension (Task 4).
- BMI-adjusted / bioavailable-testosterone / estradiol strata (later increment).

## Notes on scope

One science-task increment sized to a probe: build and F-gate the six
instruments and stop, so the exposure viability (counts, mean-F, quarantine
flags) is inspected **before** any outcome-facing estimate exists — preserving
the pre-result discipline. Task 3 (naive IVW/Egger/weighted-median) reuses this
same `r-mr` env and the emitted instrument TSVs.
