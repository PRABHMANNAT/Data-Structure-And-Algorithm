import unittest

from plagiarism_detector.tokenize import normalize_tokens


class TokenErrorTests(unittest.TestCase):
    def test_unterminated_python_string_raises(self):
        with self.assertRaises(ValueError):
            normalize_tokens('x = "unterminated', "python")

    def test_empty_input_is_valid(self):
        self.assertEqual(normalize_tokens("", "python"), [])

    def test_other_unterminated_quotes_raise(self):
        for source in ["x = 'unterminated", 'x = """unterminated']:
            with self.subTest(source=source), self.assertRaises(ValueError):
                normalize_tokens(source, "python")

    def test_escaped_quote_remains_a_string(self):
        tokens = normalize_tokens('x = "a\\\"b"', "python")
        self.assertEqual([item.value for item in tokens], ["ID", "=", "STR"])
