from django.urls import path
from .views import (home, register, profile, post_list, CustomLoginView, 
                    CustomLogoutView, post_list, PostListView, PostDetailView,
                    PostCreateView, PostUpdateView, PostDeleteView,
                    CommentCreateView, CommentUpdateView, CommentDeleteView, posts_by_tag,
                    search_posts)

urlpatterns = [
    path("", home, name="home"),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("posts/", post_list, name="posts"),
    ########################################################################
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    ########################################################################
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment_create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    ########################################################################
    path("tag/<slug:tag_slug>/", posts_by_tag, name="posts_by_tag"),
    path("search/", search_posts, name="search_posts"),
]
