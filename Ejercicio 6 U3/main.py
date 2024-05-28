from claseManejador import Manejador
from claseInterface import ICalefactor
import sys

    

def Menu(maneja: ICalefactor):
    op = input('1-Mostrar calefactores\n2-Insertar un calefactor\n3-Agregar calefactor a la coleccion\n4-Mostrar tipo de objeto q se encuentra en una posicion\n5-Mostrar calefactor a gas a menor precio\n6-Mostrar calefactores por una marca\n7-Mostrar calefactores en promocion\n8-Cargar coleccion en json\n9-Salir\n>>>')
    if op == '1':
        print(m)
        
    elif op == '2':
        maneja.insertarCalefactor()        
    
    elif op == '3':
        maneja.agregarAlaColeccion()
    
    elif op == '4':
        maneja.mostrarTipoObj()
    
    elif op == '5':
        m.mostrarCalefGasMenorPrecio()
        
    elif op == '6':
        m.mostrarCalefElectrico()
        
    elif op == '7':
        m.mostrarCalefPromocion()
        
    elif op == '8':
        diccionario = m.toJson()
        m.guardarEnJson(diccionario)
        print('Cargado')
        
    elif op == '9':
        print_program_finished()
        sys.exit()


   
def print_program_finished():
    message = "PROGRAMA TERMINADO"
    border = '+' + '-' * (len(message) + 2) + '+'
    print(border)
    print(f'| {message} |')
    print(border)        
        

if __name__ == '__main__':
    m = Manejador()
    m.cargarCalefactores()

    while True:
         Menu(ICalefactor(m))