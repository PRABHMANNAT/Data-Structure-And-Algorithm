import unittest

from plagiarism_detector.tokenize import normalize_tokens


class TextTokenTests(unittest.TestCase):
    def test_words_survive_case_and_punctuation_changes(self):
        left = normalize_tokens("Hello, WORLD! It's ready.", "text")
        right = normalize_tokens("hello world it's ready", "text")
        self.assertEqual([token.value for token in left], [token.value for token in right])

    def test_different_prose_keeps_different_words(self):
        a = normalize_tokens("Photosynthesis uses sunlight", "text")
        b = normalize_tokens("Graph search uses queues", "text")
        self.assertNotEqual([token.value for token in a], [token.value for token in b])

    def test_line_numbers_reference_extracted_text(self):
        tokens = normalize_tokens("first line\nsecond line", "text")
        self.assertEqual(tokens[2].line, 2)
