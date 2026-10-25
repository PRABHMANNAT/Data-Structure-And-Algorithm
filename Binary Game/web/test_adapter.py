"""Browser-contract tests using the actual Binary practice implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'binary-quest'
    def execute(self, **data):
        return run(self.project, data)

    def test_conversion(self):
        self.assertEqual(self.execute(decimal='42',answer='101010')['binary'],'101010')
    def test_zero(self):
        self.assertEqual(self.execute(decimal='0',answer='0')['binary'],'0')
    def test_invalid_integer(self):
        with self.assertRaises(ValueError):self.execute(decimal='1.2',answer='1')
