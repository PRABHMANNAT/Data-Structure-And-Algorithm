import unittest
from advanced_delivery_network.delivery_network.graph import DeliveryGraph
from advanced_delivery_network.delivery_network.models import Stop
from advanced_delivery_network.delivery_network.route_planner import RoutePlanner
class RoutePlannerTests(unittest.TestCase):
    def test_dijkstra_prefers_lower_total_cost(self):
        graph = DeliveryGraph()
        for code in "ABC": graph.add_stop(Stop(code, code))
        graph.add_connection("A", "B", 9); graph.add_connection("A", "C", 2); graph.add_connection("C", "B", 3)
        self.assertEqual(RoutePlanner(graph).shortest_path("A", "B").minutes, 5)
if __name__ == "__main__": unittest.main()
