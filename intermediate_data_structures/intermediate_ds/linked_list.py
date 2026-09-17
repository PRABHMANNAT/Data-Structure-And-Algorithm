class LinkedList:
    class _Node:
        def __init__(self, value, next_node=None): self.value, self.next = value, next_node
    def __init__(self): self.head = self.tail = None; self._size = 0
    def __len__(self): return self._size
    def append(self, value):
        node = self._Node(value)
        if self.tail: self.tail.next = node
        else: self.head = node
        self.tail = node; self._size += 1
    def prepend(self, value):
        self.head = self._Node(value, self.head)
        if self.tail is None: self.tail = self.head
        self._size += 1
    def remove(self, value):
        previous = None; current = self.head
        while current:
            if current.value == value:
                if previous: previous.next = current.next
                else: self.head = current.next
                if current is self.tail: self.tail = previous
                self._size -= 1; return True
            previous, current = current, current.next
        return False
    def __iter__(self):
        current = self.head
        while current: yield current.value; current = current.next
