from clasePubli import Publicacion
class Libro(Publicacion):
    def __init__(self, tit, categ, precio, nomAut, fechaEdi, cantPag) -> None:
        super().__init__(tit, categ, precio)
        
        self.__nombreAutor = nomAut
        self.__fechaEdicion = fechaEdi
        self.__cantPaginas = cantPag
        
    def __str__(self):
        return f'{super().__str__()}Nombre: {self.__nombreAutor} |Fecha de Edicion: {self.__fechaEdicion} |Cantidad de paginas: {self.__cantPaginas}|'
    
    def get_pub(self):
        return f'{super().__str__()}'