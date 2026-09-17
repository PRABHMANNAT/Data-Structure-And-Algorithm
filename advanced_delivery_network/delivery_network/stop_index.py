from .trie import Trie

class StopIndex:
    def __init__(self, graph):
        self.graph = graph; self._trie = Trie()
        for code in graph.codes(): self._trie.add(graph.stop(code).name, code)
    def suggest(self, prefix):
        return [self.graph.stop(code) for code in self._trie.suggest(prefix)]
