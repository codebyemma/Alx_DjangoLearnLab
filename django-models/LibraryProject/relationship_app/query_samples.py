from .models import Book, Library, Librarian, Author 


author = Author.objects.get(name="J.K. Rowling")

# All books by this author
books_by_author = Book.objects.filter(author=author)

# OR using reverse relationship
books_by_author = author.book_set.all()


# Optional: print titles
for book in books_by_author:
    print(book.title)


# Get the library first
library = Library.objects.get(name="Central Library")  # replace with library name or ID

# Get all books in that library
books_in_library = library.books.all()

# Optional: print titles
for book in books_in_library:
    print(book.title)


# Using OneToOneField reverse relation
library = Library.objects.get(name="Central Library")

librarian = library.Librarian  # automatically available because of OneToOneField
print(librarian.name)
