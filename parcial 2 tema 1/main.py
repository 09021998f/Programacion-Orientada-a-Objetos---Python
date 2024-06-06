from gestorProductos import *
import sys
from datetime import datetime

def menu():
    op = input('1- Agregar Producto\n2-Mostrar tipo de producto\n3-Mostrar cantidad de tipos de productos\n9-Salir\n >>>')
    if op == '1':
        tipo = input('Agregar Producto\n1-Congelado\n2-Refrigerado\n>>>')
        manejador.insertarProductos(tipo)
        manejador.ultimoLista()

    elif op == '2':
        indice = int(input('Ingrese indice: '))
        manejador.tipoProducto(indice)

    elif op == '3':
        manejador.mostrarCantTipoProd()
    elif op == '4':
        manejador.mostrarTodosLosProd()
    elif op == '9':
        print('Programa Terminado')
        sys.exit()
        
    
        

if __name__ == '__main__':
    manejador = Gestor()
    manejador.cargarDatos()

    while True:
        menu()