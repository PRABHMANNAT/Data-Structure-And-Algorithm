import unittest
from advanced_delivery_network.delivery_network.graph import DeliveryGraph
from advanced_delivery_network.delivery_network.models import Stop
from advanced_delivery_network.delivery_network.service import DeliveryService
class ServiceTests(unittest.TestCase):
    def test_reuses_planned_route(self):
        graph = DeliveryGraph(); graph.add_stop(Stop("A", "A")); graph.add_stop(Stop("B", "B")); graph.add_connection("A", "B", 2)
        service = DeliveryService(graph); self.assertIs(service.plan("A", "B"), service.plan("A", "B"))
if __name__ == "__main__": unittest.main()
