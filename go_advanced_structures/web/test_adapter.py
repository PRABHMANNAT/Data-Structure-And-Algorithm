"""Browser-contract tests using the actual Range observatory implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'go-ranges'
    def execute(self, **data):
        return run(self.project, data)

    def test_range_agreement(self):
        result=self.execute(values='3,1,4,1,5',left='1',right='3')
        self.assertEqual(result['fenwick'],6);self.assertEqual(result['segment'],6)
    def test_negative_prefix(self):
        self.assertEqual(self.execute(values='-3,2',left='0',right='1')['prefix'],[-3,-1])
    def test_out_of_range(self):
        with self.assertRaises(ValueError):self.execute(values='1,2',left='0',right='2')
