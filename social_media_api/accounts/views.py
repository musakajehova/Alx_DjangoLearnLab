from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer, UserSerializer, FollowActionSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework. authentication import TokenAuthentication
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
#############################################################################################################
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
############################################################################################################
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)
    
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
#############################################################################################

class ProfileView(generics.RetrieveAPIView):
    """
    Retrieve any user's public profile (or your own).
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'username'


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        # add to following relationship
        request.user.following.add(target)
        #####################################################################################################
        Notification.objects.create(
            recipient=target,
            actor=request.user,
            verb='started following you',
            target_content_type=None, 
            target_object_id=None,
        )
        ###################################################################################################
        return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)
        



class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target)
        return Response({"detail": f"You unfollowed {target.username}."}, status=status.HTTP_200_OK)
    
###################################################################################################################