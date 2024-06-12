from tkinter import *
from tkinter import ttk, font,messagebox
from claseJugador import Jugador
from claseGestorJugadores import GestorJugadores
import tkinter as tk
import time, random 
import datetime

class Aplicacion():
    def __init__(self):

        #   Configuraciones de la ventana
        self.__ventana =tk.Tk()
        self.__ventana.title('Simon dice')
        self.__ventana.geometry('250x450')
        self.__ventana.configure()
        self.__ventana.resizable(0,0)
        self.colores = ["#006400", "#8B0000", "#CCCC00", "#00008B"]
        
        #   Datos jugador
        self.__jugador = None
        self.__fecha = None
        self.__hora = None
        self.__puntaje = 0
        #   Creo instancias de jugadores nuevos y cargo jugadores anteriores al gestor
        self.__gestor = GestorJugadores()
        self.__gestor.cargarJugadores()
        #   Botones y sus posiciones
        self.botones = []
        #   para cada elemento de self.colores i es el indice del elemento color
        for i, color in enumerate(self.colores):
            #   Creo el canvas
            boton = tk.Canvas(self.__ventana, width=100, height=150, background=color, relief="raised")
            #   posiciono los canvas con los calculos de i // 2 y i % 2
            #   i // 2 esto organiza el canvas en filas de 2 
            #   i %  2 esto alterna en las posiciones entre las columnas 0 y 1
            boton.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            #   Agrego el boton q se creo en una lista de botones q son canvas en realidad
            self.botones.append(boton)
        #   Creo los botones de comenzar y salir
        self.botonComenzar = tk.Button(self.__ventana, text="Start", command=self.ventana_jugador)
        self.botonComenzar.grid(row=4, column=0, pady=10, padx=10)
        self.botonSalir = tk.Button(self.__ventana, text='Salir', command=self.salir_aplicacion)
        self.botonSalir.grid(row=4, column=1)
        
        #   Labels
        fuente = font.Font(weight='bold')
        self.labelJugador = tk.Label(self.__ventana, text='', font=fuente, padx=5, pady=5 )
        self.labelJugador.grid(column=0, row=3)
        self.puntaje = tk.Label(self.__ventana, text='0', font=fuente, padx=5, pady=5)
        self.puntaje.grid(column=1, row=3)
             
        #   Main loop de la ventana
        self.__ventana.mainloop()
        
#   Funciones
    #   Inicio el juego reseteando secuencia y respuesta del juegador
    def iniciar_juego(self):
        self.botonComenzar.config(state=tk.DISABLED) # luego de apretar el boton comenzar se inhabilita
        self.secuencia = []
        self.respuesta_jugador = []
        self.generar_color()  

    def generar_color(self):  # Genero el color random
        color_nuevo = random.choice(self.colores)
        self.secuencia.append(color_nuevo)
        self.mostrar_secuencia()

    def mostrar_secuencia(self):
        for color in self.secuencia:
            index_color = self.colores.index(color)
            self.botones[index_color].config(bg="gray")
            self.__ventana.update()
            time.sleep(1)
            self.botones[index_color].config(bg=color)
            self.__ventana.update()
            time.sleep(0.5)
        self.jugar()

    def jugar(self):
        self.respuesta_jugador = []
        self.__ventana.bind("<Button-1>", self.procesar_clic)

    def procesar_clic(self, event):
        boton_presionado = event.widget
        color_presionado = boton_presionado.cget("background")
        self.respuesta_jugador.append(color_presionado)
        boton_presionado.config(bg="gray")
        self.__ventana.update()
        time.sleep(0.2)
        boton_presionado.config(bg=color_presionado)
        self.__ventana.update()

        if len(self.respuesta_jugador) == len(self.secuencia):
            self.verificar_respuesta()

    def verificar_respuesta(self):
        
        if self.respuesta_jugador == self.secuencia:
            self.actualizar_puntaje(len(self.secuencia))
            self.generar_color()
        else:
            messagebox.showinfo("¡Perdiste!", "Respuesta incorrecta. ¡Inténtalo de nuevo!")
            self.botonComenzar.config(state=tk.NORMAL)
            self.guardar_record()
            self.resetPuntaje()
            
    def resetPuntaje(self):
        self.puntaje.config(text='0')
        self.__puntaje = 0    
    def actualizar_puntaje(self, puntos):
        puntaje_actual = int(self.puntaje.cget("text"))
        self.__puntaje = puntaje_actual + puntos
        self.puntaje.config(text=str(self.__puntaje)) 
        
     
    def guardar_record(self):
        fecha_hora = datetime.datetime.now()
        self.__fecha = fecha_hora.date()
        self.__hora = fecha_hora.strftime('%H:%M:%S')
        self.__gestor.agregarJugador(Jugador(self.__jugador,self.__fecha,self.__hora,self.__puntaje))
        
        self.resetPuntaje()
    
    #  Ventana donde ingresa el nombre el jugador
    def ventana_jugador(self):
        self.__ventanaJug = Toplevel()
        fuente = font.Font(weight='bold')
        self.__ventanaJug.resizable(0,0)
        self.__ventanaJug.title('Simon dice')
        
        #   Labels e inputs
        self.labelDatosJug = tk.Label(self.__ventanaJug, text='Datos del jugador')
        self.labelDatosJug.grid(row=0, column=0)
        
        self.nombre_jugador = tk.Label(self.__ventanaJug, text='Jugador', font=fuente, padx=5, pady=5)
        self.nombre_jugador.grid(row=1, column=0)
        self.__jugador = StringVar()
        self.__jugador.set('')
       
        self.ctext1 = tk.Entry(self.__ventanaJug, textvariable=self.__jugador, width=30 )
        self.ctext1.grid(column=1, row=1, columnspan=2)
        
        #   Botones
        
        self.botonIniciar = tk.Button(self.__ventanaJug, text="Start",padx=5, pady=5, command=self.actualizarNombre)
        self.botonIniciar.grid(row=2, column=1)
        self.__ventanaJug.mainloop()
        
    def actualizarNombre(self):
        self.__jugador = self.ctext1.get()
        self.labelJugador.configure(text=self.__jugador)
        self.__ventanaJug.destroy()
        self.iniciar_juego()
    
    def salir_aplicacion(self):
        print('Saliendo de la app...')
        datos = self.__gestor.toJson()
        self.__gestor.guardarJSONArchivo(datos)
        self.__ventana.destroy()

if __name__ == '__main__':
    app = Aplicacion()
    