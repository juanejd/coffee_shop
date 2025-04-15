from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .forms import OrderProductForm
from .serializers import OrderSerializer

# Vista que nos muestra en detalle la orden que hicimos
# Con LoginRequiredMixin, obligamos a que el usuario tenga una sesion iniciada para acceder a la vista
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order' # Acceder dentro del html

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active = True, user=self.request.user).first() #filter devuelve una lista y no un objeto, por eso usamos first() para transformarlo en un elemento y poder usarlo en el detailview

# Vista del boton 'add to my cart' para agregar productos a la orden
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm # Formulario para agregar productos a la orden
    success_url = reverse_lazy('my_order')

    # Metodo que verifica si la orden ya existe o si se debe crear una nueva.
    def form_valid(self, form):
        # Obtener la orden activa del usuario o crear una nueva si no existe con get_or_create
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user = self.request.user,
        )
        # Asignamos la orden a la instancia del formulario y la cantidad
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form) 
    
class OrderAPI(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

