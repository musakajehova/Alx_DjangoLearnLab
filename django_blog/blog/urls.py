from django.urls import path
from .views import (home, register, profile, post_list, CustomLoginView, 
                    CustomLogoutView, post_list, PostListView, PostDetailView,
                    PostCreateView, PostUpdateView, PostDeleteView,
                     CommentCreateView, CommentUpdateView, CommentDeleteView)
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
    path("posts/<int:post_pk>/comments/new/", CommentCreateView.as_view(), name="comment_create"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
