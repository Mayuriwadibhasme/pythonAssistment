class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display_info(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"  - {book.title}")
        else:
            print("No books borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added successfully.")

    def lend_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id and b.is_available), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book and member:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"Book '{book.title}' lent to {member.name}.")
        else:
            print("Either book not available or member not found.")

    def return_book(self, book_id, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            book = next((b for b in member.borrowed_books if b.book_id == book_id), None)
            if book:
                book.is_available = True
                member.borrowed_books.remove(book)
                print(f"Book '{book.title}' returned successfully.")
            else:
                print("This member did not borrow that book.")
        else:
            print("Member not found.")

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            book.display_info()


# Menu-driven interface
def menu():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            library.add_book(Book(book_id, title, author))

        elif choice == "2":
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == "3":
            book_id = input("Enter Book ID to lend: ")
            member_id = input("Enter Member ID: ")
            library.lend_book(book_id, member_id)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            member_id = input("Enter Member ID: ")
            library.return_book(book_id, member_id)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the menu
menu()
