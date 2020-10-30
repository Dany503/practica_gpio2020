# -*- coding: utf-8 -*-
""" SDAA

    script que incorpora la función que hace parpadear un led
"""

# importamos el módulo de GPIO
import RPi.GPIO as GPIO
# importamos el módulo de tiempo para generar el retraso
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # definimos la numeración 
GPIO.setup(7, GPIO.OUT) # definimos el pin como salida

def parpadea(periodo):
    """
    Esta función realiza el parpadeo de un led, se le tiene que
    pasar como entrada el periodo de parpadeo
    """
    estado = 0
    while(1):
        if estado == 0:
            estado = 1
            GPIO.output(7, GPIO.HIGH)
            time.sleep(float(periodo)/8)

        else:
            estado = 0
            GPIO.output(7, GPIO.LOW)
            time.sleep(7*float(periodo)/8)

parpadea(1)
    
        






