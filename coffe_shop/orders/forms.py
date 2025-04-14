from django.forms import ModelForm
from .models import OrderProduct

# Formulario para mis pedidos en donde esta la orden, producto y la cantidad
class OrderProductForm(ModelForm):
  class Meta:
    model = OrderProduct
    fields = ['product'] # Solo utilizamos el producto
