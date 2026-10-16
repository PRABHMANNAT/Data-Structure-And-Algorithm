# Plagiarism Detection System

A small, explainable source-code similarity detector for coursework review. It normalizes
identifier names and literals, selects stable token fingerprints with winnowing, retrieves
candidate pairs through an inverted index, and reports overlap plus matching source lines.
It uses only the Python standard library at runtime.

## Quick start

From this directory, run:

```powershell
python -m plagiarism_detector examples/submissions
python -m plagiarism_detector examples/submissions --format html --output report.html
python -m unittest discover -s tests -v
```

Install an optional command with `python -m pip install -e .`, then use
`plagiarism-detect path/to/submissions`.

The scanner supports Python, JavaScript, TypeScript, Java, C, C++, Go, and Rust file
extensions. It compares files within the same detected language. Unsupported, non-UTF-8,
or oversized files are skipped. Use `--help` to see thresholds and scanning limits.

## How to read a result

The score blends fingerprint containment (55%), fingerprint Jaccard overlap (30%),
and the longest shared consecutive token run (15%). A high score is a lead for a
human reviewer, not proof of misconduct. Common assignments, starter code, and
routine algorithms can produce similar solutions. Review the cited line spans and
the assignment context before making a decision.

See [architecture](docs/architecture.md), [scoring](docs/scoring.md), and
[limitations](docs/limitations.md) for the implementation and trade-offs.
