from claseVan import Van
from classAutobus import Autobus
import csv
class Gestor:
    def __init__(self) -> None:
        self.__listaVehiculos = []
    
    def agregarVehiculo(self, vehiculo):
        self.__listaVehiculos.append(vehiculo)
    
    def cargarDatos(self):
        archi = open('vehiculos.csv', encoding='utf-8')
        reader = csv.reader(archi, delimiter=';')
        band  = True
       
        for fila in reader:
            
            if band:
                band = not band
            else:
                if fila[0] == 'A':
                    self.agregarVehiculo(Autobus(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9]))
                elif fila[0] == 'V':
                    self.agregarVehiculo(Van(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7],fila[8]))
        archi.close()
    
    def __str__(self):
        cadena = ''
        for vehiculo in self.__listaVehiculos:
            cadena += str(vehiculo) + '\n'
        return cadena
    
    def insertarVehiculo(self):
        tipoVehiculo = input('Que vehiculo desea agregar (A: Autobus / V: Van)')
        if tipoVehiculo == 'a' or 'A':
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            año = input('Año de Fabricacion: ')
            capacidad = input('Capacidad de Pasajeros: ')
            numeroPlazas = input('Numero de Plazas: ')
            distRec = input('Distancia Recorrida: ')
            tarifaBase = input('Tarifa Base: ')
            tipo = input('Tipo de servicio: ')
            turno = input('Turno: ')
            self.agregarVehiculo(Autobus(marca,modelo,año,capacidad,numeroPlazas,distRec,tarifaBase,tipo,turno))
        elif tipoVehiculo == 'v' or 'V':
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            año = input('Año de Fabricacion: ')
            capacidad = input('Capacidad de Pasajeros: ')
            numeroPlazas = input('Numero de Plazas: ')
            distRec = input('Distancia Recorrida: ')
            tarifaBase = input('Tarifa Base: ')
            tipoCarroceria = input('Tipo de Carroceria: ')
            self.agregarVehiculo(Van(marca, modelo, año, capacidad, numeroPlazas, distRec, tarifaBase, tipoCarroceria))
        
    def mostrarTipo(self, indice):
        if isinstance(self.__listaVehiculos[int(indice)],Van):
            print('Es de tipo van')
        else:
            print('Es de tipo Autobus')
    
    def mostrarCantidad(self):
        contVan = 0
        contAutobus = 0
        for v in self.__listaVehiculos:
            if isinstance(v, Van):
                contVan += 1
            else:
                contAutobus += 1
        print(f'Van: {contVan} Autobus: {contAutobus}')
        
    def punto4(self):
        for v in self.__listaVehiculos:
            print(f'Modelo: {v.get_modelo()} |Año Fabricacion: {v.get_añoFabricacion()} |Capacidad {v.get_capPasajeros()} |Tarifa: {v.get_tarifa()}' )