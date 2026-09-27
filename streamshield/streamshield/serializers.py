from __future__ import annotations
import json
from .model import Event

def event_to_json(event: Event) -> str:
    return json.dumps({"key": event.key, "timestamp": event.timestamp, "value": event.value, "labels": dict(event.labels)}, sort_keys=True)

def event_from_json(value: str) -> Event:
    return Event(**json.loads(value))
