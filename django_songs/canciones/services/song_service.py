from canciones.models import Cancion

def obtener_canciones():
    return Cancion.objects.all().order_by('-popularidad', 'titulo')

def crear_cancion(datos):
    Cancion.objects.create(**datos)
    
def editar_cancion(cancion_id, datos):
    cancion = Cancion.objects.get(id=cancion_id)
    for key, value in datos.items():
        setattr(cancion, key, value)
    cancion.save()
    return cancion

def eliminar_cancion(cancion_id):
    cancion = Cancion.objects.get(id=cancion_id)
    cancion.delete()