# C++ DSA Toolkit

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the C++ sorting desk workspace](http://127.0.0.1:8765/cpp-dsa-toolkit/web/).

Compare merge sort and the toolkit quick-sort API on the same integer sequence. Inspect duplicates and value gaps.

The interface runs the native C++ implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Unsorted with duplicates, Negative values, Quick-sort API.

A C++20 compiler must be available as `g++` or through the `CXX` environment variable. The server builds the checked-in bridge on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


An intermediate-to-advanced C++20 algorithms and data-structures workbench.
It provides header-only, generic building blocks, graph and dynamic-programming
algorithms, tiny executable examples, and dependency-free tests.

## Build

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
./build/dsa_demo dijkstra
```

## Topics

- Containers: stack, queue, deque, linked list, heap, AVL tree, trie, DSU, LRU
- Algorithms: sorting, search, graph traversal, Dijkstra, DP, KMP, greedy,
  backtracking, intervals, number theory, bit operations, and prefix sums

See [docs/learning-path.md](docs/learning-path.md) for a suggested progression.
