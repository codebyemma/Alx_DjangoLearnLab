from django.contrib import admin
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

# Register your models here.
