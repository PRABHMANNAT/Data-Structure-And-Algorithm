import unittest

from plagiarism_detector.tokenize import normalize_tokens


class PythonTokenTests(unittest.TestCase):
    def test_names_and_literals_normalize(self):
        a = normalize_tokens("def add(x): return x + 4", "python")
        b = normalize_tokens("def sum(y): return y + 9", "python")
        self.assertEqual([x.value for x in a], [x.value for x in b])

    def test_comments_and_spacing_do_not_change_tokens(self):
        a = normalize_tokens("x=1 # note\n", "python")
        b = normalize_tokens("other = 2\n", "python")
        self.assertEqual([x.value for x in a], [x.value for x in b])
