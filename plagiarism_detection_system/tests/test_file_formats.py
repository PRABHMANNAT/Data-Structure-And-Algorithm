import tempfile
import unittest
from pathlib import Path

from plagiarism_detector import Detector
from plagiarism_detector.files import discover
from tests.test_ingest_docx import make_docx
from tests.test_ingest_pdf import make_pdf


class FileFormatDiscoveryTests(unittest.TestCase):
    def test_directory_scan_compares_pdf_docx_and_txt(self):
        phrase = "The quick brown fox jumps over the lazy dog"
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "a.pdf").write_bytes(make_pdf(phrase))
            (root / "b.docx").write_bytes(make_docx([phrase]))
            (root / "c.txt").write_text(phrase, encoding="utf-8")
            documents = discover(root)
            self.assertEqual(len(documents), 3)
            self.assertEqual(len(Detector().compare(documents)), 3)
