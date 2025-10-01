from django.urls import path
from .views import register, profile, CustomLoginView, CustomLogoutView, post_list, post_list, post_detail, post_create, post_update, post_delete

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("posts/", post_list, name="posts"),
    ########################################################################
    path("posts/", post_list, name="post_list"),
    path("posts/<int:pk>/", post_detail, name="post_detail"),
    path("posts/new/", post_create, name="post_create"),
    path("posts/<int:pk>/edit/", post_update, name="post_update"),
    path("posts/<int:pk>/delete/", post_delete, name="post_delete"),
    ########################################################################
]
