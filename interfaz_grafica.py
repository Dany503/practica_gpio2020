#Importamos paquete tkinter
import tkinter as tk
from tkinter import ttk

# importamos el módulo de GPIO
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # definimos la numeración 
GPIO.setup(3, GPIO.OUT) # definimos el pin como salida

#Funciones encender y apagar
def encender():
    GPIO.output(3, GPIO.HIGH)
    
def apagar():
    GPIO.output(3, GPIO.LOW)
    
#Funcion imprimir texto
def imprime():
    print(caja_texto.get())

#Ventana
ventana = tk.Tk()
ventana.config(width=300, height=200)
ventana.title("Ventana")

#Declaracion boton encender
boton_encender = ttk.Button(text="Encender", command=encender)
boton_encender.place(x=50, y=50)

#Declaracion boton apagar
boton_apagar = ttk.Button(text="Apagar", command=apagar)
boton_apagar.place(x=150, y=50)

#etiqueta introducir texto
etiqueta_texto = ttk.Label(text="Introduce texto:")
etiqueta_texto.place(x=50, y=100)

#caja para introducir texto
caja_texto = ttk.Entry()
caja_texto.place(x=50, y=120, width=200)

#Declaracion boton imprimir
boton_imprimir = ttk.Button(text="Imprime", command=imprime)
boton_imprimir.place(x=50, y=150)

ventana.mainloop()