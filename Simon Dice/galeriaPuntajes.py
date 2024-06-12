from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
from claseGestorJugadores import GestorJugadores

class Puntaje:
    def __init__(self):
        self.__ventPuntajes = tk.Tk()
        self.__ventPuntajes.title('Galeria de Puntajes')
        self.__gestor = GestorJugadores()
        self.__gestor.cargarJugadores()
        self.frame = ttk.Frame(self.__ventPuntajes)
        self.frame.pack(padx=10, pady=10)
        
        self.tree = ttk.Treeview(self.frame, columns=('Jugador', 'Fecha', 'Hora', 'Puntaje'), show='headings', height=5)
        
        self.tree.heading("Jugador", text="Jugador")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Puntaje", text="Puntaje")
        
        self.tree.column("Jugador", width=100)
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=100)
        self.tree.column("Puntaje", width=100)


        jugadores = self.__gestor.get_jugadores()
        jugadores.sort()
        for jugador in jugadores:
            self.tree.insert("", tk.END, values=(jugador.getJugador(), jugador.getFecha(), jugador.getHora(), jugador.getPuntaje()))
            
        self.tree.pack()

        # Create a close button
        close_button = ttk.Button(self.__ventPuntajes, text="Cerrar", command=self.__ventPuntajes.destroy)
        close_button.pack(pady=10)
        
        self.__ventPuntajes.mainloop()
        
if __name__ == '__main__':
    menuPuntaje = Puntaje()