from relationship_app.models import Author, Book, Library, Librarian


Book.objects.get(author="book_name")

Library.objects.all()

Library.objects.get(name="library_name")

Librarian.objects.get(library="test")