from django.shortcuts import get_object_or_404, redirect, render

from .form import CancionForm
from .services import song_service

# Create your views here.
def index(request):
    canciones = song_service.obtener_canciones()
    context = {'canciones': canciones}
    return render(request, 'index.html', context)

def crear_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            song_service.crear_cancion(form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm()
    context = {'form': form, 'accion': 'Crear Canción'}
    return render(request, 'canciones_form.html', context)

def editar_cancion(request, cancion_id):
    cancion = get_object_or_404(song_service.obtener_canciones(), id=cancion_id)
    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            song_service.editar_cancion(cancion_id, form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm(instance=cancion)
    context = {'form': form, 'accion': 'Editar Canción'}
    return render(request, 'canciones_form.html', context)

def eliminar_cancion(request, cancion_id):
    if request.method == 'POST':
        song_service.eliminar_cancion(cancion_id)
    return redirect('index')