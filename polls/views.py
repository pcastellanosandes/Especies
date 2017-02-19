# -*- coding: utf-8 -*-
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext


from .models import Specie, UserForm, Profile, Comment,Category
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    def post (self,request,*args,**kwargs): print (" campo ..."+request.POST['categorias'])
    #buscar = request.POST['categorias']
    buscar =1
    if buscar == '0' :
        species = Specie.objects.all();
    else :
        species = Specie.objects.filter(category_id=buscar)
    categories = Category.objects.all()
    context = {'species': species,'categories':categories }
    return render(request, 'polls/index.html', context)


# Atiende peticiones para la vista de adición de usuario
def add_user_view(request):
    # Si es POST
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            email = cleaned_data.get('email')
            interest = cleaned_data.get('interest')
            image_url = form.cleaned_data['imageURL']

            user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email)

            profile = Profile(user=user, interest=interest, imageURL=image_url)
            profile.save()

            return HttpResponseRedirect(reverse('images:index'))
    # Si no es POST devolver la forma para llenar
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'polls/registro.html', context)


def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('images:index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('images:index'))
        else:
            mensaje = 'Nombre de usuario o clave no valido'

    return render(request, 'polls/login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('images:index'))


def specie_information(request, id_specie):
    specie = Specie.objects.get(id=id_specie)
    specie = {'specie': specie}

    return render(request, 'polls/specie_information.html', specie)


def add_comment(request, id_specie):

    text = request.GET['comment']
    specie = Specie.objects.get(id=id_specie)
    comment = Comment(description=text, specie=specie)
    comment.save()

    specie = {'specie': specie}
    return render(request, 'polls/specie_information.html', specie)
