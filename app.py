import os

print("--------------------------------------")
print("Welcome to the bookstore!")
print("--------------------------------------")

biblioteca = {
    "libri_disponibili": [],      # Lista di titoli
    "libri_prestati": [],          # Lista di titoli
    "utenti": {}                   # Dictionary: nome utente -> lista libri presi
}

available_books = biblioteca["libri_disponibili"]
rent_books = biblioteca["libri_prestati"]
book_index = 1
is_running = True


def show_main_menu(action):
    match action:
        case 1:

            print("--------------------------------------")
            print("Add a new book section")
            print("--------------------------------------")

            new_book = input("Add a new book to the database: ").capitalize()
            add_book(new_book)
            print("--------------------------------------")
        case 2:
            show_available(book_index)
        case 3:
            show_available(book_index)
            borrow_book()
        case 4:
            pass
        case 5:
            print("--------------------------------------")
            print("Have a nice day!")
            print("--------------------------------------")
        case _:
            print("Something went wrong, choose a different number")


def show_available(book_index):
    print("--------------------------------------")
    print("Available books:")
    print("--------------------------------------")

    for book in available_books:
        print(f"{book_index} - {book}")
        book_index += 1

    print("--------------------------------------")


def add_book(new_book):
    if new_book == " " or len(new_book) < 3:
        print("Invalid value")
    else:
        available_books.append((new_book).strip())
        show_available(book_index)


def borrow_book():
    print("--------------------------------------")
    print("Borrow book")
    print("--------------------------------------")
    rent_book = input("Digit the number of the book you want to borrow: ")

    if rent_book.isdigit():
        rent_book = int(rent_book)

        if 1 > rent_book or rent_book > len(available_books):
            print(f"Invalid value, choose a different number")

        elif 1 <= rent_book and rent_book <= len(available_books):
            chosed_book = available_books[rent_book - 1]
            rent_books.append(chosed_book)
            del available_books[rent_book - 1]

            print("--------------------------------------")
            print(f"You borrowed the book '{chosed_book}'")
            print("--------------------------------------")
            is_running = False
        else:
            print("Something went wrong")
            is_running = True
    elif rent_book.isalpha() or rent_book == " ":
        print("Invalid value, insert a number")
    else:
        print("Something went wrong")

    return is_running


while len(available_books) < 3:
    new_book = input("Add a new book to the database: ").capitalize()

    add_book(new_book)

while is_running:

    is_running = borrow_book()

main_menu = {
    1: "Add a new book",
    2: "Show the available books",
    3: "Borrow a book",
    4: "Show activity users",
    5: "Exit"
}

while True:
    for key, value in main_menu.items():
        print(f"{key} - {value}")

    action = input("What do you want to do? Insert a number and press ENTER: ")

    if action.isdigit():
        action = int(action)

        show_main_menu(action)

        if action == 5:
            break

    elif action.isalpha or action == " ":
        print("Invalid value")
    else:
        print("Something went wrong")
