import unittest

from plagiarism_detector.tokenize import normalize_tokens


class GenericStringTests(unittest.TestCase):
    def test_comment_markers_inside_strings_are_not_comments(self):
        tokens = normalize_tokens('let url = "http://example.com";', "javascript")
        self.assertIn("STR", [token.value for token in tokens])

    def test_block_comments_disappear(self):
        tokens = normalize_tokens("int a; /* hello */ int b;", "cpp")
        self.assertEqual([token.value for token in tokens].count("int"), 2)
