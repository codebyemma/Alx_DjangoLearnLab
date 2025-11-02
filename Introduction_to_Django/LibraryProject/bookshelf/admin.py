from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Filters shown in the right sidebar
    list_filter = ('publication_year', 'author')
    
    # Search box for quick lookup
    search_fields = ('title', 'author')
