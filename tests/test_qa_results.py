from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from qa_results import check_results


CONFIG = {
    "contrasts": {
        "c1": {"dataset": "d1", "case": "A", "control": "B"},
        "c2": {"dataset": "d2", "case": "C", "control": "D"},
    },
    "genesets": {
        "primary_db": "hallmark",
        "databases": {"hallmark": {}, "reactome": {}},
    },
    "concordance_pairs": {
        "primary": {"x": "c1", "y": "c2"},
    },
    "permutation": {"B": 3},
    "specificity": {"nominal_p": 0.05},
    "verdict": {
        "p_perm_alpha": 0.05,
        "resolution_order": ["null_nonarbitrating"],
    },
}


def _write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(header) + "\n")
        for row in rows:
            fh.write("\t".join(str(x) for x in row) + "\n")


def _write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _populate_bundle(root: Path, *, verdict_p_perm: float = 0.2) -> tuple[Path, Path]:
    processed = root / "data/processed"
    results = root / "results"
    gene_sets = ["SET_A", "SET_B", "SET_C"]

    for contrast in CONFIG["contrasts"]:
        _write_tsv(
            processed / "de" / f"{contrast}.ranked.tsv",
            ["gene_id", "logFC", "t", "P.Value", "adj.P.Val"],
            [
                ["ENSG000001", 1.0, 3.0, 0.01, 0.03],
                ["ENSG000002", -0.5, -2.0, 0.2, 0.4],
            ],
        )
        _write_json(
            processed / "de" / f"{contrast}.diag.json",
            {
                "contrast": contrast,
                "full_rank": True,
                "residual_df": 6,
                "n_genes_tested": 2,
            },
        )

    for contrast in CONFIG["contrasts"]:
        for db in CONFIG["genesets"]["databases"]:
            _write_tsv(
                processed / "fgsea" / f"{contrast}.{db}.nes.tsv",
                ["gene_set", "db", "contrast", "NES", "pval", "padj", "size"],
                [[s, db, contrast, i + 1.0, 0.01 * (i + 1), 0.02 * (i + 1), 15 + i]
                 for i, s in enumerate(gene_sets)],
            )

    for db in CONFIG["genesets"]["databases"]:
        _write_tsv(
            processed / "concordance" / f"primary.{db}.rho.tsv",
            ["pair", "db", "rho_obs", "n_shared", "n_na_x", "n_na_y", "n_dropped_either"],
            [["primary", db, 0.5, 3, 0, 0, 0]],
        )
        _write_tsv(
            processed / "concordance" / f"primary.{db}.scatter.tsv",
            ["gene_set", "contrast_x", "contrast_y", "nes_x", "nes_y"],
            [[s, "c1", "c2", i + 1.0, i + 1.5] for i, s in enumerate(gene_sets)],
        )
        _write_tsv(
            processed / "perm" / f"primary.{db}.perm.tsv",
            ["pair", "db", "rho_obs", "p_perm", "B"],
            [["primary", db, 0.49, 0.2, 3]],
        )
        _write_tsv(
            processed / "perm" / f"primary.{db}.nulldist.tsv",
            ["perm_index", "rho_perm"],
            [[1, 0.1], [2, 0.2], [3, 0.3]],
        )
        _write_tsv(
            processed / "specificity" / f"{db}.classes.tsv",
            [
                "gene_set", "db", "nes_qfs_vs_hc", "dir_qfs_vs_hc",
                "nes_qfs_vs_qs", "p_qfs_vs_qs", "s1_pos",
                "nes_qs_vs_hc", "p_qs_vs_hc", "s2_pos", "spec_class",
            ],
            [[s, db, 1.0, 1, 1.1, 0.01, "True", 0.9, 0.2, "False", "fatigue-specific"]
             for s in gene_sets],
        )
        _write_tsv(
            processed / "rollup" / f"{db}.themes.tsv",
            [
                "theme", "db", "n_carrying", "n_fatigue_specific",
                "n_exposure_sequela", "n_unresolved", "theme_class",
                "theme_direction", "verdict_eligible", "rep_set",
            ],
            [["innate/IFN", db, 3, 3, 0, 0, "fatigue-specific", 1, "True", "SET_A"]],
        )

    _write_tsv(
        processed / "rollup/db_robustness.tsv",
        [
            "theme", "n_dbs_fatigue_specific", "dbs_fatigue_specific",
            "fs_directions", "robust_direction", "db_robust",
        ],
        [["innate/IFN", 2, "hallmark,reactome", "hallmark:+1,reactome:+1", 1, "True"]],
    )
    _write_tsv(
        processed / "rollup/compartment.tsv",
        [
            "db", "n_carrying", "n_marker", "marker_fraction",
            "compartment_confounded", "status", "marker_sets",
        ],
        [["hallmark", 3, 0, 0.0, "False", "not_marker_dominated", ""]],
    )
    _write_json(
        results / "verdict.json",
        {
            "verdict": "null_nonarbitrating",
            "confirmatory": {
                "pair": "primary",
                "db": "hallmark",
                "rho_obs_multilevel": 0.5,
                "rho_obs_perm": 0.49,
                "p_perm": verdict_p_perm,
                "B": 3,
                "alpha": 0.05,
            },
            "sensitivity_surface": [
                {"pair": "primary", "db": db, "rho_obs": 0.5, "p_perm": 0.2, "B": 3, "n_shared": 3}
                for db in CONFIG["genesets"]["databases"]
            ],
            "admissibility": {
                "limma_ok": True,
                "per_contrast": {
                    contrast: {"full_rank": True, "residual_df": 6, "n_genes_tested": 2}
                    for contrast in CONFIG["contrasts"]
                },
            },
            "specificity_summary": {
                db: {"fatigue-specific": 3}
                for db in CONFIG["genesets"]["databases"]
            },
            "theme_sets": {
                "fatigue_specific_any_db": ["innate/IFN"],
                "exposure_sequela_any_db": [],
                "db_robust": ["innate/IFN"],
            },
            "compartment": {
                "db": "hallmark",
                "n_carrying": 3,
                "n_marker": 0,
                "marker_fraction": 0.0,
                "compartment_confounded": False,
                "status": "not_marker_dominated",
            },
            "resolution_trace": [
                {"step": 1, "label": "null_nonarbitrating", "reached": True, "fired": True, "decided": True}
            ],
        },
    )
    (results / "results.md").write_text("# Synthetic result\n", encoding="utf-8")
    _write_json(results / "run_metadata.json", {"verdict": "null_nonarbitrating"})
    return processed, results


class ResultQATest(unittest.TestCase):
    def test_complete_result_bundle_passes_and_writes_sentinel(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            processed, results = _populate_bundle(Path(td))
            report = Path(td) / "qa_report.md"
            sentinel = Path(td) / "qa.pass"

            rc = check_results(
                processed=processed,
                results=results,
                config=CONFIG,
                report=report,
                sentinel=sentinel,
            )

            self.assertEqual(rc, 0)
            self.assertTrue(sentinel.exists())
            self.assertIn("PASS t035 result QA", sentinel.read_text(encoding="utf-8"))
            self.assertIn("all structural checks passed", report.read_text(encoding="utf-8"))

    def test_verdict_confirmatory_mismatch_fails_without_sentinel(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            processed, results = _populate_bundle(Path(td), verdict_p_perm=0.99)
            report = Path(td) / "qa_report.md"
            sentinel = Path(td) / "qa.pass"

            rc = check_results(
                processed=processed,
                results=results,
                config=CONFIG,
                report=report,
                sentinel=sentinel,
            )

            self.assertEqual(rc, 1)
            self.assertFalse(sentinel.exists())
            self.assertIn("confirmatory p_perm", report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
