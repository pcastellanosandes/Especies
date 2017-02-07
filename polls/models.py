from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Specie(models.Model):
    photoPath = models.CharField(max_length=1000)
  #  name = models.CharField(max_length=50, default="")
  #  scientificName = models.CharField(max_length=50, null=1)
  #  description = models.CharField(max_length=1000, null=1)
