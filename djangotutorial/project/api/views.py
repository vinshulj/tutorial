

# from rest_framework.views import APIView
# from .models import Book
# from .serializers import BookSerializer

# class BookAPIView(APIView):

#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True) # dict->Json and many=True because we are serializing a queryset
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BookSerializer(data=request.data) #request.data = client se bheja hua data (parsed form) 
#         # Q why not use request.post?
#         # ans. request.post is only for form data and it is not parsed, but request can handle all types of data like json,xml etc
#         if serializer.is_valid(): # .is_valid check if incoming request data is valid according to serializer fields and validation rules
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from api.models import Snippet
# from api.serializers import SnippetSerializer
# from rest_framework import status


# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# class SnippetListCreateAPIView(APIView):

#     def get(self, request):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SnippetSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view,parser_classes,renderer_classes,authentication_classes,throttle_classes,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

@parser_classes([JSONParser]) # this is use to parse incoming request data into python data type
@api_view(['GET', 'POST']) # this define only get and post method is allowed for other method like put delete it will give 405 method not allowed error
def hello_api(request):# request contain information like: headers,body,method,url,userinfo etc
    if request.method == "GET":
        return Response({"mes":"get method"})
    elif request.method == "POST":
        return Response({"mes":"post method"})
    return Response({
        "message": "Hello DRF",
        "status": "success"
    })
    
from rest_framework.parsers import JSONParser,FormParser, MultiPartParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

# @api_view(['POST'])
# # @parser_classes([JSONParser])
# def example_view(request, format=None):
#     """
#     A view that can accept POST requests with JSON content.
#     """
#     parser_classes=[JSONParser]  
#     return Response({'received data': request.data})

# @api_view(['POST'])
# @parser_classes([JSONParser,FormParser,MultiPartParser])
# @renderer_classes([BrowsableAPIRenderer])
# def example_view(request, format=None):
#     """
#     A view that can accept POST requests with JSON content.
#     """ 
#     return Response({'received data': request.data}) # request.data is calling parse method 

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from api.models import Book
from django.shortcuts import get_object_or_404
@api_view(["PUT","GET","POST","DELETE","PATCH"])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated,AllowAny])
def example_view(request, format=None):
    if request.method=="GET":
        print(request.parsers)
        data= Book.objects.all().values()
        
        # return render(request, "polls/index.html", context)
        response= Response({"message": "GET method","request":request.data, "data": data},status='200')
        print(response.status_code)
        return response
    if request.method=="POST":
        title = request.data.get("title")
        price = request.data.get("price")
        book = Book.objects.create(
            title=title,
            price=price
        )
        response=Response({"message": "POST method","request": request.data,"data": {"id": book.id,"title": book.title,"price": book.price}})
        print({"status_code":response.status_code,"query_params":request.query_params,"parser":request.user})
        return response
    if request.method=="PUT":
        book_id = request.data.get("id")
        print(book_id)
        if "title" not in request.data or "price" not in request.data:
            return Response({"error":"all field required"},status=404) 
        exist=Book.objects.filter(id=book_id).exists()
        print(exist)
        if exist:
            book = Book.objects.get(pk=book_id)
            book.title = request.data.get("title", book.title)
            book.price = request.data.get("price", book.price)
            book.save()  
        else:
            title = request.data.get("title")
            price = request.data.get("price")
            book = Book.objects.create(
                title=title,
                price=price
            ) 
            book.save()                          
        response= Response({"message": "PUT method","request":request.data ,"data":{"id":book.id,"title":book.title,"price":book.price}})
        return response
        # else:
        #     return Response({"message":"id requested"})
    if request.method=="PATCH":
        book_id = request.data.get("id")
        book = get_object_or_404(Book,id=book_id)
        book.title = request.data.get("title", book.title)
        book.price = request.data.get("price", book.price)
        book.save()                                             
        return Response({"message": "PUT method","request":request.data ,"data":{"id":book.id,"title":book.title,"price":book.price}})
    if request.method=="DELETE":
        book_id = request.data.get("id")
        book = get_object_or_404(Book,id=book_id)
        book.delete()
        return Response({"message": "DELETE method","request":request.data ,"data":{"id":book.id,"title":book.title,"price":book.price}})
    
from django.contrib.auth.models import User
from api.serializers import BookSerializer,ProductSerializer,UserSerializer,OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination

class BookListls(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
class BookListr(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
class BookListc(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
class BookListd(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
class BookListu(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
class BookListru(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    lookup_field="title"
class BookListrd(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
class BookListrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    
    
    
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000
class BookListl(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    pagination_class=LargeResultsSetPagination


from .models import Product,User,Order
from rest_framework.renderers import TemplateHTMLRenderer

# class ProductList(generics.ListCreateAPIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'api/product_list.html'

#     def get(self, request):
#         queryset = Product.objects.all()
#         return Response({'products': queryset})
    
class ProductList(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    template_name = 'api/product_list.json'
    serializer_class= ProductSerializer
    parser_classes=[JSONParser]

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'products': serializer.data})

class UserList(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    template_name = 'api/User_list.json'
    serializer_class= UserSerializer
    parser_classes=[JSONParser]

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        print(f"Total queries: {len(connection.queries)}")
        return Response({'users': serializer.data})

from django.db.models import F
from django.db import connection
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,BaseAuthentication
class OrderList(generics.ListCreateAPIView):
    # renderer_classes = [JSONRenderer]
    template_name = 'api/Order_list.json'
    serializer_class= OrderSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # parser_classes=[JSONParser]

    def get(self, request):
        queryset = Order.objects.annotate(  amount_total=F('Quantity')*F('Product__Price'),
                                            tax_amount=(F('amount_total')* F('Product__Price'))/100,
                                            final_amount=F('amount_total')+F('tax_amount'))
        # serializer = OrderSerializer(queryset, many=True)
        queryset=queryset.select_related("Product","User")
        serializer=OrderSerializer(queryset,many=True)
        print(f"Total queries: {len(connection.queries)}")
        return Response({'orders': serializer.data})
    
# Product_info = Order.objects.annotate(
#     amount_total=('quantity')*('Product__price'),
#     tax_amount=(amount_total*('Product__tax per'))/100,
#     final_amount=amount_total + tax_amount
# )


    # def get(self, request):
    #     queryset = User.objects.annotate( Bill_amount=sum(Order__final_amount))
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response({'users': serializer.data})

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleView(APIView):
    authentication_classes = [TokenAuthentication]  # TokenAuthentication
    # permission_classes = [AllowAny]  # User must be authenticated

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth) if request.auth else 'No token found',
        }
        return Response(content)



#admin by us
