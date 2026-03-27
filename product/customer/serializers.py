from rest_framework import serializers
from .models import User,Product,Order,Transection

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=User
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Product
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Order
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Transection