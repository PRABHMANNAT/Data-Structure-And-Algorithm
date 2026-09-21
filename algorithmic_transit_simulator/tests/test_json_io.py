import tempfile,unittest
from transit_simulator.graph import TransitGraph
from transit_simulator.json_io import dump_network,load_network
from transit_simulator.models import Connection,Stop
class JsonTests(unittest.TestCase):
 def test_round_trips_network_data(self):
  g=TransitGraph();g.add_stop(Stop("a","A"));g.add_stop(Stop("b","B"));g.add_connection(Connection("x","a","b",1,2,"L"))
  with tempfile.NamedTemporaryFile() as f: dump_network(g,f.name);self.assertEqual(load_network(f.name).connections()[0].id,"x")
