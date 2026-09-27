class RollbackDSU:
    """Union-find supporting O(1) snapshots and rollback."""
    def __init__(self, items: list[str]) -> None:
        self.parent = {item: item for item in items}; self.size = {item: 1 for item in items}; self.history: list[tuple[str, str, int] | None] = []
    def find(self, item: str) -> str:
        while self.parent[item] != item: item = self.parent[item]
        return item
    def union(self, left: str, right: str) -> bool:
        a, b = self.find(left), self.find(right)
        if a == b: self.history.append(None); return False
        if self.size[a] < self.size[b]: a, b = b, a
        self.history.append((b, a, self.size[a])); self.parent[b] = a; self.size[a] += self.size[b]; return True
    def snapshot(self) -> int: return len(self.history)
    def rollback(self, snapshot: int) -> None:
        while len(self.history) > snapshot:
            change = self.history.pop()
            if change: child, root, old_size = change; self.parent[child] = child; self.size[root] = old_size
