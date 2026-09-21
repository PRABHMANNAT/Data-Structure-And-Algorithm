import json
from pathlib import Path
from .graph import TransitGraph
from .models import Connection,Stop
def load_network(path):
 data=json.loads(Path(path).read_text()); graph=TransitGraph()
 for item in data["stops"]:graph.add_stop(Stop(**item))
 for item in data["connections"]:graph.add_connection(Connection(**item))
 return graph
def dump_network(graph,path):
 Path(path).write_text(json.dumps({"stops":[{"id":s.id,"name":s.name,"zone":s.zone,"accessible":s.accessible} for s in graph.stops.values()],"connections":[{"id":c.id,"origin":c.origin,"destination":c.destination,"departure":c.departure,"arrival":c.arrival,"line":c.line,"capacity":c.capacity,"fare":c.fare} for c in graph.connections()]},indent=2))
