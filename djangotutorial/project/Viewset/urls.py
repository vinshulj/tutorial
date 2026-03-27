from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import EmployeeViewSet,EmployeeModelViewSet,UserViewSet,EmployeeROViewSet
# router = SimpleRouter()
# router.register(r'employees', EmployeeViewSet, basename='employee')
# router.register(r'employees-m', EmployeeModelViewSet, basename='employee-model')
# urlpatterns= router.urls
# router = DefaultRouter()
# router.register(r'user',UserViewSet,basename='user')
# router.register(r'employees-ro',EmployeeROViewSet,basename='read-only')
# urlpatterns += [
#     path('',include(router.urls))
# ]

# SimpleRouter = SimpleRouter()
# SimpleRouter.register(r'employees', EmployeeViewSet, basename='employee')
# SimpleRouter.register(r'employees-m', EmployeeModelViewSet, basename='employee-model')
# DefaultRouter = DefaultRouter(trailing_slash=False)
# DefaultRouter.register(r'user',UserViewSet,basename='user')
# DefaultRouter.register(r'employees-ro',EmployeeROViewSet,basename='read-only')
# urlpatterns = [
#     path('',include(SimpleRouter.urls)),
#     path('',include(DefaultRouter.urls))
# ]


from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]
    
# router = CustomReadOnlyRouter()
# router.register(r'user',UserViewSet,basename='user')
# urlpatterns= router.urls


#By using normal path
user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_set_password=UserViewSet.as_view({
    'post':'set_password'
})
user_password=UserViewSet.as_view({
    'put':'password',
    'delete':'delete_password'
})
urlpatterns = [
    path('user/', user_list),
    path('user/<int:pk>/', user_detail),
    path('user/set_password/',user_set_password),
    path('user/<int:pk>/password/',user_password)
]

#Django salary