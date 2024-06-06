import abc
from abc import ABC

class Vehiculo:
    def __init__(self,marca, modelo, año, capacidad, numeroPlazas, distRec, tarifaBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__añoFabricacion = año
        self.__capPasajeros = capacidad
        self.__numPlazas = numeroPlazas
        self.__distRec = distRec
        self.__tarifaBase = tarifaBase

    def __str__(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año de Fabricación: {self.__añoFabricacion}, Capacidad de Pasajeros: {self.__capPasajeros}, Número de Plazas: {self.__numPlazas}, Distancia Recorrida: {self.__distRec}, Tarifa Base: {self.__tarifaBase}"


    def calcular_tarifa(self):
        pass
    
    def get_info(self):
        print()
    
    def get_modelo(self):
        return self.__modelo
    
    def get_añoFabricacion(self):
        return self.__añoFabricacion
    
    def get_capPasajeros(self):
        return self.__capPasajeros
    
    def get_tarifa(self):
        return self.__tarifaBase