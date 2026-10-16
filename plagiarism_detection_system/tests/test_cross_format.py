import unittest

from plagiarism_detector import Detector
from plagiarism_detector.ingest import document_from_bytes
from tests.test_ingest_docx import make_docx
from tests.test_ingest_pdf import make_pdf


class CrossFormatTests(unittest.TestCase):
    def test_pdf_docx_and_txt_compare_as_prose(self):
        phrase = "The quick brown fox jumps over the lazy dog"
        docs = [document_from_bytes("a.pdf", make_pdf(phrase)),
                document_from_bytes("b.docx", make_docx([phrase])),
                document_from_bytes("c.txt", phrase.lower().encode())]
        matches = Detector().compare(docs)
        self.assertEqual(len(matches), 3)
        self.assertTrue(all(match.score == 1.0 for match in matches))

    def test_code_and_prose_use_separate_comparison_groups(self):
        code = document_from_bytes("program.py", b"def solve(x): return x + 1")
        prose = document_from_bytes("essay.txt", b"def solve x return x plus one")
        self.assertEqual(Detector().compare([code, prose]), [])
