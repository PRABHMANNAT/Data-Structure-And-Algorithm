import unittest

from plagiarism_detector.tokenize import normalize_tokens


class PythonPositionTests(unittest.TestCase):
    def test_line_and_column_are_preserved(self):
        tokens = normalize_tokens("x = 1\nprint(x)\n", "python")
        self.assertEqual((tokens[0].line, tokens[0].column), (1, 0))
        self.assertEqual((tokens[3].line, tokens[3].column), (2, 0))
