from .models import Connection
class DisruptionBoard:
 def __init__(self):self.cancelled=set();self.delays={}
 def cancel(self,connection_id):self.cancelled.add(connection_id)
 def delay(self,connection_id,minutes):self.delays[connection_id]=max(0,minutes)
 def apply(self,connection:Connection):
  if connection.id in self.cancelled:return None
  delay=self.delays.get(connection.id,0)
  return Connection(connection.id,connection.origin,connection.destination,connection.departure+delay,connection.arrival+delay,connection.line,connection.capacity,connection.fare)
