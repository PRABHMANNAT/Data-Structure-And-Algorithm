# Spatial Desk

A KD tree divides Cartesian space along alternating axes. A subtree can be skipped when its split plane is farther away than the current search bound.

## Run

From the repository root, use `python -m spatialdesk --example 0`, or `python -m spatialdesk --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/spatialdesk/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Median-split points recursively by X then Y.
2. Search the nearer branch and maintain the best k points in a max-heap.
3. Visit the far branch only when its split plane could improve the result.

## Worked example

Four points one unit from the origin tie on distance; names break ties deterministically.

## Complexity and limits

Build O(n log² n) with repeated sorting; average queries often prune well, worst case O(n log k).

No. Its performance depends on dimension and geometry; worst-case search still visits every point.

## Verify

Run `python -m unittest discover -s spatialdesk/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
