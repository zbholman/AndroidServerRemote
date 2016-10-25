# Heating.py
# IST440 Team 3
# author: Nirav

#import statements

import os
import RPi.GPIO as GPIO
import time
import datetime
import sys

# GPIO pin on raspberry Pi to connect Heating Pad to pin(Fan connected to relay One)
Heating_Pin = 4

# Method to setup GPIO pins.
def GPIOsetup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Heating_Pin, GPIO.OUT)

# Method to turn relay ON that is Heating Pad ON
def HeatON():
        GPIOsetup()
        GPIO.output(Heating_Pin, 0) #Heat on
	print("Heat On")
        return()

# Method to tur relay OFF that is Heating Pad OFF
def HeatOFF():
        GPIOsetup()
        GPIO.output(Heating_Pin, 1) #Heat off
	print("Heat Off")
        return()

try:
	HeatON()
        time.sleep(15)
	HeatOFF()

except KeyboardInterrupt:
        print "Quit"

  # Reset GPIO settings
GPIO.cleanup()


