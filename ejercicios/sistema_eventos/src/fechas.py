from datetime import date

def formatear_fecha(fecha: date) -> str:
    # Diccionarios manuales para evitar 'locale'
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    return f"{fecha.day} de {meses[fecha.month - 1]} de {fecha.year}"

def calcular_dias_restantes(fecha: date) -> int:
    return (fecha - date.today()).days