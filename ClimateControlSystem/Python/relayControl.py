import os
import RPi.GPIO as GPIO
import time
import datetime
import sys

FAN_PIN = 4 
action = sys.argv.pop()

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
	if action == "on" :
   		print "Turning fan on"
   		fanON()
	elif action == "off" :
   		print "Turning fan off"
   		fanOFF()
