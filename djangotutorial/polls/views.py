# from django.shortcuts import render,get_object_or_404
# from .models import Question, Choice, Book, Author, User, sales
# from django.http import HttpResponse
# from django.template import loader
# from django.http import Http404
# from django.db.models import Sum
# # def index(request):
# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     output = ", ".join(q.question_text for q in latest_question_list)
# #     return HttpResponse(output)

# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     template = loader.get_template("polls/index.html")
# #     context = {"latest_question_list": latest_question_list}
# #     return HttpResponse(template.render(context, request))


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)


# def greet(request):
#     return HttpResponse("greeting from the server.")
# def hello(req):
#     return HttpResponse("Hello from the server")

# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)
#     # return 0
# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, "polls/detail.html", {"question": question})   
# def detail(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})    
    
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     vote = Choice.objects.filter(question_id=question_id)
#     return render(request,"polls/vote.html" ,{"vote":vote})

# # def sch(request):
# #     sch=request.scheme
# #     return HttpResponse("Scheme is %s." % sch)

# # def sch(request):
# #     sch=request.get_signed_cookie('sessionid')
# #     breakpoint()
# #     return HttpResponse("Scheme is %s." % sch)

# # def sch(request):

# def books(request):
#     books=Book.objects.annotate(total_sales=Sum("sales__price"))
#     return render(request,"polls/books.html",{"books":books})

# def user(request,sales_id):                                                                                                             
#     users=User.objects.filter(sales__book_id=sales_id)
#     return render(request,"polls/user.html",{"users":users})



from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from .models import Question, Choice, Book, Author, User, sales
from django.views.generic import DetailView
from django.views.generic.list import ListView
from polls.forms import UserloginForm
from django.views.generic.edit import FormView


class MyView(View):

    def setup(self, request, *args, **kwargs):
        # Runs FIRST (before dispatch)
        print("setup() called")
        self.request = request
        self.args = args
        self.kwargs = kwargs
        super().setup(request, *args, **kwargs)
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Runs AFTER setup(), BEFORE get/post
        print("dispatch() called")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print("get() called")
        return HttpResponse("Hello, World! (GET)")

    def post(self, request, *args, **kwargs):
        print("post() called")
        print(request.POST)
        print(request.body)
        return HttpResponse("Hello, World! (POST)")

    def http_method_not_allowed(self, request, *args, **kwargs):
        print("http_method_not_allowed() called")
        return HttpResponse("Method not allowed", status=405)
    
    def options(self,request,*args,**kwargs):
        response=HttpResponse()
        response["Allow"]="GET,POST,OPTIONS"
        return response

class HomePageView(TemplateView):
    template_name = "polls/index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["latest_question_list"] = Question.objects.all()[:5]
    #     return context
    def get_template_names(self):
        return ["polls/home.html"]

class HomeView(HomePageView):
    template_name = "polls/home.html"


class AboutView(TemplateView):
    template_name = "polls/about.html"
    
class QuestionDetailView(DetailView):
    model = Question
    template_name = "polls/question.html"
    context_object_name = "question"
    
class BookDetailView(DetailView):
    model = Author
    template_name="polls/book_detail.html"
    context_object_name="authors"
    
class UserView(DetailView):
    model=User
    template_name="polls/user.txt"
    context_object_name="user"
    content_type="text/plain"
@method_decorator(csrf_exempt, name="dispatch")  
class SalesRetortView(ListView):
    model=sales
    context_object_name="sales"
    ordering=["-sale_date"]
    template_name="polls/sales_report.html"
    paginate_by=5
    page_kwarg="p"
    # queryset=sales.objects.filter(quantity=0) #it is sane as model=sales
    paginate_orphans=2
    allow_empty=False
    # http_method_names=["get","head"]
    http_method_names=["get"]
    extra_context={"title":"Sales Report"}
    # 3 more paginator,template_engine,content_type
    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size",self.paginate_by)
    def get_ordering(self):
        return self.request.GET.get("sort_by",self.ordering[0])
    
class UserLoginView(FormView):
    template_name="polls/login.html"
    form_class=UserloginForm
    success_url="/polls/mine/"
    
    def form_valid(self, form):
        username=form.cleaned_data["User_name"]
        password=form.cleaned_data["password"]
        print(f"Username: {username}, Password: {password}")
        return super().form_valid(form)
    
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, UserUpdateForm

