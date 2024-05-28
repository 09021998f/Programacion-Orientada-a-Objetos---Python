from claseMatricula import Matricula
from claseEmpleado import Empleado
from claseProgramaCap import ProgramaCapacitacion
import csv
class GestorMatricula:
    
    def __init__(self) -> None:
        self.__listaMat = []
        
    def agregarMat(self,mat):
        self.__listaMat.append(mat)
        
    def __str__(self):
        s = ''
        for mat in self.__listaMat:
            s+= str(mat) +'\n'
        return s
    
    def test(self):
        archi = open('Matricula.csv')
        reader = csv.reader(archi, delimiter=',')
        for fila in reader:
            emp = Empleado(fila[1], fila[2], fila[3])
            prog = ProgramaCapacitacion(fila[4], fila[5], fila[6])
            mat = Matricula(fila[0], emp, prog)
            self.agregarMat(mat)
        archi.close()
    
    def punto1(self, id):
        acum = 0
        aux = None
        for i in self.__listaMat:
            emp = i.get_empleado()
            if emp.get_idEmpleado() == id:
                aux = i.get_empleado()
                prog = i.get_programa()
                acum = acum + int(prog.get_duracion())
        if aux != None:
            print(f'Empleado: {aux.get_nombre()}\nDuracion de todos los programas en los que esta matriculado: {acum}min')
        else:
            print('No hay ningun empleado con el id ingresado registrado')
                
            
    
    