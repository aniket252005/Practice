from dataclasses import dataclass, field


@dataclass
class Member:
    member_id: str
    name: str
    issued_books: list = field(default_factory=list)

    MAX_BOOKS = 3

    def can_issue(self):
        """
        Return True if member can issue another book.
        """
        return len(self.issued_books) < self.MAX_BOOKS

    def issue_book(self, isbn):
        """
        Add ISBN to issued books.
        """
        if self.can_issue():
            self.issued_books.append(isbn)

    def return_book(self, isbn):
        """
        Remove ISBN from issued books.
        """
        if isbn in self.issued_books:
            self.issued_books.remove(isbn)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "issued_books": self.issued_books,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            member_id=data["member_id"],
            name=data["name"],
            issued_books=data["issued_books"],
        )