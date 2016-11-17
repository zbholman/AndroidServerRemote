# Author: Brian Hoyer
# Class: IST440W, Abington PA
# This file allows us to take readings from MoPi
# and translate it into precentage displayable on
# both Android and an LED bar

import time
from dotstar import Adafruit_DotStar # imports library/module

numpixels = 8 # Amount if LEDs

datapin = 23 # GPIO pin 23
clockpin = 24 # GPIO pin 24
strip = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin() # initialize pins for output
strip.setBrightness(64) # limit brightness to ~1/4 duty cycle

def getVoltage(self, input=0):
        if input == 1:
                return self.readWord(0b00000101)
        elif input == 2:
                return self.readWord(0b00000110)
        else:
                return self.readWord(0b00000001)

LipoBattery = 5000 # mAh of lipo battery for the car
CurrentVoltage = (getVoltage) # takes value from currently running MoPi file (still have to work out how to get them to communicate)

grovepi.pinMode(ledbar,"OUTPUT") # establish the LED bar as the output from the GrovePi board
time.sleep(1)
i = 0

if CurrentVoltage <= 8400:
	for i in range (0,11):
		#grovepi.ledBar_init(ledbar, 1) # initialize the entire LED bar to show full charge
		strip.setPixelColor(0, 255, 0, 0)
		strip.setPixelColor(1, 255, 0, 0)
		strip.setPixelColor(2, 255, 0, 0)
		strip.setPixelColor(3, 255, 0, 0)
		strip.setPixelColor(4, 255, 0, 0)
		strip.setPixelColor(5, 255, 255, 0)
		strip.setPixelColor(6, 255, 255, 0)
		strip.setPixelColor(7, 0, 255, 0)
		strip.show()
elif CurrentVoltage < 8160:
	for i in range (0,11):
		#grovepi.ledBar_setLed(ledbar, 10, 0) # turn off top-most LED to show <90% charge left
		strip.setPixelColor(0, 0, 0, 0) # turns off first led
		strip.setPixelColor(1, 255, 0, 0)
		strip.setPixelColor(2, 255, 0, 0)
		strip.setPixelColor(3, 255, 0, 0)
		strip.setPixelColor(4, 255, 0, 0)
		strip.setPixelColor(5, 255, 255, 0)
		strip.setPixelColor(6, 255, 255, 0)
		strip.setPixelColor(7, 0, 255, 0)
		strip.show()
elif CurrentVoltage < 7920:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off two top-most LEDs to show <80% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
elif CurrentVoltage < 7680:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off three top-most LEDs to show <70% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
elif CurrentVoltage < 7440:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off four top-most LEDs to show <60% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
elif CurrentVoltage < 7200:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off five top-most LEDs to show <50% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
elif CurrentVoltage < 6960:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off six top-most LEDs to show <40% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
elif CurrentVoltage < 6720:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off seven top-most LEDs to show <30% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
		grovepi.ledBar_setLed(ledbar, 4, 0)
elif CurrentVoltage < 6480:
	for i in range (0,11):
		grovepi.ledBar_setLed(ledbar, 10, 0) # turn off eight top-most LEDs to show <20% charge left
		grovepi.ledBar_setLed(ledbar, 9, 0)
		grovepi.ledBar_setLed(ledbar, 8, 0)
		grovepi.ledBar_setLed(ledbar, 7, 0)
		grovepi.ledBar_setLed(ledbar, 6, 0)
		grovepi.ledBar_setLed(ledbar, 5, 0)
		grovepi.ledBar_setLed(ledbar, 4, 0)
		grovepi.ledBar_setLed(ledbar, 3, 0)
elif CurrentVoltage < 6240:
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
else:
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

print "Current voltage reading is: " + CurrentVoltage + ".";
