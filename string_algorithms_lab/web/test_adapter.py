"""Browser-contract tests using the actual Pattern bench implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'strings'
    def execute(self, **data):
        return run(self.project, data)

    def test_overlaps(self):
        self.assertEqual(self.execute(text='bananana',pattern='ana')['positions'],[1,3,5])
    def test_unicode(self):
        self.assertEqual(self.execute(text='🌱a🌱a',pattern='🌱a')['positions'],[0,2])
    def test_empty_pattern(self):
        with self.assertRaises(ValueError):self.execute(text='abc',pattern='')
