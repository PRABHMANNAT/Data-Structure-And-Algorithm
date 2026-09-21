import unittest
from transit_simulator.models import Connection
from transit_simulator.platforms import PlatformScheduler
class PlatformTests(unittest.TestCase):
 def test_rejects_overlapping_platform_reservation(self):
  scheduler=PlatformScheduler(); first=Connection("a","x","y",0,10,"L"); next=Connection("b","x","y",0,11,"L")
  self.assertEqual(scheduler.reserve("1",first),[]); self.assertEqual([x.value for x in scheduler.reserve("1",next)], ["a"])
