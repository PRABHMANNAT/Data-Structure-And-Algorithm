"""Browser-contract tests using the actual Structure study implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'python-structures'
    def execute(self, **data):
        return run(self.project, data)

    def test_inorder_and_membership(self):
        result=self.execute(values='7,3,9,1,5',find='5')
        self.assertEqual(result['ordered'],[1,3,5,7,9]);self.assertTrue(result['found'])
    def test_skew_and_duplicates(self):
        result=self.execute(values='1,1,2,3',find='8')
        self.assertEqual(result['height'],4);self.assertFalse(result['found'])
    def test_bad_input(self):
        with self.assertRaises(ValueError):self.execute(values='1,no',find='1')
