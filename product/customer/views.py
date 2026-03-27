from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer,OrderSerializer,ProductSerializer,TransactionSerializer
from .models import User,Order,Product,Transection

class UserView(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()                                                                     