from dataclasses import dataclass,field
from .binary_heap import MinHeap
@dataclass(order=True,frozen=True)
class Event: time:int; kind:str; payload:object=field(compare=False)
class EventQueue:
 def __init__(self):self._heap=MinHeap()
 def schedule(self,event):self._heap.push(event.time,event)
 def pop_ready(self,until):
  ready=[]
  while self._heap and self._heap._items[0][0]<=until:ready.append(self._heap.pop()[1])
  return ready
