from django.urls import path
from .views import home, register, profile, post_list, CustomLoginView, CustomLogoutView, post_list, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", home, name="home"),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("posts/", post_list, name="posts"),
    ########################################################################
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    ########################################################################
]
