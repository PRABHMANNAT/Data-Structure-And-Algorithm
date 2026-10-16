# Development

The project requires Python 3.10 or newer and has no runtime dependencies.
Run `python -m unittest discover -s tests -v` from the project directory.
The tests cover token normalization, stable hashing, rightmost-minimum winnowing,
overlap measures, candidate indexing, evidence ranges, file discovery, reports,
and the CLI.

Keep changes to lexical rules paired with tests for comments, strings, and source
positions. For scoring changes, add examples of both copied and independently
written code and explain the trade-off in `scoring.md`. Keep machine-readable
fields stable or document a schema change. Use deterministic ordering so the same
corpus yields the same report on repeated runs.
