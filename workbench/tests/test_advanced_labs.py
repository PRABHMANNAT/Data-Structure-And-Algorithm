"""HTTP checks for every new scenario and bounded validation failures."""

from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
import json
import threading
import unittest
from workbench.registry import projects
from workbench.server import Handler


class AdvancedLabs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def post(self, project, payload):
        connection = HTTPConnection("127.0.0.1", self.server.server_port, timeout=10)
        connection.request(
            "POST",
            "/api/run/" + project,
            json.dumps(payload),
            {"Content-Type": "application/json"},
        )
        response = connection.getresponse()
        status = response.status
        result = json.loads(response.read())
        connection.close()
        return status, result

    def test_thirty_scenarios_reach_real_algorithms(self):
        advanced = [
            record
            for record in projects().values()
            if record.get("level") == "Advanced"
        ]
        self.assertEqual(len(advanced), 10)
        for project in advanced:
            self.assertEqual(len(project["presets"]), 3)
            self.assertIn("lesson", project)
            self.assertIn("guide", project)
            for preset in project["presets"]:
                with self.subTest(project=project["id"], example=preset["name"]):
                    status, result = self.post(project["id"], preset["input"])
                    self.assertEqual(status, 200, result)
                    self.assertIn("metrics", result["result"])

    def test_invalid_domain_inputs_return_400(self):
        bad = {
            "cachecraft": {"keys": "a b", "capacity": 0},
            "dagflow": {"tasks": "a 1 b\nb 1 a", "workers": 2},
            "flowfoundry": {"edges": "s t -1", "source": "s", "sink": "t"},
            "spatialdesk": {"points": "a nan 0"},
            "intervalstudio": {"bookings": "a 2 1 5"},
            "textloom": {"old": "x" * 6001},
            "quantilewatch": {"values": "1 2 3", "window": 0},
            "bloomgate": {"items": "a", "queries": "a", "bits": 0},
            "shardring": {"servers": "same 1\nsame 2", "keys": "x", "added": "new"},
            "joinery": {"tables": "a 10 1\nb 20 1", "joins": "a unknown .1"},
        }
        for project, payload in bad.items():
            with self.subTest(project=project):
                self.assertEqual(self.post(project, payload)[0], 400)
