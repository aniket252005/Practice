from library import Library
from models.book import Book
from models.member import Member
from exceptions import LibraryError


def print_menu():
    print("\n" + "=" * 40)
    print("      Library Management System")
    print("=" * 40)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book by ISBN")
    print("6. Search Book by Title")
    print("7. Search Book by Author")
    print("8. List All Books")
    print("9. List All Members")
    print("10. Save Data")
    print("11. Load Data")
    print("12. Exit")
    print("=" * 40)


def main():
    library = Library()

    while True:
        print_menu()

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")

                library.add_book(Book(title, author, isbn))
                print("✅ Book added successfully.")

            elif choice == "2":
                member_id = input("Member ID: ")
                name = input("Member Name: ")

                library.register_member(Member(member_id, name))
                print("✅ Member registered.")

            elif choice == "3":
                member_id = input("Member ID: ")
                isbn = input("ISBN: ")

                library.issue_book(member_id, isbn)
                print("✅ Book issued successfully.")

            elif choice == "4":
                member_id = input("Member ID: ")
                isbn = input("ISBN: ")

                library.return_book(member_id, isbn)
                print("✅ Book returned successfully.")

            elif choice == "5":
                isbn = input("ISBN: ")

                book = library.search_by_isbn(isbn)

                if book:
                    print(book)
                else:
                    print("Book not found.")

            elif choice == "6":
                title = input("Title: ")

                books = library.search_by_title(title)

                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books found.")

            elif choice == "7":
                author = input("Author: ")

                books = library.search_by_author(author)

                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books found.")

            elif choice == "8":

                books = library.list_books()

                if not books:
                    print("No books available.")

                for book in books:
                    print(book)

            elif choice == "9":

                members = library.list_members()

                if not members:
                    print("No members registered.")

                for member in members:
                    print(member)

            elif choice == "10":

                library.save()
                print("✅ Data saved successfully.")

            elif choice == "11":

                library.load()
                print("✅ Data loaded successfully.")

            elif choice == "12":

                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except LibraryError as e:
            print(f"❌ Error: {e}")

        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()