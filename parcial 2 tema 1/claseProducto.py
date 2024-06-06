class Producto:
    def __init__(self, nom, fechaEnv, fechaVen, temp, pais, lote, costoBase):
        self.__nomProducto = nom
        self.__fechaEnvasado = fechaEnv
        self.__fechaVencimiento = fechaVen
        self.__temperatura = temp
        self.__pais = pais
        self.__numLote = lote
        self.__costoBase = costoBase
        
    def __str__(self):
        return f'Nombre: {self.__nomProducto}| Fecha envasado: {self.__fechaEnvasado}| Fecha vencimiento: {self.__fechaVencimiento}| Temperatura: {self.__temperatura}| Pais: {self.__pais}| Lote: {self.__numLote}| Costo base: {self.__costoBase}'

    def get_costoBase(self):
        return self.__costoBase
    
    def get_fechaVen(self):
        return self.__fechaVencimiento

    def calcularTarifa(self):
        pass
    
    def mostrarPunto4(self):
        return f'|Nombre:{self.__nomProducto}\n|Pais de origen: {self.__pais}\n|Temperatura:{self.__temperatura}\n|Importe:{self.calcularTarifa()}\n'
              