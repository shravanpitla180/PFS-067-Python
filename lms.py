# lms--> Library management system 
 
# Abstraction method 
from abc import ABC, abstractmethod 
 
class Libraryitem(ABC): 
    @abstractmethod 
    def display(self): 
        pass 
 
    @abstractmethod 
    def get_type(self): 
        pass 
 

# Basic Class Book 
class Book(Libraryitem): 
    total_books = 0 
 
    def __init__(self, book_id, title, author): 
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.__is_available = True 
        Book.total_books += 1 
 
# Encapsulation use is about we don't want anyone to modify important information 
    def issue_book(self): 
        if self.__is_available: 
            self.__is_available = False 
            print("Book issued successfully") 
        else: 
            print("Book already issued") 
 
    def return_book(self): 
        self.__is_available = True 
        print("Book returned successfully") 
     
    def is_available(self): 
        return self.__is_available 
 
    def display(self): 
        print("Book ID: ", self.book_id) 
        print("Title: ", self.title) 
        print("Author: ", self.author) 
        print("Available: ", self.is_available()) 
 
    def get_type(self): 
        return "Book" 
 
# Operator overloading 
    def __eq__(self, other): 
        if isinstance(other, Book): 
            return self.book_id == other.book_id 
        return False 
 
    def __str__(self): 
        return f"{self.title} by {self.author}" 
 

# EBook 
class Ebook(Book): 
    def __init__(self, book_id, title, author, file_size): 
        super().__init__(book_id, title, author) 
        self.file_size = file_size 
 
# Method Overriding 
    def issue_book(self): 
        if self.is_available(): 
            self._Book__is_available = False 
            print(f"'{self.title}' ebook access granted.") 
        else: 
            print("EBook already issued.") 
 
    def get_type(self): 
        return "EBook" 
 
    def display(self): 
        print( 
            f"ID: {self.book_id} | " 
            f"Title: {self.title} | " 
            f"Author: {self.author} | " 
            f"File Size: {self.file_size}" 
        ) 
# Printed Book 
class PrintedBook(Book): 
    def __init__(self, book_id, title, author, pages): 
        super().__init__(book_id, title, author) 
        self.pages = pages 
    def issue_book(self): 
        if self.is_available(): 
            super().issue_book() 
            print(f"Printed book '{self.title}' issued physically.") 
        else: 
            print("Book already issued.")  
    def get_type(self): 
        return "PrintedBook" 
    def display(self): 
        super().display() 
        print("Pages: ", self.pages) 
 

# Member class 
class member: 
    def __init__(self, member_id, name): 
        self.member_id = member_id 
        self.name = name 
        self.borrowed_books = [] 
    def borrow_book(self, book): 
        if book.is_available(): 
            book.issue_book() 
            self.borrowed_books.append(book) 
            print(f"{self.name} borrowed {book.title}") 
        else: 
            print(f"{book.title} is not available.") 
    def return_book(self, book): 
        if book in self.borrowed_books: 
            book.return_book() 
            self.borrowed_books.remove(book) 
            print(f"{self.name} returned {book.title}") 
        else: 
            print("Book was not borrowed by this member.") 
 
    def display_member(self): 
        print("\nMember ID: ", self.member_id) 
        print("Name: ", self.name) 
        print("Borrowed Books: ") 
        if not self.borrowed_books: 
            print("No books borrowed.") 
        else: 
            for book in self.borrowed_books: 
                print("-", book) 
 

# Student member 
class StudentMember(member): 
    def __init__(self, member_id, name, college): 
        super().__init__(member_id, name) 
        self.college = college 
    def display_member(self): 
        super().display_member() 
        print("College: ", self.college) 
 

# Faculty member 
class FacultyMember(member): 
    def __init__(self, member_id, name, department): 
        super().__init__(member_id, name) 
        self.department = department 
    def display_member(self): 
        super().display_member() 
        print("Department: ", self.department) 
 

class Library: 
    def __init__(self, name): 
        self.name = name 
        self.books = [] 
        self.members = [] 
 
# Add book 
    def add_book(self, book): 
        self.books.append(book) 
        print(f"Book {book.title} added successfully.") 
 
# Remove book 
    def remove_book(self, book_id): 
        for book in self.books: 
            if book.book_id == book_id: 
                self.books.remove(book) 
                print("Book removed successfully") 
                return 
        print("Book not found") 
 
# Register member 
    def register_member(self, member): 
        self.members.append(member) 
        print(f"Member {member.name} added successfully.") 
 
# Search book 
    def search_book(self, title=None, author=None): 
        found = False 
        for book in self.books: 
            if title and title.lower() in book.title.lower(): 
                book.display() 
                found = True 
            elif author and author.lower() in book.author.lower(): 
                book.display() 
                found = True 
        if not found: 
            print("No book found.") 
 
# Display books 
    def display_books(self): 
        print("\nLibrary Books:")  
        if not self.books: 
            print("No books available") 
            return  
        for book in self.books: 
            book.display() 
 
# Display Members 
    def display_members(self): 
        print("\n------ Members ------") 
 
        for member in self.members: 
            member.display_member() 
 
# Find member 
    def find_member(self, member_id): 
        for member in self.members: 
            if member.member_id == member_id: 
                return member 
        return None 
 
# Find book 
    def find_book(self, book_id): 
        for book in self.books: 
            if book.book_id == book_id: 
                return book 
        return None 
 
library = Library("ABC Central Library") 
book1 = Book(101, "Python", "Guido") 
book2 = Book(102, "Java", "van") 
book3 = Book(103, "ML", "Andrew") 
library.add_book(book1) 
library.add_book(book2) 
library.add_book(book3) 
student = StudentMember(1, "Shravan", "MLRITM college") 
faculty = FacultyMember(2, "Dr.Arun", "CSI")  
library.register_member(student) 
library.register_member(faculty)  
library.display_books() 
student.borrow_book(book1) 
student.display_member() 
student.return_book(book1) 
library.search_book(title="Python") 
library.search_book(author="van") 
library.search_book(author="ML")

