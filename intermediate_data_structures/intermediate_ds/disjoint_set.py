class DisjointSet:
    def __init__(self, values=()):
        self.parent = {}; self.rank = {}
        for value in values: self.add(value)
    def add(self, value):
        if value not in self.parent: self.parent[value] = value; self.rank[value] = 0
    def find(self, value):
        if value not in self.parent: raise KeyError(value)
        if self.parent[value] != value: self.parent[value] = self.find(self.parent[value])
        return self.parent[value]
    def union(self, first, second):
        first, second = self.find(first), self.find(second)
        if first == second: return False
        if self.rank[first] < self.rank[second]: first, second = second, first
        self.parent[second] = first
        if self.rank[first] == self.rank[second]: self.rank[first] += 1
        return True
