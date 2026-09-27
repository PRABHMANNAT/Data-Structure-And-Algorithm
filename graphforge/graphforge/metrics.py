from collections import Counter

class Metrics:
    def __init__(self) -> None: self._values: Counter[str] = Counter()
    def add(self, name: str, value: int = 1) -> None: self._values[name] += value
    def export(self) -> dict[str, int]: return dict(self._values)
