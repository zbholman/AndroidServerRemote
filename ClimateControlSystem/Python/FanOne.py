import RPi.GPIO as GPIO
import time
import datetime
import sys

FAN_PIN = 4

def GPIOsetup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FAN_PIN, GPIO.OUT)

def fanON():
        GPIOsetup()
        GPIO.output(FAN_PIN, 0) #fan on
        return()
def fanOFF():
        GPIOsetup()
        GPIO.output(FAN_PIN, 1) #fan off
        return()

while True:
        try:
                fanON()
        except KeyboardInterrupt:
                print "  Quit"

  # Reset GPIO settings
GPIO.cleanup()

