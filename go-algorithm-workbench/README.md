# Go Algorithm Workbench

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Go sorting room workspace](http://127.0.0.1:8765/go-algorithm-workbench/web/).

Run an in-place quicksort and compare its ordered output with the input sequence.

The interface runs the native Go implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Unsorted with duplicates, Negative values.

Go 1.27+ must be installed. The server builds the checked-in bridge into an ignored cache on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


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
