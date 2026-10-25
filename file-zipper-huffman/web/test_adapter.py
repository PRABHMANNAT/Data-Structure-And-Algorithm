"""Browser-contract tests using the actual Compression room implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'huffman'
    def execute(self, **data):
        return run(self.project, data)

    def test_utf8_roundtrip(self):
        result=self.execute(text='café 🌱 '*30)
        self.assertTrue(result['verified']);self.assertEqual(result['decoded'],'café 🌱 '*30)
    def test_empty_roundtrip(self):
        result=self.execute(text='');self.assertTrue(result['verified']);self.assertEqual(result['input_bytes'],0)
    def test_single_symbol(self):
        result=self.execute(text='a'*5000);self.assertTrue(result['verified']);self.assertLess(result['archive_bytes'],5000)
