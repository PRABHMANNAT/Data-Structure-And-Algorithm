"""Browser-contract tests using the actual Network atlas implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'graphforge'
    def execute(self, **data):
        return run(self.project, data)

    def test_revision_changes_route(self):
        data=dict(edges='A B 9\nA C 1\nC B 2',origin='A',destination='B')
        self.assertEqual(self.execute(**data,revision='1')['cost'],9)
        self.assertEqual(self.execute(**data,revision='0')['cost'],3)
    def test_directed(self):
        self.assertIsNone(self.execute(edges='A B 1',origin='B',destination='A')['cost'])
    def test_unknown_endpoint(self):
        with self.assertRaises(ValueError):self.execute(edges='A B 1',origin='X',destination='A')
