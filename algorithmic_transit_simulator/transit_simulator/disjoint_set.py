class DisjointSet:
    """Union-find with path compression and union by size."""
    def __init__(self, items=()):
        self.parent = {item: item for item in items}; self.size = {item: 1 for item in items}

    def add(self, item):
        if item not in self.parent: self.parent[item] = item; self.size[item] = 1

    def find(self, item):
        self.add(item)
        if self.parent[item] != item: self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, left, right):
        left, right = self.find(left), self.find(right)
        if left == right: return False
        if self.size[left] < self.size[right]: left, right = right, left
        self.parent[right] = left; self.size[left] += self.size[right]
        return True

    def connected(self, left, right): return self.find(left) == self.find(right)
