import unittest
from transit_simulator.metrics import Metrics
class MetricsTests(unittest.TestCase):
 def test_summarizes_counters_and_observations(self):
  m=Metrics();m.increment("routes");m.increment("routes");m.observe("wait",2);m.observe("wait",4)
  self.assertEqual(m.summary(),{"routes":2,"wait_mean":3})
