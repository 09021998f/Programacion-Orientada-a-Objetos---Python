from claseEmpleado import Empleado
import csv
class GestorEmp:
    def __init__(self):
        self.__listaEmp = []
        
    def agregarEmp(self, emp):
        self.__listaEmp.append(emp)
        
    def __str__(self):
        s = ''
        for emp in self.__listaEmp:
            s += str(emp) + '\n'
        return s
        
    def test(self):
        archi = open('Empleados.csv')
        reader = csv.reader(archi, delimiter=',')
        for fila in reader:
            emp = Empleado(fila[0],fila[1],fila[2])
            self.agregarEmp(emp)
        archi.close()
        
        
    def punto1(self, id):
        i = 0
        while i < len(self.__listaEmp) and self.__listaEmp[i].get_idEmpleado() != id:
            i+=1
            
        if i < len(self.__listaEmp) and self.__listaEmp[i].get_idEmpleado() == id:
            return True
        else:
            return False