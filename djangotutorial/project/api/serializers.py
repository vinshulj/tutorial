from rest_framework import serializers
from .models import Book,User,Product,Order

class BookSerializer(serializers.ModelSerializer): # ModelSerializer is use to convert modal data into jason
    class Meta:
        model = Book
        fields = '__all__'


        # fields=['amount_total','tax_amount','final_amount']
        # extra_fields=['UserO_set']

class OrderSerializer(serializers.ModelSerializer):
    amount_total=serializers.FloatField(required=False)
    tax_amount=serializers.FloatField(required=False)
    final_amount=serializers.FloatField(required=False)
    class Meta:
        model= Order
        fields='__all__'
from django.db.models import F

class UserSerializer(serializers.ModelSerializer):
    UserO = OrderSerializer(many=True, read_only=True)
    # UserO = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # UserO = serializers.StringRelatedField(many=True,query_set=Order.object.all)
    # UserO=serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name="Order_detail")
    # UserO=serializers.HyperlinkedIdentityField(view_name="Order_detail")
    # amount_total=serializers.FloatField(required=False)
    # tax_amount=serializers.FloatField(required=False)
    # final_amount=serializers.FloatField(required=False)
    # User=OrderSerializer(read_only=True)
    # Product=ProductSerializer(read_only=True)
    class Meta:
        model= User
        # fields='__all__'
        fields = ['User_name', 'User_id', 'Age', 'Contect_info','UserO']
        
    
class ProductSerializer(serializers.ModelSerializer):
    # ProductO= OrderSerializer(many=True,read_only=True)
    class Meta:
        model= Product
        # fields='__all__'
        fields = ['Product_name', 'Price', 'Fiber', 'Brand', 'Tax_per', 'Fashion', 'Quantity_ava']
        
class OrderSerializer(serializers.ModelSerializer):
    amount_total=serializers.FloatField(required=False)
    tax_amount=serializers.FloatField(required=False)
    final_amount=serializers.FloatField(required=False)
    # User=serializers.CharField()
    User = UserSerializer(read_only=True)
    # User=Order.objects.prefetch_related("Product","User")
    Product = ProductSerializer(read_only=True)                                           
    class Meta:
        model= Order
        # fileds='__all__'
        fields=['User_name','amount_total','final_amount','tax_amount','Product']
    # User_name = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # User_name = serializers.StringRelatedField(many=True, read_only=True)
    # User_name = ProductSerializer(many=True, read_only=True)
# Product_info = Order.objects.annotate(
#     amount_total=('quantity')*('Product__price'),
#     tax_amount=(amount_total*('Product__tax per'))/100,
#     final_amount=amount_total + tax_amount
# )


