from rest_framework.serializers import ModelSerializer
from shop.models import Product

class ListProductsSerializer(ModelSerializer):
    class Meta :
        model = Product
        fields =['id','name','date_created','date_updated','category']