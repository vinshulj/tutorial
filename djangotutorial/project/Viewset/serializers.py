from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','dept','exp']

class PasswordSerializer(serializers.Serializer):
    password=serializers.CharField(write_only=True)
   
    def validate(self, attrs):
        if len(attrs['password']) < 8:
            password = attrs.get('password')
            return serializers.ValidationError("password is short")
        return super().validate(attrs)
    
    
class UserSerializer(serializers.ModelSerializer):
    # You can customize the fields to be serialized based on your needs
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined']

