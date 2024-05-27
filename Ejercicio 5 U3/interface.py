from zope.interface import Interface


class IControlador(Interface):

    def mostarElemento(self):
        pass
    
    def insertarElemento(self):
        pass
    
    def agregarElemento(self):
        pass