"""Browser-contract tests using the actual Dispatch desk implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'delivery'
    def execute(self, **data):
        return run(self.project, data)

    def test_shortest(self):
        self.assertEqual(self.execute(edges='A B 4\nA C 1\nC B 2',origin='A',destination='B')['cost'],3)
    def test_unreachable(self):
        self.assertIsNone(self.execute(edges='A B 1\nC D 2',origin='A',destination='D')['cost'])
    def test_negative(self):
        with self.assertRaises(ValueError):self.execute(edges='A B -1',origin='A',destination='B')
