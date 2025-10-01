from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, ProfileForm, PostForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

def home(request):
    return render(request, "blog/base.html")

# Registration view (function based)
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          # saves and hashes password
            login(request, user)       # log user in immediately after register
            messages.success(request, "Registration successful.")
            return redirect('home')    # or 'profile' or 'posts'
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})


# Use Django's LoginView and LogoutView (simple subclassing optional)
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'blog/logged_out.html'


# Profile view — user must be logged in
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})

def post_list(request):
    return render(request, "blog/post_list.html")


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    #ordering = ['-created_at']  # newest first


# 2. View details of a post (public)
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


# 3. Create a new post (only for logged-in users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']   # we don’t include author, we set it in form_valid
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # assign logged in user as author
        return super().form_valid(form)


# 4. Update a post (only the author can edit)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# 5. Delete a post (only the author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post-list')  # redirect after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author