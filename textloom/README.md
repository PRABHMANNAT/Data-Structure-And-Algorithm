# Textloom

Myers follows the furthest reachable position on each edit diagonal, extending equal-line runs for free. Backtracking produces a shortest insert/delete script.

## Run

From the repository root, use `python -m textloom --example 0`, or `python -m textloom --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/textloom/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Tokenize documents as lines while preserving newline characters.
2. Expand edit-distance frontiers until the revised document is reached.
3. Backtrack, apply the patch and apply its inverse to verify both directions.

## Worked example

Changing a
b to a
c requires one deletion and one insertion; replacement is not a primitive operation.

## Complexity and limits

O((N+M)D) frontier work; saved backtracking frontiers use O(D²) memory; input is capped at 120 lines.

No. This model counts only insertions and deletions, so replacement costs two edits.

## Verify

Run `python -m unittest discover -s textloom/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
