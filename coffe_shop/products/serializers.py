from rest_framework.serializers import ModelSerializer
from .models import Product

# Serializers  que permite convertir los datos de un modelo a un formato JSON 
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "available", "photo"]
