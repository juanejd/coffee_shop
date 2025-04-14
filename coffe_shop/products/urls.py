from django.urls import path
from .views import ProductFromView, ProductListView, ProductListAPI

urlpatterns = [
    path('', ProductListView.as_view(), name='list_product'),
    path('api/', ProductListAPI.as_view(), name='list_product_api'),
    path('agregar/', ProductFromView.as_view(), name='add_product'),
]
