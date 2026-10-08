"""Repeated exact queries over one suffix-array index."""

from .suffix_array import suffix_array


class SuffixIndex:
    def __init__(self, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.text = text
        self.order = suffix_array(text)

    def find_all(self, pattern: str) -> list[int]:
        if not isinstance(pattern, str):
            raise TypeError("pattern must be a string")
        if not pattern:
            return list(range(len(self.text) + 1))

        def boundary(upper: bool) -> int:
            low, high = 0, len(self.order)
            while low < high:
                mid = (low + high) // 2
                prefix = self.text[self.order[mid]:self.order[mid] + len(pattern)]
                if prefix < pattern or (upper and prefix == pattern):
                    low = mid + 1
                else:
                    high = mid
            return low

        return sorted(self.order[boundary(False):boundary(True)])
