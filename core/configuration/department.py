from __future__ import unicode_literals
from django.db import models
from .country import Country


class Department(models.Model):
    country = models.ForeignKey(Country, on_delete = models.RESTRICT, verbose_name='País')
    code = models.CharField(max_length=2, verbose_name='Código')  # Codigo identificador del departamento no es llave primaria
    description = models.CharField(max_length=45, verbose_name='Descripción')

    def __str__(self):
        return self.description