from __future__ import annotations
from collections.abc import Callable
from math import inf
from .graph import DirectedGraph
from .model import Route
from .priority_queue import MinQueue

def astar(graph: DirectedGraph, source: str, target: str, heuristic: Callable[[str], float]) -> Route | None:
    queue, g_score, previous = MinQueue(), {source: 0.0}, {}
    queue.push(heuristic(source), source)
    while queue:
        _, vertex = queue.pop()
        if vertex == target:
            path = [target]
            while path[-1] != source: path.append(previous[path[-1]])
            return Route(tuple(reversed(path)), g_score[target])
        for nxt, weight in graph.neighbors(vertex):
            candidate = g_score[vertex] + weight
            if candidate < g_score.get(nxt, inf): g_score[nxt] = candidate; previous[nxt] = vertex; queue.push(candidate + heuristic(nxt), nxt)
    return None
