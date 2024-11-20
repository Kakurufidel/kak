from rest_framework.views import APIView
from .models import Category,Product
from project.CategorySerializer import CategorySerializer
from project.ListProductsSerializer import ListProductsSerializer
from rest_framework.response import Response

from rest_framework.viewsets import ReadOnlyModelViewSet


class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()
    # def get(self, *args, **kwargs):
    #     categories =Category.objects.all()
    #     serializer = CategorySerializer(categories, many = True)
    #     return Response(serializer.data)
    
class ListProductsViewset(ReadOnlyModelViewSet):
    
    serializer_class = ListProductsSerializer
    query = Product.objects.all()
    
    
    # def get(self, *args, **kwargs):
    #     query = Product.objects.all()
    #     serializer= ListProductsSerializer(query, many = True)
    #     return Response(serializer.data)   
    
    def get_queryset(self):
        return Product.objects.all()