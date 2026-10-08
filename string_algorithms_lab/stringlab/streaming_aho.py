"""Incremental multi-pattern scanning over text chunks."""

from .aho_corasick import AhoCorasick


class AhoStream:
    def __init__(self, patterns: list[str] | tuple[str, ...]) -> None:
        self.automaton = AhoCorasick(patterns)
        self.state = self.automaton.root
        self.offset = 0

    def feed(self, chunk: str) -> dict[str, list[int]]:
        if not isinstance(chunk, str):
            raise TypeError("chunk must be a string")
        result = {pattern: [] for pattern in self.automaton.patterns}
        for index, char in enumerate(chunk):
            self.state = self.automaton.step(self.state, char)
            for pattern in self.state.outputs:
                result[pattern].append(self.offset + index - len(pattern) + 1)
        self.offset += len(chunk)
        return result
