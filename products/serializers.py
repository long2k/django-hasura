from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Product, ProductCategory

class ProductSerializer(serializers.Serializer):
    class Meta: 
        model = Product
        fields =["product_id", "name", "price", "img_url", "description", "created", "updated"]