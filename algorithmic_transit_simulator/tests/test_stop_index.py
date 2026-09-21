import unittest
from transit_simulator.models import Stop
from transit_simulator.stop_index import StopIndex

class StopIndexTests(unittest.TestCase):
    def test_resolves_stop_models_from_a_name_prefix(self):
        index = StopIndex(); index.add(Stop("c", "Central")); index.add(Stop("p", "Park"))
        self.assertEqual([s.id for s in index.find("cen")], ["c"])
