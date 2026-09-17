# Typical workflow

1. Load a JSON network with `load_graph`.
2. Use `RoutePlanner(graph).shortest_path(origin, destination)`.
3. Validate the result with `validate_route` and inspect it with `route_metrics`.
4. Wrap the graph with `DeliveryService` when repeat requests should be cached.
