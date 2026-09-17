import json
from .graph import DeliveryGraph
from .models import Stop

def load_graph(path):
    data = json.loads(path.read_text(encoding="utf-8")); graph = DeliveryGraph()
    for item in data["stops"]: graph.add_stop(Stop(**item))
    for item in data["connections"]: graph.add_connection(**item)
    return graph

def dump_route(route):
    return json.dumps({"stops": route.stops, "minutes": route.minutes})
