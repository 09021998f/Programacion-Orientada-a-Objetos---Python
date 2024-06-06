from claseVehiculo import Vehiculo
class Autobus(Vehiculo):

    def __init__(self,marca, mod, año, cap, num , dis ,taf ,tipo, turno):
        super().__init__(marca, mod, año, cap, num, dis, taf)
        self.__tipo = tipo
        self.__turno = turno

    def __str__(self):
        return f'{super().__str__()} Tipo: {self.__tipo} Turno: {self.__turno}'
    
    def get_modelo(self):
        return super().get_modelo()
    
    def get_marca(self):
        return super().get_marca()
    
    def get_año(self):
        return super().get_año()
    
    def get_capacidad(self):
        return super().get_capacidad()
    
    def get_tarifa(self):
        return super().get_tarifa()
    
