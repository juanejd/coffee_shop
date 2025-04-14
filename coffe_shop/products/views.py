from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm

class ProductFromView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product') # cuando el producto este creado, redirigira al url especificado

    def form_valid(self, form):
      form.save()
      return super().form_valid(form)
    
