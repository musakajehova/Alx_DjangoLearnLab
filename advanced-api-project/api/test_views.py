from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Creates a user for the testing
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        self.author1 = Author.objects.create(name="William S. Vincent")
        self.author2 = Author.objects.create(name="Daniel Roy Greenfeld")
        
        # Creating instances of books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author=self.author1,
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Two Scoops of Django",
            author=self.author2,
            publication_year=2021
        )

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book2.id])

    ############################################################################
    """ Find all the tests """

    def test_list_books(self):
        """Ensure we can list all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Ensure we can get details of a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_requires_authentication(self):
        """Unauthenticated user should not be able to create a book"""
        data = {"title": "New Book", "author": "John Doe", "publication_year": 2025}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated user can create a book"""
        self.client.login(username='testuser', password='testpass123')
        data = {"title": "API Design", "author": self.author1.id, "publication_year": 2024}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        """Authenticated user can update a book"""
        self.client.login(username='testuser', password='testpass123')
        data = {"title": "Updated Django", "author": self.author1.id, "publication_year": 2023}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django")

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_search_books(self):
        """Ensure searching by title works"""
        response = self.client.get(self.list_url, {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # All results should contain 'Django' in the title
        for book in response.data:
            self.assertIn('Django', book['title'])

    def test_ordering_books(self):
        """Ensure ordering by publication_year works"""
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))