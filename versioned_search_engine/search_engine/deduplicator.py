from .bloom_filter import BloomFilter
class Deduplicator:
 def __init__(self):self.seen=BloomFilter();self.exact=set()
 def first_seen(self,key):
  if key in self.seen and key in self.exact:return False
  self.seen.add(key);self.exact.add(key);return True
