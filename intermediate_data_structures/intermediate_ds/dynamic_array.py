class DynamicArray:
    """Resizable contiguous collection with explicit capacity management."""
    def __init__(self, capacity=4):
        self._data = [None] * max(1, capacity); self._size = 0
    def __len__(self): return self._size
    def _grow(self):
        self._data.extend([None] * len(self._data))
    def append(self, value):
        if self._size == len(self._data): self._grow()
        self._data[self._size] = value; self._size += 1
    def get(self, index):
        if not 0 <= index < self._size: raise IndexError("index out of range")
        return self._data[index]
    def set(self, index, value):
        if not 0 <= index < self._size: raise IndexError("index out of range")
        self._data[index] = value
    def pop(self):
        if not self._size: raise IndexError("pop from empty array")
        self._size -= 1; value = self._data[self._size]; self._data[self._size] = None
        return value
    def __iter__(self):
        for i in range(self._size): yield self._data[i]
