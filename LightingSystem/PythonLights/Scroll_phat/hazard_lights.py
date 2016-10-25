#!/usr/bin/env python

import math
import sys
import time

import scrollphat


def millis():
    return int(round(time.time() * 1000))

scrollphat.set_brightness(5000)

def clear(pause):
    for x in range(11):
        for y in range(5):
            scrollphat.set_pixel(x,y,0)
            scrollphat.update()
            #time.sleep(pause)

def paint(pause):
    for x in range(11):
        for y in range(5):
            scrollphat.set_pixel(x,y,1)
            scrollphat.update()
            #time.sleep(pause)

while(True):
    try:
        pause_time = 0.1
        paint(pause_time)
        clear(pause_time)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
