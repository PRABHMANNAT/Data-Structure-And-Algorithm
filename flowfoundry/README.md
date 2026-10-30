# Flow Foundry

Capacity constraints turn pathfinding into a flow problem. Reverse residual arcs let later augmentations undo earlier choices.

## Run

From the repository root, use `python -m flowfoundry --example 0`, or `python -m flowfoundry --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/flowfoundry/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Construct an independent residual/reverse pair for every input edge.
2. Use BFS levels and blocking-flow DFS until the sink is unreachable.
3. Find the reachable residual side; outgoing original capacities form the minimum cut.

## Worked example

s→a capacity 7 and a→t capacity 4 carry at most 4 units; the final cut has capacity 4.

## Complexity and limits

Dinic has a general O(V²E) bound; the bounded demo records one trace per BFS phase.

No. Original antiparallel and parallel edges need separate residual pairs to preserve capacities and flow accounting.

## Verify

Run `python -m unittest discover -s flowfoundry/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
