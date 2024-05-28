class Matricula:
    
    def __init__(self,fecha, emp, progCap) -> None:
        self.__fecha = fecha
        self.__empleado = emp
        self.__programa = progCap
    
    def __str__(self):
        return f'|Fecha: {self.__fecha} |Empleado: {self.__empleado.get_nombre()} |Programa: {self.__programa.get_nombre()}'
        
    def get_empleado(self):
        return self.__empleado
    
    def get_programa(self):
        return self.__programa
    
    def get_fecha(self):
        return self.__fecha
    
    def get_empleado(self):
        return self.__empleado
    
    def get_programa(self):
        return self.__programa
    
    
        
    