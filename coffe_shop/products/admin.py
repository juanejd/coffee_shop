from django.contrib import admin
from .models import Product

# CModificar productos en el administrador
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price'] # campos que se mostraran en los productos en la interfaz del admin
    search_fields = ['name'] # campo de busqueda en la interfaz del admin


admin.site.register(Product, ProductAdmin)
