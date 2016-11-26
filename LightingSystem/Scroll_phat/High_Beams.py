# The following program simulates high beams on the scroll-phat
# by turning on all pixels at max brightness. similar to running lights
# Date: 10/23/16
# Author: John Harrison
# IST 440W - Joe Oakes
# Penn State Abington

import sys
import sys
import time
import scrollphat

#max brightness
scrollphat.set_brightness(5000)

#go through columns then rows, turning all pixels on
for y in range(5):
    for x in range(11):
        scrollphat.set_pixel(x,y,True)
        scrollphat.update()
