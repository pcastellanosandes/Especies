from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.forms import forms
from django.forms import ModelForm


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    imageURL = models.CharField(max_length=1000, null=True)
    interest = models.TextField(max_length=1000, null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, null=False)
    search_fields = ('name',)
    def __unicode__(self): return self.name

class Specie(models.Model):
    name = models.CharField(max_length=50, default="")
    scientificName = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000, null=True)
    imageURL = models.CharField(max_length=1000, null=True)
    taxonomic_classification = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __unicode__(self): return self.name

class Comment(models.Model):
    description = models.CharField(max_length=1000, null=False)
    specie = models.ForeignKey(Specie, related_name='comments',  null=True, on_delete=models.CASCADE)


class UserForm(ModelForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'interest', 'imageURL', 'password', 'password2']

    def clean_username(self):
        """Comprueba que no exista un username igual en la bd"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la bd"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual al registrado.')
        return email

    def clean_paswword(self):
        """Comprueba que password y password2 sean iguales"""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Los password no coinciden.')
        return password

class UpdateUser(ModelForm):
    username = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'readonly':'readonly'}))
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email']
        #fields = ['username', 'first_name', 'last_name', 'email', 'interest', 'imageURL', 'password', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        print (username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

class UpdateProfile(ModelForm):
    imageURL = models.CharField(max_length=1000, null=True)
    interest = models.TextField(max_length=1000, null=True)

    class Meta:
        model = Profile
        fields = ['interest', 'imageURL']
        # fields = ['username', 'first_name', 'last_name', 'email', 'interest', 'imageURL', 'password', 'password2']

    def clean_imageURL(self):
        imageURL = self.cleaned_data['imageURL']
        print(imageURL)
        return imageURL

    def clean_interest(self):
        interest = self.cleaned_data['interest']
        print(interest)
        return interest

