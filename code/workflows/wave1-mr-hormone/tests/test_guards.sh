#!/usr/bin/env bash
# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#
# Guard-fixture test for harmonize_estimate.R (plan:0009 Task 3, Step 5).
#
# Exercises the two non-fatal safety paths on tiny synthetic fixtures — no
# conda env beyond r-mr (TwoSampleMR must be installed, i.e. run this AFTER
# `setup_twosamplemr` has produced .setup_twosamplemr.json), no outcome
# download, no real instruments:
#
#   (a) quarantine: a sidecar with eligible_for_mr=false must drive
#       status="skipped-quarantined", a header-only (1-line) harmonised TSV,
#       and no methods emitted — the estimator core must never run.
#   (b) weak: a 2-instrument TSV harmonised against a matching 2-row fake
#       outcome (both SNPs present, no drops needed) must drive
#       status="insufficient-harmonised-instruments" without crashing, and no
#       methods emitted.
#
# Usage: bash code/workflows/wave1-mr-hormone/tests/test_guards.sh
# (run from the repo root; requires the r-mr conda env active — Rscript with
# data.table + jsonlite + yaml + TwoSampleMR on the library path)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
SCRIPT="$REPO_ROOT/code/workflows/wave1-mr-hormone/scripts/harmonize_estimate.R"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

fail() { echo "FAIL: $*" >&2; exit 1; }

# --- shared tiny config -------------------------------------------------------
cat > "$WORK/config.yaml" <<'EOF'
exposures:
  - name: "fake-stratum"
    accession: "GCSTFAKE"
    trait: "fake-hormone"
    sex: "combined"
outcome:
  name: "fake-outcome"
  accession: "GCSTFAKEOUT"
harmonise:
  action: 2
estimate:
  methods: ["mr_ivw", "mr_egger_regression", "mr_weighted_median"]
  weighted_median_seed: 20260705
  weighted_median_bootstrap_n: 1000
  harmonisation_dropout_warn_frac: 0.5
EOF

# =============================================================================
# (a) quarantine path — eligible_for_mr: false
# =============================================================================
mkdir -p "$WORK/a"
cat > "$WORK/a/sidecar.json" <<'EOF'
{
  "stratum": "fake-stratum", "accession": "GCSTFAKE", "trait": "fake-hormone", "sex": "combined",
  "eligible_for_mr": false, "eligibility_reasons": ["weak_mean_f", "too_few_instruments"],
  "quality_flags": []
}
EOF
# Instrument/outcome are never read once quarantined; still must exist as
# Snakemake inputs would.
printf "SNP\tchr\tpos\tEA\tOA\tbeta\tse\teaf\tpval\tF\n" > "$WORK/a/instrument.tsv"
printf "" | gzip > "$WORK/a/outcome.h.tsv.gz"

Rscript "$SCRIPT" --config "$WORK/config.yaml" --stratum fake-stratum \
  --instrument "$WORK/a/instrument.tsv" --sidecar "$WORK/a/sidecar.json" \
  --outcome "$WORK/a/outcome.h.tsv.gz" \
  --harmonised-out "$WORK/a/harmonised.tsv" --results-out "$WORK/a/results.json"

grep -q '"status": *"skipped-quarantined"' "$WORK/a/results.json" \
  || fail "(a) expected status skipped-quarantined, got: $(cat "$WORK/a/results.json")"
grep -q '"methods": *\[\]' "$WORK/a/results.json" \
  || fail "(a) expected empty methods array, got: $(cat "$WORK/a/results.json")"
n_lines_a="$(wc -l < "$WORK/a/harmonised.tsv")"
[ "$n_lines_a" -eq 1 ] || fail "(a) expected header-only (1-line) harmonised TSV, got $n_lines_a lines"
echo "PASS (a) quarantine: status=skipped-quarantined, methods=[], harmonised TSV header-only"

# =============================================================================
# (b) weak path — 2 instruments harmonised against a matching 2-row outcome
#     (both present -> guaranteed <3 kept regardless of any drop)
# =============================================================================
mkdir -p "$WORK/b"
cat > "$WORK/b/sidecar.json" <<'EOF'
{
  "stratum": "fake-stratum", "accession": "GCSTFAKE", "trait": "fake-hormone", "sex": "combined",
  "eligible_for_mr": true, "eligibility_reasons": [], "quality_flags": []
}
EOF
printf "SNP\tchr\tpos\tEA\tOA\tbeta\tse\teaf\tpval\tF\n" > "$WORK/b/instrument.tsv"
printf "rs1\t1\t1000\tA\tG\t0.01\t0.002\t0.3\t1e-9\t25\n" >> "$WORK/b/instrument.tsv"
printf "rs2\t2\t2000\tC\tT\t0.02\t0.003\t0.4\t1e-10\t44\n" >> "$WORK/b/instrument.tsv"

{
  printf "hm_rsid\thm_chrom\thm_pos\thm_effect_allele\thm_other_allele\thm_beta\tstandard_error\thm_effect_allele_frequency\tp_value\n"
  printf "rs1\t1\t1000\tA\tG\t0.05\t0.01\t0.3\t0.01\n"
  printf "rs2\t2\t2000\tC\tT\t-0.03\t0.02\t0.4\t0.02\n"
} | gzip > "$WORK/b/outcome.h.tsv.gz"

Rscript "$SCRIPT" --config "$WORK/config.yaml" --stratum fake-stratum \
  --instrument "$WORK/b/instrument.tsv" --sidecar "$WORK/b/sidecar.json" \
  --outcome "$WORK/b/outcome.h.tsv.gz" \
  --harmonised-out "$WORK/b/harmonised.tsv" --results-out "$WORK/b/results.json"

grep -q '"status": *"insufficient-harmonised-instruments"' "$WORK/b/results.json" \
  || fail "(b) expected status insufficient-harmonised-instruments, got: $(cat "$WORK/b/results.json")"
grep -q '"methods": *\[\]' "$WORK/b/results.json" \
  || fail "(b) expected empty methods array, got: $(cat "$WORK/b/results.json")"
echo "PASS (b) weak: status=insufficient-harmonised-instruments, methods=[], no crash"

echo "test_guards.sh: ALL PASS"
