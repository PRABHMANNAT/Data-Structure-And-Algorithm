from collections import OrderedDict
class LRUCache:
 def __init__(self, capacity=128):
  if capacity < 1: raise ValueError("capacity must be positive")
  self.capacity=capacity; self._data=OrderedDict(); self.hits=self.misses=0
 def get(self,key,default=None):
  if key not in self._data: self.misses+=1; return default
  self.hits+=1; self._data.move_to_end(key); return self._data[key]
 def put(self,key,value):
  self._data[key]=value; self._data.move_to_end(key)
  if len(self._data)>self.capacity: self._data.popitem(last=False)
 def __contains__(self,key): return key in self._data
