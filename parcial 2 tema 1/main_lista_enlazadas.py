from claseLista import *
from claseCongelados import Congelados
from claseRefrigerados import Refrigerado
import csv

def agregarProductos(lista):
    archi = open('productos.csv')
    reader = csv.reader(archi, delimiter=';')
    for fila in reader:
        if fila[0] == 'C':
            lista.agregarProducto(Congelados(fila[1], fila[2], fila[3], fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10], fila[11], fila[12]))
        elif fila[0] == 'R':
            lista.agregarProducto(Refrigerado(fila[1], fila[2], fila[3], fila[4],fila[5],fila[6],fila[7],fila[8]))



if __name__ == '__main__':
    lista_prod = GestorProductos()
    agregarProductos(lista_prod)
    for p in lista_prod:
        print(p)
    