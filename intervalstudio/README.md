# Interval Studio

Finding overlaps and choosing the best compatible set are different problems. An augmented AVL tree answers overlap queries; a dynamic program maximizes booking value.

## Run

From the repository root, use `python -m intervalstudio --example 0`, or `python -m intervalstudio --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/intervalstudio/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Insert bookings into a balanced tree with each subtree’s maximum endpoint.
2. Prune overlap searches using maximum ends and half-open boundaries.
3. Sort by finish time, binary-search predecessors and backtrack the optimal value DP.

## Worked example

A long booking worth 10 loses to two touching bookings worth 8 each: total 16.

## Complexity and limits

AVL insertion O(log n); weighted scheduling O(n log n); overlap query may visit O(n) nodes.

No. That booking can block several compatible ones whose combined value is larger.

## Verify

Run `python -m unittest discover -s intervalstudio/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
