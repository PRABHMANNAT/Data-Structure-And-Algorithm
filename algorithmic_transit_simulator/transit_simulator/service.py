from .cached_router import CachedRouter
from .graph import TransitGraph
from .models import Stop,Connection
from .router import EarliestArrivalRouter
from .stop_index import StopIndex
class TransitService:
 def __init__(self):
  self.graph=TransitGraph();self.index=StopIndex();self.router=CachedRouter(EarliestArrivalRouter(self.graph))
 def add_stop(self,stop:Stop):self.graph.add_stop(stop);self.index.add(stop)
 def add_connection(self,connection:Connection):self.graph.add_connection(connection);self.router.invalidate()
 def plan(self,origin,destination,departure):return self.router.route(origin,destination,departure)
 def search_stops(self,prefix):return self.index.find(prefix)
