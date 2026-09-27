from graphforge.cache import LRU
def test_lru_evicts_oldest() -> None:
    cache = LRU[str, int](1); cache.put("a", 1); cache.put("b", 2); assert cache.get("a") is None
