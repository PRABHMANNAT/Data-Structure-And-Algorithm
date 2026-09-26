# C++ DSA Toolkit

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
