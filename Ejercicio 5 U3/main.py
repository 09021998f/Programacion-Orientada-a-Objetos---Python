from controlador import Controlador
from interface import *



def controlador(manejador :IControlador):
    '''Muestra el elemento en una posicion dada'''
    # indice = int(input('Indice:'))
    # elem = manejador.mostrarElemento(indice)
    '''Inserta un elemento en la posicion dada'''
    # pos = int(input('Ingrese posicion en la que desea agregar: '))
    # elemento = int(input('Elemento: '))
    # elem = manejador.insertarElemento(pos, elemento)
    '''Agregar elemento al final de la lista'''
    elem = int(input('Elemento: '))
    c = manejador.agregarElemento(elem)

if __name__ == '__main__':
    c = Controlador()
    c.agregarElementos()
    c.mostrarLista()
    print('*******')
    # c.mostrarElemento(5)
    controlador(IControlador(c))
    c.mostrarLista()