from libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    def agregar_libro(self, libro: Libro):
        self._libros.append(libro)
    
    def buscar_libros_por_autor(self, autor) -> Libro:
        libros = [l for l in self._libros if l.autor == autor]
        return libros
    
    def buscar_libros_por_genero(self, genero) -> Libro:
        libros = [l for l in self._libros if l.genero == genero]
        return libros
    def mostrar_libros(self):
        return self._libros
    def mostrar_libro(self, libro: Libro):
        return f"Titulo: {libro.titulo}\nAutor: {libro.autor}\nGenero: {libro.genero}"
    