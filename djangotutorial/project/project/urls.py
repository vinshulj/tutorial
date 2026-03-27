"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from oauth2_provider import urls as oauth2_urls
from django.urls import path, include
from django.conf import settings
import oauth2_provider.views as oauth2_views

# 1. Pre-made OAuth2 endpoints (Login, Token, etc.)
oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

# 2. Management endpoints (Only visible during development/DEBUG mode)
if settings.DEBUG:
    oauth2_endpoint_views += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('adminpage/', include("adminpage.urls")),
    path('jwtapi/',include('jwtapi.urls')),
    path('signal_app/',include('signal_app.urls')),
    path('viewset/',include('Viewset.urls')),
    # path('o/', include(oauth2_urls)),
    path("oauth/",include('o_auth.urls')),
    path('o/', include((oauth2_endpoint_views, 'oauth2_provider'), namespace="oauth2_provider")),
    path("ser/",include('adv_serilizer.urls'))
]
from oauth2_provider.views import DeviceAuthorizationView,DeviceUserCodeView

oauth2_endpoint_views += [
    path('device-authorization/', DeviceAuthorizationView.as_view(), name='device-authorization'),
    path('device/',DeviceUserCodeView.as_view())
]                                                                                                                                                   