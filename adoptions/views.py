from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from django.http import Http404


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets':pets})


def pet_detail(request, id):
    try:
     pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_details.html', {'pet': pet})

    



