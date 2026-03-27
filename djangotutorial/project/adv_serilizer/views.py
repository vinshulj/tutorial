from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer
from rest_framework.generics import ListAPIView
from rest_framework import generics

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer