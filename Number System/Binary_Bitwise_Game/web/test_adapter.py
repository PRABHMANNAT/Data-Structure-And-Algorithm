"""Browser-contract tests using the actual Bit workshop implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'bitrealm'
    def execute(self, **data):
        return run(self.project, data)

    def test_mask(self):
        self.assertEqual(self.execute(a='173',b='15',operation='AND')['value'],13)
    def test_rotate(self):
        self.assertEqual(self.execute(a='129',b='1',operation='ROTL')['value'],3)
    def test_bad_shift(self):
        with self.assertRaises(ValueError):self.execute(a='1',b='8',operation='SHL')
