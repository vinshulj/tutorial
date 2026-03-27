import base64
from email.mime import text
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from adminpage.models import Adduser 
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import jwt

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    password=serializers.CharField(write_only=True)
    phone_number=serializers.CharField(required=True)
    address=serializers.CharField(read_only=True)
    class Meta:
        fields = ['password','phone_number','address']
    def validate(self, attrs):
        data = super().validate(attrs)
        # user = self.user
        adduser_profile=Adduser.objects.select_related('user').filter(phone_number=attrs["phone_number"]).first()
        # adduser_profile=Adduser.objects.filter(user=adduser_profile.user).first()
        
        # breakpoint()
        if not adduser_profile:
            raise serializers.ValidationError("wrong phone_number")
        
        data['phone_number'] = adduser_profile.phone_number        
        data['address'] = adduser_profile.address
        # data['password'] = user.password
        # breakpoint()
        user = adduser_profile.user
        if not user.check_password(attrs["password"]):
            raise serializers.ValidationError("invalid password")

        data['username']=user.username
        # breakpoint()
        return data
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #     token['username'] = user.username
    #     adduser_profile = Adduser.objects.get(user=user)
    #     token['phone_number'] = adduser_profile.phone_number
    #     token['address'] = adduser_profile.address
    #     return token
    
    

class MyTokenSerializer(TokenObtainPairSerializer):
    password=serializers.CharField(write_only=True)
    phone_number=serializers.CharField(required=True)
    address=serializers.CharField(read_only=True)
    class Meta:
        fields = ['password','phone_number','address']
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        adduser_profile=Adduser.objects.filter(phone_number=attrs["phone_number"]).first()
        if not adduser_profile:
            raise serializers.ValidationError("wrong phone_number")
        # data['password'] = user.password
        user=adduser_profile.user
        user = authenticate(username=user.username, password=attrs["password"])
        if not user:
            raise serializers.ValidationError("invalid password")
        header, payload, signature = data["refresh"].split('.')
        payload += '=' * (-len(payload) % 4)
        decoded_bytes = base64.urlsafe_b64decode(payload)
        decoded_string = decoded_bytes.decode('utf-8')
        data["about_data"]=decoded_string
        return data    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        adduser_profile = Adduser.objects.get(user=user)
        token['phone_number'] = adduser_profile.phone_number
        token['address'] = adduser_profile.address
        return token