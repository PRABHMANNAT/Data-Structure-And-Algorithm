# Testing strategy

Tests use small graphs with known optimal paths. Add property tests for path cost
consistency and compare A* with zero heuristic against Dijkstra. Include cycles,
disconnected graphs, duplicate edges, and revision isolation.
