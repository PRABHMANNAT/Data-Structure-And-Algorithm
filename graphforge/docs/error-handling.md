# Error handling

Negative edges are rejected at construction because the bundled Dijkstra and A*
implementations require non-negative weights. Cycle detection is explicit in
topological sorting; disconnected vertices simply receive no route.
