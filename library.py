import os

class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        os.system('clear' if os.name == 'posix' else 'cls')  
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books available.")
            return
        print("List of Books:")
        for book in books:
            book_info = book.strip().split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Date: {book_info[2]}, Pages: {book_info[3]}")

    def add_book(self):
        os.system('clear' if os.name == 'posix' else 'cls')  
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self, title):
        os.system('clear' if os.name == 'posix' else 'cls')  
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        removed = False
        for book in books:
            if title.lower() not in book.lower():
                new_books.append(book)
            else:
                removed = True
        if removed:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(new_books)
            print("Book removed successfully.")
        else:
            print("Book not found.")

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        title = input("Enter the title of the book to remove: ")
        lib.remove_book(title)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
