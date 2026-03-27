from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=355)
    last_name=models.CharField(max_length=355)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    def __str__(self):
        return self.first_name+self.last_name
    
    
class Order(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15,decimal_places=2)
    quantity=models.IntegerField()
    def __str__(self):
        return self.quantity
    
class Product(models.Model):
    product_name=models.CharField(max_length=355)
    amount=models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.product_name
    
    
class Transection(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15,decimal_places=2)
    quantity=models.IntegerField()                          