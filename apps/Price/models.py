from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.db.models import Max
from django.db.models import Min
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, userName, email, password, password2):
        errors = []
        if len(userName) < 3:
            errors.append(" Username must be more than 3 char")
        if len(email) < 1:
            errors.append('Email is required')
        elif not EMAIL_REGEX.match(email): #check thru Regex
            errors.append('invalid email')
        else: 
            userMatchingEmail = User.objects.filter(email = email)# check if email already exist in data Base
            if len(userMatchingEmail)> 0:
                errors.append("email already used")
        
       
        if len(password) < 1:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("password must be at least 8 chars")
        elif password != password2: #check if confrim pass is matched
            errors.append("password must match")

        response = {
            "errors": errors,
            "valid": True,
            "user": None
        }
        if len(errors) > 0:
            response["valid"] = False
            response["errors"] = errors
        else:
            
            response["user"] = User.objects.create(
            userName = userName, 
            email = email, 
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            )        
        return response

    def login(self, email, password):
        errors = []

        if len(email) < 1:
            errors.append('Email is required')
        elif not EMAIL_REGEX.match(email): #check thru Regex
            errors.append('invalid email')
        else: 
            userMatchingEmail = User.objects.filter(email = email)# check if email already exist in data Base
            if len(userMatchingEmail)== 0:
                errors.append("unknown email")
        
        if len(password) < 1:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("password must be at least 8 chars")
        
        response = {
            "errors": errors,
            "valid": True,
            "user": None
        }

        if len (errors) == 0:
            if bcrypt.checkpw(password.encode(), userMatchingEmail[0].password.encode()):
            #password.encode to un unicode the password
            #bcrypt.checkpw to check the password
            #the whole line from left to right mean brypt check the encoded password and see if it match the user.password input) 
                response['user'] = userMatchingEmail[0]
            else:
                errors.append("incorrect password")

        if len(errors) > 0:
            response['errors'] = errors
            response['valid'] = False

        return response

class User(models.Model):
    userName = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    objects = UserManager()
    


class Retailer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



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

class Stock(models.Model):
    product_id = models.ForeignKey(Product, related_name='product_id', on_delete=models.CASCADE)
    retailer_id = models.ForeignKey(Retailer, related_name='retailer_id', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
