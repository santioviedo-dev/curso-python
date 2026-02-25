# # import locale
# from datetime import datetime

# # locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# # fecha = datetime.now()
# # fecha_formateada = fecha.strftime("%A, %d de %B de %Y")

# # print(f"Fecha actual: {fecha_formateada}")
# # strptime -> convierte una cadena a un objeto datetime
# # strftime -> convierte un objeto datetime a una cadena formateada

# # meses = {
# #     1: "enero",
# #     2: "febrero",
# #     3: "marzo",
# #     4: "abril",
# #     5: "mayo",
# #     6: "junio",
# #     7: "julio",
# #     8: "agosto",
# #     9: "septiembre",
# #     10: "octubre",
# #     11: "noviembre",
# #     12: "diciembre"
# # }

# # dias = {
# #     0: "domingo",
# #     1: "lunes",
# #     2: "martes",
# #     3: "miércoles",
# #     4: "jueves",
# #     5: "viernes",
# #     6: "sábado"
# # }

# # fecha = datetime.now()
# # nombre_dia = dias[fecha.weekday()]
# # nombre_mes = meses[fecha.month]
# # fecha_formateada = f"{nombre_dia}, {fecha.day} de {nombre_mes} de {fecha.year}"



# from babel.dates import format_date
# import requests

# fecha = datetime.now()
# fecha_formateada = format_date(fecha, "EEEE, d 'de' MMMM 'de' y" , locale='es_ES')

# print(f"Fecha actual: {fecha_formateada}")
