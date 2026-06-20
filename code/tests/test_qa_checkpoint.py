#!/usr/bin/env python3
"""Corrupted-fixture halt test for the WP2 QA checkpoint (plan:0003 WP2 DoD).

Proves the two-severity contract end-to-end WITHOUT a pytest dependency:
  * clean inputs  -> exit 0, sentinel WRITTEN (positive control);
  * each deliberately-corrupted fixture -> exit non-zero, sentinel WITHHELD
    (so a Snakemake DAG built on the sentinel would halt).

Run:  python code/tests/test_qa_checkpoint.py   (exits non-zero on any failure)
"""
from __future__ import annotations

import gzip
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QA = ROOT / "code" / "scripts" / "qa_checkpoint.py"
CONFIG = ROOT / "code" / "workflows" / "config.yaml"
PROC = ROOT / "data" / "processed"

G14577 = {
    "gpl96": PROC / "GSE14577/expr_GPL96.probe_x_sample.tsv.gz",
    "gpl97": PROC / "GSE14577/expr_GPL97.probe_x_sample.tsv.gz",
    "meta": PROC / "GSE14577/sample_metadata.tsv",
}
G130353 = {
    "sheet": PROC / "GSE130353/sample_sheet.tsv",
    "contract": PROC / "GSE130353/parse_contract.json",
}

_PASS = 0
_FAIL = 0


def run_qa(dataset: str, paths: dict, workdir: Path) -> tuple[int, bool]:
    """Invoke qa_checkpoint.py against `paths`; return (returncode, sentinel_exists)."""
    sentinel = workdir / "out.qa.pass"
    report = workdir / "report.md"
    cmd = [sys.executable, str(QA), "--dataset", dataset, "--config", str(CONFIG),
           "--report", str(report), "--sentinel", str(sentinel)]
    for k, v in paths.items():
        cmd += [f"--{k}", str(v)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, sentinel.exists()


def expect(label: str, cond: bool) -> None:
    global _PASS, _FAIL
    if cond:
        _PASS += 1
        print(f"  ok   {label}")
    else:
        _FAIL += 1
        print(f"  FAIL {label}")


def drop_last_column_gz(src: Path, dst: Path) -> None:
    with gzip.open(src, "rt", encoding="utf-8") as fh:
        rows = [ln.rstrip("\n").split("\t")[:-1] for ln in fh]
    with open(dst, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as gz:
        gz.write(("\n".join("\t".join(r) for r in rows) + "\n").encode("utf-8"))


def main() -> int:
    if not all(p.exists() for p in (*G14577.values(), *G130353.values())):
        print("FAIL: real WP1 inputs missing — run acquisition first", file=sys.stderr)
        return 2

    # --- positive controls: clean inputs must PASS + write the sentinel -------
    print("[positive control]")
    with tempfile.TemporaryDirectory() as d:
        rc, sen = run_qa("gse14577", G14577, Path(d))
        expect("clean gse14577 -> exit 0 + sentinel written", rc == 0 and sen)
    with tempfile.TemporaryDirectory() as d:
        rc, sen = run_qa("gse130353", G130353, Path(d))
        expect("clean gse130353 -> exit 0 + sentinel written", rc == 0 and sen)

    # --- corrupted fixtures: each must HALT (exit!=0) + WITHHOLD the sentinel --
    print("[corrupted fixtures -> must halt]")

    # 1. GSE14577 metadata missing a required group code (drop all HC rows)
    with tempfile.TemporaryDirectory() as d:
        w = Path(d)
        meta = (G14577["meta"]).read_text().splitlines()
        gi = meta[0].split("\t").index("group")
        kept = [meta[0]] + [r for r in meta[1:] if r.split("\t")[gi] != "HC"]
        (w / "meta.tsv").write_text("\n".join(kept) + "\n")
        rc, sen = run_qa("gse14577", {**G14577, "meta": w / "meta.tsv"}, w)
        expect("gse14577 missing HC group -> halt, no sentinel", rc != 0 and not sen)

    # 2. GSE14577 GPL96 truncated by one sample column -> n_samples 14 != 15
    with tempfile.TemporaryDirectory() as d:
        w = Path(d)
        drop_last_column_gz(G14577["gpl96"], w / "gpl96.tsv.gz")
        rc, sen = run_qa("gse14577", {**G14577, "gpl96": w / "gpl96.tsv.gz"}, w)
        expect("gse14577 GPL96 truncated column -> halt, no sentinel", rc != 0 and not sen)

    # 3. GSE130353 sheet group counts broken (relabel one QFS row to 'unknown')
    with tempfile.TemporaryDirectory() as d:
        w = Path(d)
        sheet = G130353["sheet"].read_text().splitlines()
        gi = sheet[0].split("\t").index("group")
        out = [sheet[0]]
        flipped = False
        for r in sheet[1:]:
            cells = r.split("\t")
            if cells[gi] == "QFS" and not flipped:
                cells[gi] = "unknown"
                flipped = True
            out.append("\t".join(cells))
        (w / "sheet.tsv").write_text("\n".join(out) + "\n")
        rc, sen = run_qa("gse130353", {**G130353, "sheet": w / "sheet.tsv"}, w)
        expect("gse130353 broken group counts -> halt, no sentinel", rc != 0 and not sen)

    # 4. GSE130353 contract with G2 verdict flipped to HALT
    with tempfile.TemporaryDirectory() as d:
        w = Path(d)
        c = json.loads(G130353["contract"].read_text())
        c["g2_verdict"]["verdict"] = "HALT"
        (w / "contract.json").write_text(json.dumps(c))
        rc, sen = run_qa("gse130353", {**G130353, "contract": w / "contract.json"}, w)
        expect("gse130353 G2 verdict HALT -> halt, no sentinel", rc != 0 and not sen)

    # --- distribution severity: a warning must SURFACE but NOT halt -----------
    print("[distribution severity -> surfaced, not fatal]")
    # set one GPL96 cell above the log2 ceiling (dims unchanged -> structural OK)
    with tempfile.TemporaryDirectory() as d:
        w = Path(d)
        with gzip.open(G14577["gpl96"], "rt", encoding="utf-8") as fh:
            rows = [ln.rstrip("\n").split("\t") for ln in fh]
        rows[1][1] = "999.0"  # first data row, first sample -> > log2 ceiling 16
        with open(w / "gpl96.tsv.gz", "wb") as raw, gzip.GzipFile(
            filename="", mode="wb", fileobj=raw, mtime=0
        ) as gz:
            gz.write(("\n".join("\t".join(r) for r in rows) + "\n").encode("utf-8"))
        rc, sen = run_qa("gse14577", {**G14577, "gpl96": w / "gpl96.tsv.gz"}, w)
        report = (w / "report.md").read_text() if (w / "report.md").exists() else ""
        expect("gse14577 out-of-range value -> exit 0 + sentinel written (not fatal)",
               rc == 0 and sen)
        expect("gse14577 out-of-range value -> warning surfaced in report",
               "log2 ceiling" in report and "Distribution warnings:** 1" in report)

    print(f"\n{_PASS} passed, {_FAIL} failed")
    return 1 if _FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
