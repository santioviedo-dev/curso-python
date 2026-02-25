from empresa import Empresa
from empleado import Empleado


if __name__ == "__main__":
    empresa = Empresa("Santec")
    print(empresa.empleados)
    empresa.contratar_empleado("Santiago", "Informática")
    empresa.contratar_empleado("Federico", "Contabilidad")
    
    
    dpto_informatica = empresa.obtener_empleados_por_dpto("Informática") 
    for empleado in dpto_informatica:
        print(f"{empleado.nombre} de informatica")
    dpto_contabilidad = empresa.obtener_empleados_por_dpto("Contabilidad") 
    for empleado in dpto_contabilidad:
        print(f"{empleado.nombre} de contabilidad")
    # print(empresa.obtener_empleados_por_dpto("Contabilidad"))
    # print(empresa.obtener_empleados_por_dpto("Finanzas"))
