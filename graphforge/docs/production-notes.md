# Production notes

For large graphs, replace in-memory copy-on-write with persistent adjacency shards.
Bound request search work, enforce route deadlines, and include the graph revision in
every response and cache key so clients can reason about consistency.
