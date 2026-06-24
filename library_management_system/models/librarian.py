class Librarian:

    def __init__(self, name):
        self.name = name

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, isbn):
        library.remove_book(isbn)

    def issue_book(self, library, member_id, isbn):
        library.issue_book(member_id, isbn)

    def return_book(self, library, member_id, isbn):
        library.return_book(member_id, isbn)