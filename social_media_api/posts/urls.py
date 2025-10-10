from .views import CommentView, PostView, FeedListView, LikePostView, UnlikePostView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'Comments', CommentView, basename='Comment')
router.register(r'Posts', PostView, basename='Post')

urlpatterns =[
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    ##############################################################
    path('feed/', FeedListView.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]