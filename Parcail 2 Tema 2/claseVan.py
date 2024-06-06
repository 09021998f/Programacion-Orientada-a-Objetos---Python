from claseVehiculo import Vehiculo



class Van(Vehiculo):
    def __init__(self,marca, modelo, año, capacidad, numeroPlazas, distRec, tarifaBase, tipoCar ):
        super().__init__(marca, modelo, año, capacidad, numeroPlazas, distRec, tarifaBase)
        self.__tipoCarroceria= tipoCar
    
    def __str__(self):
        return f'{super().__str__()} Tipo Carroceria: {self.__tipoCarroceria}'
    
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