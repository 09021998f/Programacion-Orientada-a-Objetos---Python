import numpy as np
from claseMovimientos import Movimiento
import csv

class GestorMovimiento:
    def __init__(self, dimension):
        self.__arregloMov = np.empty(dimension, dtype = Movimiento )
        self.__dimension = dimension
        self.__cantidad = 0

    def agregarMov(self, mov):
        self.__arregloMov[self.__cantidad] = mov
        self.__cantidad +=1

    def test(self):
        archi = open('MovimientosAbril2024.csv')
        reader = csv.reader(archi, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                mov = Movimiento(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarMov(mov)

    def __str__(self):
        s = ""
        for mov in self.__arregloMov:
            s += str(mov) + "\n"
        return s


    def obtenerMovimientosPuntoA(self, numTarjeta, saldoAnt):
        
        for i in self.__arregloMov:
            if i.get_numTarjeta() == numTarjeta:
                print(f'{i.get_fecha()}   {i.get_descripcion()}       {i.get_importe()}$      {i.get_tipoMov()}')
                if i.get_tipoMov() == 'C':
                    saldoAnt += int(i.get_importe())
                    
                elif i.get_tipoMov() == 'P':
                    saldoAnt -= int(i.get_importe())
                    
        print(f"Saldo Actualizado: {saldoAnt}$")

    def obtenerMovimientoPuntoB(self, numTarj, cliente):
        i = 0
        while i < len(self.__arregloMov) and self.__arregloMov[i].get_numTarjeta() != numTarj:
            i += 1
        
        if i< len(self.__arregloMov) and self.__arregloMov[i].get_numTarjeta() == numTarj:
           print("Se encontro Movientos")
        else:
            print(f'Nombre: {cliente[0]} Apellido: {cliente[1]}')
            

    def ordenarMovimientos(self):
        self.__arregloMov.sort()
        

    