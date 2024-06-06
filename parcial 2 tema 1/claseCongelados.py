from claseProducto import Producto
from datetime import datetime
class Congelados(Producto):
    def __init__(self, nom, fechaEnv, fechaVen, temp, pais, lote, costoBase, nitro, oxigeno, dioxCarbono, vaporAgua, met):
        super().__init__(nom, fechaEnv, fechaVen, temp, pais, lote, costoBase)
        self.__nitrogeno = nitro
        self.__oxigeno = oxigeno
        self.__dioxCarbono = dioxCarbono
        self.__vaporAgua = vaporAgua
        self.__metodoCongelacion = met	
    
    def __str__(self):
        return f'{super().__str__()}| Nitrogeno: {self.__nitrogeno}% | Oxigeno:{self.__oxigeno}% |Dioxido de carbono: {self.__dioxCarbono}% |Vapor de agua: {self.__vaporAgua}% |Met. Congelacion {self.__metodoCongelacion}'
    def calcularTarifa(self):
        costoBase = float(super().get_costoBase())
        
        
        if self.__metodoCongelacion == 'mecanico':   
            aumento = costoBase * 0.15
            importe_final = costoBase + aumento
            return importe_final
        else:
            aumento = costoBase * 0.15
            importe_final = costoBase + aumento
            return importe_final