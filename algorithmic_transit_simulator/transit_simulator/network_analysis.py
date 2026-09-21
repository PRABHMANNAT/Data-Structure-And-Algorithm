from .disjoint_set import DisjointSet
from .graph import TransitGraph


def connected_components(graph: TransitGraph) -> list[set[str]]:
    groups = DisjointSet(graph.stops)
    for edge in graph.connections(): groups.union(edge.origin, edge.destination)
    result: dict[str, set[str]] = {}
    for stop in graph.stops: result.setdefault(groups.find(stop), set()).add(stop)
    return list(result.values())


def isolated_stops(graph: TransitGraph) -> set[str]:
    return {group.pop() for group in connected_components(graph) if len(group) == 1}
