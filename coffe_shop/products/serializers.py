from rest_framework.serializers import ModelSerializer
from .models import Product

# Serializer que permite convertir los datos de un modelo escrito en python a un formato JSON 
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "available"]