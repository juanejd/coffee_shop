from django.urls import path

from .views import MyOrderView, CreateOrderProductView, OrderAPI

urlpatterns = [
    path("mi-orden", MyOrderView.as_view(), name="my_order"),
    path("agregar-producto", CreateOrderProductView.as_view(), name="add_product"),
    path(
        "api", OrderAPI.as_view(), name="order_product_api"
    ),  # API para obtener las ordenes activas de los usuarios
]
