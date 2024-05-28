from claseNodo import Nodo
from claseLibro import Libro
from claseCd import Cd
import csv
class Lista:
    __indice :int
    __tope :int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice +=1
            dato = self.__actual.getPublicacion()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def agregarPublicacion(self, publi):
        pub = Nodo(publi)
        pub.setSiguiente(self.__comienzo)
        self.__comienzo = pub
        self.__actual = pub
        self.__tope += 1
    
    
    def mostrarPublicaciones(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getPublicacion())
            aux = aux.getSiguiente()

    def mostrarLibros(self):
        aux = self.__comienzo
        
        while aux != None:
            clase = aux.getPublicacion()
            if isinstance(clase, Libro):
                print(aux.getPublicacion())
            aux = aux.getSiguiente()
    
    def obtenerActual(self):
        return self.__actual

    def obtenerComienzo(self):
        return self.__comienzo
    
    def mostrarPorIndice(self, indice):
        i = 0
        aux = self.__comienzo   
        while aux != None and i < indice:
            i += 1
            aux = aux.getSiguiente()
        if i == indice and aux != None:
            return aux.getPublicacion()
                
                    
    
    def cantTipoPub(self):
        aux  = self.__comienzo
        contLibro = 0
        contCd = 0
        while aux != None:
            clase = aux.getPublicacion()
            if isinstance(clase, Libro):
                contLibro += 1
            elif isinstance(clase, Cd):
                contCd += 1
            aux = aux.getSiguiente()
        print(f'Cantidad de Libros: {contLibro}\nCantidad de CD: {contCd}')
            
    def mostrarPunto4(self):
        aux = self.__comienzo
        
        while aux != None:
            pub = aux.getPublicacion()
            print(f'{pub.get_pub()}')
            aux = aux.getSiguiente()