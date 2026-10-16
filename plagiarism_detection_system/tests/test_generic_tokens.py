import unittest

from plagiarism_detector.tokenize import normalize_tokens


class GenericTokenTests(unittest.TestCase):
    def test_identifiers_and_numbers_normalize(self):
        left = normalize_tokens("int add(int a) { return a + 1; }", "cpp")
        right = normalize_tokens("int f(int b) { return b + 8; }", "cpp")
        self.assertEqual([t.value for t in left], [t.value for t in right])

    def test_line_comment_is_ignored(self):
        tokens = normalize_tokens("let x = 2; // comment\n", "javascript")
        self.assertNotIn("comment", [t.value for t in tokens])
