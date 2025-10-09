from .views import CommentView, PostView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Comments', CommentView, basename='Comment')
router.register(r'Posts', PostView, basename='Post')

urlpatterns =[
    path('', include(router.urls)),
]