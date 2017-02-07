from django.shortcuts import render
from .models import Specie


# Create your views here.
def index(request):
    species = Specie.objects.all()
    context = {'species': species}
    return render(request, 'polls/index.html', context)
