from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class AbstractUser(ABC):
    @abstractmethod
    def borrow_book(self, book):
        pass
    
    @abstractmethod
    def return_book(self, book):
        pass

class AbstractBook(ABC):
    @abstractmethod
    def get_title(self):
        pass
    
    @abstractmethod
    def get_author(self):
        pass
    
    @abstractmethod
    def get_isbn(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass
    
    @abstractmethod
    def set_status(self, status):
        pass

class AbstractLibrary(ABC):
    @abstractmethod
    def add_book(self, book):
        pass
    
    @abstractmethod
    def remove_book(self, book):
        pass
    
    @abstractmethod
    def find_book(self, query):
        pass

class Book(AbstractBook):
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.due_time = None

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_isbn(self):
        return self.isbn
    
    def get_status(self):
        return self.is_available
    
    def set_status(self, status):
        self.is_available = status

class Patron(AbstractUser):
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.jarima = None
    
    def borrow_book(self, book: Book, days=14):
        if book.get_status():
            book.due_time = datetime.now() + timedelta(days=days)
            book.set_status(False)
            self.borrowed_books.append(book)
            print(f"{book.get_title()} borrowed by {self.name} for {days} days\n"
                  f"It gives book at {book.due_time}")
        elif book.due_time > datetime.now():
            print(f"Book will be available at {book.due_time}")
        else:
            print(f"Book is not available!")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            if book.due_time > datetime.now():
                print(f"Oh Great!")
                book.set_status(True)
                book.due_time = None
                self.borrowed_books.remove(book)
            else:
                print(f"Kech Qolganing Uchun 2 kun Kitob Ololmaysan!")
                book.set_status(True)
                book.due_time = None
                self.jarima = datetime.now() + timedelta(days=2)
                self.borrowed_books.remove(book)
        else:
            print(f"Siz Bunday Kitob Olmagansiz!")

class Library(AbstractLibrary):
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"{book.get_title()} - Kutubxonaga Qo'shildi!")
    
    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book.get_title()} - Kutubxonadan O'chirildi!")
        else:
            print(f"{book.get_title()} - Kitob Topilmadi!")
    
    def find_book(self, query):
        filtered_books = [
            book for book in self.books
            if query.lower() in book.get_title().lower() or
               query.lower() in book.get_author().lower() or
               query.lower() in book.get_isbn().lower()
        ]
        for book in filtered_books:
            a = 'Available' if book.get_status() else 'Not Available'
            print(f"{book.get_title()} / {book.get_author()} / {book.get_isbn()} - {a}")
    
    def add_patron(self, patron: Patron):
        self.patrons.append(patron)
        print(f"{patron.name} - Kutubxonaga Azo Bo'ldi!")
    
    def display_borrowed_books(self, patron: Patron):
        for book in patron.borrowed_books:
            print(f"{book.get_title()}/{book.get_author()}/{book.get_isbn()} borrowed until {book.due_time}\n"
                  f"{(book.due_time - datetime.now()).days} days remaining")


library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")
patron1 = Patron("Alice", "P001")

library.add_book(book1)
library.add_book(book2)
library.add_patron(patron1)

patron1.borrow_book(book1, 14)
patron1.borrow_book(book2, 15)
library.display_borrowed_books(patron1)

patron1.return_book(book2)
library.display_borrowed_books(patron1)
