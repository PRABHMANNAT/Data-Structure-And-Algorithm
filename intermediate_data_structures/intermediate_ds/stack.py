class Stack:
    def __init__(self): self._items = []
    def __len__(self): return len(self._items)
    def push(self, value): self._items.append(value)
    def peek(self):
        if not self._items: raise IndexError("peek from empty stack")
        return self._items[-1]
    def pop(self):
        if not self._items: raise IndexError("pop from empty stack")
        return self._items.pop()
