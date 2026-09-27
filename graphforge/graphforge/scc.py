from .graph import DirectedGraph

def strongly_connected(graph: DirectedGraph) -> tuple[tuple[str, ...], ...]:
    index = 0; stack: list[str] = []; indices: dict[str, int] = {}; low: dict[str, int] = {}; active: set[str] = set(); result: list[tuple[str, ...]] = []
    def visit(vertex: str) -> None:
        nonlocal index
        indices[vertex] = low[vertex] = index; index += 1; stack.append(vertex); active.add(vertex)
        for nxt, _ in graph.neighbors(vertex):
            if nxt not in indices: visit(nxt); low[vertex] = min(low[vertex], low[nxt])
            elif nxt in active: low[vertex] = min(low[vertex], indices[nxt])
        if low[vertex] == indices[vertex]:
            component = []
            while True:
                item = stack.pop(); active.remove(item); component.append(item)
                if item == vertex: break
            result.append(tuple(sorted(component)))
    for vertex in graph.vertices():
        if vertex not in indices: visit(vertex)
    return tuple(result)
