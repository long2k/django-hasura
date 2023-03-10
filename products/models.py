from django.db import models
from django.contrib.postgres.fields import ArrayField
from categories.models import Category

# Create your models here.
class Product(models.Model):
    product_id = models.BigIntegerField(db_index=True)
    name = models.CharField(max_length=255)
    price =  models.CharField(max_length=255)
    img_url = ArrayField(models.TextField())
    description =  models.TextField()
    created = models.DateTimeField(auto_now_add= True, blank=True)
    updated = models.DateTimeField(auto_now_add= True, blank= True)
    class Meta:
        db_table = 'product'
        managed = False
    
    
class ProductCategory(models.Model):
    id = models.BigIntegerField(primary_key=True, db_index=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add= True, blank= True)
    updated = models.DateTimeField(auto_now_add= True, blank= True)
    class Meta:
        db_table = 'product_category'
        managed = False
        

class Order(models.Model):
    order_id = models.BigIntegerField(db_index= True, primary_key=True)
    created = models.DateTimeField(auto_now_add = True, blank= True)
    updated = models.DateTimeField(auto_now_add= True, blank= True)
    class Meta:
        db_table = 'order'
        managed = False
  
class ProductOrder(models.Model):
    id = models.BigIntegerField(db_index=True, primary_key=True)
    product_id =  models.ForeignKey(Product, on_delete= models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete= models.CASCADE)
    amount = models.BigIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add= True, blank= True)
    class Meta: 
        db_table = 'product_order'
        managed = False
    

