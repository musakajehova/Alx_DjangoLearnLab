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
# 🔹 Register view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect("home")  # 👈 you can change this redirect target
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# 🔹 Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # 👈 redirect after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# 🔹 Logout view
@login_required
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


######################################################################