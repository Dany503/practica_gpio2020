# -*- coding: utf-8 -*-
""" SDAA

    Script que incorpora la función muestrea 
"""

# importamos el modulo de GPIO
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # definimos la numeracion 
GPIO.setup(11, GPIO.IN, GPIO.PUD_UP) # definimos el pin entrada


def muestrea_pin (periodo):
    """
    Muestreamos un 
    """
    while(1):
        time.sleep(periodo)
        if (GPIO.input(11)) == 0:
            print "Entrada a 0"
        else:
            print "Entrada a 1"

muestrea_pin(1)
            



    
        






