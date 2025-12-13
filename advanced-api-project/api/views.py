from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['publication_year', 'author', 'title']
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']



    def get_queryset(self):
        """
        Optionally filter books by publication year:
        /api/books/?year=2020
        """
        queryset = Book.objects.all()
        year = self.request.query_params.get('year')
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        if year:
            queryset = queryset.filter(publication_year=year)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__id=author)
        return queryset



class BookDetailView(generics.RetrieveAPIView):
    """
    Handles retrieval of a single Book instance by ID.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Handles creation of a new Book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Handles updating an existing Book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deletion of a Book instance.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
