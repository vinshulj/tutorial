from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.views.generic import ScopedProtectedResourceView,ProtectedResourceView

class ApiEndpoint(ProtectedResourceView):
    # required_scopes = ['read']  # The token MUST have this scope
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2! Client Credentials worked.')


from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .serializers import DataSerializer
from rest_framework.generics import GenericAPIView
from .models import data
from rest_framework.response import Response

class DataView(GenericAPIView):
    queryset = data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [TokenHasReadWriteScope]
    
    def delete(self, request, *args, **kwargs):
        return Response({data:"delete"})
