from claseGestorClientes import GestorCliente
from claseGestorMovimiento import GestorMovimiento
import sys

def menu():
    op = int(input("1-Punto A\n2-Punto B\n3-Punto C\n4-Mostrar Clientes\n9-Salir\nOpcion >>"))
    if op == 1:
        puntoA()
    elif op == 2:
        puntoB()
    elif op == 3:
        puntoC()
    elif op == 4:
        print(cliente)
    elif op == 9:
        print("programa terminado")
        sys.exit()

def puntoC():
    movimiento.ordenarMovimientos()
    print("Movimientos Ordenados")
    print(movimiento)

def puntoB():
    numTarjeta = input("Ingrese numero de tarjeta >>")
    datosObtenidos = cliente.obtenerDatosPuntoB(numTarjeta)
    movimiento.obtenerMovimientoPuntoB(numTarjeta, datosObtenidos)
        
              

def puntoA():
    dni = input("DNI del cliente >>")
    clienteObtenido = cliente.obtenerDatosPuntoA(dni)
   
    print(f'|CUENTA\n|Apellido y Nombre: {clienteObtenido.get_apellido()}, {clienteObtenido.get_nombre()}                  |Numero Tarjeta: {clienteObtenido.get_numTarjeta()}\n|Saldo Anterior {clienteObtenido.get_saldoAnt()}$\n')
    print('|Fecha   |Descripcion       | Importe | Tipo de movimiento |\n')
    movimiento.obtenerMovimientosPuntoA(clienteObtenido.get_numTarjeta(), int(clienteObtenido.get_saldoAnt()))


if __name__ == '__main__':
    cliente = GestorCliente()
    movimiento = GestorMovimiento(21)
    cliente.test()
    movimiento.test()
    #print(cliente)
    #print(movimiento)    
    
    while True:
        menu()


