from claseNodo import Nodo

class Lista:
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def agregarCalefactores(self, calefa):
        nodo = Nodo(calefa)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
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
            dato = self.__actual.get_calefactor()
            self.__actual = self.__actual.get_siguiente()
            return dato
    
    def get_tope(self):
        return self.__tope
    
    def insertarElemento1(self, calefa, pos):
        i = 0
        aux = self.__comienzo
        nodo = Nodo(calefa)
        while aux != None:
            if pos == 0 and aux != None:
                nodo.set_siguiente(aux.get_siguiente())
                aux.set_siguiente(nodo)
            elif pos == i and aux != None:
                nodo.set_siguiente(aux.get_siguiente())
                aux.set_siguiente(nodo)
            i += 1
            aux=aux.get_siguiente()
        self.__tope += 1
        
    def tipoObjeto(self,pos):
        i = 0
        aux = self.__comienzo
        while aux != None:
            if pos == 0 and aux != None:
                return aux.get_calefactor()
            else:
                if pos == i and aux != None:
                    return aux.get_calefactor()
            i += 1
            aux = aux.get_siguiente()   
            
        
        
        