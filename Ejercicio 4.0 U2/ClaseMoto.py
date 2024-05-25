class Moto:
    
    def __init__(self,pat,marca,nom,ap,km):
        self.__patente = pat
        self.__marca = marca
        self.__nombre = nom
        self.__apellido = ap
        self.__kilometraje = km

    def __str__(self):
        return "|Patente:%s|Moto:%s |Nombre:%s |Apellido:%s |Kilometraje:%s " % (self.__patente, self.__marca, self.__nombre, self.__apellido, self.__kilometraje)
    
    def getPatente(self):
        return self.__patente
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
        


    
    
    


