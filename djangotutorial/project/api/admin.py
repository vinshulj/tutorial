from django.contrib import admin
from .models import Book,Product,Order,User

admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)