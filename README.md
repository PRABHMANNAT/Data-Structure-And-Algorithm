# Data Structures & Algorithms

**Fieldnotes** is a collection of 21 hands-on experiments in Python, Go, C++, and JavaScript. Draw a route, inspect a tree, search a collection, settle a trip, or solve a small crossword. Each interface puts the input, the algorithm, and the result within reach.

The original libraries and command-line tools remain available. The browser workspaces run their real implementations locally.

## Open the collection

```sh
git clone https://github.com/PRABHMANNAT/Data-Structure-And-Algorithm.git
cd Data-Structure-And-Algorithm
python -m workbench.server
```

Open **[localhost:8765](http://127.0.0.1:8765/)**. There is no frontend build step, package installation, account, or API key required to use the workbench.

| Tool | Needed for |
| --- | --- |
| Python 3.11+ | Local server and Python projects |
| Go 1.27+ | Five Go projects; compiled on first run |
| C++20 compiler (`g++`) | Six C++ projects; compiled on first run |
| Node.js 22+ and pytest | Running the complete verification suite |

Set `CXX` to the full path of your compiler if it is not on `PATH`. First runs of native projects take longer while the bridge compiles. Build artifacts stay in `.workbench-cache/`. RouteLab and The Daily Grid can also run on any static HTTP server; the other workspaces need the Python server.

On Windows, Application Control can block locally compiled executables. The interface reports this as an execution-policy error; native projects require an environment that permits development builds. The full Linux verification also runs in GitHub Actions.

## The collection

| Workspace | Source project | What you can do |
| --- | --- | --- |
| [RouteLab](11-map-routing-pathfinding-visualizer/01-source/) | [Pathfinding visualizer](11-map-routing-pathfinding-visualizer/) | Draw terrain, pause and step through a search, compare A* and Dijkstra, undo edits, save/load maps |
| [The Daily Grid](12-crossword-puzzle-game/) | [Crossword game](12-crossword-puzzle-game/) | Solve three corrected grids, navigate with the keyboard, save each puzzle, undo edits, inspect best times |
| [Structure study](intermediate_data_structures/web/) | [intermediate_data_structures](intermediate_data_structures/) | Build a search tree from an insertion sequence. Inspect its shape, traversal, and membership. |
| [Dispatch desk](advanced_delivery_network/web/) | [advanced_delivery_network](advanced_delivery_network/) | Plan the shortest delivery route across a weighted network. Change a road cost and see the route respond. |
| [Network atlas](graphforge/web/) | [graphforge](graphforge/) | Explore versioned directed graphs. Find a weighted route and inspect an earlier revision of the network. |
| [Departure board](algorithmic_transit_simulator/web/) | [algorithmic_transit_simulator](algorithmic_transit_simulator/) | Find an earliest-arrival journey through a timetable. Explore missed transfers, waiting time, and fares. |
| [Reading room](versioned_search_engine/web/) | [versioned_search_engine](versioned_search_engine/) | Search your own small document collection with BM25 ranking. Inspect matched terms and autocomplete suggestions. |
| [Pattern bench](string_algorithms_lab/web/) | [string_algorithms_lab](string_algorithms_lab/) | Find every occurrence of a pattern. Cross-check five exact matchers and inspect overlapping matches. |
| [Source comparison](plagiarism_detection_system/web/) | [plagiarism_detection_system](plagiarism_detection_system/) | Compare two source files through normalized tokens and winnowing fingerprints. Inspect the evidence behind a similarity score. |
| [Stream monitor](streamshield/web/) | [streamshield](streamshield/) | Replay event-time data through a sliding window. Inspect late arrivals, the watermark, and heavy hitters. |
| [Go collection desk](go_data_structures_lab/web/) | [go_data_structures_lab](go_data_structures_lab/) | Min-heap extraction with a custom comparator. Every output value comes from the repository heap. |
| [Go learning journal](go-data-structures-journey/web/) | [go-data-structures-journey](go-data-structures-journey/) | Follow a divide-and-conquer merge sort with duplicate and negative-value inputs. |
| [Go sorting room](go-algorithm-workbench/web/) | [go-algorithm-workbench](go-algorithm-workbench/) | Run an in-place quicksort and compare its ordered output with the input sequence. |
| [Range observatory](go_advanced_structures/web/) | [go_advanced_structures](go_advanced_structures/) | Compare Fenwick and segment-tree sums over an inclusive range. See the prefix totals behind the query. |
| [Prefix index](go_search_structures/web/) | [go_search_structures](go_search_structures/) | Build a trie from your own vocabulary. Inspect lexicographic prefix completions and the indexed words. |
| [C++ sorting desk](cpp-dsa-toolkit/web/) | [cpp-dsa-toolkit](cpp-dsa-toolkit/) | Compare merge sort and the toolkit quick-sort API on the same integer sequence. Inspect duplicates and value gaps. |
| [Number notebook](Number%20System/web/) | [Number System](Number%20System/) | Convert signed decimal integers into binary and inspect every division step. |
| [Binary practice](Binary%20Game/web/) | [Binary Game](Binary%20Game/) | Check a binary answer against the original game conversion. Use the division trail to understand each bit. |
| [Bit workshop](Number%20System/Binary_Bitwise_Game/web/) | [Number System/Binary_Bitwise_Game](Number%20System/Binary_Bitwise_Game/) | Work with an eight-bit register. Apply the original game operations and inspect which bits change. |
| [Settle up](splitwise-cashflow-minimizer/web/) | [splitwise-cashflow-minimizer](splitwise-cashflow-minimizer/) | Turn shared expenses into net balances and a compact settlement plan. Every amount stays in integer cents. |
| [Compression room](file-zipper-huffman/web/) | [file-zipper-huffman](file-zipper-huffman/) | Compress text with the C++ Huffman codec, decompress it, and verify an exact byte-for-byte round trip. |

Links in the table browse the source on GitHub. To interact with a workspace, start the local server and choose it from the collection, or use its `/web/` address on localhost.

## Designed for working things out

The visual system uses paper surfaces, graphite type, thin rules, and data-driven color. Each project has its own result view: network diagrams, timetable itineraries, binary registers, branch inspections, search rankings, event histories, balance charts, or compression byte frequencies. Layouts adapt to small screens, keyboard focus stays visible, and print layouts remove controls.

Every library workspace includes:

- Editable input and named example scenarios, including difficult cases.
- Project-specific validation and useful error messages.
- Up to 12 saved runs, unfinished input persistence, and favorite projects.
- A previous-run comparison and a JSON result download.
- A raw-data inspector alongside the visual result.

Settle up also exports settlement CSV. Compression room exports the actual `.huf` archive and verifies decompression. Network atlas can query an earlier graph revision. Range observatory cross-checks Fenwick and segment-tree sums.

## Correctness improvements

- Crossword puzzles now cover every open square with a clue, so every grid is completable. Switching puzzles updates the correct timer, and keyboard focus advances to an input rather than its container.
- RouteLab measures the actual distinct frontier, renders the final path above visited cells, and uses stable priority ties. Map files validate dimensions, coordinates, and endpoint placement.
- Go trie completions visit sorted branches before applying the limit, making top-k suggestions deterministic.
- BM25 document-length normalization counts token occurrences rather than the character lengths of unique terms.
- Shared expenses distribute leftover cents in alphabetical participant order, preserving every cent and rejecting duplicate participants.
- Source comparison rejects malformed Python string literals consistently across Python 3.10 and newer tokenizers.

## Verify the projects

```sh
python -m pip install pytest
python scripts/verify.py
```

The verification command runs the original Python, Go, and C++ suites, all 19 browser-adapter contracts, every bundled scenario over HTTP, server/validation checks, crossword-model checks, and pathfinding regression tests. The pathfinding suite checks both algorithms across 30 deterministic terrains and verifies every step of each returned route.

Focused checks:

```sh
python scripts/verify.py --web
python scripts/verify.py --python
python scripts/verify.py --go
python scripts/verify.py --cpp
node --test 11-map-routing-pathfinding-visualizer/tests/search.test.mjs
node 12-crossword-puzzle-game/tests/puzzle-model.test.mjs
```

[GitHub Actions](https://github.com/PRABHMANNAT/Data-Structure-And-Algorithm/actions/workflows/workbench.yml) runs the complete suite on Linux. Runtime libraries use the standard library; pytest is only a development dependency for GraphForge and StreamShield tests.

## Repository layout

```text
workbench/                   Shared browser interface, local HTTP server, validation
scripts/verify.py            Repository-wide verification entrypoint
<project>/web/project.json   Input fields and named example scenarios
<project>/web/adapter.py     Validated calls into the existing implementation
<project>/web/view.js        Project-specific result visualization
<project>/web/test_adapter.py Integration tests of the browser contract
<project>/web/native*        Fixed native bridges where C++ or Go is needed
11-map-routing-pathfinding-visualizer/01-source/  Modular browser application
11-map-routing-pathfinding-visualizer/dist/       Matching static distribution
12-crossword-puzzle-game/    Dependency-free crossword application
```

Each project README documents its original API, command-line examples, concepts, and interactive workspace. Existing learning notes remain in their project directories.

## Execution and data

The server binds to `127.0.0.1`, accepts same-origin browser requests, blocks hidden files and directory listings, and limits request bodies to 64 KiB. Native bridges compile checked-in code and receive input through stdin; input is never turned into shell commands. This is a local development tool, not a production hosting service.

Favorites, drafts, maps, puzzle progress, and run history stay in this browser. Private browsing or clearing site data can remove them. You can export important results before clearing history. Results from similarity detection support human review; they do not establish plagiarism. The cashflow heap reduces transfers but does not guarantee a globally minimum transfer count.

## Learning path

Start with Number notebook and Binary practice. Move through the collection desks and Range observatory to study data structures. Use Dispatch desk, Departure board, and Network atlas to compare graph models. Continue into Reading room, Pattern bench, and Source comparison for retrieval and text algorithms. Finish with Stream monitor, Settle up, and Compression room to see data structures solve practical problems.
