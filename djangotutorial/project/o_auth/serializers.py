from rest_framework import serializers
from .models import data
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fileds="__all__"
        Model=data