import os
from pelicula import Pelicula

class ServicioPeliculas:
    NOMBRE_ARCHIVO = "peliculas.txt"
    
    def __init__(self):
        self._peliculas = []
        
        if not os.path.isfile(self.NOMBRE_ARCHIVO):
            with open(self.NOMBRE_ARCHIVO, "w") as archivo:
                peliculas_base = ["Toy Story", "Monsters Inc.", "Cars 2"]
                archivo.writelines(pelicula + "\n" for pelicula in peliculas_base)
                self._peliculas.extend(Pelicula(pelicula) for pelicula in peliculas_base)
        else: 
            with open(self.NOMBRE_ARCHIVO, "r") as archivo:
                peliculas = [Pelicula(linea.strip()) for linea in archivo]
                self._peliculas.extend(peliculas)
    
    def agregar_pelicula(self, nombre):
        try:
            with open(self.NOMBRE_ARCHIVO, "a+") as archivo:
                if nombre.strip() in [linea.strip() for linea in archivo.readlines()]:
                    raise Exception("La película ya está agregada.")
                archivo.write(nombre.strip() + "\n")
                self._peliculas.append(Pelicula(nombre))
        except Exception as e:
            print(f"error al agregar película: {e}") 
    
    def listar_peliculas(self):
        return self._peliculas

    def eliminar_peliculas(self):
        try:
            os.remove(self.NOMBRE_ARCHIVO)
        except Exception as e:
            print(f"Error al eliminar peliculas: {e}")
        else:
            print("Peliculas eliminadas correctamente.")