# Routing

Use Dijkstra for general non-negative networks. Use A* only when the supplied
heuristic is admissible; otherwise its early goal exit may not be optimal. Route
alternatives are intentionally simple paths and should be bounded at the API edge.
