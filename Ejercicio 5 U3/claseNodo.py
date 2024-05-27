class Nodo:
    __objeto :object
    __siguiente :object
    
    def __init__(self, obj):
        self.__objeto = obj
        self.__siguiente = None
    
    def get_siguiente(self):
        return self.__siguiente
    
    def get_objeto(self):
        return self.__objeto
    
    def set_siguiente(self,sig):
        self.__siguiente = sig