class Nodo:
    def __init__(self, dato):
        self.__prod = dato
        self.__siguiente = None
        
    
    def set_siguiente(self, sig):
        self.__siguiente = sig
    
    def get_siguiente(self):
        return self.__siguiente

    def get_dato(self):
        return self.__prod 
        