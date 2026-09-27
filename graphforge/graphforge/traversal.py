from collections import deque
from .graph import DirectedGraph

def bfs(graph: DirectedGraph, source: str) -> tuple[str, ...]:
    seen, queue, order = {source}, deque([source]), []
    while queue:
        vertex = queue.popleft(); order.append(vertex)
        for nxt, _ in graph.neighbors(vertex):
            if nxt not in seen: seen.add(nxt); queue.append(nxt)
    return tuple(order)

def dfs(graph: DirectedGraph, source: str) -> tuple[str, ...]:
    seen, stack, order = set(), [source], []
    while stack:
        vertex = stack.pop()
        if vertex in seen: continue
        seen.add(vertex); order.append(vertex); stack.extend(reversed([n for n, _ in graph.neighbors(vertex)]))
    return tuple(order)
