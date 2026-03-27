from .views import TaskListView
from django import urls
from django.urls import path
urlpatterns=[
    path('task',TaskListView.as_view())
]