import unittest
from advanced_delivery_network.delivery_network.models import Route
from advanced_delivery_network.delivery_network.route_repository import RouteRepository
class RouteRepositoryTests(unittest.TestCase):
    def test_persists_route_history(self):
        repository = RouteRepository(); route = Route(("A", "B"), 3); repository.save("D-1", route)
        self.assertEqual(repository.get("D-1"), route); self.assertEqual(repository.all_ids(), ("D-1",))
if __name__ == "__main__": unittest.main()
