from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views  import APIView
from rest_framework.response import Response

from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer

class ProductFromView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product') # cuando el producto este creado, redirigira al url especificado

    def form_valid(self, form):
      form.save()
      return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products' # nombre del contexto que se pasara al template

# Vista que muestra la lista de productos en formato JSON
class ProductListAPI(APIView):
    # Sin autenticacion
    authentication_classes = []
    permission_classes = []

    # Modificamos el metodo get para que devuelva la lista de productos en formato JSON
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) # many para que el serializer sepa que es una lista
        return Response(serializer.data) # devuelve la lista de productos en formato JSON
