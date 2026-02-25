class Empleado:
    contador_empleados: int = 0
    
    def __init__(self, nombre, departamento):
        Empleado.contador_empleados += 1
        self._nombre = nombre
        self._departamento = departamento
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
    
    @classmethod
    def total_empleados(cls) -> int: 
        return cls.contador_empleados
    
    