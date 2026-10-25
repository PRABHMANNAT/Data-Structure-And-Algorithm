"""Browser-contract tests using the actual Departure board implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'transit'
    def execute(self, **data):
        return run(self.project, data)

    def test_earliest_arrival(self):
        result=self.execute(services='A B 10 20 100\nB C 22 30 50',origin='A',destination='C',departure='0',buffer='2')
        self.assertEqual(result['arrival'],30);self.assertEqual(result['fare'],150)
    def test_missed_transfer(self):
        self.assertIsNone(self.execute(services='A B 10 20 100\nB C 21 30 50',origin='A',destination='C',departure='0',buffer='2')['arrival'])
    def test_invalid_time(self):
        with self.assertRaises(ValueError):self.execute(services='A B 20 10 0',origin='A',destination='B')
