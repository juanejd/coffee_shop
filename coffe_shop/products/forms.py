from django import forms
from .models import Product


# Formulario para el modelo Products
class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)

    # metodo que guarda la informacion del formulario cuando el usuario haga submit y crear estos datos en la base de datos
    def save(self):
        Product.objects.create(
            # cleaned_data --> informacion limpia desde el request del usuario
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            available = self.cleaned_data['available'],
            photo = self.cleaned_data['photo'],
        )