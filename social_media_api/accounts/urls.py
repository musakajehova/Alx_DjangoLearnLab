from django.urls import path
from .views import RegisterView, LoginView, ProfileView


urlpatterns =[
    path('register/', RegisterView.as_view(), name='register_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('profiles/<int:pk>/', ProfileView.as_view(), name='profile_view'),
] 