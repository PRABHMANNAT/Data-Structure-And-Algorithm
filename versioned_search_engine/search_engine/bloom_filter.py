class BloomFilter:
 def __init__(self,size=2048,hashes=4):self.size=size;self.hashes=hashes;self.bits=0
 def _spots(self,item):return (hash((seed,item))%self.size for seed in range(self.hashes))
 def add(self,item):
  for spot in self._spots(item):self.bits|=1<<spot
 def __contains__(self,item):return all(self.bits&(1<<spot) for spot in self._spots(item))
