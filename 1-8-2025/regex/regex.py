import re

patron = "H.la"

texto = "H0la, ¿cómo estás? Hola, ¿qué tal? hnla, HOLA hola"

# resultado = re.findall(patron, texto)
# print(resultado)  # Muestra el objeto de coincidencia

resultados = re.finditer(patron, texto, re.IGNORECASE)

for match in resultados:
  print(match.group(), match.start(), match.end())