# Quantile Watch

A treap combines search-tree order with hash-derived heap priorities. Subtree sizes let it select a rank without sorting the whole window.

## Run

From the repository root, use `python -m quantilewatch --example 0`, or `python -m quantilewatch --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/quantilewatch/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Insert the new sample and delete the expired occurrence.
2. Use subtree sizes to select ranks and interpolate quartiles.
3. Score each incoming sample against the previous full window’s IQR.

## Worked example

For [1,3,5,7], median is 4, Q1 is 2.5 and Q3 is 5.5 under linear interpolation.

## Complexity and limits

Expected O(log w) updates and rank selection; adversarial treap shape can degrade to O(w).

No. It is a statistical signal. A changed distribution can generate flags without a system failure; windows shorter than four are not scored.

## Verify

Run `python -m unittest discover -s quantilewatch/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
