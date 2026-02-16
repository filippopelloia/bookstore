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


while len(available_books) < 3:
    new_book = input("Add a new book to the database: ").capitalize()

    if new_book == " " or len(new_book) < 3:
        print("Invalid value")
    else:
        print("Valid")
        available_books.append((new_book).strip())

        print("--------------------------------------")
        print("Available books: ")
        print("--------------------------------------")

        book_index = 1

        for book in available_books:
            print(f"{book_index} - {book}")
            book_index += 1


while True:
    rent_book = input("Digit the number of the book you want to borrow: ")

    if rent_book.isdigit():
        rent_book = int(rent_book)

        print(len(available_books))

        if 1 > rent_book or rent_book > len(available_books):
            print(f"Invalid value, choose a different number")

        elif 1 <= rent_book and rent_book <= len(available_books):
            chosed_book = available_books[rent_book - 1]
            print(f"You chosed: {chosed_book}")
            rent_books.append(chosed_book)
            del available_books[rent_book - 1]

            break
        else:
            print("Something went wrong")
    elif rent_book.isalpha() or rent_book == " ":
        print("Invalid value, insert a number")
    else:
        print("Something went wrong")
