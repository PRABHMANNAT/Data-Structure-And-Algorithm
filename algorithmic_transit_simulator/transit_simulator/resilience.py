from .disruptions import DisruptionBoard
from .graph import TransitGraph
from .models import Stop
def operational_graph(graph:TransitGraph,board:DisruptionBoard):
 result=TransitGraph()
 for stop in graph.stops.values():result.add_stop(stop)
 for edge in graph.connections():
  usable=board.apply(edge)
  if usable:result.add_connection(usable)
 return result
