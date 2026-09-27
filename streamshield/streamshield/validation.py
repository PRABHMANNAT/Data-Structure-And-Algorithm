from .limits import ResourceLimits
from .model import Event

def validate_event(event: Event, limits: ResourceLimits = ResourceLimits()) -> Event:
    limits.validate_key(event.key)
    if len(event.labels) > limits.max_labels: raise ValueError("too many labels")
    if any(not key or not value for key, value in event.labels.items()): raise ValueError("labels must be non-empty")
    return event
