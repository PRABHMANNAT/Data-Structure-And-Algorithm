import unittest

from textloom.core import diff
from textloom.extra import apply, invert
from textloom.models import Edit


class CoreTests(unittest.TestCase):
    def test_empty_documents(self):
        self.assertEqual(diff([], []), [])

    def test_newline_fidelity(self):
        a = ["a\n", "last"]
        b = ["a\n", "last\n"]
        edits = diff(a, b)
        self.assertEqual(apply(a, edits), b)
        self.assertEqual(apply(b, invert(edits)), a)

    def test_source_mismatch(self):
        with self.assertRaises(ValueError):
            apply(["wrong"], [Edit("delete", "expected")])

    def test_unchanged(self):
        self.assertTrue(all(e.kind == "equal" for e in diff(["a", "b"], ["a", "b"])))
