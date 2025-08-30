from bookshelf.models import book

test = book(title="1984", author="George Orwell", publication_year=1949)
test.save()
test.id

[comment]: <> (1)