"""Aho-Corasick automaton for simultaneous pattern matching."""

from collections import deque

from .validation import validate_patterns


class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}
        self.fail: Node | None = None
        self.outputs: list[str] = []


class AhoCorasick:
    def __init__(self, patterns: list[str] | tuple[str, ...]) -> None:
        self.patterns = validate_patterns(patterns)
        self.root = Node()
        self.root.fail = self.root
        for pattern in self.patterns:
            node = self.root
            for char in pattern:
                node = node.children.setdefault(char, Node())
            node.outputs.append(pattern)
        queue: deque[Node] = deque()
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)
        while queue:
            node = queue.popleft()
            for char, child in node.children.items():
                failure = node.fail
                while failure is not self.root and char not in failure.children:
                    assert failure is not None
                    failure = failure.fail
                assert failure is not None
                child.fail = failure.children.get(char, self.root)
                child.outputs.extend(child.fail.outputs)
                queue.append(child)

    def step(self, state: Node, char: str) -> Node:
        while state is not self.root and char not in state.children:
            assert state.fail is not None
            state = state.fail
        return state.children.get(char, self.root)

    def find_all(self, text: str) -> dict[str, list[int]]:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        result = {pattern: [] for pattern in self.patterns}
        state = self.root
        for index, char in enumerate(text):
            state = self.step(state, char)
            for pattern in state.outputs:
                result[pattern].append(index - len(pattern) + 1)
        return result
