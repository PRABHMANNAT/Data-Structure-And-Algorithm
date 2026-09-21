import unittest
from transit_simulator.models import Connection,Journey
from transit_simulator.validator import validate_journey
class ValidatorTests(unittest.TestCase):
 def test_flags_short_transfer_and_disconnected_legs(self):
  trip=Journey((Connection("a","x","y",1,3,"L"),Connection("b","z","q",4,5,"L")))
  self.assertEqual(validate_journey(trip),["legs are disconnected","transfer buffer violated"])
