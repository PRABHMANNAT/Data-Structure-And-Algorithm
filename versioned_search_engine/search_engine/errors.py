class SearchError(Exception):
    """Base exception for search engine operations."""

class QuerySyntaxError(SearchError):
    """Raised when a Boolean query cannot be parsed."""

class UnknownDocumentError(SearchError):
    """Raised when a required document cannot be located."""
