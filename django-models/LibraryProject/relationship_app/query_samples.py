from relationship_app.models import Author, Book, Library, Librarian


Book.objects.get(author="book_name")

Library.objects.all()

Library.objects.get(name=library_name)
books.all()

Author.objects.get(name=author_name)
objects.filter(author=author)

Librarian.objects.get(library=library_name)