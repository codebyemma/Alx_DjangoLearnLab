from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book data and validates publication year.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author data with nested books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
