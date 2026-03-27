from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.title



    

class User(models.Model):
    User_name=models.TextField()
    User_id=models.CharField(max_length=5)
    Age=models.IntegerField()
    Contect_info=models.IntegerField(default=999999999)
    # def __str__(self):
    #     return "%s,%s,%d,%d" % (self.User_id,self.User_name,self.Age,self.Contect_info)
    
class Product(models.Model):
    Product_name=models.CharField(max_length=100)
    Price=models.IntegerField()
    Fiber=models.CharField(max_length=100)
    Brand=models.CharField(max_length=100)
    Tax_per=models.FloatField(default=18)
    Fashion=models.CharField(max_length=100)
    Quantity_ava=models.IntegerField(default=0)
       
class Order(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="ProductO")
    User=models.ForeignKey(User, on_delete=models.CASCADE,related_name="UserO")
    Quantity=models.IntegerField()
    # def __str__(self):
    #     return '%d' % (self.Quantity)
    

