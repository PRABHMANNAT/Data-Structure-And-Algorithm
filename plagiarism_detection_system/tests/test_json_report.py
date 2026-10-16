import json
import unittest

from plagiarism_detector.models import Match
from plagiarism_detector.report import to_json


class JsonReportTests(unittest.TestCase):
    def test_machine_readable_schema(self):
        match = Match("a", "b", 0.8, 0.9, 0.7, 0.5, 3, ())
        data = json.loads(to_json([match]))
        self.assertEqual(data["matches"][0]["shared_fingerprints"], 3)
