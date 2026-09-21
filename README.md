# Data Structures and Algorithms

A hands-on collection of data-structure and algorithm projects in C++ and Python. The repository progresses from number-system fundamentals to reusable data structures, routing systems, transit operations, and full-text retrieval.

## What you can explore

| Area | Project | Concepts |
| --- | --- | --- |
| C++ foundations | Number System | Decimal-to-binary conversion and positional representation |
| C++ practice | Binary Game | Interactive binary-conversion challenges |
| Python data structures | Intermediate Data Structures | Arrays, linked lists, stacks, queues, trees, heaps, graphs, tries, and union-find |
| Applied Python | Advanced Delivery Network | Dijkstra routing, indexed priority queues, graph analysis, caching, prefix search, and event handling |
| Applied Python | Algorithmic Transit Simulator | Timetable routing, AVL indexes, interval conflicts, disruption simulation, and caching |
| Applied Python | Versioned Search Engine | Inverted indexing, Boolean/phrase search, BM25 ranking, autocomplete, and snapshots |

## Repository layout

```text
Binary Game/                  C++ binary-learning console game
Number System/                C++ number-system exercises
intermediate_data_structures/ Python implementations of core data structures
advanced_delivery_network/    Graph-based delivery route-planning project
algorithmic_transit_simulator/ Timetable-aware transit planning and simulation
versioned_search_engine/     Full-text search and retrieval algorithms project
```

## Featured applied projects

**Algorithmic Transit Simulator** models a timetable as a graph and plans earliest-arrival journeys with transfer buffers. It also demonstrates AVL trees, interval conflict detection, union-find connectivity analysis, prefix tries, LRU caching, disruption projection, and event simulation.

**Versioned Search Engine** is a dependency-free retrieval system. It combines positional inverted indexes for phrase search, Boolean posting-set operations, BM25 ranking, trie autocomplete, bounded top-k selection, Bloom-filter deduplication, LRU caching, snapshots, and link-graph recommendations.

## Run the C++ exercises

From the repository root, compile either number-system exercise with a C++ compiler:

```bash
g++ "Number System/decimal_to_binary.cpp" -o decimal_to_binary
./decimal_to_binary

g++ "Number System/decimal_to_binary_place_value.cpp" -o decimal_to_binary_place_value
./decimal_to_binary_place_value
```

Run the binary game with:

```bash
g++ "Binary Game/binary_quest.cpp" -o binary_quest
./binary_quest
```

## Run the Python projects

The Python projects have no third-party dependencies and require Python 3.10 or newer.

```bash
python -m unittest discover -s intermediate_data_structures/tests -v
python intermediate_data_structures/examples/demo.py

python -m unittest discover -s advanced_delivery_network/tests -v
python advanced_delivery_network/examples/demo.py

python -m unittest discover -s algorithmic_transit_simulator/tests -t algorithmic_transit_simulator -v
python algorithmic_transit_simulator/examples/demo.py

python -m unittest discover -s versioned_search_engine/tests -t versioned_search_engine -v
python versioned_search_engine/examples/demo.py
```

## Learning path

Start with binary conversion to understand representations. Next, explore the intermediate implementations to see how collections, trees, heaps, and graphs work internally. Continue with the delivery-network planner and transit simulator to see graph algorithms combined with operational data structures. Finish with the versioned search engine to study indexing, ranking, caching, and retrieval.

Each Python project includes focused unit tests, a runnable demo, and documentation on the relevant operations and complexity trade-offs.
