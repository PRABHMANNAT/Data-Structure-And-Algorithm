import unittest
from transit_simulator.models import Connection,Stop
from transit_simulator.service import TransitService
class ServiceTests(unittest.TestCase):
 def test_facade_combines_stop_search_and_route_planning(self):
  svc=TransitService();svc.add_stop(Stop("a","Atlas"));svc.add_stop(Stop("b","Baker"));svc.add_connection(Connection("x","a","b",1,3,"L"))
  self.assertEqual(svc.search_stops("atl")[0].id,"a");self.assertEqual(svc.plan("a","b",0).arrival,3)
