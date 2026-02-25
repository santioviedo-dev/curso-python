from libro import Libro
from biblioteca import Biblioteca

if __name__ == "__main__":
    libro1 = Libro("Hábitos Atómicos", "Santiago Oviedo", "Desarrollo personal")
    libro2 = Libro("Administración de sistemas", "Fernando Rivero", "Computación")
    
    biblioteca = Biblioteca("Tras los Pasos")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    
    print("Libros de Santiago Oviedo:")
    for l in biblioteca.buscar_libros_por_autor("Santiago Oviedo"):
        print(l.titulo)
    
    print("Libros de Computación:")
    for l in biblioteca.buscar_libros_por_genero("Computación"):
        print(l.titulo)
    
    print("Todos los libros:")
    for l in biblioteca.mostrar_libros():
        print(f"Libro -> titulo: {l.titulo}, autor: {l.autor}, genero: {l.genero}")
        
    biblioteca.mostrar_libro(libro1)
        
    
    