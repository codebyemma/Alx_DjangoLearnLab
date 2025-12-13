from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    """

    def setUp(self):
        """
        Set up test data and users.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

        self.author = Author.objects.create(name='Chinua Achebe')

        self.book = Book.objects.create(
            title='Things Fall Apart',
            publication_year=1958,
            author=self.author
        )

        self.book_list_url = reverse('book-list')

    def test_list_books_unauthenticated(self):
        """
        Ensure unauthenticated users can list books.
        """
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book_detail(self):
        """
        Ensure a single book can be retrieved.
        """
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Things Fall Apart')

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a book.
        """
        self.client.login(username='testuser', password='password123')

        data = {
            'title': 'No Longer at Ease',
            'publication_year': 1960,
            'author': self.author.id
        }

        response = self.client.post(
            reverse('book-create'),
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create books.
        """
        data = {
            'title': 'Arrow of God',
            'publication_year': 1964,
            'author': self.author.id
        }

        response = self.client.post(
            reverse('book-create'),
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.login(username='testuser', password='password123')

        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Things Fall Apart (Updated)'}

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Things Fall Apart (Updated)')

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.login(username='testuser', password='password123')

        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

