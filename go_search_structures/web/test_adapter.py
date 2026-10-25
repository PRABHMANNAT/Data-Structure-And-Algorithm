"""Browser-contract tests using the actual Prefix index implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'go-prefix'
    def execute(self, **data):
        return run(self.project, data)

    def test_lexicographic_limit(self):
        self.assertEqual(self.execute(words='cat\ncar\ncap\ncan',prefix='ca',limit='2')['matches'],['can','cap'])
    def test_no_match(self):
        self.assertEqual(self.execute(words='tree\ntrie',prefix='z',limit='3')['matches'],[])
    def test_invalid_limit(self):
        with self.assertRaises(ValueError):self.execute(words='a',prefix='a',limit='0')
