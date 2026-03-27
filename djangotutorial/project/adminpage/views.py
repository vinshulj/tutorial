from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer,AddRegisterSerializer
from django.contrib.auth.models import User 
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Adduser

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'id': user.id, 'username': user.username, 'email': user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"token": serializer.validated_data["token"]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddRegisterView(generics.CreateAPIView):
    serializer_class = AddRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            adduser_profile = Adduser.objects.get(user=user)
            user_data =AddRegisterSerializer(user).data  
            user_data['phone_number'] = adduser_profile.phone_number
            user_data['address'] = adduser_profile.address
            user_data.pop('user_profile', None)
            return Response(user_data, status=status.HTTP_201_CREATED)
            # user = serializer.save()
            # user_profile = user.adduser #run this istead
            # return Response({'id': user.id, 'username': user.username, 'email': user.email,"address":user_profile.address,"phone_no":user_profile.phone_number}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        user=request.data.get('username')
        if serializer.is_valid():
            return Response({"token": serializer.validated_data["token"]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


