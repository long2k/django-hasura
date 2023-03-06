from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Product(models.Model):
    product_id = models.BigIntegerField(db_index=True)
    name = models.CharField(max_length=255)
    price =  models.CharField(max_length=255)
    img_url = ArrayField(models.TextField())
    description =  models.TextField()
    created = models.DateTimeField(auto_now_add= True, blank=True)
    updated = models.DateTimeField(null = True)
    
    
class ProductCategory(models.Model):
    product_id = models.BigIntegerField(db_index=True)
    category_id = models.BigIntegerField(db_index=True)
    created = models.DateTimeField(auto_now_add= True, blank= True)
    updated = models.DateField(null=True)
