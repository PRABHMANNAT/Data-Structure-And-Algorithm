from delivery_network.graph import DeliveryGraph
from delivery_network.models import Stop
from delivery_network.route_planner import RoutePlanner
from delivery_network.errors import PathNotFoundError
from workbench.validation import edges, text

def run(data):
    roads=edges(data);graph=DeliveryGraph()
    names=set(name for road in roads for name in road[:2])
    origin=text(data,'origin');destination=text(data,'destination')
    if origin not in names or destination not in names:raise ValueError('Both endpoints must appear in the connections')
    for name in sorted(names):graph.add_stop(Stop(name,name))
    for a,b,cost in roads:graph.add_connection(a,b,cost)
    try:
        route=RoutePlanner(graph).shortest_path(origin,destination)
        vertices,cost=list(route.stops),route.minutes
    except PathNotFoundError:vertices,cost=[],None
    return dict(edges=roads,vertices=vertices,cost=cost,directed=False)
