from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    available: bool = True

    def borrow(self):
        """
        Mark the book as borrowed.
        """
        self.available = False

    def return_book(self):
        """
        Mark the book as returned.
        """
        self.available = True

    def to_dict(self):
        """
        Convert Book object into dictionary.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Book object from dictionary.
        """
        return cls(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            available=data["available"],
        )