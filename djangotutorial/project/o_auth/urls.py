from django.urls import path
from .views import ApiEndpoint,secret_page,DataView

urlpatterns = [
    path('hello/', ApiEndpoint.as_view()),
    path("secret",secret_page) ,
    path("data/",DataView.as_view()),
]
