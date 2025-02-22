class Book:
    book_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = Book.book_count
        self.available = True
        Book.book_count += 1

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available.")

    def check_available(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Book {self.title} by {self.author} [ID: {self.book_id}] - Status: {status}")

books = []

while True:
    print("__Menu__")
    print("1. List books")
    print("2. Add book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Check book availability")
    print("6. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        if not books:
            print("No available books.")
        else:
            for index, book in enumerate(books, start=1):
                status = "Available" if book.available else "Borrowed"
                print(f"{index}. {book.title} by {book.author} ID: {book.book_id} - {status}")

    elif menu == "2":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        new_book = Book(title, author)
        books.append(new_book)
        print(f"Book {title} by {author} has been added with ID {new_book.book_id}.")

    elif menu == "3":
        book_id = int(input("Enter book ID to borrow: "))
        found = False
        for book in books:
            if book.book_id == book_id:
                book.borrow_book()
                found = True
                break
        if not found:
            print("Book with that ID was not found.")

    elif menu == "4":
        book_id = int(input("Enter book ID to return: "))
        found = False
        for book in books:
            if book.book_id == book_id:
                book.return_book()
                found = True
                break
        if not found:
            print("Book with that ID was not found.")

    elif menu == "5":
        book_id = int(input("Enter book ID to check availability: "))
        found = False
        for book in books:
            if book.book_id == book_id:
                book.check_available()
                found = True
                break
        if not found:
            print("Book with that ID was not found.")

    elif menu == "6":
        print("Exiting library system...")
        break

    else:
        print("Invalid menu option. Please try again.")