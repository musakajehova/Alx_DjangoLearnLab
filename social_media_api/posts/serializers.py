from rest_framework import serializers
from .models import Post, Comment
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fiels = ['created_at'] 



