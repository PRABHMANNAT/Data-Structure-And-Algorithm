from .disjoint_set import DisjointSet

class NetworkAnalysis:
    def __init__(self, graph): self.graph = graph
    def components(self):
        groups = DisjointSet(self.graph.codes())
        for code in self.graph.codes():
            for edge in self.graph.neighbors(code): groups.union(code, edge.destination)
        buckets = {}
        for code in self.graph.codes(): buckets.setdefault(groups.find(code), set()).add(code)
        return tuple(frozenset(group) for group in buckets.values())
    def is_connected(self): return len(self.components()) <= 1
