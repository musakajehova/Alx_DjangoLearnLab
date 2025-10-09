from django.urls import path
from .views import RegisterView, LoginView, ProfileView


urlpatterns =[
    path('accounts/register/', RegisterView.as_view(), name='register_view'),
    path('accounts/login/', LoginView.as_view(), name='login_view'),
    path('accounts/profiles/<int:pk>/', ProfileView.as_view(), name='profile_view'),
] 