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
    likes_count = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'likes_count', 'has_liked']
        read_only_fiels = ['created_at'] 

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_has_liked(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return obj.likes.filter(user=user).exists()


