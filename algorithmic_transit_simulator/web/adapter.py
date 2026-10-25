from dataclasses import asdict
from transit_simulator.graph import TransitGraph
from transit_simulator.models import Stop, Connection
from transit_simulator.router import EarliestArrivalRouter
from workbench.validation import lines, text, integer

def run(data):
    graph=TransitGraph();services=[]
    for index,row in enumerate(lines(data,'services',80)):
        parts=row.split()
        if len(parts)!=5:raise ValueError('Use: from to departure arrival fare')
        origin,destination,departure,arrival,fare=parts
        dep=integer({'v':departure},'v',minimum=0,maximum=10080)
        arr=integer({'v':arrival},'v',minimum=0,maximum=10080)
        cost=integer({'v':fare},'v',minimum=0)
        services.append(Connection(str(index+1),origin,destination,dep,arr,'Line '+str(index+1),fare=cost))
        for name in (origin,destination):
            if name not in graph.stops:graph.add_stop(Stop(name,name))
    for service in services:graph.add_connection(service)
    origin=text(data,'origin');destination=text(data,'destination')
    if origin not in graph.stops or destination not in graph.stops:raise ValueError('Both stops must appear in the timetable')
    departure=integer(data,'departure',minimum=0,maximum=10080)
    buffer=integer(data,'buffer',2,0,120)
    route=EarliestArrivalRouter(graph,buffer).route(origin,destination,departure)
    connections=[asdict(c) for c in route.connections] if route else []
    arrival=departure if origin==destination else route.arrival if route else None
    return dict(connections=connections,arrival=arrival,fare=route.fare if route else 0,departure=departure,origin=origin,destination=destination)
