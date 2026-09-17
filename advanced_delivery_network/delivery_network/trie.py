class Trie:
    def __init__(self): self._root = {}
    def add(self, word, value):
        node = self._root
        for char in word.lower(): node = node.setdefault(char, {})
        node.setdefault("_values", []).append(value)
    def suggest(self, prefix, limit=5):
        node = self._root
        for char in prefix.lower():
            if char not in node: return []
            node = node[char]
        result = []
        def visit(current):
            result.extend(current.get("_values", []))
            for char in sorted(key for key in current if key != "_values"):
                if len(result) < limit: visit(current[char])
        visit(node); return result[:limit]
