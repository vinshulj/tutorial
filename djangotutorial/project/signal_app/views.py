from django.shortcuts import render

from rest_framework.response import Response
from .models import UserAddressList
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserLoginSerializer,UserAddressListSerializer
# Create your views here.
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            address_list = UserAddressList.objects.filter(user__username=request.data["username"])
            if not address_list:
                empty_address = UserAddressList(user=User.objects.get(username=request.data["username"]))
                empty_address.save()
                address_list = UserAddressList.objects.filter(user__username=request.data["username"])
            return Response({"message": "Login successful", "address_list": address_list.values()}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            address_instance = UserAddressList.objects.get(user__username=request.data.get('username'))
            serializer=UserAddressListSerializer(address_instance, data=request.data)    
            if serializer.is_valid():    
                serializer.save()                           
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            address_instance = UserAddressList.objects.get(user__username=request.data.get('username'))
            serializer = UserAddressListSerializer(
                address_instance, 
                data=request.data, 
                partial=True
            )
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from django.contrib.auth.models import User
from adminpage.serializers import RegisterSerializer


class Register(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            address_list = UserAddressList.objects.filter(user__username=request.data["username"])
            return Response({"user": serializer.data, "address_list": address_list.values()}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        try:
            address_instance = UserAddressList.objects.get(user__username=request.data.get('username'))
            serializer=UserAddressListSerializer(address_instance, data=request.data)    
            if serializer.is_valid():    
                serializer.save()                           
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserAddressList.DoesNotExist:
            return Response({"error": "Create account first"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, *args, **kwargs):
        try:
            address_instance = UserAddressList.objects.get(user__username=request.data.get('username'))
            serializer = UserAddressListSerializer(
                address_instance, 
                data=request.data, 
                partial=True
            )
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserAddressList.DoesNotExist:
            return Response({"error": "Create account first"}, status=status.HTTP_404_NOT_FOUND)
        