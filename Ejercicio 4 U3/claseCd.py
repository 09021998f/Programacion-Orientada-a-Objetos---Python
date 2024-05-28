from clasePubli import Publicacion

class Cd(Publicacion):
    
    def __init__(self, titulo, categ, pre, tiempo, nombre) -> None:
        super().__init__(titulo, categ, pre)
        self.__tiempo = tiempo
        self.__narrador = nombre
        
    def __str__(self) -> str:
        return f'{super().__str__()}Tiempo: {self.__tiempo} |Narrador: {self.__narrador}|'

    
    def get_pub(self):
        return f'{super().__str__()}'