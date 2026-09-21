class BloomFilter:
 def __init__(self,size=1024,hashes=3): self.size=size;self.hashes=hashes;self.bits=0
 def _positions(self,item):
  text=str(item)
  for seed in range(self.hashes):yield hash((seed,text))%self.size
 def add(self,item):
  for position in self._positions(item):self.bits|=1<<position
 def __contains__(self,item):return all(self.bits&(1<<position) for position in self._positions(item))
