import pytest

from library import Library
from models.book import Book
from models.member import Member


@pytest.fixture
def library():
    lib = Library("test.json")

    lib.add_book(Book("Python", "Mark Lutz", "101"))
    lib.add_book(Book("Fluent Python", "Luciano", "102"))

    lib.register_member(Member("M001", "Alice"))
    lib.register_member(Member("M002", "Bob"))

    return lib