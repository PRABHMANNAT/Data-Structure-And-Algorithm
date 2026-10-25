# Go Data Structures Journey

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Go learning journal workspace](http://127.0.0.1:8765/go-data-structures-journey/web/).

Follow a divide-and-conquer merge sort with duplicate and negative-value inputs.

The interface runs the native Go implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Unsorted with duplicates, Negative values.

Go 1.27+ must be installed. The server builds the checked-in bridge into an ignored cache on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A dependency-free Go module that implements classic data structures with clear APIs, tests, examples, and complexity notes.

## Packages

The project grows one structure at a time: lists, stacks, queues, trees, hash tables, heaps, tries, graphs, and supporting algorithms.

## Run

```bash
go test ./...
```
