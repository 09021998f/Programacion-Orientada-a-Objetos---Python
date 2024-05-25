class Cliente:

    def __init__(self, nom, ap, dni, numT, sAnt):
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = dni
        self.__numTarjeta = numT
        self.__saldoAnt = sAnt

    def __str__(self):
        return f'|Nombre: {self.__nombre} |Apellido: {self.__apellido} |DNI: {self.__dni} |Numero Tarjeta: {self.__numTarjeta} |Saldo Anterior: {self.__saldoAnt}'


    def get_dni(self):
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_numTarjeta(self):
        return self.__numTarjeta
    
    def get_saldoAnt(self):
        return self.__saldoAnt