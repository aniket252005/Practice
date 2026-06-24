class LibraryError(Exception):
    """Base exception for Library."""
    pass


class BookNotFound(LibraryError):
    """Raised when book is not found."""
    pass


class BookUnavailable(LibraryError):
    """Raised when book is already borrowed."""
    pass


class MemberNotFound(LibraryError):
    """Raised when member is not found."""
    pass


class DuplicateISBN(LibraryError):
    """Raised when ISBN already exists."""
    pass


class LimitExceeded(LibraryError):
    """Raised when member has reached maximum book limit."""
    pass