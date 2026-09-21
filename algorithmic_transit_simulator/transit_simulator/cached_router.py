from .lru_cache import LRUCache
from .router import EarliestArrivalRouter

class CachedRouter:
 def __init__(self,router:EarliestArrivalRouter,capacity=256): self.router=router;self.cache=LRUCache(capacity)
 def route(self,origin,destination,departure):
  key=(origin,destination,departure)
  cached=self.cache.get(key)
  if cached is not None:return cached
  result=self.router.route(origin,destination,departure)
  if result is not None:self.cache.put(key,result)
  return result
 def invalidate(self): self.cache=LRUCache(self.cache.capacity)
