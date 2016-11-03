#IST440
#Climate Control
#Ahmad Alhaddad/ Yusef Savage
#10/23/2016
#Fan ON

import RPi.GPIO as GPIO
import time
# GPIO pin on raspberry Pi to connect relay pin(Fan connected to relay One)

FAN_PIN = 4

#General Purpose input/output
def GPIOsetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    GPIO.setwarnings(False)
#Turns the fan on 
def fanON(): #
    GPIOsetup()
    GPIO.output(FAN_PIN, 0)#Pin means fan is on 
    print("fan on")#It displays that the fan is on
    return()

#turns fan on
fanON()

# Reset GPIO settings
GPIO.cleanup()
