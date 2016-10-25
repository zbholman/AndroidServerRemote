# FanOne.py
# IST440 Team 3
# author: Nirav

#import statements

import os
import RPi.GPIO as GPIO
import time
import datetime
import sys

# GPIO pin on raspberry Pi to connect relay pin(Fan connected to relay One)

FAN_PIN = 4

# Method to setup GPIO pins.
def GPIOsetup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FAN_PIN, GPIO.OUT)

# Method to turn relay ON that is Fan ON
def fanON():
        GPIOsetup()
        GPIO.output(FAN_PIN, 0) #fan on
        return()

# Method to tur relay OFF that is Fan OFF
def fanOFF():
        GPIOsetup()
        GPIO.output(FAN_PIN, 1) #fan off
        return()

#While loop to keep Fan On until user end loop using Ctrl + Z
while True:
        try:
                fanON()
        except KeyboardInterrupt:
                print "  Quit"

  # Reset GPIO settings
GPIO.cleanup()
