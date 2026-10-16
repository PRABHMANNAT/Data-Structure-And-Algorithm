import unittest

from plagiarism_detector.languages import language_for


class LanguageMappingTests(unittest.TestCase):
    def test_supported_extensions(self):
        self.assertEqual(language_for("answer.PY"), "python")
        self.assertEqual(language_for("answer.cpp"), "cpp")
        self.assertEqual(language_for("answer.tsx"), "typescript")

    def test_unknown_extension(self):
        self.assertIsNone(language_for("answer.txt"))
