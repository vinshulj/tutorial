# from django.urls import path

# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("greet/",views.greet,name="greet"),
#     path("greet/hello",views.hello,name="hlo"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
#     path("books/",views.books,name="books"),
#     path("books/<int:sales_id>/",views.user,name="user"),
#     # path("sch",views.sch,name="sch"),
#     ]

from django.urls import path

from polls.views import MyView,HomePageView,HomeView, QuestionDetailView
from django.views.generic import RedirectView, ListView
from . import views

urlpatterns = [
    path("mine/", MyView.as_view(), name="my-view"),
    path("", HomePageView.as_view(),name="home"),
    path("home/", HomeView.as_view(),name="home-view"),
    path("about/", RedirectView.as_view(url="mine/", permanent=True),name="my-view-again"),
    path("about/mine/", MyView.as_view(), name="my-view-again"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    path("questions/", RedirectView.as_view(url="1/", permanent=False),name="questions-home"),
    path("questions/<int:pk>/", QuestionDetailView.as_view(),name="question-detail"),
    path("books/<int:pk>/", views.BookDetailView.as_view(),name="book-detail"),
    path("books/", views.booksXMLView.as_view(),name="books-xml"),
    path("user/<int:pk>/", views.UserView.as_view(),name="user-detail"),
    path("books/sales_report/", views.SalesRetortView.as_view(),name="sales-report"),
    # path("login/", views.UserLoginView.as_view(),name="login"),
    path("user_login/", views.LoginView.as_view(), name="user-login"),
    path("dashboard/", views.TemplateView.as_view(template_name="polls/dashboard.html"), name="dashboard"),
    path("create_user/", views.CreateUserView.as_view(), name="create-user"),
    # path("create_users/", views.CreateUserView.as_view(), name="create-user"),
    path("update_user/<int:pk>/", views.UpdateUserView.as_view(), name="update-user"),
    # path("sales/create/", SalesCreateView.as_view(), name="sales-create"),
    # path("sales/update/<int:pk>/", SalesUpdateView.as_view(), name="sales-update"),
    path("authors/", views.autherView.as_view(), name="author-list"),
    path("authors/create/", views.authercreateView.as_view(), name="author-create"),
    path("authors/update/<int:pk>/", views.autherupdateView.as_view(), name="author-update"),
    path("authors/delete/<int:pk>/", views.authordeleteview.as_view(), name="author-delete"),
    path("books/create/", views.BookCreateView.as_view(), name="book-create"),
    path("json/<int:pk>/", views.jsonView.as_view(), name="json-user"),
]