from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order

# Con mixin solo accderemos a la vista si el usuario esta logeado
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order' # Acceder dentro del html

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active = True, user=self.request.user).first() #filter devuelve una lista y no un objeto, por eso usamos first() para obtener el primer elemento de la lista
