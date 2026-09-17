def find_stops(graph, query):
    normalized = query.casefold()
    return [graph.stop(code) for code in graph.codes() if normalized in graph.stop(code).name.casefold()]
