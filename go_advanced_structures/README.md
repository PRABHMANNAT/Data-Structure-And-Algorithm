# Go Advanced Structures

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Range observatory workspace](http://127.0.0.1:8765/go_advanced_structures/web/).

Compare Fenwick and segment-tree sums over an inclusive range. See the prefix totals behind the query.

The interface runs the native Go implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Middle range, Single value.

Go 1.27+ must be installed. The server builds the checked-in bridge into an ignored cache on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A dependency-free Go lab for balanced trees, range-query structures, randomized search trees, and connectivity algorithms.

Run `go test ./...` or `go run ./cmd/demo`.
