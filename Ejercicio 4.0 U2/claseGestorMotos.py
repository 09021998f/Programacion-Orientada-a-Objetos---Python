from ClaseMoto import Moto
import csv

class GestorMoto:
    def __init__(self) -> None:
        self.__listaMotos = []
        
    def agregarMoto(self, moto):
        self.__listaMotos.append(moto)
    #instancio Objetos de la clase Moto    
    def testMoto(self):
        archi = open("datosMotos.csv")
        reader = csv.reader(archi, delimiter=",")
        for fila in reader:
            pat = fila[0]
            marca = fila[1]
            nom = fila[2]
            ap = fila[3]
            km = fila[4]
            unaMoto = Moto(pat, marca, nom, ap, km) #instancia
            self.agregarMoto(unaMoto)
        archi.close()
        
    def buscarMoto(self, pat):
        i=0
        while i < len(self.__listaMotos) and self.__listaMotos[i].getPatente() != pat: #busca la patante si esta en la lista
            i += 1                                                                     #que contiene los objetos de la clase Moto
        
        if i < len(self.__listaMotos) and self.__listaMotos[i].getPatente() == pat : #si la encuentra devuelve True sino no devuelve nada tambien verifica si llego al final de la lista sin encontrar la patente
            return True
    
    def obtenerPatentes(self): #de vuelve una lista con todas las patentes
        listaPatantes = []
        for i in range(len(self.__listaMotos)):
            listaPatantes.append(self.__listaMotos[i].getPatente())
        return listaPatantes    

    def obtenerDatosNecarios(self, pat):# pat son las patente que busco para devolver los datos 
        i = 0
        while i < len(self.__listaMotos):
            
            if self.__listaMotos[i].getPatente() == pat:
                print(f'|Patente: {self.__listaMotos[i].getPatente()}\n|Nombre: {self.__listaMotos[i].getNombre()}, {self.__listaMotos[i].getApellido()}')
            i+=1            #muestro en pantalla los datos q coincidan con pat
    
    def __str__(self):
        s = ""
        for moto in self.__listaMotos:
            s += str(moto) + "\n"
        return s