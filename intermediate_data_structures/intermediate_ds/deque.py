class Deque:
    def __init__(self): self._items = []
    def __len__(self): return len(self._items)
    def append_left(self, value): self._items.insert(0, value)
    def append_right(self, value): self._items.append(value)
    def pop_left(self):
        if not self._items: raise IndexError("pop from empty deque")
        return self._items.pop(0)
    def pop_right(self):
        if not self._items: raise IndexError("pop from empty deque")
        return self._items.pop()
