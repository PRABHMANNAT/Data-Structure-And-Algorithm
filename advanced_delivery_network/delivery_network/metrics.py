def route_metrics(route):
    legs = max(0, len(route.stops) - 1)
    return {"stops": len(route.stops), "legs": legs, "minutes": route.minutes, "average_leg_minutes": route.minutes / legs if legs else 0}

def network_metrics(graph):
    edges = sum(len(graph.neighbors(code)) for code in graph.codes())
    return {"stops": len(graph.codes()), "directed_edges": edges}
