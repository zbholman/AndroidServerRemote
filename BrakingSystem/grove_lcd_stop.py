#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung
from grovepi import *
import sys
import atexit
atexit.register(stop)
from grove_rgb_lcd import *
import time

ultrasonic_ranger = 4  # Insert ultrasonic_ranger to D4
buzzer = 8
led= 2
led1= 3


while True:
    try:
        # Read distance value from Ultrasonic
        distant = ultrasonicRead(ultrasonic_ranger)
        d = str(distant)
        if distant <= 10:
            setRGB(0,128,64)
            setRGB(0,255,0)
            digitalWrite(led, 1)#led's turned on
            digitalWrite(led1, 1)#led turned on
            grovepi.digitalWrite(buzzer, 1)#activates the buzzer
            setText("STOP!!! " + d + "cm")
            stop()#stops the go pi go
            time.sleep(10)  # sleep time added
        elif distant <= 15:
            setText("Getting a little too Close " + d + " cm")
        else:
            setText("Dist = " + d + " cm")

    except TypeError:
        print("Error")
        setText("Error")
    except IOError:
        print("Error")
        setText("Error")
