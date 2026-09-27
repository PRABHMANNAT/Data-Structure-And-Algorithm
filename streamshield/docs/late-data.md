# Late data

Late events are rejected rather than silently included. This preserves a clear
event-time contract: an event earlier than the current watermark cannot alter an
already-finalised result. Callers can count and route `LateEvent` exceptions.
