"""Exact O(1) LRU implemented with a map and an intrusive linked list."""


class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self.next = None


class LRU:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.nodes = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def access(self, key):
        hit = key in self.nodes
        evicted = None
        if hit:
            node = self.nodes[key]
            self._unlink(node)
        else:
            if len(self.nodes) == self.capacity:
                victim = self.head.next
                evicted = victim.key
                self._unlink(victim)
                del self.nodes[evicted]
            node = Node(key)
            self.nodes[key] = node
        self._append(node)
        return hit, evicted

    def snapshot(self):
        result = []
        node = self.head.next
        while node is not self.tail:
            result.append(node.key)
            node = node.next
        return result
