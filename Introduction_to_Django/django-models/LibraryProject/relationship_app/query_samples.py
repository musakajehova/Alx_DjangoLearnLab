from relationship_app.models import Author, Book, Library, Librarian

Book.objects.get(author="1958")

Library.objects.all()

Librarian.objects.get(library="test")