import unittest
from advanced_delivery_network.delivery_network.graph import DeliveryGraph
from advanced_delivery_network.delivery_network.models import Stop
class GraphTests(unittest.TestCase):
    def test_stops_and_weighted_connections(self):
        graph = DeliveryGraph(); graph.add_stop(Stop("A", "Alpha")); graph.add_stop(Stop("B", "Beta"))
        graph.add_connection("A", "B", 6)
        self.assertEqual(graph.neighbors("A")[0].minutes, 6); self.assertEqual(graph.neighbors("B")[0].destination, "A")
if __name__ == "__main__": unittest.main()
