class _Node:
    def __init__(self): self.children = {}; self.values = []

class PrefixTrie:
    def __init__(self): self.root = _Node()
    def insert(self, word, value):
        node = self.root
        for char in word.casefold(): node = node.children.setdefault(char, _Node())
        node.values.append(value)
    def search(self, prefix, limit=10):
        node = self.root
        for char in prefix.casefold():
            if char not in node.children: return []
            node = node.children[char]
        matches = []
        def visit(current):
            if len(matches) >= limit: return
            matches.extend(current.values)
            for key in sorted(current.children): visit(current.children[key])
        visit(node); return matches[:limit]
