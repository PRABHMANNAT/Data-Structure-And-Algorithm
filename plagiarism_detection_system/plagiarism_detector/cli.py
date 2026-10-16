"""Command-line interface for corpus scans and individual comparisons."""

import argparse
import sys
from pathlib import Path

from .engine import Detector, DetectorConfig
from .files import discover
from .report import to_html, to_json, to_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Find similar source-code files for review")
    parser.add_argument("paths", nargs="+", help="Files or directories to compare")
    parser.add_argument("--format", choices=("text", "json", "html"), default="text")
    parser.add_argument("--output", type=Path, help="Write report to a file")
    parser.add_argument("--threshold", type=float, default=0.35, help="Minimum score, 0 to 1")
    parser.add_argument("--k", type=int, default=5, help="Tokens in each fingerprint k-gram")
    parser.add_argument("--window", type=int, default=4, help="Winnowing window size")
    parser.add_argument("--max-bytes", type=int, default=8_000_000)
    parser.add_argument("--exclude", action="append", default=[], help="Directory name to skip")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = DetectorConfig(k=args.k, window=args.window, min_score=args.threshold)
        documents = []
        for path in args.paths:
            documents.extend(discover(path, args.max_bytes, set(args.exclude)))
        matches = Detector(config).compare(documents)
    except (ValueError, FileNotFoundError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    render = {"text": to_text, "json": to_json, "html": to_html}[args.format]
    output = render(matches)
    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0
