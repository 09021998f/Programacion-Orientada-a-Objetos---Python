class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

    def resolver_item4(self):
        # Código para resolver el item 4
        pass

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    # Puede sobrescribir el método descripción si es necesario

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, carga_maxima):
        super().__init__(marca, modelo)
        self.carga_maxima = carga_maxima

    # Puede sobrescribir el método descripción si es necesario

# Crear instancias y usar el método
automovil = Automovil("Toyota", "Camry", "Rojo")
camioneta = Camioneta("Ford", "F150", 1000)

print(automovil.descripcion())  # Imprime la descripción del automóvil
print(camioneta.descripcion())  # Imprime la descripción de la camioneta

automovil.resolver_item4()  # Llama al método resolver_item4() de la superclase
camioneta.resolver_item4()  # Llama al método resolver_item4() de la superclase
