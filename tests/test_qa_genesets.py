from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "code/scripts/qa_genesets.R"


def _run_r(code: str, cwd: Path) -> None:
    subprocess.run(["Rscript", "-e", code], cwd=cwd, check=True, text=True)


class GeneSetQATest(unittest.TestCase):
    def test_geneset_universe_passes_and_writes_sentinel(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            tmp_path = Path(td)
            _run_r(
                """
                saveRDS(list(HALLMARK_A=c('ENSG000001','ENSG000002')), 'hallmark.rds')
                saveRDS(list(REACTOME_A=c('ENSG000003','ENSG000004')), 'reactome.rds')
                saveRDS(list(GOBP_A=c('ENSG000005','ENSG000006')), 'gobp.rds')
                """,
                tmp_path,
            )
            (tmp_path / "theme_map.tsv").write_text(
                "db\tgene_set\ttheme\tsize\n"
                "hallmark\tHALLMARK_A\tother\t2\n"
                "reactome\tREACTOME_A\tother\t2\n"
                "gobp\tGOBP_A\tother\t2\n",
                encoding="utf-8",
            )
            (tmp_path / "members.tsv").write_text(
                "set_key\tname\tmember_ids\tdb\ttheme\tsize\n"
                "hallmark:HALLMARK_A\tHALLMARK_A\tENSG000001;ENSG000002\thallmark\tother\t2\n"
                "reactome:REACTOME_A\tREACTOME_A\tENSG000003;ENSG000004\treactome\tother\t2\n"
                "gobp:GOBP_A\tGOBP_A\tENSG000005;ENSG000006\tgobp\tother\t2\n",
                encoding="utf-8",
            )
            (tmp_path / "release_hash.txt").write_text(
                "msigdb_release\tTEST\n"
                "id_space\tsymbols\n"
                "multimap_policy\tfirst\n"
                "size_filter\t2-10\n"
                "hallmark_sha256\tabc\n"
                "reactome_sha256\tdef\n"
                "gobp_sha256\tghi\n",
                encoding="utf-8",
            )
            report = tmp_path / "report.md"
            sentinel = tmp_path / "clean.qa.pass"

            result = subprocess.run(
                [
                    "Rscript",
                    str(SCRIPT),
                    "--dbs",
                    "hallmark,reactome,gobp",
                    "--rds",
                    "hallmark.rds,reactome.rds,gobp.rds",
                    "--theme-map",
                    "theme_map.tsv",
                    "--members",
                    "members.tsv",
                    "--release-hash",
                    "release_hash.txt",
                    "--expected-release",
                    "TEST",
                    "--expected-sha256s",
                    "abc,def,ghi",
                    "--min-size",
                    "2",
                    "--max-size",
                    "10",
                    "--report",
                    str(report),
                    "--sentinel",
                    str(sentinel),
                ],
                cwd=tmp_path,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(sentinel.exists())
            self.assertIn("PASS gene-set clean universe", sentinel.read_text(encoding="utf-8"))
            self.assertIn("all structural checks passed", report.read_text(encoding="utf-8"))

    def test_geneset_qa_rejects_members_table_missing_retained_set(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            tmp_path = Path(td)
            _run_r(
                """
                saveRDS(list(HALLMARK_A=c('ENSG000001','ENSG000002')), 'hallmark.rds')
                saveRDS(list(REACTOME_A=c('ENSG000003','ENSG000004')), 'reactome.rds')
                saveRDS(list(GOBP_A=c('ENSG000005','ENSG000006')), 'gobp.rds')
                """,
                tmp_path,
            )
            (tmp_path / "theme_map.tsv").write_text(
                "db\tgene_set\ttheme\tsize\n"
                "hallmark\tHALLMARK_A\tother\t2\n"
                "reactome\tREACTOME_A\tother\t2\n"
                "gobp\tGOBP_A\tother\t2\n",
                encoding="utf-8",
            )
            (tmp_path / "members.tsv").write_text(
                "set_key\tname\tmember_ids\tdb\ttheme\tsize\n"
                "hallmark:HALLMARK_A\tHALLMARK_A\tENSG000001;ENSG000002\thallmark\tother\t2\n"
                "reactome:REACTOME_A\tREACTOME_A\tENSG000003;ENSG000004\treactome\tother\t2\n",
                encoding="utf-8",
            )
            (tmp_path / "release_hash.txt").write_text(
                "msigdb_release\tTEST\n"
                "id_space\tsymbols\n"
                "multimap_policy\tfirst\n"
                "size_filter\t2-10\n"
                "hallmark_sha256\tabc\n"
                "reactome_sha256\tdef\n"
                "gobp_sha256\tghi\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    "Rscript",
                    str(SCRIPT),
                    "--dbs",
                    "hallmark,reactome,gobp",
                    "--rds",
                    "hallmark.rds,reactome.rds,gobp.rds",
                    "--theme-map",
                    "theme_map.tsv",
                    "--members",
                    "members.tsv",
                    "--release-hash",
                    "release_hash.txt",
                    "--expected-release",
                    "TEST",
                    "--expected-sha256s",
                    "abc,def,ghi",
                    "--min-size",
                    "2",
                    "--max-size",
                    "10",
                    "--report",
                    str(tmp_path / "report.md"),
                    "--sentinel",
                    str(tmp_path / "clean.qa.pass"),
                ],
                cwd=tmp_path,
                text=True,
                capture_output=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("members.tsv lacks", result.stderr)


if __name__ == "__main__":
    unittest.main()
