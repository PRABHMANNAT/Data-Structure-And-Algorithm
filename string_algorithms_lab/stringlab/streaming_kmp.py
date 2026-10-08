"""KMP matcher whose state survives arbitrarily split input chunks."""

from .prefix import prefix_function


class KMPStream:
    def __init__(self, pattern: str) -> None:
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("stream pattern must be a nonempty string")
        self.pattern = pattern
        self.prefix = prefix_function(pattern)
        self.matched = 0
        self.offset = 0

    def feed(self, chunk: str) -> list[int]:
        if not isinstance(chunk, str):
            raise TypeError("chunk must be a string")
        positions: list[int] = []
        for index, char in enumerate(chunk):
            while self.matched and char != self.pattern[self.matched]:
                self.matched = self.prefix[self.matched - 1]
            if char == self.pattern[self.matched]:
                self.matched += 1
            if self.matched == len(self.pattern):
                positions.append(self.offset + index - self.matched + 1)
                self.matched = self.prefix[self.matched - 1]
        self.offset += len(chunk)
        return positions
