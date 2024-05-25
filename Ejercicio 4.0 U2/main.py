from claseGestorMotos import GestorMoto
from claseGestorPedido import GestorPedido
import sys

def agregarPedido():
    pat = input("Patente\n>> ")              #ingreso la patente cual busca en el gestor de motos si esta la patente
    if moto.buscarMoto(pat) == True:        #ver el metodo en el gestor de motos
        pedido.agregarNuevoPedido(pat) #se ejecuta el metodo agregarNuevoPedido() si devule True el metodo buscarMoto()
    else:
        print("No se encontro moto")
        
def punto4():
    pat = input("Patente >>")
    idPedido = input("Id del Pedido >>")
    pedido.buscarPatenteYidPedido(pat, idPedido)

def punto5():
    pat = input("Patente >>")
    if moto.buscarMoto(pat) == True:
        pedido.obtenerPromedioTRE(pat)
    else:
        print(f"No existe la patente {pat}")
def punto6():
    listaPatentes = moto.obtenerPatentes()#obtengo todas las patentes q estan el el archivo .css y las devuelvo en una lista
    
    for i in range(len(listaPatentes)): #con la lista obtengo los datos de la moto y los datos de los pedidos
        print('************************')
        moto.obtenerDatosNecarios(listaPatentes[i]) #funcion q me da los datos de las motos
        pedido.calcularComisiones(listaPatentes[i]) #funcion q me da los datos de los pedidos
        print('************************')

def punto7():
    pedido.ordenar()
    print("Lista de pedidos ordenada!")
        
def menu():
    print("*********************")
    op = int(input("1-Mostrar datos\n2-Agregar Pedido\n3-Agregar Tiempo real de entrega\n4-Promedio de tiempo real de entrega \n5-Generar listado\n6-Ordenar Pedidos \n7-Salir\nOpcion >> "))
    print("*************************")
    if op == 1:
        print("***************************")
        print(moto)
        print("***************************")
        print(pedido)
        print('****************************')
    elif op == 2:
        agregarPedido()
    elif op == 3:
        punto4()
    elif op == 4:
        punto5()
    elif op ==5:
        punto6()
    elif op == 6:
        punto7()
    elif op == 7:
        print("****Programa Terminado****")
        print("**************************")
        sys.exit()
        
if __name__ == '__main__':
    #inicidaliza los gestores
    #carga los datos del .csv cuando inicia el programa
    moto = GestorMoto()
    pedido = GestorPedido()
    pedido.testPedido()
    moto.testMoto()
    
    while True:
        menu()
    