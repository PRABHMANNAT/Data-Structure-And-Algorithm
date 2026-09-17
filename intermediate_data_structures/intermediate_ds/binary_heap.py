class MinHeap:
    def __init__(self): self._items = []
    def __len__(self): return len(self._items)
    def push(self, value):
        self._items.append(value); index = len(self._items) - 1
        while index:
            parent = (index - 1) // 2
            if self._items[parent] <= value: break
            self._items[index] = self._items[parent]; index = parent
        self._items[index] = value
    def pop(self):
        if not self._items: raise IndexError("pop from empty heap")
        smallest, last = self._items[0], self._items.pop()
        if self._items:
            index = 0
            while 2 * index + 1 < len(self._items):
                child = 2 * index + 1
                if child + 1 < len(self._items) and self._items[child + 1] < self._items[child]: child += 1
                if self._items[child] >= last: break
                self._items[index] = self._items[child]; index = child
            self._items[index] = last
        return smallest
