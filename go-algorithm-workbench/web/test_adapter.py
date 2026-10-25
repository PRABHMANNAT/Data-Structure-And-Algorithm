"""Browser-contract tests using the actual Go sorting room implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'go-workbench'
    def execute(self, **data):
        return run(self.project, data)

    def test_orders_with_duplicates(self):
        result=self.execute(values='7,2,9,1,2')
        self.assertEqual(result['ordered'],[1,2,2,7,9])
    def test_negative_values(self):
        self.assertEqual(self.execute(values='-5,0,-2')['ordered'],[-5,-2,0])
    def test_invalid_number(self):
        with self.assertRaises(ValueError):self.execute(values='one,two')
