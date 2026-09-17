from .errors import PathNotFoundError

def validate_route(graph, route):
    if not route.stops: raise PathNotFoundError("route must include a stop")
    total = 0
    for first, second in zip(route.stops, route.stops[1:]):
        matches = [edge for edge in graph.neighbors(first) if edge.destination == second]
        if not matches: raise PathNotFoundError(f"missing edge: {first} -> {second}")
        total += matches[0].minutes
    return total == route.minutes
