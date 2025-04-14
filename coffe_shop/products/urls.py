from django.urls import path
from .views import ProductFromView

urlpatterns = [
    path('agregar/', ProductFromView.as_view(), name='add_product'),
]
