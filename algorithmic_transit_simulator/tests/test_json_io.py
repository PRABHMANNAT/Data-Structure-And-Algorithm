import tempfile,unittest
from transit_simulator.graph import TransitGraph
from transit_simulator.json_io import dump_network,load_network
from transit_simulator.models import Connection,Stop
class JsonTests(unittest.TestCase):
 def test_round_trips_network_data(self):
  g=TransitGraph();g.add_stop(Stop("a","A"));g.add_stop(Stop("b","B"));g.add_connection(Connection("x","a","b",1,2,"L"))
  with tempfile.TemporaryDirectory() as directory:
   path=f"{directory}/network.json";dump_network(g,path);self.assertEqual(load_network(path).connections()[0].id,"x")
