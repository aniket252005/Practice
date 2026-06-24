from storage import Storage
from exceptions import (
    BookNotFound,
    BookUnavailable,
    MemberNotFound,
    DuplicateISBN,
    LimitExceeded,
)


class Library:

    def __init__(self, filename="data/library.json"):
        self.books = []
        self.members = []
        self.storage = Storage(filename)

    # -------------------------
    # BOOK METHODS
    # -------------------------

    def add_book(self, book):

        if self.search_by_isbn(book.isbn):
            raise DuplicateISBN("Book with this ISBN already exists.")

        self.books.append(book)

    def remove_book(self, isbn):

        book = self.search_by_isbn(isbn)

        if not book:
            raise BookNotFound("Book not found.")

        self.books.remove(book)

    # -------------------------
    # MEMBER METHODS
    # -------------------------

    def register_member(self, member):

        self.members.append(member)

    def remove_member(self, member_id):

        member = next(
            (m for m in self.members if m.member_id == member_id),
            None
        )

        if not member:
            raise MemberNotFound("Member not found.")

        self.members.remove(member)

    # -------------------------
    # SEARCH METHODS
    # -------------------------

    def search_by_isbn(self, isbn):

        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def search_by_title(self, title):

        return [
            book
            for book in self.books
            if title.lower() in book.title.lower()
        ]

    def search_by_author(self, author):

        return [
            book
            for book in self.books
            if author.lower() in book.author.lower()
        ]

    # -------------------------
    # ISSUE / RETURN
    # -------------------------

    def issue_book(self, member_id, isbn):

        member = next(
            (m for m in self.members if m.member_id == member_id),
            None
        )

        if not member:
            raise MemberNotFound("Member not found.")

        book = self.search_by_isbn(isbn)

        if not book:
            raise BookNotFound("Book not found.")

        if not book.available:
            raise BookUnavailable("Book is already issued.")

        if not member.can_issue():
            raise LimitExceeded("Member has reached borrowing limit.")

        member.issue_book(isbn)
        book.borrow()

    def return_book(self, member_id, isbn):

        member = next(
            (m for m in self.members if m.member_id == member_id),
            None
        )

        if not member:
            raise MemberNotFound("Member not found.")

        book = self.search_by_isbn(isbn)

        if not book:
            raise BookNotFound("Book not found.")

        member.return_book(isbn)
        book.return_book()

    # -------------------------
    # LIST METHODS
    # -------------------------

    def list_books(self):
        return self.books

    def list_members(self):
        return self.members

    # -------------------------
    # STORAGE METHODS
    # -------------------------

    def save(self):

        self.storage.save(
            self.books,
            self.members
        )

    def load(self):

        self.books, self.members = self.storage.load()