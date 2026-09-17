import unittest
from advanced_delivery_network.delivery_network.models import Edge, Route, Stop
class ModelTests(unittest.TestCase):
    def test_immutable_route_domain_objects(self):
        stop = Stop("A", "Airport")
        self.assertEqual((stop.code, Edge("B", 5).minutes, Route(("A", "B"), 5).stops), ("A", 5, ("A", "B")))
if __name__ == "__main__": unittest.main()
