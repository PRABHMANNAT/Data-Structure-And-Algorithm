# Architecture

`VersionedGraph` supplies immutable reader snapshots through copy-on-write commits.
`RouteEngine` layers a revision-keyed LRU cache above it. Algorithms consume plain
`DirectedGraph` instances, making them independently testable and reusable.
