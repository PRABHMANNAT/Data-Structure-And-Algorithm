import unittest
from pathlib import Path
from transit_simulator.json_io import load_network
class SampleDataTests(unittest.TestCase):
 def test_sample_network_is_loadable(self):
  graph=load_network(Path(__file__).parents[1]/"data"/"sample_network.json");self.assertEqual(len(graph.stops),4)
