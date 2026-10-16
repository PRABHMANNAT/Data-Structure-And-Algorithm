import unittest
import base64

from plagiarism_detector.web import analyze
from tests.test_ingest_docx import make_docx


class WebAnalysisTests(unittest.TestCase):
    def test_renamed_pair_returns_review_evidence(self):
        result = analyze({"files": [
            {"name": "original.py", "content": "def f(x): return x + 1"},
            {"name": "renamed.py", "content": "def g(y): return y + 2"},
        ]})
        self.assertEqual(result["files"], 2)
        self.assertEqual(len(result["matches"]), 1)
        self.assertEqual(result["matches"][0]["score"], 1.0)
        self.assertTrue(result["matches"][0]["evidence"])

    def test_invalid_uploads_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "between 2 and 50"):
            analyze({"files": []})
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            analyze({"files": [{"name": "a.xyz", "content": "x"},
                               {"name": "b.py", "content": "y"}]})
        with self.assertRaisesRegex(ValueError, "unique"):
            analyze({"files": [{"name": "a.py", "content": "x"},
                               {"name": "a.py", "content": "y"}]})

    def test_names_are_reduced_to_basename(self):
        result = analyze({"files": [
            {"name": "folder\\one.py", "content": "def f(x): return x + 1"},
            {"name": "../two.py", "content": "def f(x): return x + 1"},
        ]})
        self.assertEqual((result["matches"][0]["left"], result["matches"][0]["right"]),
                         ("one.py", "two.py"))

    def test_binary_docx_upload_matches_plain_text(self):
        phrase = "The quick brown fox jumps over the lazy dog"
        result = analyze({"files": [
            {"name": "essay.docx", "content_base64": base64.b64encode(make_docx([phrase])).decode()},
            {"name": "notes.txt", "content": phrase},
        ]})
        self.assertEqual(len(result["matches"]), 1)

    def test_invalid_base64_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Invalid encoded content"):
            analyze({"files": [{"name": "a.pdf", "content_base64": "%%%"},
                               {"name": "b.txt", "content": "text"}]})
