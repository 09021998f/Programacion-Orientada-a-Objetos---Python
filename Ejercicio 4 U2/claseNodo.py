class Nodo:
    def __init__(self, pub) -> None:
        self.__publicacion = pub
        self.__siguiente = None
    
    def setSiguiente(self, sig):
        self.__siguiente = sig
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getPublicacion(self):
        return self.__publicacion
    
    def getTipo(self):
        return type(self.__publicacion)