from claseCalefactor import Calefactor


class Gas(Calefactor):
    def __init__(self, marc, mod, pais, precio, formaPago, cuotas, prom, matricula, calorias):
        super().__init__(marc, mod, pais, precio, formaPago, cuotas, prom)
        self.__matricula = matricula
        self.__calorias = calorias
    
    def __str__(self):
        return f'{super().__str__()}|Matricula: {self.__matricula} |Calorias: {self.__calorias}'

    def get_precio(self):
        return super().get_precio()
    
    def get_marca(self):
        return super().get_marca()
    
    def get_modelo(self):
        return super().get_modelo()
    
    def get_promocion(self):
        return super().get_promocion()
    
    def get_formaDePago(self):
        return super().get_formaDePago()

    def get_calorias(self):
        return self.__calorias
    
    def get_cuotas(self):
        return super().get_cuotas()
    
    def toJson(self):
        d = dict(
                     tipo = self.__class__.__name__,
                     marca = self.get_marca(),
                     modelo = self.get_modelo(),
                     pais_de_fabricacion = self.get_paisDeFabricacion(),
                     precio_de_lista = self.get_precio(),
                     forma_de_pago = self.get_formaDePago(),
                     cant_cuotas = self.get_cuotas(),
                     promocion = self.get_promocion(),
                     matricula=self.__matricula,
                     calorias = self.__calorias
                     
                 )
        return d