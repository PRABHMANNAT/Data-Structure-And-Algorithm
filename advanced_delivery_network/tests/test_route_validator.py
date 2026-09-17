import unittest
from advanced_delivery_network.delivery_network.graph import DeliveryGraph
from advanced_delivery_network.delivery_network.models import Route, Stop
from advanced_delivery_network.delivery_network.route_validator import validate_route
class RouteValidatorTests(unittest.TestCase):
    def test_accepts_matching_route_cost(self):
        graph = DeliveryGraph(); graph.add_stop(Stop("A", "A")); graph.add_stop(Stop("B", "B")); graph.add_connection("A", "B", 4)
        self.assertTrue(validate_route(graph, Route(("A", "B"), 4)))
if __name__ == "__main__": unittest.main()
