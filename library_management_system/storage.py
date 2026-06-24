import json
import os

from models.book import Book
from models.member import Member


class Storage:

    def __init__(self, filename):
        self.filename = filename

    def save(self, books, members):
        """
        Save books and members to a JSON file.
        """
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        data = {
            "books": [book.to_dict() for book in books],
            "members": [member.to_dict() for member in members]
        }

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        """
        Load books and members from a JSON file.
        """
        if not os.path.exists(self.filename):
            return [], []

        with open(self.filename, "r") as file:
            data = json.load(file)

        books = [Book.from_dict(book) for book in data.get("books", [])]
        members = [Member.from_dict(member) for member in data.get("members", [])]

        return books, members