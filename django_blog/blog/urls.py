from django.urls import path
from .views import register, profile, CustomLoginView, CustomLogoutView, post_list

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("posts/", post_list, name="posts"),
]
