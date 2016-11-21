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

#flip direction of arrow
scrollphat.set_rotate(True)

#turn lights off
def clear(pause):
    for x in range(11):
        for y in range(5):
            #arrow body
            scrollphat.set_pixel(0,2,0)
            scrollphat.set_pixel(1,2,0)
            scrollphat.set_pixel(2,2,0)
            scrollphat.set_pixel(3,2,0)
            scrollphat.set_pixel(4,2,0)
            scrollphat.set_pixel(5,2,0)
            scrollphat.set_pixel(6,2,0)
            scrollphat.set_pixel(7,2,0)
            scrollphat.set_pixel(8,2,0)
            scrollphat.set_pixel(9,2,0)
            scrollphat.set_pixel(10,2,0)

            # arrow tip part
            scrollphat.set_pixel(8,0,0)
            scrollphat.set_pixel(9,1,0)
            scrollphat.set_pixel(9,3,0)
            scrollphat.set_pixel(8,4,0)

            scrollphat.update()
            time.sleep(pause)

#turn lights off
def paint(pause):
    for x in range(11):
        for y in range(5):
            #arrow body
            scrollphat.set_pixel(0,2,1)
            scrollphat.set_pixel(1,2,1)
            scrollphat.set_pixel(2,2,1)
            scrollphat.set_pixel(3,2,1)
            scrollphat.set_pixel(4,2,1)
            scrollphat.set_pixel(5,2,1)
            scrollphat.set_pixel(6,2,1)
            scrollphat.set_pixel(7,2,1)
            scrollphat.set_pixel(8,2,1)
            scrollphat.set_pixel(9,2,1)
            scrollphat.set_pixel(10,2,1)

            # arrow tip part
            scrollphat.set_pixel(8,0,1)
            scrollphat.set_pixel(9,1,1)
            scrollphat.set_pixel(9,3,1)
            scrollphat.set_pixel(8,4,1)

            scrollphat.update()
            time.sleep(pause)            
            


while(True):
    try:
        pause_time = 0.005
        paint(pause_time)
        clear(pause_time)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)





