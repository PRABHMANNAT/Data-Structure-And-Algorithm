# Command-line usage

Scan a directory with `python -m plagiarism_detector submissions`. Pass multiple
files or directories to compare them in one corpus. Text output is the default;
`--format json` emits structured matches and `--format html --output report.html`
writes a standalone review page.

`--threshold 0.6` hides lower-ranked pairs. `--k 7 --window 5` requires longer
matching fragments. `--max-bytes 500000` limits individual source files, while
`--exclude generated` skips any directory with that name. Default exclusions
include `.git`, virtual environments, Node dependencies, build output, and Python
cache directories.

The program exits with status 0 after a successful scan, including when no matches
are found. Invalid arguments or nonexistent paths return status 2 with an error
message. A result does not change any submission file.
