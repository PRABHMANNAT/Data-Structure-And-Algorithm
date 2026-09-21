from .event_queue import Event,EventQueue
from .metrics import Metrics
class Simulator:
 def __init__(self):self.queue=EventQueue();self.metrics=Metrics();self.clock=0
 def schedule(self,time,kind,payload=None):self.queue.schedule(Event(time,kind,payload))
 def run_until(self,until,handler):
  for event in self.queue.pop_ready(until):self.clock=event.time;handler(event);self.metrics.increment(f"event_{event.kind}")
  self.clock=until
