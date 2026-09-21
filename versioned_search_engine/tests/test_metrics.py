import unittest
from search_engine.metrics import Metrics
class MetricsTests(unittest.TestCase):
 def test_counts_named_events(self):
  m=Metrics();m.inc("query");m.inc("query");self.assertEqual(m.get("query"),2)
 def test_defaults_unknown_metric_to_zero(self):self.assertEqual(Metrics().get("missing"),0)
