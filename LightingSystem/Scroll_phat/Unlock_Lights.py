# This program blinks the running lights, it is called when the car is unlocked
# Date: 10/23/16
# Author: John Harrison
# IST 440W - Joe Oakes
# Penn State Abington

import sys
import time

import scrollphat

#low brightness
scrollphat.set_brightness(10)

#iterate through columns and rows, turning all pixels on
for y in range(5):
    for x in range(11):
        scrollphat.set_pixel(x,y,True)
        scrollphat.update()

time.sleep(.500)
scrollphat.clear()
time.sleep(.250)
#iterate through columns and rows, turning all pixels on
for y in range(5):
    for x in range(11):
        scrollphat.set_pixel(x,y,True)
        scrollphat.update()

time.sleep(.500)
scrollphat.clear()
