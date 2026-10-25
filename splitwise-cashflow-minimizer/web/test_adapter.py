"""Browser-contract tests using the actual Settle up implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'cashflow'
    def execute(self, **data):
        return run(self.project, data)

    def test_settlement_conserves_cents(self):
        result=self.execute(expenses='A,900,A|B|C')
        self.assertEqual(sum(value for _,value in result['balances']),0)
        self.assertEqual(sum(p['cents'] for p in result['payments']),600)
    def test_uneven_split(self):
        result=self.execute(expenses='A,100,A|B|C')
        self.assertEqual(sum(value for _,value in result['balances']),0)
    def test_duplicate_participant(self):
        with self.assertRaises(ValueError):self.execute(expenses='A,10,A|A')
