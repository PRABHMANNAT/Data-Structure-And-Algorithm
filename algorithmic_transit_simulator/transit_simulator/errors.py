class TransitError(Exception):
    """Base exception for invalid transit operations."""


class UnknownStopError(TransitError):
    """Raised when a requested stop is absent from the network."""


class InvalidConnectionError(TransitError):
    """Raised when a connection violates timetable rules."""
