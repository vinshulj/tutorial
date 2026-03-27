from django.db import models
from django.db.models.functions import Coalesce

# Abstract class
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class StudentA(CommonInfo):
    address = models.CharField(max_length=5)
    
class Teacher(CommonInfo):
    subject=models.CharField(max_length=100)
    
    
    
#Multi-table inheritance
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    
    
#Proxy models
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)



class MyPerson(Person):
    # full_name=models.CharField(max_length=30)
    class Meta:
        proxy = True

    def do_something(self):
        return "function is used"
    
class FirstPerson(Person):
    pass


