from .models import Journey
def zone_fare(journey:Journey,cap:int=12):
 """Charge summed legs up to a daily fare cap."""
 return min(journey.fare,cap)
def transfer_count(journey:Journey):return max(0,len(journey.connections)-1)
