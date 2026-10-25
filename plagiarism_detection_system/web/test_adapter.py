"""Browser-contract tests using the actual Source comparison implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'similarity'
    def execute(self, **data):
        return run(self.project, data)

    def test_identical_sources(self):
        source='def sum_items(items):\n    total = 0\n    for item in items: total += item\n    return total'
        self.assertEqual(self.execute(left=source,right=source,language='python')['matches'][0]['score'],1)
    def test_empty_sources(self):
        self.assertEqual(self.execute(left='',right='',language='python')['matches'],[])
    def test_bad_language(self):
        with self.assertRaises(ValueError):self.execute(left='x',right='x',language='shell')
