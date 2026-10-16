import unittest

from plagiarism_detector.web import analyze


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
            analyze({"files": [{"name": "a.txt", "content": "x"},
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
