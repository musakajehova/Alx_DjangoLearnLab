from .views import CommentView, PostView, FeedListView
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
]