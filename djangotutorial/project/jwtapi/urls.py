from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import APILogoutView,CustomTokenObtainPairView,CustomToken,CustomTokenB

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout/',APILogoutView.as_view()),
    path('api/ctoken/',CustomTokenObtainPairView.as_view()),
    path('api/ctoken/a/', CustomToken.as_view() ),
    path('api/ctoken/b/', CustomTokenB.as_view() ),
]