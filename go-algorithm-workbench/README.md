# Go Algorithm Workbench

A practical, intermediate-to-advanced data-structures and algorithms library
written in modern Go. The project favors clear APIs, generic implementations,
complexity notes, and executable examples.

## Included

- Core structures: stack, queue, linked list, min-heap, AVL tree, trie, and
  disjoint set union.
- Algorithms: sorting, binary search, graph traversal, shortest paths,
  topological sorting, strongly connected components, dynamic programming, and
  Knuth-Morris-Pratt string matching.
- Systems-flavored structure: an O(1) LRU cache.
- A small CLI that demonstrates several algorithms with deterministic input.

## Quick start

```bash
go test ./...
go run ./cmd/workbench -demo dijkstra
```

## Layout

| Directory | Purpose |
| --- | --- |
| `structures/` | Generic reusable data structures |
| `algorithms/` | Algorithm implementations grouped by topic |
| `cmd/workbench/` | Runnable demonstration CLI |
| `docs/` | Complexity and learning notes |

Every public operation documents its asymptotic time complexity. See
[the learning path](docs/learning-path.md) for a suggested order of study.
