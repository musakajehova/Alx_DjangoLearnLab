from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, ProfileForm, PostForm, CommentForm
from .models import Post, Comment, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q

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


# 1. List posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ['-id']  # newest first


# 2. Detail view
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # all comments for this post (ordered by created_at due to Meta)
        context['comments'] = self.object.comments.all()
        # a fresh form to render on the detail page
        context['comment_form'] = CommentForm()
        return context

# 3. Create view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
    # set author and save post first
        form.instance.author = self.request.user
        response = super().form_valid(form)  # saves self.object
        # handle tags_input
        tags_input = form.cleaned_data.get('tags_input', '')
        if tags_input:
            tag_names = [t.strip() for t in tags_input.split(',') if t.strip()]
            tags = []
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                tags.append(tag_obj)
            self.object.tags.set(tags)
        return response

# 4. Update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def get_initial(self):
        initial = super().get_initial()
        # set the tags_input initial value from existing tags
        tags_qs = self.get_object().tags.all()
        initial['tags_input'] = ', '.join([t.name for t in tags_qs])
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)  # saves self.object
        tags_input = form.cleaned_data.get('tags_input', '')
        if tags_input:
            tag_names = [t.strip() for t in tags_input.split(',') if t.strip()]
            tags = []
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                tags.append(tag_obj)
            self.object.tags.set(tags)
        else:
            self.object.tags.clear()
        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# 5. Delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    # Create comment (nested URL with post_pk)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def dispatch(self, request, *args, **kwargs):
        # load the post we are commenting on
        self.post = get_object_or_404(Post, pk=kwargs.get('post_pk'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post
        form.save()
        # After saving, redirect to the post detail page
        return redirect('post_detail', pk=self.post.pk)


####################################################################################

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
####################################################################################

# posts by tag
class PostsByTagListView(ListView):
    model = Post
    template_name = "blog/posts_by_tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        return Post.objects.filter(tags__name__iexact=tag_name).distinct().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_name')
        return context

# search
def search_posts(request):
    q = request.GET.get('q', '').strip()
    posts = Post.objects.none()
    if q:
        posts = Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(tags__name__icontains=q)
        ).distinct().order_by('-created_at')
    return render(request, "blog/search_results.html", {"posts": posts, "query": q})
