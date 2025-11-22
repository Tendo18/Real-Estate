from django.shortcuts import render
from .models import User
from rest_framework import generics, status
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError

#Views for registration 
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User registered successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)
    
#Views for login and token generation
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        required_fields = {'email', 'password'}
        if not required_fields.issubset(request.data):
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({
            "access": serializer.validated_data['access'],
            "refresh": serializer.validated_data['refresh'],
            "message": "Login successful"
        }, status=status.HTTP_200_OK)

#Views for user profile
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Profile updated successfully", "user": serializer.data}, status=status.HTTP_200_OK)