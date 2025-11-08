# Delete Operation

### Command:
```python
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.all()
book.delete()

# Verify deletion
Book.objects.all()
