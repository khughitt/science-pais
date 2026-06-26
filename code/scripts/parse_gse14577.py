# science:code
# status: exploratory
# task_ids: [t035]
# science:end

#!/usr/bin/env python3
"""Parse GSE14577 family SOFT -> per-platform probe x sample matrices (t035 WP1).

Rule-callable refactor of the original `g1_acquire.parse_gse14577`. Reads the
LOCAL `GSE14577_family.soft.gz` (the series_matrix 404s upstream) and writes,
into `--out-dir`:

  expr_GPL96.probe_x_sample.tsv.gz   U133A, as-deposited (NO collapse/normalize)
  expr_GPL97.probe_x_sample.tsv.gz   U133B
  sample_metadata.tsv                accession/group/patient_key/chip/platform/sex/title
  parse_contract.json                scale stats + group counts + independent-unit note

As-deposited only: probe->gene collapse, normalization, and filtering are
pipeline steps (WP3/WP4), NOT acquisition. The independent unit is the patient
(1 patient = chip A GPL96 + chip B GPL97); pairing happens at the collapse step.
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from pathlib import Path

from acquire_common import scale_stats, sha256_path

PLATFORM_FILENAMES = {
    "GPL96": "expr_GPL96.probe_x_sample.tsv.gz",
    "GPL97": "expr_GPL97.probe_x_sample.tsv.gz",
}


def parse(soft: Path) -> tuple[dict, dict]:
    """Return (samples, matrices) parsed from the SOFT. No file writes."""
    samples: dict[str, dict] = {}
    cur = None
    in_table = False
    header = None
    matrices: dict[str, dict[str, dict[str, float]]] = {}

    with gzip.open(soft, "rt", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("^SAMPLE = "):
                cur = line.split(" = ", 1)[1].strip()
                samples[cur] = {"accession": cur}
                in_table = False
                header = None
            elif line.startswith("!Sample_title = ") and cur:
                samples[cur]["title"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!Sample_characteristics_ch1 = ") and cur:
                samples[cur]["characteristics"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!Sample_platform_id = ") and cur:
                samples[cur]["platform"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!sample_table_begin"):
                in_table = True
                header = None
            elif line.startswith("!sample_table_end"):
                in_table = False
            elif in_table and cur:
                if header is None:
                    header = line.split("\t")
                    continue
                parts = line.split("\t")
                if len(parts) < 2:
                    continue
                probe, val = parts[0], parts[1]
                try:
                    fval = float(val)
                except ValueError:
                    continue
                plat = samples[cur].get("platform", "UNKNOWN")
                matrices.setdefault(plat, {}).setdefault(probe, {})[cur] = fval

    # derive group / chip / patient key from title + characteristics
    for s in samples.values():
        title = s.get("title", "")
        chars = s.get("characteristics", "")
        s["sex"] = "Male" if "Male" in chars else ("Female" if "Female" in chars else "unknown")
        if "post-infectious CFS" in chars or title.lower().startswith("cfs"):
            s["group"] = "PI-CFS"
        elif "healthy normal control" in chars or title.lower().startswith("control"):
            s["group"] = "HC"
        else:
            s["group"] = "unknown"
        m = re.search(r"patient\s+(\d+)", title)
        num = m.group(1) if m else "NA"
        chip = "B" if "chip B" in title else ("A" if "chip A" in title else "NA")
        s["chip"] = chip
        s["platform_chip"] = f"{s.get('platform', '?')}/{chip}"
        s["patient_key"] = f"{s['group']}_{num}"  # unique within group
    return samples, matrices


def write_matrices(matrices: dict, out_dir: Path) -> dict:
    platform_summaries = {}
    for plat, probes in matrices.items():
        fname = PLATFORM_FILENAMES.get(plat, f"expr_{plat}.probe_x_sample.tsv.gz")
        plat_samples = sorted({sm for p in probes.values() for sm in p})
        mat_path = out_dir / fname
        all_vals: list[float] = []
        lines = ["ID_REF\t" + "\t".join(plat_samples) + "\n"]
        for probe in sorted(probes):
            row = probes[probe]
            vals = [row.get(sm) for sm in plat_samples]
            all_vals.extend(v for v in vals if v is not None)
            lines.append(probe + "\t" + "\t".join("" if v is None else f"{v:.6g}" for v in vals) + "\n")
        # deterministic gzip: no embedded filename, mtime=0 (plan:0003 KD10) so
        # re-runs are byte-identical, not just content-identical.
        with open(mat_path, "wb") as raw, gzip.GzipFile(
            filename="", mode="wb", fileobj=raw, mtime=0
        ) as gz:
            gz.write("".join(lines).encode("utf-8"))
        platform_summaries[plat] = {
            "matrix_file": fname,
            "n_probes": len(probes),
            "n_samples": len(plat_samples),
            "samples": plat_samples,
            "scale_stats": scale_stats(all_vals),
            "sha256": sha256_path(mat_path),
        }
    return platform_summaries


def write_metadata(samples: dict, meta_path: Path) -> None:
    cols = ["accession", "group", "patient_key", "chip", "platform", "platform_chip", "sex", "title"]
    with meta_path.open("w", encoding="utf-8") as w:
        w.write("\t".join(cols) + "\n")
        for acc in sorted(samples):
            s = samples[acc]
            w.write("\t".join(str(s.get(c, "")) for c in cols) + "\n")


def run(soft: Path, out_dir: Path) -> dict:
    """Parse + write all GSE14577 outputs into out_dir; return the contract dict."""
    if not soft.exists():
        sys.exit(f"[parse_gse14577] HALT: missing {soft}")
    out_dir.mkdir(parents=True, exist_ok=True)

    samples, matrices = parse(soft)
    platform_summaries = write_matrices(matrices, out_dir)
    meta_path = out_dir / "sample_metadata.tsv"
    write_metadata(samples, meta_path)

    groups: dict[str, int] = {}
    patients: set[str] = set()
    for s in samples.values():
        groups[s["group"]] = groups.get(s["group"], 0) + 1
        patients.add(s["patient_key"])

    contract = {
        "dataset": "GSE14577",
        "source": "parsed from local GSE14577_family.soft.gz (series_matrix 404s)",
        "delimiter": "tab",
        "table_columns": ["ID_REF", "VALUE"],
        "value_semantics": "depositor VALUE column; scale stats below confirm log2 intensities",
        "platforms": platform_summaries,
        "n_geo_samples": len(samples),
        "group_counts_samples": groups,
        "n_unique_patients": len(patients),
        "sample_metadata": meta_path.name,
        "independent_unit_note": "1 patient = 2 GEO samples (chip A GPL96 + chip B GPL97); pair on patient_key at collapse step",
        "status": "parsed",
    }
    (out_dir / "parse_contract.json").write_text(json.dumps(contract, indent=2) + "\n")

    for plat, ps in platform_summaries.items():
        ss = ps["scale_stats"]
        print(f"[parse_gse14577] {plat}: {ps['n_probes']} probes x {ps['n_samples']} samples; "
              f"min={ss['min']} max={ss['max']} %int={ss['pct_integer_like']}", file=sys.stderr)
    print(f"[parse_gse14577] groups(samples)={groups} unique_patients={len(patients)}", file=sys.stderr)
    return contract


def main() -> int:
    ap = argparse.ArgumentParser(description="parse GSE14577 SOFT -> matrices + contract")
    ap.add_argument("--soft", required=True, type=Path)
    ap.add_argument("--out-dir", required=True, type=Path)
    args = ap.parse_args()
    run(args.soft, args.out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
