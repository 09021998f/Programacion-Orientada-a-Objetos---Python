from claseCliente import Cliente
import csv

class GestorCliente:
    __listaCliente :list

    def __init__(self):
        self.__listaCliente = []

    def agregarCliente(self, cliente):
        self.__listaCliente.append(cliente)

    def test(self):
        archi = open('ClientesAbril2024.csv')
        reader = csv.reader(archi, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else: 
                cliente = Cliente(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarCliente(cliente)
        archi.close 

    def __str__(self):
        s = ""
        for cliente in self.__listaCliente:
            s += str(cliente) + "\n" 
        return s  
        
    def obtenerDatosPuntoA(self, dni):
        i = 0
        while i < len(self.__listaCliente) and self.__listaCliente[i].get_dni() != dni:
            i+=1

        if i < len(self.__listaCliente) and self.__listaCliente[i].get_dni() == dni:
            datosAobtener = self.__listaCliente[i]
        return datosAobtener
    
    def obtenerDatosPuntoB(self, numTarj):
        i = 0
        while i < len(self.__listaCliente) and self.__listaCliente[i].get_numTarjeta() != numTarj:
            i+=1

        if i < len(self.__listaCliente) and self.__listaCliente[i].get_numTarjeta() == numTarj:
            datosObtenidos = [self.__listaCliente[i].get_nombre(), self.__listaCliente[i].get_apellido()]
        return datosObtenidos