# Retrieve Operation

### Command:
```python
from bookshelf.models import Book

# Retrieve the book just created
book = Book.objects.all()

# Display all attributes
book.id, book.title, book.author, book.publication_year
