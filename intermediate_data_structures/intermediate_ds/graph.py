class Graph:
    def __init__(self, directed=False): self.directed = directed; self._edges = {}
    def add_vertex(self, vertex): self._edges.setdefault(vertex, set())
    def add_edge(self, source, target):
        self.add_vertex(source); self.add_vertex(target); self._edges[source].add(target)
        if not self.directed: self._edges[target].add(source)
    def bfs(self, start):
        if start not in self._edges: raise KeyError(start)
        seen, order, pending = {start}, [], [start]
        while pending:
            vertex = pending.pop(0); order.append(vertex)
            for neighbor in sorted(self._edges[vertex]):
                if neighbor not in seen: seen.add(neighbor); pending.append(neighbor)
        return order
