from claseProducto import Producto
from datetime import datetime
class Refrigerado(Producto):
    def __init__(self, nom, fechaEnv, fechaVen, temp, pais, lote, costoBase, cod):
        super().__init__(nom, fechaEnv, fechaVen, temp,pais,lote, costoBase)
        self.__codSupervision = cod
        
    def __str__(self):
        return super().__str__() + " Codigo de supervision: " + str(self.__codSupervision) 
    
    def calcularTarifa(self):
        costoBase = float(super().get_costoBase())
        fechaVen = datetime.strptime(super().get_fechaVen(), '%d/%m/%Y')
        fecha_actual = datetime.now()
        
        if fechaVen.month - fecha_actual.month >= 2:   
            descuento = costoBase * 0.10
            importe_final = costoBase - descuento
            return importe_final
        else:
            aumento = costoBase * 0.01
            importe_final = costoBase + aumento
            return importe_final