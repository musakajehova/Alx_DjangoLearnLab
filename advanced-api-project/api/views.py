from django.shortcuts import render

# Create your views here.
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics, filters
from .models import Book, Author
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated , IsAdminUser

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author', 'publication_year']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a specific user,
        by filtering based on the `username` query parameter in the URL.
        """
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        publication_year = self.request.query_params.get('publication_year')

        if title is not None:
            queryset = queryset.filter(title=title)
        if author is not None:
            queryset = queryset.filter(author=author)
        if publication_year is not None:
            queryset = queryset.filter(publication_year = publication_year)
        
        return queryset

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
