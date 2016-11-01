#IST440
#Climate Control
#Ahmad Alhaddad/Yusef Savage
#10/23/2016
#Fan OFF

#import statements

import RPi.GPIO as GPIO
import time

# GPIO pin on raspberry Pi to connect relay pin(Fan connected to relay One)

FAN_PIN = 4

#General Purpose input/output 
def GPIOsetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    GPIO.setwarnings(False)
#Turns the fan off 
def fanOFF():
    GPIO.output(FAN_PIN, 1) #Pin means fan is off 
    print("fan off") #It displays that the fan is off
    return()

#turns fan off
fanOFF()
