from claseProgramaCap import ProgramaCapacitacion
import csv

class GestorProg:
    def __init__(self) -> None:
        self.__listaProg = []
        
    def agregarProg(self,prog):
        self.__listaProg.append(prog)
        
    def __str__(self):
        s = ''
        for prog in self.__listaProg:
            s+= str(prog) +'\n'
        return s
    
    def test(self):
        archi = open('Programas.csv')
        reader = csv.reader(archi, delimiter=',')
        for fila in reader:
            prog = ProgramaCapacitacion(fila[0],fila[1],fila[2])
            self.agregarProg(prog)
        archi.close()
        
    