from django.shortcuts import render

#Create Django Logout JWT APIView¶
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken


class APILogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})
    


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from adminpage.models import Adduser 
from .serializers import MyTokenObtainPairSerializer,MyTokenSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from adminpage.models import Adduser 
from rest_framework import serializers

class CustomTokenObtainPairView(TokenObtainPairView):              
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = request.data.get('username')
        adduser_profile = Adduser.objects.get(user__username=user)
        adduser=Adduser.objects.filter(phone_number=request.data["phone_number"]).first()
        if not adduser:
            raise serializers.ValidationError("wrong phone_number")
        response.data['phone_number'] = adduser_profile.phone_number
        response.data['address'] = adduser_profile.address
        user=adduser.user
        user = authenticate(username=user.username, password=request.data["password"])
        if not user:
            raise serializers.ValidationError("invalid username or password")
        return response
    
class CustomToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    # breakpoint()
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # breakpoint()
        # serializer = self.get_serializer(data=request.data)
        # # breakpoint()
        # if serializer.is_valid():
        #     # breakpoint()
        #     return response
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response
    
class CustomTokenB(TokenObtainPairView):
    serializer_class = MyTokenSerializer
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)