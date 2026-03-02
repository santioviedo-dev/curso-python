class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, value):
        self._apellido = value
    @property
    def membresia(self):
        return self._membresia
    @membresia.setter
    def membresia(self, value):
        self._membresia = value
    

    def __str__(self):
        return f"Cliente(id={self._id}, nombre={self._nombre}, apellido={self._apellido}, membresia={self._membresia})"