#!/usr/bin/env python

# The following program simulates hazard lights on the scroll-phat
# based off progress.py example and turn signals
# Date: 10/23/16
# Author: John Harrison
# IST 440W - Joe Oakes
# Penn State Abington

import math
import sys
import time

import scrollphat

#defining a millisecond 
def millis():
    return int(round(time.time() * 1000))

#set brightness to max 	
scrollphat.set_brightness(5000)

#the next few methods iterate through the rows and columns of the matrix
#turning all the lights on then all off rapidly to simulate blinking

#turns lights off
def clear(pause):
    for x in range(11):   #11 pixels in a row
        for y in range(5):  # 5 pixels in a column
            scrollphat.set_pixel(x,y,0)
            scrollphat.update()
            #time.sleep(pause)
			
#turn lights on
def paint(pause):
    for x in range(11):   #11 pixels in a row
        for y in range(5):  #5 pixels in a column
            scrollphat.set_pixel(x,y,1)
            scrollphat.update()
            #time.sleep(pause)

while(True):
    try:
        pause_time = 0.1  #low pause time to simulate blinking
        paint(pause_time)
        clear(pause_time)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)