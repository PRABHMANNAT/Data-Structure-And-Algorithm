"""Breadth-first graph traversal for contrast with the other examples."""

from collections import deque


def reachable(graph, start):
    seen = {start}
    pending = deque([start])
    while pending:
        node = pending.popleft()
        for neighbor in graph.get(node, ()):
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append(neighbor)
    return seen
