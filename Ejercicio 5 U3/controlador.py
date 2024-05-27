from claseLista import Lista
from interface import *
from zope.interface import implementer
@implementer(IControlador)
class Controlador:
    
    def __init__(self):
        self.__lista = Lista()
    
    
    def agregarElementos(self):
        for i in range(10):
            self.__lista.agregarObjeto(i)
         
    def mostrarLista(self):
        for dato in self.__lista:
            print(dato)
    
    def insertarElemento(self, pos, elem):
        self.__lista.insertarElemento(pos-1, elem)
        
    def agregarElemento(self, elem):
        self.__lista.agregarElemento(elem)
    
    def mostrarElemento(self, indice):
        self.__lista.mostarObjeto(indice-1)
                 
    def mostarTope(self):
        return self.__lista.get_tope()    
            
            
            
        