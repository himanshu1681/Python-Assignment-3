from book import Book
from inventory import LibraryInventory

def main():
    library = LibraryInventory()

    while True:
        print("Menu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added.")

        elif choice == '2':
            isbn = input("ISBN to issue: ")
            book = library.search_by_isbn(isbn)
            if book and book.issue():
                print("Book issued.")
            else:
                print("Book not available or not found.")

        elif choice == '3':
            isbn = input("ISBN to return: ")
            book = library.search_by_isbn(isbn)
            if book and book.return_book():
                print("Book returned.")
            else:
                print("Book not found or already available.")

        elif choice == '4':
            library.display_all()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()