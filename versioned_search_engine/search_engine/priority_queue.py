import heapq
class TopK:
 def __init__(self,k):self.k=k;self.items=[]
 def add(self,score,value):
  heapq.heappush(self.items,(score,value))
  if len(self.items)>self.k:heapq.heappop(self.items)
 def results(self):return tuple(value for _,value in sorted(self.items,reverse=True))
