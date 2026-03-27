
from django.contrib.auth.models import User
from .models import Adduser
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password']
    
    def validate(self, dic):
        user = authenticate(username=dic['username'], password=dic['password'])
        if not user:
            raise serializers.ValidationError("invalid username or password")
        token, created = Token.objects.get_or_create(user=user)
        dic["token"]=token.key
        return dic

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adduser
        fields = ['phone_number', 'address']

class AddRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    user_profile = UserProfileSerializer(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2','user_profile']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        if len(str(data['user_profile']['phone_number'])) != 10:
            raise serializers.ValidationError("Invalid phone number.")
        return data
    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        user_profile_data = validated_data.pop('user_profile')
        # user_profile_data = validated_data['user_profile']
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        Adduser.objects.create(
            user=user,
            phone_number=user_profile_data['phone_number'],
            address=user_profile_data['address']
        )
        # breakpoint()
        return user

from .models import Adduser

class LoginSerializer(serializers.Serializer):
    phone_number=serializers.CharField()
    password=serializers.CharField()
    class Meta:
        model = User
        fields = ["phone_number"]
    
    def validate(self, dic):
        adduser=Adduser.objects.filter(phone_number=dic["phone_number"]).first()
        if not adduser:
            raise serializers.ValidationError("wrong phone_number")
        user=adduser.user
        user = authenticate(username=user.username, password=dic["password"])
        if not user:
            raise serializers.ValidationError("invalid username or password")
        token, created = Token.objects.get_or_create(user=user)
        dic["token"]=token.key
        return dic