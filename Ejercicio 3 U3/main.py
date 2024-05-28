from claseGestorEmpleado import GestorEmp
from claseGestorMat import GestorMatricula
from claseGestorProg import GestorProg
import sys

def menu():
    op = int(input('1-Mostrar Objetos\n2-Punto 1\n>>'))
    if op == 1:
        print(f'EMPLEADOS\n{gEmpleado}\nPROGRAMAS\n{gPrograma}\nMATRICULAS\n{gMatricula}')
    elif op == 2:
        punto1()
    elif op == 9:
        sys.exit()

def punto1():
    id = input('Ingrese Id del Empleado >>>')
    emp = gEmpleado.punto1(id)

    if emp == True:
        gMatricula.punto1(id)
    elif emp == False:
        print('Id de empleado no encontrado')

if __name__ == '__main__':
    gEmpleado = GestorEmp()
    gMatricula = GestorMatricula()
    gPrograma = GestorProg()
    gEmpleado.test()
    gMatricula.test()
    gPrograma.test()
    
    
    while True:
        menu()
    
    