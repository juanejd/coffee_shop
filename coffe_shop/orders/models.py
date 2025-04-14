from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Modelo de pedidos
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True) #saber si la orden esta activa o agregando productos
    order_date = models.DateTimeField(auto_now_add=True) #fecha de creacion al momento de registrar la orden

    def __str__(self):
        return f'order {self.id} by {self.user}'
    
# Modelo para guardar la orden, el producto y la cantidad
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) #relacion con el modelo de orden
    product = models.ForeignKey(Product, on_delete=models.PROTECT) #si la orden esta lista y el producto se elimina, necesitamos dejar la orden en su estado anterior
    quantity = models.IntegerField() 

    def __str__(self):
        return f'{self.order} - {self.product}'