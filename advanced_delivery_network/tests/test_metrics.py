import unittest
from advanced_delivery_network.delivery_network.metrics import route_metrics
from advanced_delivery_network.delivery_network.models import Route
class MetricTests(unittest.TestCase):
    def test_route_summary_counts_legs(self):
        self.assertEqual(route_metrics(Route(("A", "B", "C"), 12))["average_leg_minutes"], 6)
if __name__ == "__main__": unittest.main()
