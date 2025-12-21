from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.serializer_class.Meta.model.objects.get(
            username=response.data['username']
        )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'user': response.data,
            'token': token.key
        })

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if not user:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
    

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        if target_user == request.user:
            return Response(
                {'error': 'You cannot follow yourself'},
                status=400
            )

        request.user.following.add(target_user)
        return Response({'message': f'You are now following {target_user.username}'})


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        request.user.following.remove(target_user)
        return Response({'message': f'You unfollowed {target_user.username}'})