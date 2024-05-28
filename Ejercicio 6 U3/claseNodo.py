class Nodo:
    def __init__(self,calefa):
        self.__calefactor = calefa
        self.__siguiente = None
        
    def set_siguiente(self, sig):
        self.__siguiente = sig
    
    def get_siguiente(self):
        return self.__siguiente
    
    def get_calefactor(self):
        return self.__calefactor