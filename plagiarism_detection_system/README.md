# Plagiarism Detection System

A small, explainable source and document similarity detector for coursework review.
It compares PDF, DOCX, TXT, and Markdown files as prose, and also compares supported
source-code files. It selects stable token fingerprints with winnowing, retrieves
candidate pairs through an inverted index, and reports overlap plus matching lines.
The only runtime dependency is `pypdf` for text-based PDFs.

## Quick start

From this directory, run:

```powershell
python -m pip install -e .
python -m plagiarism_detector.web --port 8000
```

Open `http://127.0.0.1:8000/` in your browser. Choose files or load the
sample pair, then select **Analyze files**. The server binds to your computer's
loopback address, and uploaded files remain in memory during the comparison.
Each browser file may be up to 8 MB; a comparison request may be up to 32 MB.

The command-line workflow is also available:

```powershell
python -m plagiarism_detector examples/submissions
python -m plagiarism_detector examples/submissions --format html --output report.html
python -m unittest discover -s tests -v
```

Install an optional command with `python -m pip install -e .`, then use
`plagiarism-detect path/to/submissions`.

The scanner supports PDF, DOCX, TXT, Markdown, Python, JavaScript, TypeScript, Java,
C, C++, Go, and Rust file extensions. PDF, DOCX, TXT, and Markdown can be compared
against one another. Source files are compared within the same detected language.
The CLI skips unsupported, unreadable, or oversized files. Scanned image-only PDFs
need OCR before comparison; password-protected PDFs are not supported. Use `--help`
to see thresholds and scanning limits.

## How to read a result

The score blends fingerprint containment (55%), fingerprint Jaccard overlap (30%),
and the longest shared consecutive token run (15%). A high score is a lead for a
human reviewer, not proof of misconduct. Common assignments, starter code, and
routine algorithms can produce similar solutions. Review the cited line spans and
the assignment context before making a decision.

See [architecture](docs/architecture.md), [scoring](docs/scoring.md), and
[limitations](docs/limitations.md) for the implementation and trade-offs.
