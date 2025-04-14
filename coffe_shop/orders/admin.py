from django.contrib import admin
from .models import Order, OrderProduct

# Modselos para el admin de django para crear, editar y eliminar los productos de la orden
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0 


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)
