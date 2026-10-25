# Go Data Structures Lab

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Go collection desk workspace](http://127.0.0.1:8765/go_data_structures_lab/web/).

Min-heap extraction with a custom comparator. Every output value comes from the repository heap.

The interface runs the native Go implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Unsorted with duplicates, Negative values.

Go 1.27+ must be installed. The server builds the checked-in bridge into an ignored cache on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A dependency-free, generic Go implementation of foundational data structures.

Run the verification suite with `go test ./...` and the example with `go run ./cmd/demo`.

Included: linked list, stack, queue, deque, hash map, min heap, trie, directed graph, union-find, and LRU cache.
