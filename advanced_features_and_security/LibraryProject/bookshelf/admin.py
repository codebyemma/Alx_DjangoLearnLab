from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Admin settings for CustomUser model."""

    model = CustomUser

    # Fields visible when editing a user
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Fields shown when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    list_display = ("username", "email", "date_of_birth", "is_staff")
    search_fields = ("username", "email")


admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Filters shown in the right sidebar
    list_filter = ('publication_year', 'author')
    
    # Search box for quick lookup
    search_fields = ('title', 'author')
