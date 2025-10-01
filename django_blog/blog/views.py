from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, ProfileForm, PostForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

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


# List all posts
def post_list(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blog/post_list.html", {"posts": posts})

# Show single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

# Create post
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # set logged-in user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

# Update post
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:  # only author can edit
        return redirect("post_detail", pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})

# Delete post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
    return redirect("post_list")
