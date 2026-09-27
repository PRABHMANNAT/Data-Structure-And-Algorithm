# GraphForge

GraphForge is a dependency-free Python toolkit for versioned routing networks.
It focuses on algorithms that production routing services actually need: immutable
revisions, transactional edits, shortest-path strategies, constrained search, and
deterministic algorithm diagnostics.

## Highlights

- Copy-on-write graph revisions with cheap read isolation.
- Dijkstra and A* with admissible-heuristic checks.
- K-shortest simple routes, strongly connected components, and topological analysis.
- Rollback union-find for offline connectivity queries.

Run `python -m graphforge --help` after installation.
