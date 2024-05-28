class Publicacion:
    def __init__(self, tit, catg, precio) -> None:
        self.__tit = tit
        self.__categ = catg
        self.__precio = precio

    def __str__(self):
        return f'|Titulo: {self.__tit} |Categoria: {self.__categ} |Precio: {self.__precio}|'
        
    def get_titulo(self):
        return self.__tit
    
    

        