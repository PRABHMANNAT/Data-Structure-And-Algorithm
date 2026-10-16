import unittest

from plagiarism_detector.tokenize import normalize_tokens


class TokenErrorTests(unittest.TestCase):
    def test_unterminated_python_string_raises(self):
        with self.assertRaises(ValueError):
            normalize_tokens('x = "unterminated', "python")

    def test_empty_input_is_valid(self):
        self.assertEqual(normalize_tokens("", "python"), [])
