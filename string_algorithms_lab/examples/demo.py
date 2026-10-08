"""Small self-contained tour of the public algorithms."""

from stringlab.aho_corasick import AhoCorasick
from stringlab.api import compare
from stringlab.palindrome import longest_palindrome
from stringlab.suffix_search import SuffixIndex


if __name__ == "__main__":
    text = "bananana"
    print("Exact matches:", {key: value.positions for key, value in compare(text, "ana").items()})
    print("Multi-pattern:", AhoCorasick(["ana", "na"]).find_all(text))
    print("Suffix index:", SuffixIndex(text).find_all("ana"))
    print("Longest palindrome:", longest_palindrome(text))
