import sys
import time

import scrollphat

scrollphat.set_brightness(10)

for y in range(5):
    for x in range(11):
        scrollphat.set_pixel(x,y,True)
        scrollphat.update()
    




