import json

file = 'books.json'

#Load books
try:
    with open(file, 'r') as f:
        books = json.load(f)
except FileNotFoundError:
    books = []

#Save books
def save_books():
    with open("books.json", "w") as data:
        json.dump(books, data, indent=4)

# Add a new book
def add_book():
    title = input("Insert book title: ")
    author = input("Insert book author: ")
    year = input("Insert book year: ")
    genre = input("Insert book genre: ")
    borrowed = input("Is the book borrowed (yes/no): ")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "borrowed": borrowed
    }

    books.append(book)
    list_books()
    save_books()

# List all books
def list_books():
    if not books:
        print("No books available.")
    for index, book in enumerate(books):
        print("No:", index + 1)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Genre:", book["genre"])
        print("Borrowed:", book["borrowed"])
        print("-----")

# Edit a book
def edit_book():
    list_books()
    try:
        no_book = int(input("Choose book number you want to edit: "))
        new_book = books[no_book - 1]
    except (IndexError, ValueError):
        print("Invalid book number.")
        return

    print('1. Title:', new_book['title'])
    print('2. Author:', new_book['author'])
    print('3. Year:', new_book['year'])
    print('4. Genre:', new_book['genre'])
    print('5. Borrowed:', new_book['borrowed'])

    update_field = input("Choose field number to update: ")
    if update_field == "1":
        new_book['title'] = input('Input new title: ')
    elif update_field == "2":
        new_book['author'] = input('Input new author: ')
    elif update_field == "3":
        new_book['year'] = input('Input new year: ')
    elif update_field == "4":
        new_book['genre'] = input('Input new genre: ')
    elif update_field == "5":
        new_book['borrowed'] = input('Is the book borrowed (yes/no): ')
    else:
        print("No such option.")
        return

    books[no_book - 1] = new_book
    save_books()
    print("Book updated.")

# Delete a book
def delete_book():
    list_books()
    try:
        no_book = int(input("Choose book number you want to delete: "))
        books.pop(no_book - 1)
        save_books()
        print("Book deleted.")
    except (IndexError, ValueError):
        print("Invalid book number.")

# Main menu loop
while True:
    print("\n-- Please Choose Menu --")
    print("1. Add book")
    print("2. List of books")
    print("3. Edit book")
    print("4. Delete book")
    print("5. Exit")

    menu = input("Choose menu: ")
    if menu == "1":
        add_book()
    elif menu == "2":
        list_books()
    elif menu == "3":
        edit_book()
    elif menu == "4":
        delete_book()
    elif menu == "5":
        print("Exiting...")
        break
    else:
        print("Invalid menu. Please try again.")
