# Go Search Structures

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Prefix index workspace](http://127.0.0.1:8765/go_search_structures/web/).

Build a trie from your own vocabulary. Inspect lexicographic prefix completions and the indexed words.

The interface runs the native Go implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Shared branches, Unicode vocabulary.

Go 1.27+ must be installed. The server builds the checked-in bridge into an ignored cache on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


An advanced, dependency-free search-index project built from a Bloom filter, prefix trie, inverted postings, LRU cache, and top-k ranking.

Run `go test ./...` or `go run ./cmd/demo`.
