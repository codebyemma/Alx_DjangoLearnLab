# Update Operation

### Command:
```python
from bookshelf.models import Book

# Retrieve and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book.title
