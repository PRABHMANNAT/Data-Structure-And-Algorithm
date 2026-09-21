from .models import Stop
from .trie import PrefixTrie

class StopIndex:
    def __init__(self): self._trie = PrefixTrie(); self._stops = {}
    def add(self, stop: Stop):
        self._stops[stop.id] = stop; self._trie.insert(stop.name, stop.id)
    def find(self, prefix: str, limit: int = 10) -> list[Stop]:
        return [self._stops[stop_id] for stop_id in self._trie.search(prefix, limit)]
