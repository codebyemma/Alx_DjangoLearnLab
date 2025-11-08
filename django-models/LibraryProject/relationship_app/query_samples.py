from .models import Book, Library, Librarian, Author 


author = Author.objects.get(name=author_name)

# All books by this author
books_by_author = Book.objects.filter(author=author)

# OR using reverse relationship
books_by_author = author.book_set.all()


# Optional: print titles
for book in books_by_author:
    print(book.title)


# Get the library first
library = Library.objects.get(name=library_name)  # replace with library name or ID

# Get all books in that library
books_in_library = library.books.all()

# Optional: print titles
for book in books_in_library:
    print(book.title)


# Using OneToOneField reverse relation
library = Library.objects.get(name=library_name)

librarian = library.Librarian  # automatically available because of OneToOneField
print(librarian.name)
