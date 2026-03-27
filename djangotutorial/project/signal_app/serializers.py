from rest_framework import serializers
from .models import UserAddressList
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password']
    def validate(self, dic):
        user = authenticate(username=dic["username"], password=dic["password"])
        if not user:
            raise serializers.ValidationError("invalid username or password")
        return dic
        
        
class UserAddressListSerializer(serializers.ModelSerializer):
    pin_code = serializers.IntegerField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    class Meta:
        model = UserAddressList
        fields = ['pin_code','city','state','country']
    
    def update(self, instance, validated_data):
        instance.city = validated_data.get('city', instance.city)
        instance.pin_code = validated_data.get('pin_code', instance.pin_code)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        
        instance.save() 
        return super().update(instance, validated_data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def validate(self, dic):
    #     if len(str(dic['pin_code'])) != 6:
    #         raise serializers.ValidationError("Pin code must be a 6-digit number.")
        # if not dic['city'].isalpha() :
        #     raise serializers.ValidationError("City name must contain only letters.")
    #     if not dic['state'].isalpha():
    #         raise serializers.ValidationError("State name must contain only letters.")
    #     if not dic['country'].isalpha():
    #         raise serializers.ValidationError("Country name must contain only letters.")
    #     return dic  