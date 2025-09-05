from bookshelf.models import book

book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
test.save()

[comment]: <> (book: Title: Nineteen Eighty-Four Author: George Orwell Pub year: 1949)