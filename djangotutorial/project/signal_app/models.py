from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(blank=True, null=True)
    
from adminpage.models import Adduser

class AddressList(models.Model):
    adduser=models.ForeignKey(Adduser, on_delete=models.CASCADE)
    pin_code=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.city}, {self.state}, {self.country} - {self.pin_code}"

class UserAddressList(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    pin_code=models.IntegerField(null=True, default=None)
    city=models.CharField(max_length=100, null=True, default=None)
    state=models.CharField(max_length=100, null=True, default=None)
    country=models.CharField(max_length=100, null=True, default=None)
    def __str__(self):
        return f"{self.city}, {self.state}, {self.country} - {self.pin_code}"