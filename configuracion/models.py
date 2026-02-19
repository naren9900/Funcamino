from __future__ import unicode_literals
from django.db import models


# Create your models here.

#============================================================
#                      CONFIGURACIONES
#============================================================
class Continentes(models.Model):
    codigo = models.CharField(max_length=2)   # Codigo identificador del Continente no es llave primaria
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.descripcion

class Paises(models.Model):
    continentes = models.ForeignKey(Continentes, on_delete = models.RESTRICT)
    codigo = models.CharField(max_length=3)  # Codigo identificador del pais no es llave primaria
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.descripcion

class Departamentos(models.Model):
    paises = models.ForeignKey(Paises, on_delete = models.RESTRICT)
    codigo = models.CharField(max_length=2)  # Codigo identificador del departamento no es llave primaria
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.descripcion

class Municipios(models.Model):
    departamentos = models.ForeignKey(Departamentos, on_delete = models.RESTRICT)
    codigo = models.CharField(max_length=5)  # Codigo identificador del municipio no es llave primaria
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.descripcion



#============================================================
#                           EDUCATE
#============================================================