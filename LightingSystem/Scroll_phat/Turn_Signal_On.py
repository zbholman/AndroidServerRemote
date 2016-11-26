#Author: John Harrison
#Date: 11/9/16
#Joe Oakes IST 440 Lighting System
#This program creates a turn signal arrow on the scroll phat and blinks it

import math
import sys
import time
import scrollphat

#define miliseconds
def millis():
    return int(round(time.time() * 1000))

#set brightness to same as running lights
scrollphat.set_brightness(10)

#set rotation based on turn signal direction
direction = sys.argv[1]
if direction == "L":
    scrollphat.set_rotate(True)
elif direction == "R":
    scrollphat.set_rotate(False)

#turn lights off
def clear(pause):
    # arrow body
    for x in range(11):
        scrollphat.set_pixel(x,2,0)
        
    # arrow tip part
    scrollphat.set_pixel(8,0,0)
    scrollphat.set_pixel(9,1,0)
    scrollphat.set_pixel(9,3,0)
    scrollphat.set_pixel(8,4,0)

    scrollphat.update()
    time.sleep(pause)

#turn lights of
def paint(pause):
    # arrow body
    for x in range(11):
        scrollphat.set_pixel(x,2,1)
        
    # arrow tip part
    scrollphat.set_pixel(8,0,1)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(9,3,1)
    scrollphat.set_pixel(8,4,1)

    scrollphat.update()
    time.sleep(pause)

while(True):
    try:
        pause_time = 0.5
        paint(pause_time)
        clear(pause_time)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)




