from src.eventos import agregar_evento, listar_proximos_eventos

def main():
    while True:
        print("\n1. Agregar evento\n2. Ver eventos\n3. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del evento: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            print(agregar_evento(nombre, fecha))
            
        elif opcion == "2":
            eventos = listar_proximos_eventos()
            for evento in eventos:
                print(f"{evento['nombre']}: {evento['fecha_formateada']} ({evento['dias_restantes']} días restantes)")
                
        elif opcion == "3":
            break

if __name__ == "__main__":
    main()