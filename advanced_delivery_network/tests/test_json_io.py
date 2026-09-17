import json, tempfile, unittest
from pathlib import Path
from advanced_delivery_network.delivery_network.json_io import dump_route, load_graph
from advanced_delivery_network.delivery_network.models import Route
class JsonIoTests(unittest.TestCase):
    def test_loads_network_and_serializes_route(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "network.json"
            path.write_text(json.dumps({"stops":[{"code":"A","name":"Alpha"}],"connections":[]}))
            self.assertEqual(load_graph(path).codes(), ("A",))
        self.assertIn("minutes", dump_route(Route(("A",), 0)))
if __name__ == "__main__": unittest.main()
