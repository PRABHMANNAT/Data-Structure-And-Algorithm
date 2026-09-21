from .models import Journey
def validate_journey(journey:Journey,minimum_transfer=2):
 errors=[]
 for prior,current in zip(journey.connections,journey.connections[1:]):
  if prior.destination!=current.origin:errors.append("legs are disconnected")
  if current.departure-prior.arrival<minimum_transfer:errors.append("transfer buffer violated")
 return errors
