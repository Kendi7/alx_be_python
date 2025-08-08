class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # ✅ Removed self from arguments
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # ✅ Removed self from arguments
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            # Base detail
            details = f"{type(book).__name__}: {book.title} by {book.author}"

            # Add conditional attributes
            if hasattr(book, "file_size"):
                details += f", File Size: {book.file_size}KB"
            if hasattr(book, "page_count"):
                details += f", Page Count: {book.page_count}"

            print(details)
