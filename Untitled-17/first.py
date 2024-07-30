#
#
# class Book:
#     def __init__(self, title: str, author: str, isbn: str):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#
#
# class Patron:
#     def __init__(self, name: str, member_id: str):
#         self.name = name
#         self.member_id = member_id
#
#
# class Library:
#     def __init__(self):
#         books = []
#         member = []
from collections import defaultdict
from datetime import datetime, timedelta


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        # keep track of availablity and due time of book
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.due_time = None


class Patron:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.jarima = None
        # store borrowed books


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        # books and patrons
        ...

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"{book.title} - Kutubxonaga Qo'shildi!")
        # add book
        ...

    def add_patron(self, patron: Patron):
        self.patrons.append(patron)
        print(f"{patron.name} - Kutubxonaga Azo Bo'ldi!")
        # add patron
        ...

    def borrow_book(self, book: Book, patron: Patron, days=14):
        if book.is_available:
            book.due_time = datetime.now() + timedelta(days=days)
            book.is_available = False
            patron.borrowed_books.append(book)
            print(f"{book.title} borrowed {patron.name} for {days} days\n"
                  f"It gives book at {book.due_time}")
        elif book.due_time > datetime.now():
            print(f"Book will available at {book.due_time}")
        else:
            print(f"Book is not available!")
        # check is_available
        # set due_time
        # borrowed books append
        # give info
        ...

    def return_book(self, book: Book, patron: Patron):
        if book in patron.borrowed_books:
            if book.due_time > datetime.now():
                print(f"Oh Great!")
                book.is_available = True
                book.due_time = None
                patron.borrowed_books.remove(book)

            else:
                print(f"Kech Qolganing Uchun 2 kun Kitob Ololmaysan!")
                book.is_available = True
                book.due_time = None
                patron.jarima += datetime.now() + timedelta(days=2)
                patron.borrowed_books.remove(book)
        else:
            print(f"Siz Bunday Kitob Olmagansiz!")
        # check if book is borrowed
        # remove from borrowed
        ...

    def search_books(self, query):
        filtered_books = [
            book for book in self.books
            if query.lower() in book.title.lower() or
               query.lower() in book.author.lower() or
               query.lower() in book.isbn.lower()
        ]
        # search by title, author, isbn
        ...

    def display_borrowed_books(self, patron: Patron):
        for book in patron.borrowed_books:
            print(f"{book.title}/{book.author}/{book.isbn} borrowed for {book.due_time}\n"
                  f"{book.due_time - datetime.now()} - Qoldi")
        # display borrowed books
        ...


library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")
patron1 = Patron("Alice", "P001")

library.add_book(book1)
library.add_book(book2)
library.add_patron(patron1)

library.borrow_book(book1, patron1, 14)
library.borrow_book(book2, patron1, 15)
library.display_borrowed_books(patron1)

library.return_book(book2, patron1)
library.display_borrowed_books(patron1)
