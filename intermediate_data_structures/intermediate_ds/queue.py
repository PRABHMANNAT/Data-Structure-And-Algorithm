from collections import deque
class Queue:
    def __init__(self): self._items = deque()
    def __len__(self): return len(self._items)
    def enqueue(self, value): self._items.append(value)
    def dequeue(self):
        if not self._items: raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    def peek(self):
        if not self._items: raise IndexError("peek from empty queue")
        return self._items[0]
