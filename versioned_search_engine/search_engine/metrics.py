from collections import Counter
class Metrics:
 def __init__(self):self.counts=Counter()
 def inc(self,key):self.counts[key]+=1
 def get(self,key):return self.counts[key]
