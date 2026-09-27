from __future__ import annotations
from math import inf
from .graph import DirectedGraph
from .model import Route
from .priority_queue import MinQueue

def dijkstra(graph: DirectedGraph, source: str, target: str) -> Route | None:
    queue, distance, previous = MinQueue(), {source: 0.0}, {}
    queue.push(0, source)
    while queue:
        cost, vertex = queue.pop()
        if cost != distance[vertex]: continue
        if vertex == target:
            path = [target]
            while path[-1] != source: path.append(previous[path[-1]])
            return Route(tuple(reversed(path)), cost)
        for nxt, weight in graph.neighbors(vertex):
            candidate = cost + weight
            if candidate < distance.get(nxt, inf): distance[nxt] = candidate; previous[nxt] = vertex; queue.push(candidate, nxt)
    return None
