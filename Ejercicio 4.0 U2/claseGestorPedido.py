from ClasePedidos import Pedido

import csv

class GestorPedido:
    def __init__(self):
        self.__listaPedido = []
        
    def agregarPedido(self, pedido):
        self.__listaPedido.append(pedido)
    #instacio Objetos de la Clase Pedido    
    def testPedido(self):
        archi = open('datosPedidos.csv')
        reader = csv.reader(archi,delimiter=",")
        for fila in reader:
            pat = fila[0]
            idPedido = fila[1]
            comida = fila[2]
            tee = fila[3]
            precio = fila[4]
            unPedido = Pedido(pat,idPedido, comida, tee, precio)
            self.agregarPedido(unPedido)
    
    def agregarNuevoPedido(self, pat):
        pat = pat
        idPedido = input("Ingrese id >>")
        com = input("Comdia >>")
        tee = input("Tiempo estimado de entrega >>")
        precio = input("Precio >>")   
        unPedido = Pedido(pat,idPedido,com,tee,precio) #Creo un nuevo Objeto de la clase Pedido y la inserto en la lista
        self.agregarPedido(unPedido)
        
    def buscarPatenteYidPedido(self, pat, idPedido):
        i = 0

        while i < len(self.__listaPedido) and self.__listaPedido[i].getIdPedido() != idPedido or self.__listaPedido[i].getPatente() != pat:
            i += 1
        
        if i<len(self.__listaPedido) and self.__listaPedido[i].getPatente() == pat and self.__listaPedido[i].getIdPedido() == idPedido:
            tre = int(input("Tiempo real de entrega: "))
            self.__listaPedido[i].setTRE(tre)
        else:
            print("Patene o Id no existen")

    
    def obtenerPromedioTRE(self, pat):
        acum = 0
        cont = 0
        i=0
        while i< len(self.__listaPedido):
            if self.__listaPedido[i].getPatente() == pat:
                acum += int(self.__listaPedido[i].getTRE())
                cont += 1
            i+=1
        prom = acum // cont
        print('**************************')
        print(f'Promedio de tiempo real de entrega de {pat} es de {prom} minutos')
        print('**************************')
        
    def calcularComisiones(self, pat): 
        i=0
        acum = 0
        porcentaje = 20
        print("||Identificador del pedido || Tiempo estimado || Tiempo Real || Precio ")
        while i < len(self.__listaPedido):
            if self.__listaPedido[i].getPatente() == pat:
                print(f'   {self.__listaPedido[i].getIdPedido()}                                  {self.__listaPedido[i].getTEE()}         {self.__listaPedido[i].getTRE()}           {self.__listaPedido[i].getPrecio()} ')
                acum += int(self.__listaPedido[i].getPrecio())
            i+=1        #muestro en pantalla los datos q coincidan con pat   falta hacer el calculo de la comicion y el total del precio 
        print(f"|Total: {acum}$")
        comision = (porcentaje / 100) * acum
        print(f"|Comision: {comision}$")
    
    def ordenar(self):
        self.__listaPedido.sort()   
                
    def __str__(self):
        s = ""
        for pedido in self.__listaPedido:
            s += str(pedido) + "\n"
        return s