"""One result shape for the exact-search algorithms."""

from collections.abc import Callable

from . import horspool, kmp, naive, rabin_karp, z_search
from .models import SearchResult
from .validation import validate_text_pattern

ALGORITHMS: dict[str, Callable[[str, str], list[int]]] = {
    "naive": naive.find_all,
    "kmp": kmp.find_all,
    "z": z_search.find_all,
    "rabin-karp": rabin_karp.find_all,
    "horspool": horspool.find_all,
}


def search(text: str, pattern: str, algorithm: str = "kmp") -> SearchResult:
    validate_text_pattern(text, pattern)
    try:
        matcher = ALGORITHMS[algorithm]
    except KeyError as exc:
        raise ValueError(f"unknown algorithm: {algorithm}") from exc
    return SearchResult(algorithm, pattern, len(text), tuple(matcher(text, pattern)))


def compare(text: str, pattern: str) -> dict[str, SearchResult]:
    results = {name: search(text, pattern, name) for name in ALGORITHMS}
    expected = results["naive"].positions
    if any(result.positions != expected for result in results.values()):
        raise AssertionError("exact matchers disagree")
    return results
