from servicio_peliculas import ServicioPeliculas

# filepath: d:\dev\curso-python\catalogo_peliculas\app_catalogo_peliculas.py

def main():
    servicio = ServicioPeliculas()
    
    while True:
        print("\n--- Catálogo de Películas ---")
        print("1. Listar películas")
        print("2. Agregar película")
        print("3. Eliminar todas las películas")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            peliculas = servicio.listar_peliculas()
            if peliculas:
                print("\nPelículas en el catálogo:")
                for i, pelicula in enumerate(peliculas, 1):
                    print(f"{i}. {pelicula.nombre}")
            else:
                print("No hay películas en el catálogo.")
        
        elif opcion == "2":
            nombre = input("Ingresa el nombre de la película: ").strip()
            if nombre:
                servicio.agregar_pelicula(nombre)
                print(f"Película '{nombre}' agregada correctamente.")
            else:
                print("El nombre no puede estar vacío.")
        
        elif opcion == "3":
            confirmacion = input("¿Estás seguro de que deseas eliminar todas las películas? (s/n): ").strip().lower()
            if confirmacion == "s":
                servicio.eliminar_peliculas()
                servicio._peliculas.clear()
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()