class Pedido:

    def __init__(self, pat, idPedido, comida, tee, precio):
        self.__patente = pat
        self.__idPedido = idPedido
        self.__comida = comida
        self.__tiempoEstEntrega = tee
        self.__tiempoRealEntrega = 0
        self.__precio = precio
        
    def __str__(self):
        return "|Patente: %s |id Pedido:%s |Comida: %s |TEE: %s |TRE: %s |Precio: %s" % (self.__patente, self.__idPedido, self.__comida, self.__tiempoEstEntrega, self.__tiempoRealEntrega, self.__precio)
    
    def getPatente(self):
        return self.__patente
    
    def setTRE(self, tre ):
        self.__tiempoRealEntrega = tre

    def getIdPedido(self):
        return self.__idPedido
    
    def getTEE(self):
        return self.__tiempoEstEntrega
    
    def getPrecio(self):
        return self.__precio
    
    def getTRE(self):
        return self.__tiempoRealEntrega
    
    def __lt__(self, otro):
        return self.__patente < otro.__patente
  