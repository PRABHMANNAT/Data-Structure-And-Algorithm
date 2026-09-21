import unittest
from transit_simulator.intervals import Interval, IntervalIndex
class IntervalTests(unittest.TestCase):
 def test_reports_only_overlapping_intervals(self):
  index=IntervalIndex(); index.add(Interval(10,20,"a")); index.add(Interval(30,40,"b"))
  self.assertEqual([x.value for x in index.conflicts(Interval(15,25,"new"))],["a"])
 def test_rejects_empty_occupancy_interval(self):
  with self.assertRaises(ValueError):IntervalIndex().add(Interval(4,4,"invalid"))
