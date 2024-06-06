from claseCongelados import Congelados
from claseRefrigerados import Refrigerado
import csv
import datetime

class Gestor:
    def __init__(self):
        self.__listaProd = []
        
    def agregarProducto(self, producto):
        self.__listaProd.append(producto)
        
    def cargarDatos(self):
        archi = open('productos.csv', encoding='utf-8')
        reader = csv.reader(archi, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                if fila[0] == 'C':
                    self.agregarProducto(Congelados(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12]))
                elif fila[0] == 'R':
                    self.agregarProducto(Refrigerado(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8]))
        archi.close
    
    def insertarProductos(self, tipo):
        if tipo == '1':
            nom = input('Nombre:')
            fechaEnv = input('Fecha envasado:')
            fechaVen = input('Fecha Vencimiento:')
            temp = input('Temperatura')
            pais = input('Pais: ')
            lote = input('Lote: ')
            costoBase = input('Costo base: ')
            nitro = input('Nitrogeno: ')
            oxigeno = input('Oxigeno: ')
            dioxCarbono = input('Dioxido de carbono: ')
            vaporAgua = input('Vapor de agua: ')
            met = input('Metodo de congelado: ')
            self.agregarProducto(Congelados(nom,fechaEnv,fechaVen,temp,pais,lote,costoBase,nitro,oxigeno, dioxCarbono,vaporAgua,met))
        elif tipo == '2':
            nom = input('Nombre:')
            fechaEnv = input('Fecha envasado:')
            fechaVen = input('Fecha Vencimiento:')
            temp = input('Temperatura')
            pais = input('Pais: ')
            lote = input('Lote: ')
            costoBase = input('Costo base: ')
            cod = input('Codigo de supervision:')
            self.agregarProducto(Refrigerado(nom,fechaEnv,fechaVen,temp,pais,lote,costoBase,cod))
        else:
            print('Opcion no valida')
        
        
    def tipoProducto(self, indice):
        if isinstance(self.__listaProd[indice -1], Refrigerado):
            print('El tipo de producto es Refrigerado')
        else:
            print('El tipo de producto es Congelado')
            
    def mostrarCantTipoProd(self):
        cantCon = 0
        cantRef = 0
        for prod in self.__listaProd:
            if isinstance(prod, Refrigerado):
                cantRef += 1
            else:
                cantCon += 1
        print('La cantidad de productos congelados es: ', cantCon)
        print('La cantidad de productos refrigerados es: ', cantRef)
        
    def ultimoLista(self):
        print(self.__listaProd[- 1])
    
    def mostrarTodosLosProd(self):
        for prod in self.__listaProd:
            print(prod.mostrarPunto4())
    
    def __str__(self):
        cadena = ''
        for prod in self.__listaProd:
            cadena += str(prod) + '\n'
        return cadena