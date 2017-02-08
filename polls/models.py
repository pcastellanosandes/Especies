from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imageFile = models.ImageField(upload_to='images', null=True)
    interest = models.TextField(max_length=1000, null=True)


# Create your models here.
class Specie(models.Model):
    name = models.CharField(max_length=50, default="")
    scientificName = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000, null=True)
    imageFile = models.ImageField(upload_to='images', null=True)


class Comment(models.Model):
    description = models.CharField(max_length=1000, null=False)


class Category(models.Model):
    name = models.CharField(max_length=20, null=False)