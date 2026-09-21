class LinkGraph:
 def __init__(self):self.edges={}
 def add(self,source,target):self.edges.setdefault(source,set()).add(target)
 def neighbors(self,source):return tuple(sorted(self.edges.get(source,())))
 def recommend(self,source,limit=5):
  scores={}
  for neighbor in self.neighbors(source):
   for candidate in self.neighbors(neighbor):
    if candidate!=source:scores[candidate]=scores.get(candidate,0)+1
  return tuple(key for key,_ in sorted(scores.items(),key=lambda item:(-item[1],item[0]))[:limit])
