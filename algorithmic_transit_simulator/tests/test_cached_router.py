import unittest
from transit_simulator.cached_router import CachedRouter
class _Router:
 def __init__(self):self.calls=0
 def route(self,*args):self.calls+=1;return args
class CachedRouterTests(unittest.TestCase):
 def test_reuses_identical_route_query(self):
  router=_Router(); cached=CachedRouter(router);cached.route("a","b",1);cached.route("a","b",1)
  self.assertEqual(router.calls,1)
