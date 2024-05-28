class Empleado:
    
    def __init__(self,nya,idEmp,puesto):
        self.__nombreYapellido = nya
        self.__idEmpleado = idEmp
        self.__puesto = puesto
        
    def __str__(self):
        return f'|Nombre:{self.__nombreYapellido} |Id Empleado: {self.__idEmpleado} |Puesto: {self.__puesto}'
    
    def get_nombre(self):
        return self.__nombreYapellido
    
    def get_idEmpleado(self):
        return self.__idEmpleado
    
    def get_puesto(self):
        return self.__puesto
    
    