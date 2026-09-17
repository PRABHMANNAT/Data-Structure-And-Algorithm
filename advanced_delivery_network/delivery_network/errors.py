class DeliveryNetworkError(Exception):
    """Base error for the domain."""

class DuplicateStopError(DeliveryNetworkError):
    pass

class UnknownStopError(DeliveryNetworkError):
    pass

class PathNotFoundError(DeliveryNetworkError):
    pass
