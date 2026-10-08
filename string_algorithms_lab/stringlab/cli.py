"""Command-line entry point for the algorithm lab."""

import argparse
import json

from .aho_corasick import AhoCorasick
from .api import ALGORITHMS, compare, search
from .common_substring import longest_common_substring
from .edit_distance import edit_distance
from .lcs import longest_common_subsequence
from .palindrome import longest_palindrome
from .repeated_substring import longest_repeated_substring
from .rotation import minimal_rotation
from .suffix_search import SuffixIndex
from .wildcard import glob_match


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="stringlab", description="Explore string algorithms")
    commands = root.add_subparsers(dest="command", required=True)
    exact = commands.add_parser("search", help="find all exact matches")
    exact.add_argument("text")
    exact.add_argument("pattern")
    exact.add_argument("--algorithm", choices=ALGORITHMS, default="kmp")
    for name in ("compare", "suffix"):
        sub = commands.add_parser(name)
        sub.add_argument("text")
        sub.add_argument("pattern")
    multi = commands.add_parser("multi", help="match several patterns")
    multi.add_argument("text")
    multi.add_argument("patterns", nargs="+")
    for name in ("palindrome", "repeat", "rotate"):
        commands.add_parser(name).add_argument("text")
    for name in ("distance", "lcs", "substring", "glob"):
        sub = commands.add_parser(name)
        sub.add_argument("left")
        sub.add_argument("right")
    return root


def run(args: argparse.Namespace) -> object:
    name = args.command
    if name == "search":
        return search(args.text, args.pattern, args.algorithm).as_dict()
    if name == "compare":
        return {key: value.as_dict() for key, value in compare(args.text, args.pattern).items()}
    if name == "suffix":
        return {"positions": SuffixIndex(args.text).find_all(args.pattern)}
    if name == "multi":
        return AhoCorasick(args.patterns).find_all(args.text)
    if name == "palindrome":
        return {"substring": longest_palindrome(args.text)}
    if name == "repeat":
        return {"substring": longest_repeated_substring(args.text)}
    if name == "rotate":
        return {"rotation": minimal_rotation(args.text)}
    if name == "distance":
        return {"distance": edit_distance(args.left, args.right)}
    if name == "lcs":
        return {"subsequence": longest_common_subsequence(args.left, args.right)}
    if name == "substring":
        return {"substring": longest_common_substring(args.left, args.right)}
    if name == "glob":
        return {"matches": glob_match(args.left, args.right)}
    raise ValueError(f"unknown command: {name}")


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    print(json.dumps(run(args), ensure_ascii=False, sort_keys=True))
    return 0
