import json
from claseLista import Lista
from claseElectrico import Electrico
from claseGas import Gas
from zope.interface import implementer
from claseInterface import ICalefactor
@implementer(ICalefactor)

class Manejador:

    def __init__(self):
        self.__lista = Lista()
    
    def cargarCalefactores(self):
        with open('calefactores.json', encoding= 'utf-8') as archi:
            data = json.load(archi)
        for calefa in data['calefactores']:
            if calefa['tipo'] == 'gas':
                gas = Gas(calefa['marca'], calefa['modelo'], calefa['pais_de_fabricacion'], calefa['precio_de_lista'], calefa['forma_de_pago'] ,calefa['cant_cuotas'], calefa['promocion'], calefa['matricula'], calefa['calorias'])
                self.__lista.agregarCalefactores(gas) 
            else:
                elec = Electrico(calefa['marca'], calefa['modelo'], calefa['pais_de_fabricacion'], calefa['precio_de_lista'], calefa['forma_de_pago'] ,calefa['cant_cuotas'], calefa['promocion'], calefa['potencia_max'])
                self.__lista.agregarCalefactores(elec)

    def __str__(self):
        s = ''
        for dato in self.__lista:
            s+= str(dato) + '\n'
        return s
    '''Punto 1'''
    def insertarCalefactor(self):
        tipo = input('1-Electrico\n2-Gas\n>>>')
        pos = int(input('Posicion en la q desea agregar'))
        if pos > self.__lista.get_tope():
            raise IndexError('Posicion fuera de la lista')
        else:  
            if tipo == '1':
                marca = input('Marca: ')
                mod = input('Modelo: ')
                pais = input('Pais: ')
                precio = input('Precio: ')
                metodo = input('Metodo de pago: ')
                cuotas = input('Cantidad de cuotas: ')
                prom = input('Promocion (Si/No): ')
                if prom.lower() == 'si':
                    promo = True
                elif prom.lower() == 'no':
                    promo = False
                else:
                    print('Error! escriba si o no ')
                potencia = input('Potencia: ')
                elec = Electrico(marca,mod,pais,precio,metodo,cuotas,promo,potencia)
                self.__lista.insertarElemento1(elec,pos-1)
                
            elif tipo == '2':
                marca = input('Marca: ')
                mod = input('Modelo: ')
                pais = input('Pais: ')
                precio = input('Precio: ')
                metodo = input('Metodo de pago: ')
                cuotas = input('Cantidad de cuotas: ')
                prom = input('Promocion (Si/No): ')
                if prom.lower() == 'si':
                    promo = True
                elif prom.lower() == 'no':
                    promo = False
                else:
                    print('Error! escriba si o no ')
                matricula = input('Matricula: ')
                cal = input('Calorias: ')
                gas = Gas(marca,mod,pais,precio,metodo,cuotas,promo,matricula,cal)
                self.__lista.insertarElemento1(gas, pos-1)
            else:
                raise ValueError('Error! opcion no permitida.')
            
    '''Punto 2'''            
    def agregarAlaColeccion(self):
        tipo = input('1-Electrico\n2-Gas\n>>>')
        if tipo == '1':
            marca = input('Marca: ')
            mod = input('Modelo: ')
            pais = input('Pais: ')
            precio = input('Precio: ')
            metodo = input('Metodo de pago: ')
            cuotas = input('Cantidad de cuotas: ')
            prom = input('Promocion (Si/No): ')
            if prom.lower() == 'si':
                promo = True
            elif prom.lower() == 'no':
                promo = False
            else:
                print('Error! escriba si o no ')
            potencia = input('Potencia: ')
            elec = Electrico(marca,mod,pais,precio,metodo,cuotas,promo,potencia)
            self.__lista.agregarCalefactores(elec)  
        elif tipo == '2':
            marca = input('Marca: ')
            mod = input('Modelo: ')
            pais = input('Pais: ')
            precio = input('Precio: ')
            metodo = input('Metodo de pago: ')
            cuotas = input('Cantidad de cuotas: ')
            prom = input('Promocion (Si/No): ')
            if prom.lower() == 'si':
                promo = True
            elif prom.lower() == 'no':
                promo = False
            else:
                print('Error! escriba si o no ')
            matricula = input('Matricula: ')
            cal = input('Calorias: ')
            gas = Gas(marca,mod,pais,precio,metodo,cuotas,promo,matricula,cal)
            self.__lista.agregarCalefactores(gas)
        else:
            raise ValueError('Error! opcion no permitida.')
    
    '''Punto 3'''    
    def mostrarTipoObj(self):
        pos = int(input('Posicion de la lista: '))
        if pos > self.__lista.get_tope():
            raise IndexError('Posicion fuera del rango de la lista')
        else:
            obj = self.__lista.tipoObjeto(pos-1)
            
        if obj != None:
            if isinstance(obj,Electrico):
                print(f'El objeto de la posicion {pos} es de tipo Electrico')
                
            else:
                print(f'El objeto de la posicion {pos} es de tipo Gas')
                
        else:
            print('No se encontro ningun calefactor')
    
    '''Punto 4'''
    def mostrarCalefGasMenorPrecio(self):
        min = 999999999
        aux = None
        for dato in self.__lista:
            if isinstance(dato,Gas):
                if dato.get_precio() < min:
                    min = dato.get_precio()
                    aux = dato
        
        if aux is not None:
            print(f'Calefactor de menor precio {aux.get_precio()}$ es:')
            print(f'|Marca:{aux.get_marca()} |Modelo: {aux.get_modelo()} |Kilocarias: {aux.get_calorias()}\n')    
                
    '''Punto 5'''
    def mostrarCalefElectrico(self):
        aux = None
        marca = input('Ingrese marca de calefactor:')
        for dato in self.__lista:
            if isinstance(dato,Electrico):
                if dato.get_marca().lower() == marca.lower():
                    aux = dato

        if aux is not None:
            print(f'Marca: {aux.get_marca()} |Modelo: {aux.get_modelo()} |Potencia: {aux.get_potencia()} |Precio de lista: {aux.get_precio()}')
        else:
            print(f'No hay calefactor electrico con la marca {marca}')
            
    '''Punto 6'''
    
    def mostrarCalefPromocion(self):
        precioFinal = 0
        for dato in self.__lista:
            if isinstance(dato,Electrico):
                if dato.get_promocion() == True:
                    self.calcularImporteFinal(dato,'electrico')
                else:
                    print(f'|Marca:{dato.get_marca()} |Modelo: {dato.get_modelo()} |Importe: {dato.get_precio()}')
            if isinstance(dato,Gas):
                if dato.get_promocion() == True:
                    self.calcularImporteFinal(dato, 'gas')
                else:
                    print(f'|Marca:{dato.get_marca()} |Modelo: {dato.get_modelo()} |Importe: {dato.get_precio()}')
                
             
            
                         
    def calcularImporteFinal(self, dato,tipo):
        precioFinal = 0
        if tipo == 'electrico':
            precioFinal = dato.get_precio() * (1-0.15)  
            if dato.get_potencia() > 1000:
                precioFinal = precioFinal * (1+0.01)
            if dato.get_formaDePago() == 'cuotas':
                precioFinal = precioFinal * (1+0.30)
            print(f'|Marca:{dato.get_marca()} |Modelo: {dato.get_modelo()} |Importe: {precioFinal}')
                
        if tipo == 'gas':
            precioFinal = dato.get_precio() * (1-0.15)  
            if dato.get_calorias() > 3000:
                precioFinal = precioFinal * (1+0.01)
            if dato.get_formaDePago() == 'cuotas':
                precioFinal = precioFinal * (1+0.40)
            print(f'|Marca:{dato.get_marca()} |Modelo: {dato.get_modelo()} |Importe: {precioFinal}')
        
                
                
                
                
                
                
                
                
                
    