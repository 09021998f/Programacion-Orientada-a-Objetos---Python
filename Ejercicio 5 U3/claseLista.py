from claseNodo import Nodo

class Lista:
    
    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0    
    
    def agregarObjeto(self, obj):
        nodo = Nodo(obj)
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
            dato = self.__actual.get_objeto()
            self.__actual = self.__actual.get_siguiente()
            return dato
    
    def get_tope(self):
        return self.__tope
       
    def insertarElemento(self,pos, elem):
        i = 0
        aux = self.__comienzo
        nodo = Nodo(elem)
        if pos > self.__tope:
            raise IndexError(f'La posicion {pos} no se encuentra en la lista')
        elif pos <= self.__tope:
            if self.__comienzo == None or pos == i:
                nodo.set_siguiente(self.__comienzo)
                self.__actual = nodo
                self.__comienzo = nodo
            else:
                while aux != None:
                    if i == pos and aux != None:
                        nodo.set_siguiente(aux.get_siguiente())
                        aux.set_siguiente(nodo)    
                    i += 1
                    aux = aux.get_siguiente()
        self.__tope += 1                    
        

    def agregarElemento(self, elem):
        i = 0
        aux = self.__comienzo
        nodo = Nodo(elem)
        while aux != None:
            if aux.get_siguiente() == None and i < self.__tope:
                nodo.set_siguiente(None)
                aux.set_siguiente(nodo)    
            i += 1
            aux = aux.get_siguiente()    
        self.__tope += 1
    
    
    def mostarObjeto(self, indice):
        i = 0
        aux = self.__comienzo
        if indice > self.__tope:
            raise IndexError('Indice fuera del rango de la lista')
        elif indice <= self.__tope:
            while aux != None:
                if i == indice and aux !=None:
                    print(aux.get_objeto())
                i += 1
                aux = aux.get_siguiente()
            
    