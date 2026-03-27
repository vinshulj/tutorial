from django.urls import path
from .views import hello_api,example_view,BookListls,BookListr,BookListd,BookListu,BookListl,BookListc,BookListrd,BookListrud,BookListru
from .views import ProductList,UserList,OrderList,ExampleView
urlpatterns = [
    path('hello/', hello_api),
    # path('example/', example_view),
    # generic
    path('books/ls', BookListls.as_view()),# Listcreate
    path('books/<int:pk>/r', BookListr.as_view()),#r
    path('books/<int:pk>/u', BookListu.as_view()),
    path('books/<int:pk>/d', BookListd.as_view()),
    path('books/l', BookListl.as_view()),
    path('books/c', BookListc.as_view()),
    path('books/<int:pk>/ru', BookListru.as_view()),
    path('books/<int:pk>/rd', BookListrd.as_view()),
    path('books/<int:pk>/rud', BookListrud.as_view()),
    # Cloth brand
    path("cloth/product/", ProductList.as_view()),
    path("cloth/user/", UserList.as_view()),
    path("cloth/order/", OrderList.as_view(),name="Order_detail"),
    path("example/",ExampleView.as_view())
]

from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]