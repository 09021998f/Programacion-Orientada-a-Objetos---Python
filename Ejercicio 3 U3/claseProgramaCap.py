class ProgramaCapacitacion:
    
    def __init__(self,nom,cod,dur) -> None:
        self.__nombre = nom
        self.__codigo = cod
        self.__duracion = dur
        
    def __str__(self) -> str:
        return f'|Nombre: {self.__nombre} |Codigo: {self.__codigo} |Duracion: {self.__duracion}'
    
    
    def get_nombre(self):
        return self.__nombre
    
    def get_codigo(self):
        return self.__codigo
    
    def get_duracion(self):
        return self.__duracion