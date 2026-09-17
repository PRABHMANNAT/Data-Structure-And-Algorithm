class Trie:
    def __init__(self): self._root = {}
    def add(self, word):
        node = self._root
        for letter in word: node = node.setdefault(letter, {})
        node[""] = True
    def contains(self, word):
        node = self._root
        for letter in word:
            if letter not in node: return False
            node = node[letter]
        return "" in node
    def starts_with(self, prefix):
        node = self._root
        for letter in prefix:
            if letter not in node: return False
            node = node[letter]
        return True
