from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    category = models.CharField(max_length=45)

class Retailer(models.Model):
    name = models.CharField(max_length=255)

class Stock(models.Model):
    product_id = models.ForeignKey(Product, related_name='product_id')
    retailer_id = models.ForeignKey(Retailer, related_name='retailer_id')
    price = models.FloatField()
