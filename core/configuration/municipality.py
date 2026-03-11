from __future__ import unicode_literals
from django.db import models
from .department import Department


class Municipality(models.Model):
    department = models.ForeignKey(Department, on_delete = models.RESTRICT, verbose_name='Departamento')
    code = models.CharField(max_length=5, verbose_name='Código')  # Codigo identificador del municipio no es llave primaria
    description = models.CharField(max_length=45, verbose_name='Descripción')

    def __str__(self):
        return self.description