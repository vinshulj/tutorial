from django.urls import path
from .views import UserView
from rest_framework.routers import DefaultRouter,SimpleRouter
router=DefaultRouter()
router.register(r'user',UserView)
urlpatterns = router.urls                   
                                             