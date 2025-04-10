from django.shortcuts import render, get_object_or_404, redirect
from .models import Veterinaria
from .forms import VeterinariaForm 

def home(request):
    veterinarias = Veterinaria.objects.all()  # Obtiene todas las veterinarias
    return render(request, 'veterinarias/home.html', {'veterinarias': veterinarias})

def lista_veterinarias(request):
    veterinarias = Veterinaria.objects.all()
    return render(request, 'veterinarias/lista.html', {'veterinarias': veterinarias})

def detalle_veterinaria(request, pk):
    veterinaria = get_object_or_404(Veterinaria, pk=pk)
    return render(request, 'veterinarias/detalle.html', {'veterinaria': veterinaria})

def crear_veterinaria(request):
    if request.method == 'POST':
        form = VeterinariaForm(request.POST)
        if form.is_valid():
            veterinaria = form.save()

            # Recibe múltiples horarios
            dias = request.POST.getlist('dia')
            aperturas = request.POST.getlist('hora_apertura')
            cierres = request.POST.getlist('hora_cierre')

            for i in range(len(dias)):
                if dias[i] and aperturas[i] and cierres[i]:
                    HorarioAtencion.objects.create(
                        veterinaria=veterinaria,
                        dia=dias[i],
                        hora_apertura=aperturas[i],
                        hora_cierre=cierres[i]
                    )

            return redirect('home')  # Redirige donde tú quieras
    else:
        form = VeterinariaForm()
    return render(request, 'veterinarias/formulario.html', {'form': form})



def editar_veterinaria(request, pk):
    veterinaria = get_object_or_404(Veterinaria, pk=pk)
    if request.method == 'POST':
        form = VeterinariaForm(request.POST, instance=veterinaria)
        if form.is_valid():
            form.save()
            return redirect('lista_veterinarias')
    else:
        form = VeterinariaForm(instance=veterinaria)
    return render(request, 'veterinarias/formulario.html', {'form': form})

def eliminar_veterinaria(request, pk):
    veterinaria = get_object_or_404(Veterinaria, pk=pk)
    if request.method == 'POST':
        veterinaria.delete()
        return redirect('lista_veterinarias')
    return render(request, 'veterinarias/confirmar_eliminar.html', {'veterinaria': veterinaria})

def lista_veterinarias(request):
    query = request.GET.get('q')
    if query:
        veterinarias = Veterinaria.objects.filter(nombre__icontains=query)
    else:
        veterinarias = Veterinaria.objects.all()
    return render(request, 'veterinarias/lista.html', {'veterinarias': veterinarias, 'query': query})
