from empleado import Empleado

class Empresa:
    
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._empleados = []
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def empleados(self):
        return self._empleados
    
    def contratar_empleado(self, nombre, departamento):
        self._empleados.append(Empleado(nombre, departamento))
        
    def obtener_empleados_por_dpto(self, departamento):
        num = [emp for emp in self._empleados if emp.departamento == departamento]
        return num