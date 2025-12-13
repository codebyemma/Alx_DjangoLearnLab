from rest_framework import serializer
from .models import Book, Author
from django.utils.timezone import now


class BookSerializer(serializer.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

    def validate(self, data):
        if data["publication_year"] > now().year:
            raise serializer.ValidationError("Invalid publication year")
        return data
    
class AuthorSerializer(serializer.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["name", "books"]