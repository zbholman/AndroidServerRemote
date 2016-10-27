# Author: Brian Hoyer
# Class: IST440W, Abington PA
# This file allows us to take readings from MoPi
# and translate it into precentage displayable on
# both Android and an LED bar

import math
import time
import grovepi

LipoBattery = 5000 # mAh of lipo battery for the car
CurrentVoltage = (getVoltage) # takes value from currently running MoPi file (still have to work out how to get them to communicate)

grovepi.pinMode(ledbar,"OUTPUT") # establish the LED bar as the output from the GrovePi board
time.sleep(1)
i = 0

if CurrentVoltage <= 11200:
	for i in range (0,11):
		grovepi.ledBar_init(ledbar, 1) # initialize the entire LED bar to show full charge
else CurrentVoltage < 10880:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off top-most LED to show <90% charge left
else CurrentVoltage < 10560:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off two top-most LEDs to show <80% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
else CurrentVoltage < 10240:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off three top-most LEDs to show <70% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
else CurrentVoltage < 9920:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off four top-most LEDs to show <60% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
else CurrentVoltage < 9600:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off five top-most LEDs to show <50% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
else CurrentVoltage < 9280:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off six top-most LEDs to show <40% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
else CurrentVoltage < 8960:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off seven top-most LEDs to show <30% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
		grovepi.ledBar_setLed(ledbar, 4, 0)
else CurrentVoltage < 8640:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off eight top-most LEDs to show <20% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
		grovepi.ledBar_setLed(ledbar, 4, 0)
		grovepi.ledBar_setLed(ledbar, 3, 0)
else CurrentVoltage < 8320:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off nine top-most LEDs to show <10% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
		grovepi.ledBar_setLed(ledbar, 4, 0)
		grovepi.ledBar_setLed(ledbar, 3, 0)
		grovepi.ledBar_setLed(ledbar, 2, 0)
else CurrentVoltage < 8000:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off all LEDs to show 0% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
		grovepi.ledBar_setLed(ledbar, 4, 0)
		grovepi.ledBar_setLed(ledbar, 3, 0)
		grovepi.ledBar_setLed(ledbar, 2, 0)
		grovepi.ledBar_setLed(ledbar, 1, 0)

