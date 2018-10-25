from django.db import models
from datetime import datetime
from django.db.models import Max
from django.db.models import Min

# class ProductManager(models.Manager):
#     def lowestPrice(self, productID):
#         compare = Stock.objects.filter(product_id=1)
#         compare.aggregate(Min('price'))
#         compare.aggregate(Max('price'))
#         len(compare) 
#         for i in compare:
#             print(i.price)        
# 
# for i in product:
              #print(i.price)

#         #for price in Stock.objects.all() 
#         #print(price.price)    
#         #Count
#         #Compare prices



#         #Return lowest


class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    category = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    #objects=ProductManager()

class User(models.Model):
    userName = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)





class Retailer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Stock(models.Model):
    product_id = models.ForeignKey(Product, related_name='product_id')
    retailer_id = models.ForeignKey(Retailer, related_name='retailer_id')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