class LoginView(FormView):
    template_name = "polls/user_login.html"              
    form_class = LoginForm                    
    success_url = reverse_lazy("dashboard")        
    initial = {"username": "name", "password": "abc@123"}                
    prefix = "login"                          
    http_method_names = ["get", "post"]       
    extra_context = {"title": "Login Page"}   
    success_message = "Login successful!!"

    def get_form_kwargs(self):
        """
        Why: pass extra data to form
        """
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get_form(self, form_class=None):
        """
        Why: modify form instance
        """
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs["class"] = "form-control"
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"] = "Enter your credentials"
        return context

    def form_valid(self, form):
        username = form.cleaned_data["username"]# to remove extra space , normalize , change data type
        password = form.cleaned_data["password"]

        user = authenticate(self.request, username=username, password=password) # to check in database 

        if user is not None:
            login(self.request, user) # create a session so that browser remembers the user
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password")#it give non field error AND PRINT THE MESSAGE at the top of form method=post
            return self.form_invalid(form)

    def form_invalid(self, form):
        print("Login failed:", form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return self.success_url
    
    
# class CreateUserView(FormView):
#     template_name = "polls/create_user.html"
#     form_class = LoginForm
#     success_url = reverse_lazy("user-login")
#     extra_context = {"title": "Create User", "subtitle": "Fill the form to create a new user"}

#     def form_valid(self, form):
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]

#         User.objects.create_user(username=username, password=password)

#         return super().form_valid(form)
    
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import UserCreateForm, UserUpdateForm, AuthorUpdateForm , AuthorDeleteForm , BookForm 
from django.contrib.auth.models import User


class CreateUserView(CreateView):
    # model = User
    # fields = ["username", "password"]
    form_class = UserCreateForm
    template_name = "polls/create_user.html"
    success_url = reverse_lazy("user-login")
    extra_context = {"title": "Create User", "subtitle": "Fill the form to create a new user"}

class UpdateUserView(UpdateView):
    model=User
    form_class = UserUpdateForm
    template_name = "polls/update_user.html"
    success_url = reverse_lazy("user-login")
    
# views.py
# from django.views.generic import CreateView
# from django.urls import reverse_lazy
# from .models import sales
# from .forms import SalesForm

# class SalesCreateView(CreateView):
#     model = sales
#     form_class = SalesForm
#     template_name = "sales_form.html"
#     success_url = reverse_lazy("success")
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         # ensure FK dropdown is always valid
#         form.fields['book'].queryset = Book.objects.all()
#         return form
#     def form_valid(self, form):
#         # is_valid() already passed here ✅ 

#         # cleaned_data
#         book = form.cleaned_data.get("book")
#         quantity = form.cleaned_data.get("quantity")

#         # save(commit=False)
#         sale = form.save(commit=False)

#         # instance (before save)
#         print("Instance before save:", form.instance)

#         # custom logic before save
#         if quantity > 500:
#             form.add_error("quantity", "Bulk sales need manager approval")
#             return self.form_invalid(form)

#         sale.save()  # actual DB save

#         return super().form_valid(form)

#     def form_invalid(self, form):
#         # errors
#         print(form.errors)

#         # non-field errors
#         print(form.non_field_errors())

#         return super().form_invalid(form)

# from django.views.generic import UpdateView

# class SalesUpdateView(UpdateView):
#     model = sales
#     form_class = SalesForm
#     template_name = "sales_form.html"
#     success_url = reverse_lazy("success")
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         # ensure FK dropdown is always valid
#         form.fields['book'].queryset = Book.objects.all()
#         return form
#     def form_valid(self, form):
#         # instance (existing object)
#         sale = form.instance

#         # has_changed()
#         if form.has_changed():
#             print("Changed fields:", form.changed_data)

#         # cleaned_data
#         new_qty = form.cleaned_data.get("quantity")

#         if new_qty > 1000:
#             form.add_error("quantity", "Quantity too large to update")
#             return self.form_invalid(form)

#         return super().form_valid(form)

class autherView(ListView):
    model=Author
    template_name="polls/author.html"
    context_object_name="authors"

class authercreateView(CreateView):
    model=Author
    fields=["name"]
    template_name="polls/author_form.html"
    success_url=reverse_lazy("author-list")
    extra_context={"title":"Create Author"}

class autherupdateView(UpdateView):
    model=Author
    form_class=AuthorUpdateForm
    template_name="polls/author_form.html"
    success_url=reverse_lazy("author-list")
    extra_context={"title":"Update Author"}
    
    
from django.views.generic.edit import DeleteView   
                                                 
class authordeleteview(DeleteView):
    model = Author
    form_class = AuthorDeleteForm
    template_name = "polls/author_confirm_delete.html"
    success_url = reverse_lazy("author-list")
    extra_context = {"title": "Delete Author"}


class BookCreateView(CreateView):
    model=Book
    form_class=BookForm
    fieldsets = (
    ("Basic Info", {"fields": ("title",)}),
    ("Extra Info", {"fields": ("author",)}),)
    # fields=["title","author"]
    template_name="polls/book_form.html"
    success_url=reverse_lazy("books")

class booksXMLView(ListView):
    model=Book
    template_name="polls/books.xml"
    content_type="application/xml"

class jsonView(DetailView):
    model=User
    template_name="polls/abc.json"
    content_type="application/json"
    context_object_name = "user"
    
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_api(request):
    return Response({
        "message": "Hello DRF",
        "status": "success"
    })
