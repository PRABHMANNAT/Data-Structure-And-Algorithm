from graphforge.engine import RouteEngine
from graphforge.model import Edge
from workbench.validation import edges, text, integer

def run(data):
    roads=edges(data);engine=RouteEngine()
    for a,b,cost in roads:engine.add(Edge(a,b,cost))
    revision=integer(data,'revision',0,0,len(roads)) or len(roads)
    active=roads[:revision]
    origin=text(data,'origin');destination=text(data,'destination')
    names={v for edge in active for v in edge[:2]}
    if origin not in names or destination not in names:raise ValueError('Endpoints must exist in the selected revision')
    route=engine.route(origin,destination,revision)
    return dict(edges=active,vertices=list(route.vertices) if route else [],cost=route.cost if route else None,directed=True,revision=revision)
