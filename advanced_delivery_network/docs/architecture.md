# Architecture

`DeliveryGraph` holds the weighted adjacency map. `RoutePlanner` runs Dijkstra's algorithm using `IndexedPriorityQueue` for efficient decrease-key updates. Higher-level services add caching, search, validation, network analysis, and route history without coupling those concerns to the routing core.
