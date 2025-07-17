from datetime import datetime
from utils.archivos import cargar_eventos, guardar_evento
from src.fechas import formatear_fecha, calcular_dias_restantes

def agregar_evento(nombre: str, fecha_str: str) -> str:
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        if fecha < datetime.now().date():
            return "¡La fecha debe ser futura!"
        
        guardar_evento(nombre, fecha_str)
        return "Evento registrado ✅"
    
    except ValueError:
        return "Formato inválido. Usa YYYY-MM-DD."

def listar_proximos_eventos() -> list:
    eventos = cargar_eventos()
    hoy = datetime.now().date()
    
    eventos_futuros = []
    for nombre, fecha_str in eventos:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        if fecha >= hoy:
            dias_restantes = calcular_dias_restantes(fecha)
            eventos_futuros.append({
                "nombre": nombre,
                "fecha_formateada": formatear_fecha(fecha),
                "dias_restantes": dias_restantes
            })
    
    return sorted(eventos_futuros, key=lambda x: x["dias_restantes"])