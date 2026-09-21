from collections import Counter
class Metrics:
 def __init__(self):self.counts=Counter();self.samples={}
 def increment(self,name,amount=1):self.counts[name]+=amount
 def observe(self,name,value):self.samples.setdefault(name,[]).append(value)
 def summary(self):return {**self.counts,**{f"{k}_mean":sum(v)/len(v) for k,v in self.samples.items()}}
