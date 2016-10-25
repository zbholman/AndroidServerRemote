#Class: IST440W 
#Professor: Joe Oakes
#Team 3
#Authors: Nirav 


import os
import RPi.GPIO as GPIO
import time
import datetime
import sys
 
#If the temp is > 65 the script will start the fan until the temperature goes down to 66. When it does, the script will end,
# shutting down the fan as well. If the script executes again while a previous script is running, the latter will exit.
 
# Identify which pin controls the relay
FAN_PIN = 4
# the yellow box ex: GPIO18
# Temperature check. Start fan if temp > 49C
FAN_START = 65
# Temperature check. Shut down under 28C
FAN_END = 66

DHT_SENSOR_TYPE = 1
# Connect the DHT sensor to one of the digital pins (i.e. 2, 3, 4, 7, or 8)
DHT_SENSOR_PIN = 3

CONVERT_TO_FAHRENHEIT = True
# ---------------------------------

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Get what action. If you manually turning on/off the fan
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
       
def get_temp_from_system():
        
	[temp_c,hum] = grovepi.dht(DHT_SENSOR_PIN,DHT_SENSOR_TYPE)
        if isFloat(temp_c):
                if (CONVERT_TO_FAHRENHEIT):
                        temp_f = temp_c * 9.0 / 5.0 + 32.0
                        print "Temperature(F):", temp_f
                else:
                        print "Temperature(C):", temp_c
 
def check_fan(pin):
        GPIOsetup()
        return GPIO.input(pin)
 
def run(pin):
        temp = get_temp_from_system()
        if float(temp) >= FAN_START:
                if check_fan(pin) == 1:
                        print('Fan is Off...Starting Fan')
                        fanON()
                else:
                        print('Fan is ON')
        elif float(temp) <= FAN_END:
                if check_fan(pin) == 0:
                        print('Fan is on...Shuting it Down')
                        fanOFF()
                        GPIO.cleanup()
                        return 1 # exit script. 
                else:
                        print('Fan is OFF')
                       
#testing command line                        
if action == "on" :
   print "Turning fan on"
   fanON()
elif action == "off" :
   print "Turning fan off"
   fanOFF()
