import unittest
from transit_simulator.disruptions import DisruptionBoard
from transit_simulator.models import Connection
class DisruptionTests(unittest.TestCase):
 def test_cancels_or_delays_connections(self):
  trip=Connection("x","a","b",5,10,"L");board=DisruptionBoard();board.delay("x",3)
  self.assertEqual(board.apply(trip).arrival,13);board.cancel("x");self.assertIsNone(board.apply(trip))
