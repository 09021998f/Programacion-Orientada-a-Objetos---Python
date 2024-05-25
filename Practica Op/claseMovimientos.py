class Movimiento:

    def __init__(self, nTarjeta, fecha, desc, tMov, imp):
        self.__numTarjeta = nTarjeta
        self.__fecha = fecha
        self.__descripcion = desc
        self.__tipoMov = tMov
        self.__importe = imp


    def __str__ (self):
        return f'|Numero Tarjeta: {self.__numTarjeta} |Fecha {self.__fecha} |Descripcion: {self.__descripcion} |Tipo Movimiento: {self.__tipoMov} |Importe: {self.__importe}'
    
    def get_numTarjeta(self):
        return self.__numTarjeta
    
    def get_fecha(self):
        return self.__fecha
    
    def get_descripcion(self):
        return self.__descripcion

    def get_tipoMov(self):
        return self.__tipoMov
    
    def get_importe(self):
        return self.__importe
    
    def __lt__(self, otro):
        return self.__numTarjeta < otro.__numTarjeta