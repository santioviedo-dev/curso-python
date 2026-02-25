import csv



# with open('mi_csv.csv', newline='', encoding="utf-8") as f:
#     lector = csv.reader(f)
#     print(lector)


# with open('mi_csv.csv', newline='', encoding="utf-8") as f:
#     lector = csv.DictReader(f)
#     for fila in lector:
#         print(fila)
#         print(fila['nombre'], fila['edad'])


# datos = [
#     ['Nombre', 'Correo'],
#     ['Santiago', 'asd@gmail.com'],
#     ['Ricardo', 'ricardo@gmail.com'],
# ]

# with open('ejemplo.csv', 'w', newline='', encoding="utf-8") as f:
#     escritor = csv.writer(f)
#     escritor.writerows(datos)


# datos = [
#     {'nombre': 'Santiago', 'apellido': 'Oviedo', 'edad': 22},
#     {'nombre': 'Ricardo', 'apellido': 'Rodriguez', 'edad': 34},
# ]

# with open('ejemplo.csv', 'w', newline='', encoding="utf-8") as f:
#     campos = ['nombre', 'apellido', 'edad']
#     escritor = csv.DictWriter(f, fieldnames=campos, delimiter=',')
#     escritor.writeheader()
#     escritor.writerows(datos)

