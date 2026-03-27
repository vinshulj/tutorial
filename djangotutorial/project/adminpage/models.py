# adminpage/models.py
from django.db import models
from django.contrib.auth.models import User

class Adduser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='adduser')
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    def __str__(self):
        return self.phone_number

