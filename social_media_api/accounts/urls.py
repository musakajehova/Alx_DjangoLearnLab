from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView


urlpatterns =[
    path('register/', RegisterView.as_view(), name='register_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('profiles/<int:pk>/', ProfileView.as_view(), name='profile_view'),
    ########################################################################
    path('profile/<str:username>/', ProfileView.as_view(), name='profile-by-username'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    ########################################################################
] 