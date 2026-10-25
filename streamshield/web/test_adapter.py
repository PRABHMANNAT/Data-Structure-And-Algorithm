"""Browser-contract tests using the actual Stream monitor implementation."""
import unittest
from workbench.registry import run

class WebAdapterTests(unittest.TestCase):
    project = 'streamshield'
    def execute(self, **data):
        return run(self.project, data)

    def test_late_event(self):
        result=self.execute(events='a 1000 2\na 2000 3\na 0 9',window='1000',lateness='100')
        self.assertEqual(result['stats']['accepted'],2);self.assertEqual(result['stats']['rejected_late'],1)
    def test_window_total(self):
        self.assertEqual(self.execute(events='a 10 2\nb 20 3',window='100',lateness='0')['total'],5)
    def test_invalid_window(self):
        with self.assertRaises(ValueError):self.execute(events='a 1 1',window='0')
