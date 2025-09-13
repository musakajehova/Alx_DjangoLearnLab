from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from .models import Book, CustomUser
from django.http import HttpRequest


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def can_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        if title and author and publication_year:
            Book.objects.create(
                title=title,
                author=author,
                publication_year=publication_year
            )
            return redirect('book_list')

    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def can_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
            book.title = request.POST.get('title')
            book.author = request.POST.get('author')
            book.publication_year = request.POST.get('publication_year')
            book.save()
            return redirect('book_list')

    return render(request, 'bookshelf/edit_book', {'book': book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def can_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})