from django.db import models

# Create your models here.
class Email(models.Model):
    email=models.EmailField()
    message=models.TextField(max_length=250)

class Event(models.Model):
    name = models.CharField(max_length=155)
    room_number = models.CharField()
    date = models.DateField()
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title