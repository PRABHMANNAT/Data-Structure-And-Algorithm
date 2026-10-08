"""Longest repeated substring from adjacent suffixes."""

from .lcp import lcp_array
from .suffix_array import suffix_array


def longest_repeated_substring(text: str) -> str:
    order = suffix_array(text)
    lcp = lcp_array(text, order)
    if not lcp:
        return ""
    best = max(range(len(lcp)), key=lambda i: lcp[i])
    return text[order[best]:order[best] + lcp[best]]
