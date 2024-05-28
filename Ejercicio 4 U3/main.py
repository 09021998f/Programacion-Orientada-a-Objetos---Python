from claseLista import Lista
from claseLibro import Libro
from clasePubli import Publicacion
from claseCd import Cd
import csv
import sys

def cargarCd():
    archi = open('cd.csv', encoding='utf-8')
    reader = csv.reader(archi, delimiter=';')
    band = True
    for fila in reader:
        if band:
            band = not band
        else:
            cd = Cd(fila[0], fila[1], fila[2], fila[3], fila[4])
            listaPub.agregarPublicacion(cd)

def cargarLibros():
    archi = open('libros.csv', encoding='utf-8')
    reader = csv.reader(archi, delimiter=';')
    band = True
    for fila in reader:
        if band:
            band = not band
        else:
            lib = Libro(fila[0], fila[1], fila[2], fila[3], fila[4],fila[5])
            listaPub.agregarPublicacion(lib)


                
def menu():
    op = int(input("\n****MENU****\n1-Mostrar todas las publicaciones\n2-Agegrar publicacion\n3-Mostrar objeto por el indice\n4-Mostrar cantidad de publicaciones de cada tipo\n5-Mostrar solo publicacion\n9-Salir\n************\n>>>"))
    if op == 1:
        for dato in listaPub:
            print('\n')
            print(dato)
    
    elif op == 2:
        agregarPubliNueva()
    elif op == 3:
        indice = int(input('Indice: '))
        encontrado = listaPub.mostrarPorIndice(indice-1)
        
        if isinstance(encontrado, Libro):
            print('La publicacion es de tipo Libro')
        elif isinstance(encontrado, Cd):
            print('La publicacion es de tipo Cd')
    elif op == 4:
        #listaPub.cantTipoPub()
        contLibro = 0
        contCd = 0
        for pub in listaPub:
            if isinstance(pub, Libro):
                contLibro += 1
            elif isinstance(pub, Cd):
                contCd += 1
        print(f'Cantidad de publiciones\nLibro: {contLibro}\nCD: {contCd}')
    elif op == 5:
        for dato in listaPub:
            print(dato.get_pub())
    elif op == 9:
        print('**********************\n* PROGRAMA TERMINADO *\n**********************')
        sys.exit()    
        
def agregarPubliNueva():
    
    tipo = int(input('Que tipo de publicacion desea agregar?\n1-Libro\n2-CD\n>>>'))
    
    if tipo == 1:
        tit = input('Titulo:')
        categ = input('Categoria:')
        precio = input('Precio:')
        nomAut = input('Nombre del autor:')
        fechaEdi = input('Fecha de edicion')
        cantPag = input('Cantidad de paginas:')
        pub  = Libro(tit,categ,precio,nomAut,fechaEdi,cantPag)
        listaPub.agregarPublicacion(pub)
    elif tipo == 2:
        tit = input('Titulo:')
        categ = input('Categoria:')
        precio = input('Precio:')
        tiempo = input('Tiempo:')
        nombre = input('Narrador:')
        pub = Cd(tit,categ,precio,tiempo, nombre)
        listaPub.agregarPublicacion(pub)
            
if __name__ == '__main__':
    listaPub = Lista()
    lib = Libro
    cargarCd()
    cargarLibros()
    
    # for dato in listaPub:
    #     print(dato.get_pub())
    
    while True:
        menu()
    
    # comienzo = listaPub.obtenerComienzo()
    # print(comienzo.getPublicacion())
    
    # actual = listaPub.obtenerActual()
    # print(actual.getPublicacion())