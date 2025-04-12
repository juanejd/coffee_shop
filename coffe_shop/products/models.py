from django.db import models


class Product(models.Model):
    # verbose_name --> como queremos que nuestro campo se vea en el usuario final o en el admin de django
    # el cual nos permite administrador los datos de nuestro modelo
    name = models.TextField(max_length=200, verbose_name='nombre')
    description = models.TextField(max_length=300, verbose_name='descripcion')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
    available = models.BooleanField(default=True, verbose_name='disponible')
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name='foto') # parametros para permitir subir un producto sin foto

    def __str__(self):
        return self.name
