from rest_framework import serializers
from django.core.mail import send_mail

class Comment:
    def __init__(self, email, message, created=None):
        self.email = email
        self.messange = message

comment = Comment(email='leila@example.com', message='foo bar')


# Individual fields on a serializer can include validators, by declaring them on the field instance, for example:

def message_limit(value):
    if len(value)<10:
        raise serializers.ValidationError('invalid message')
    elif len(value)>100:
        raise serializers.ValidationError("explain in short")

class ContactForm(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField(validators=[message_limit])
    
    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('message', instance.message)
        return instance


    def save(self):
        email = self.validated_data['email']
        message = self.validated_data['message']
        send_mail(send_mail=email, message=message)
        
# Serializer classes can also include reusable validators that are applied to the complete set of field data. These validators are included by declaring them on an inner Meta class, like so:
from rest_framework.validators import UniqueTogetherValidator
from .models import Event
class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    room_number = serializers.ChoiceField(choices=[101, 102, 103, 201])
    date = serializers.DateField()

    class Meta:
        # Each room only has one event per day.
        validators = [
            UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=['room_number', 'date']
            )
        ]
# depth = 1  # Expands the 'author' ForeignKey into a full object


from .models import Task
from django.db import models

class YesNoBooleanField(serializers.Field):
    """A custom field that turns True/False into Yes/No"""
    def to_representation(self, value):
        return "Yes" if value else "No"


class TaskSerializer(serializers.ModelSerializer):
    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        models.BooleanField: YesNoBooleanField
    }
    class Meta:
        model = Task
        fields = ['title', 'is_completed']
