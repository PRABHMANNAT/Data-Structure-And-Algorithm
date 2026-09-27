import json
from .graph import DirectedGraph
from .model import Edge

def dump(graph: DirectedGraph) -> str:
    return json.dumps([edge.__dict__ if hasattr(edge, "__dict__") else {"source": edge.source, "target": edge.target, "weight": edge.weight} for edge in graph.edges()])

def load(value: str) -> DirectedGraph:
    return DirectedGraph(Edge(**entry) for entry in json.loads(value))
