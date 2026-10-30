# DAGflow

A dependency graph separates what can run concurrently from what must wait. The critical path bounds completion time even with unlimited workers.

## Run

From the repository root, use `python -m dagflow --example 0`, or `python -m dagflow --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/dagflow/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Topologically order tasks and reject cycles.
2. Compute earliest/latest times to identify zero-slack critical tasks.
3. List-schedule ready tasks on the worker pool; longest ready task wins.

## Worked example

Two independent tasks lasting 4 and 3 finish in 4 with two workers, but 7 with one.

## Complexity and limits

Topology/critical passes O(V+E), with heap ordering overhead; scheduling here scans pending tasks.

No. Slack is computed from dependencies alone. Actual resource contention can create additional waiting.

## Verify

Run `python -m unittest discover -s dagflow/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
