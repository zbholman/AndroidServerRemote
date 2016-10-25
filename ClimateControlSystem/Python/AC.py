# AC.py
# IST440 Team 3
# author: Nirav

#import statements
import RPi.GPIO as GPIO
import time


# GPIO pin on raspberry Pi to connect relay pin(Fan connected to relay One)

AC_PIN = 4

# Method to setup GPIO pins.
def GPIOsetup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(AC_PIN, GPIO.OUT)

# Method to turn relay ON that is Ac ON
def AcON():
        GPIOsetup()
        GPIO.output(AC_PIN, 0) #Ac On
        return()

# Method to tur relay OFF that is Ac OFF
def AcOFF():
        GPIOsetup()
        GPIO.output(AC_PIN, 1) #Ac off
        return()

#While loop to keep Fan On until user end loop using Ctrl + Z
while True:
        try:
                AcON()
        except KeyboardInterrupt:
                print "  Quit"

  # Reset GPIO settings
GPIO.cleanup()


