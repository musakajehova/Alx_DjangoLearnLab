from django.shortcuts import render
from .models import Library
from .models import Book

# Create your views here.
from django.http import HttpResponse
from django.views.generic.detail import DetailView

def list_all_books(request):
    books_list = Book.objects.all()              #Fetchin all book instances
    context = {"book_list": books_list}
    return render(request, "relationship_app/list_books.html", context)


class BookDetailView(DetailView):
    """Displays all the books available"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "Library"