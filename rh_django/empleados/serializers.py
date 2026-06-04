from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    idEmpleado = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Empleado
        fields = '__all__'
    
    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value
    def validate_departamento(self, value):
        if not value.strip():
            raise serializers.ValidationError("El departamento no puede estar vacío.")
        return value
    
    def validate_sueldo(self, value):
        if value is None:
            raise serializers.ValidationError("El sueldo es obligatorio.")
        
        if value <= 0:
            raise serializers.ValidationError("El sueldo debe ser un número positivo.")
        return value