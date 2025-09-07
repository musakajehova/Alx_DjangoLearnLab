from django.shortcuts import render
from .models import Library
from .models import Book

# Create your views here.
from django.http import HttpResponse
from django.views.generic.detail import DetailView

##########################################################################
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
#########################################################################

def list_books(request):
    books = Book.objects.all()              #Fetchin all book instances
    context = {"book_list": books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    """Displays all the books available"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "Library"



#######################################################################
# Register view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
#            return redirect("home")  
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

######################################################################