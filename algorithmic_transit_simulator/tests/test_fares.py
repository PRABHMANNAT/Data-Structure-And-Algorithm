import unittest
from transit_simulator.fares import transfer_count,zone_fare
from transit_simulator.models import Connection,Journey
class FareTests(unittest.TestCase):
 def test_applies_fare_cap_and_counts_transfers(self):
  legs=(Connection("a","x","y",1,2,"L",fare=9),Connection("b","y","z",3,4,"L",fare=9));journey=Journey(legs)
  self.assertEqual((zone_fare(journey,10),transfer_count(journey)),(10,1))
