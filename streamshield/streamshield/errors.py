class StreamShieldError(Exception):
    """Base exception for a rejected stream operation."""


class InvalidEvent(StreamShieldError):
    """An event does not meet the engine contract."""


class LateEvent(StreamShieldError):
    """An event is older than the accepted watermark."""


class SnapshotCorrupt(StreamShieldError):
    """A snapshot failed integrity verification."""
