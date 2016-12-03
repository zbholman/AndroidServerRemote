# Author: Brian Hoyer
# Class: IST440W, Abington PA
# This file allows us to take readings from MoPi
# and translate it into precentage displayable on
# both Android and an LED bar

import mopi_api
import smbus
import errno
import time
from dotstar import Adafruit_DotStar # imports library/module

mopi3 = mopi_api.mopiapi()
Volt = mopi3.getVoltage()

#CurrentVoltage =  # takes value from currently running MoPi file

numpixels = 8 # Amount of LEDs

datapin   = 23 # GPIO pin 23
clockpin  = 24 # GPIO pin 24
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # initialize pins for output
strip.setBrightness(10) # limit brightness to ~1/4 duty cycle

#while CurrentVoltage >= 6000:
print "Current voltage reading is: %d" % Volt;

if Volt > 8100:
                # initialize the entire LED bar to show full charge
                strip.setPixelColor(0, 255, 0, 0)
                strip.setPixelColor(1, 255, 0, 0)
                strip.setPixelColor(2, 255, 0, 0)
                strip.setPixelColor(3, 255, 0, 0)
                strip.setPixelColor(4, 255, 0, 0)
                strip.setPixelColor(5, 255, 255, 0)
                strip.setPixelColor(6, 255, 255, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()
		
elif Volt > 7800:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off first LED
                strip.setPixelColor(1, 255, 0, 0)
                strip.setPixelColor(2, 255, 0, 0)
                strip.setPixelColor(3, 255, 0, 0)
                strip.setPixelColor(4, 255, 0, 0)
                strip.setPixelColor(5, 255, 255, 0)
                strip.setPixelColor(6, 255, 255, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()

elif Volt > 7500:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off two LEDs
                strip.setPixelColor(1, 0, 0, 0) 
                strip.setPixelColor(2, 255, 0, 0)
                strip.setPixelColor(3, 255, 0, 0)
                strip.setPixelColor(4, 255, 0, 0)
                strip.setPixelColor(5, 255, 255, 0)
                strip.setPixelColor(6, 255, 255, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()

elif Volt > 7200:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off three LEDs
                strip.setPixelColor(1, 0, 0, 0)
                strip.setPixelColor(2, 0, 0, 0)
                strip.setPixelColor(3, 255, 0, 0)
                strip.setPixelColor(4, 255, 0, 0)
                strip.setPixelColor(5, 255, 255, 0)
                strip.setPixelColor(6, 255, 255, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()

elif Volt > 6900:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off four LEDs
                strip.setPixelColor(1, 0, 0, 0)
                strip.setPixelColor(2, 0, 0, 0)
                strip.setPixelColor(3, 0, 0, 0)
                strip.setPixelColor(4, 255, 0, 0)
                strip.setPixelColor(5, 255, 255, 0)
                strip.setPixelColor(6, 255, 255, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()

elif Volt > 6600:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off five LEDs
                strip.setPixelColor(1, 0, 0, 0)
                strip.setPixelColor(2, 0, 0, 0)
                strip.setPixelColor(3, 0, 0, 0)
                strip.setPixelColor(4, 0, 0, 0)
                strip.setPixelColor(5, 255, 255, 0)
                strip.setPixelColor(6, 255, 255, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()

elif Volt > 6300:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off six LEDs
                strip.setPixelColor(1, 0, 0, 0)
                strip.setPixelColor(2, 0, 0, 0)
                strip.setPixelColor(3, 0, 0, 0)
                strip.setPixelColor(4, 0, 0, 0)
                strip.setPixelColor(5, 0, 0, 0)
                strip.setPixelColor(6, 255, 255, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()

elif Volt > 6000:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off seven LEDs
                strip.setPixelColor(1, 0, 0, 0)
                strip.setPixelColor(2, 0, 0, 0)
                strip.setPixelColor(3, 0, 0, 0)
                strip.setPixelColor(4, 0, 0, 0)
                strip.setPixelColor(5, 0, 0, 0)
                strip.setPixelColor(6, 0, 0, 0)
                strip.setPixelColor(7, 0, 255, 0)
                strip.show()

else:
                # turn off LEDs to show amount of charge left
                strip.setPixelColor(0, 0, 0, 0) # turns off all eight LEDs
                strip.setPixelColor(1, 0, 0, 0)
                strip.setPixelColor(2, 0, 0, 0)
                strip.setPixelColor(3, 0, 0, 0)
                strip.setPixelColor(4, 0, 0, 0)
                strip.setPixelColor(5, 0, 0, 0)
                strip.setPixelColor(6, 0, 0, 0)
                strip.setPixelColor(7, 0, 0, 0)
                strip.show()
