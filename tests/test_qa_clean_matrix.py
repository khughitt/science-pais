from __future__ import annotations

import gzip
import json
import tempfile
import unittest
from pathlib import Path

from qa_checkpoint import check_clean_matrix


def _write_matrix(path: Path, rows: list[tuple[str, list[str]]], samples: list[str] | None = None) -> None:
    samples = samples or ["S1", "S2"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as fh:
        fh.write("ensembl_gene_id\t" + "\t".join(samples) + "\n")
        for gene, values in rows:
            fh.write(gene + "\t" + "\t".join(values) + "\n")


def _write_audit(path: Path, *, n_genes: int = 2, samples: list[str] | None = None) -> None:
    samples = samples or ["S1", "S2"]
    path.write_text(
        json.dumps(
            {
                "dataset": "SYNTH",
                "canonical_axis": "ensembl_gene_id",
                "n_patients": len(samples),
                "patients": samples,
                "counts": {"n_genes_total": n_genes},
            }
        ),
        encoding="utf-8",
    )


class CleanMatrixQATest(unittest.TestCase):
    def test_clean_matrix_passes_and_writes_sentinel(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            tmp_path = Path(td)
            matrix = tmp_path / "expr.gene.tsv.gz"
            audit = tmp_path / "cohort_audit.json"
            sentinel = tmp_path / "clean.qa.pass"
            report = tmp_path / "report.md"
            _write_matrix(matrix, [("ENSG000001", ["1.0", "2.0"]), ("ENSG000002", ["NA", "3.5"])])
            _write_audit(audit)

            rc = check_clean_matrix(
                dataset="synth",
                expr=matrix,
                audit=audit,
                expected_samples=2,
                report=report,
                sentinel=sentinel,
            )

            self.assertEqual(rc, 0)
            self.assertTrue(sentinel.exists())
            self.assertIn("PASS synth clean matrix", sentinel.read_text(encoding="utf-8"))
            self.assertIn("all structural checks passed", report.read_text(encoding="utf-8"))

    def test_clean_matrix_rejects_duplicate_gene_ids_without_sentinel(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            tmp_path = Path(td)
            matrix = tmp_path / "expr.gene.tsv.gz"
            audit = tmp_path / "cohort_audit.json"
            sentinel = tmp_path / "clean.qa.pass"
            report = tmp_path / "report.md"
            _write_matrix(matrix, [("ENSG000001", ["1.0", "2.0"]), ("ENSG000001", ["4.0", "5.0"])])
            _write_audit(audit)

            rc = check_clean_matrix(
                dataset="synth",
                expr=matrix,
                audit=audit,
                expected_samples=2,
                report=report,
                sentinel=sentinel,
            )

            self.assertEqual(rc, 1)
            self.assertFalse(sentinel.exists())
            self.assertIn("duplicate gene id", report.read_text(encoding="utf-8"))

    def test_clean_matrix_rejects_sample_audit_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            tmp_path = Path(td)
            matrix = tmp_path / "expr.gene.tsv.gz"
            audit = tmp_path / "cohort_audit.json"
            sentinel = tmp_path / "clean.qa.pass"
            report = tmp_path / "report.md"
            _write_matrix(matrix, [("ENSG000001", ["1.0", "2.0"]), ("ENSG000002", ["4.0", "5.0"])])
            _write_audit(audit, samples=["S1", "S3"])

            rc = check_clean_matrix(
                dataset="synth",
                expr=matrix,
                audit=audit,
                expected_samples=2,
                report=report,
                sentinel=sentinel,
            )

            self.assertEqual(rc, 1)
            self.assertFalse(sentinel.exists())
            self.assertIn("sample columns do not match audit sample list", report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
