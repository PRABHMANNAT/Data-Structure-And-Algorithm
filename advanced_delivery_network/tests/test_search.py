import unittest
from advanced_delivery_network.delivery_network.graph import DeliveryGraph
from advanced_delivery_network.delivery_network.models import Stop
from advanced_delivery_network.delivery_network.search import find_stops
class SearchTests(unittest.TestCase):
    def test_finds_stops_by_partial_name(self):
        graph = DeliveryGraph(); graph.add_stop(Stop("A", "Central Station")); graph.add_stop(Stop("B", "Airport"))
        self.assertEqual([stop.code for stop in find_stops(graph, "station")], ["A"])
if __name__ == "__main__": unittest.main()
