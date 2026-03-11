from __future__ import unicode_literals
from django.db import models
from .continent import Continent


class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete = models.RESTRICT, verbose_name='Continente')
    code = models.CharField(max_length=3, verbose_name='Código')  # Codigo identificador del pais no es llave primaria
    description = models.CharField(max_length=45, verbose_name='Descripción')

    def __str__(self):
        return self.description