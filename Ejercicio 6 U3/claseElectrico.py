from claseCalefactor import Calefactor


class Electrico(Calefactor):
    def __init__(self, marca, mod, pais, precio, metodo, cuotas, promo,potencia):
        super().__init__(marca,mod,pais,precio,metodo,cuotas,promo)
        self.__potencia = potencia
        
    def __str__(self):
        return f'{super().__str__()}|Potencia:{self.__potencia}'
    
    def get_marca(self):
        return super().get_marca()
    
    def get_modelo(self):
        return super().get_modelo()
    
    def get_precio(self):
        return super().get_precio()
    
    def get_paisDeFabricacion(self):
        return super().get_paisDeFabricacion()
    
    def get_promocion(self):
        return super().get_promocion()
    
    def get_formaDePago(self):
        return super().get_formaDePago()
    
    def get_potencia(self):
        return self.__potencia