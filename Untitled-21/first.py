from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Optional, Dict

class Status(Enum):
    AVAILABLE = "available"
    NOT_AVAILABLE = "not available"

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: Status = Status.AVAILABLE
    due_time: Optional[datetime] = None

@dataclass
class Patron:
    name: str
    member_id: str
    borrowed_books: Optional[List[Book]] = None
    jarima: Optional[datetime] = None

@dataclass
class Library:
    books: Optional[List[Book]] = None
    patrons: Optional[List[Patron]] = None

    def add_book(self, book: Book):
        if self.books is not None:
            self.books.append(book)
        else:
            self.books = [book]
        print(f"{book.title} - Kutubxonaga Qo'shildi!")

    def add_patron(self, patron: Patron):
        if self.patrons is not None:
            self.patrons.append(patron)
        else:
            self.patrons = [patron]
        print(f"{patron.name} - Kutubxonaga Azo Bo'ldi!")

    def borrow_book(self, book: Book, patron: Patron, days=14):
        if book.status == Status.AVAILABLE:
            book.due_time = datetime.now() + timedelta(days=days)
            book.status = Status.NOT_AVAILABLE
            if patron.borrowed_books is not None:
                patron.borrowed_books.append(book)
            else:
                patron.borrowed_books = [book]
            print(f"{book.title} borrowed by {patron.name} for {days} days\n"
                  f"It gives book at {book.due_time}")
        else:
            print(f"Book is not available! It will be available at {book.due_time}")

    def return_book(self, book: Book, patron: Patron):
        if book in patron.borrowed_books:
            if book.due_time > datetime.now():
                print(f"Oh Great!")
            else:
                print(f"Kech Qolganing Uchun 2 kun Kitob Ololmaysan!")
                patron.jarima = datetime.now() + timedelta(days=2)
            book.status = Status.AVAILABLE
            book.due_time = None
            patron.borrowed_books.remove(book)
        else:
            print(f"Siz Bunday Kitob Olmagansiz!")

    def search_books(self, query: str):
        filtered_books = [
            book for book in self.books
            if query.lower() in book.title.lower() or
               query.lower() in book.author.lower() or
               query.lower() in book.isbn.lower()
        ]
        for book in filtered_books:
            print(f"Found: {book.title} by {book.author} (ISBN: {book.isbn})")

    def display_borrowed_books(self, patron: Patron):
        for book in patron.borrowed_books:
            print(f"{book.title}/{book.author}/{book.isbn} borrowed for {book.due_time}\n"
                  f"{(book.due_time - datetime.now()).days} days remaining")


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
