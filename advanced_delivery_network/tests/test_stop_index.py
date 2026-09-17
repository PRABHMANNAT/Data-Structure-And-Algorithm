import unittest
from advanced_delivery_network.delivery_network.graph import DeliveryGraph
from advanced_delivery_network.delivery_network.models import Stop
from advanced_delivery_network.delivery_network.stop_index import StopIndex
class StopIndexTests(unittest.TestCase):
    def test_prefix_index_returns_stops(self):
        graph = DeliveryGraph(); graph.add_stop(Stop("H", "Harbor")); graph.add_stop(Stop("A", "Airport"))
        self.assertEqual([stop.code for stop in StopIndex(graph).suggest("ha")], ["H"])
if __name__ == "__main__": unittest.main()
