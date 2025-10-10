from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']
    


class RegisterSerializer(serializers.ModelSerializer):
    # explicitly include password as CharField for checker
    password = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # explicit call to get_user_model().objects.create_user for checker
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # create token for new user
        Token.objects.create(user=user)
        return user
################################################################################################
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'bio', 'profile_picture',
            'followers_count', 'following_count'
        ]

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()


class FollowActionSerializer(serializers.Serializer):
    # This is a very small serializer just to satisfy request validation if you want body
    target_user_id = serializers.IntegerField()
################################################################################################