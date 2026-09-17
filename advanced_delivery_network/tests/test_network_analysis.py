import unittest
from advanced_delivery_network.delivery_network.graph import DeliveryGraph
from advanced_delivery_network.delivery_network.models import Stop
from advanced_delivery_network.delivery_network.network_analysis import NetworkAnalysis
class NetworkAnalysisTests(unittest.TestCase):
    def test_identifies_separate_components(self):
        graph = DeliveryGraph()
        for code in "ABC": graph.add_stop(Stop(code, code))
        graph.add_connection("A", "B", 1)
        self.assertFalse(NetworkAnalysis(graph).is_connected()); self.assertEqual(len(NetworkAnalysis(graph).components()), 2)
if __name__ == "__main__": unittest.main()
