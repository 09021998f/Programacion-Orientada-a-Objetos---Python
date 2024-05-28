class Calefactor:
    def __init__(self, marc, mod, pais, precio, formaPago, cuotas, prom):
        self.__marca = marc
        self.__modelo = mod
        self.__paisDeFabricacion = pais
        self.__precio = precio
        self.__formaDePago = formaPago
        self.__promocion = prom
        self.__cuotas = cuotas
        
        
    def __str__(self):
       
        return f'|Marca:{self.__marca} |Modelo:{self.__modelo}|Pais: {self.__paisDeFabricacion} |Precio: {self.__precio}|Metodo de pago: {self.__formaDePago}|Cuotas: {self.__cuotas}|Promocion:{self.__promocion}'
       
    def get_precio(self):
        return self.__precio
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_paisDeFabricacion(self):
        return self.__paisDeFabricacion
    
    def get_promocion(self):
        return self.__promocion
    
    def get_formaDePago(self):
        return self.__formaDePago
    
    def get_cuotas(self):
        return self.__cuotas
        