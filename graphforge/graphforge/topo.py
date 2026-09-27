from collections import deque
from .errors import CycleDetected
from .graph import DirectedGraph

def topological_order(graph: DirectedGraph) -> tuple[str, ...]:
    degree = {v: 0 for v in graph.vertices()}
    for edge in graph.edges(): degree[edge.target] += 1
    ready, order = deque(sorted(v for v, d in degree.items() if d == 0)), []
    while ready:
        vertex = ready.popleft(); order.append(vertex)
        for nxt, _ in graph.neighbors(vertex):
            degree[nxt] -= 1
            if degree[nxt] == 0: ready.append(nxt)
    if len(order) != len(degree): raise CycleDetected("topological ordering requires a DAG")
    return tuple(order)
