from django.shortcuts import render
from .models import Veterinaria

def home(request):
    veterinarias = Veterinaria.objects.all()  # Obtiene todas las veterinarias
    return render(request, 'home.html', {'veterinarias': veterinarias})