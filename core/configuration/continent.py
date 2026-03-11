from __future__ import unicode_literals
from django.db import models


class Continent(models.Model):
    code = models.CharField(max_length=2, verbose_name='Codigo')
    description = models.CharField(max_length=45, verbose_name='Descripción')

    def __str__(self):
        return self.description