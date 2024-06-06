from claseGestorV import Gestor
import sys
def menu():
    op = int(input('1-Agregar Vehiculo\n2-punto 2\n3-punto 3\n4-punto 4\n9-Salir\n>>>'))
    if op == 1:
        gestor.insertarVehiculo()
        print(gestor)
    elif op == 2:
        i = input('Indice: ')
        gestor.mostrarTipo(i)
    elif op == 3:
        gestor.mostrarCantidad()
    elif op == 4:
        gestor.punto4()
    elif op == 9:
        sys.exit(0)

if __name__ == '__main__':
    gestor = Gestor()
    gestor.cargarDatos()
    while True:
        menu()
    