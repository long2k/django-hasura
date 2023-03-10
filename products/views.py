from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from products.serializers import ProductSerializer


class ProductViewset(viewsets.GenericViewSet):
    endpoint_url = name ='product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=["get"])
    def list_product(self, request, *args, **kwargs):
        data = self.get_queryset()
        print(data)
        return Response(data,status=status.HTTP_200_OK)
        
    
# class OrderProduct():
#     endpoint_url = name = 'order'
    
    
    

# Create your views here.
