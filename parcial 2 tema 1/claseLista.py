from claseNodo import Nodo

class GestorProductos:
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def agregarProducto(self, dato):
        nuevo = Nodo(dato)
        nuevo.set_siguiente(self.__comienzo)
        self.__comienzo = nuevo
        self.__actual = nuevo
        self.__tope += 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return dato
    
    