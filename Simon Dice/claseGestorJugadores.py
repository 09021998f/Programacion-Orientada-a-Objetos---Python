import json
from claseJugador import Jugador
class GestorJugadores:
    def __init__(self):
        self.__jugadores = []
    
    def agregarJugador(self, jugador):
        self.__jugadores.append(jugador)


    def cargarJugadores(self):
        with open('puntos.json') as archi:
            data = json.load(archi)
        for jug in data['jugadores']:
            self.agregarJugador(Jugador(jug['jugador'],jug['fecha'], jug['hora'], jug['puntaje']))
        archi.close()
    def __str__(self):
        s = ''
        for jug in self.__jugadores:
            s += str(jug) + '\n'
        return s
    
    def toJson(self):
        d = dict(
            jugadores = [jug.toJson() for jug in self.__jugadores]
        )
        return d

    def guardarJSONArchivo(self, dic):
        
        with open('puntos.json', 'w') as archi:
            json.dump(dic, archi,indent=4)
            
    